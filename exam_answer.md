## Kafka
### 说说kafka是怎样选举的
- 当新的分区创建时，Kafka选择ISR(In-Sync Replica)列表中的第一个副本作为领导者
- 当领导者发生故障
  - ZooKeeper将会检测到它的`会话过期`
  ```
  当Kafka broker启动时，会与Zookeeper建立一个会话，并定期发送心跳信号，保持会话的活跃状态
  Kafka broker会定期发送心跳到Zookeeper，告诉它自己还活着
  如果因为网路原因，broker故障等原因，Zookeeper在一定时间内（通常是几秒到几分钟的超时时间）没有收到broker的心跳信号，就会认为这个broker已经失效，称之为会话过期
  ```
  - Zookeeper会将该broker标记为失效，并通知其他相关组件
  - 如果失效的是某个分区的leader，Zookeeper会触发leader选举机制，从该分区的其他副本中选出一个新的leader
  ```java
  // Zookeeper维护了每个分区的ISR列表，该列表包含当前处于同步状态的副本
  // /brokers/topics/example-topic/partitions/0/state
  {
    "controller_epoch": 1,
    "leader": 1,
    "version": 1,
    "leader_epoch": 1,
    "isr": [1, 2, 3]
  }
  
  /brokers/topics/example-topic/partitions/1/state
  {
    "controller_epoch": 1,
    "leader": 2,
    "version": 1,
    "leader_epoch": 1,
    "isr": [2, 1, 3]
  }
  
  /brokers/topics/example-topic/partitions/2/state
  {
    "controller_epoch": 1,
    "leader": 3,
    "version": 1,
    "leader_epoch": 1,
    "isr": [3, 1, 2]
  }
  //从ISR列表中选择brokerID最小的副本作为新的leader
  List<Integer> isr = getIsrForPartition(partitionId);
  int newLeader = Collections.min(isr);  // 选择 ID 最小的副本作为新的 leader
  updatePartitionLeader(partitionId, newLeader);
  ```
  
  - Zookeeper会将新的leader信息通知Kafka集群中的其他brokers和相关消费者，让它们更新leader信息，继续处理消息
 
### 说一下同步投递和重复消费
- 同步投递
  - 同步投递是Kafka中实现消息可靠性的重要机制, 但这种方式可能增加延迟和资源消耗，适用于对消息传递要求严格的场景
  - 其具体实现细节如下
    - 生产者先从集群获取分区的leader
      - 生产者初始化的时候，会连接到Kafka集群的一个或多个broker(通常称为bootstrap servers)
      - 生产者会向这些broker请求集群元数据信息，包括主题的分区信息和每个分区的leader副本
      - broker收到请求后会返回主题的分区信息，包括每个分区的leader副本和ISR列表
      - 生产者将这些元数据缓存到本地，以便在发送消息时快速查找每个分区的leader信息
    - 生产者将消息发送给leader副本
    - leader副本将消息写入本地日志文件
    - leader副本将消息传递给ISR列表中的所有follower副本
    - 每个follower副本将消息写入自己的本地日志文件
    - 每个foolower副本在成功写入消息后，发送确认给leader副本
    - 当leader副本收到所有ISR副本的确认后，向生产者发送确认消息
    - 生产者在接受到副本的确认后，才认为消息已成功发送

```shell
# acks配置
acks=0: 生产者不会等待任何确认。消息发送后立即返回。这种方式最快，但风险最大，因为消息可能丢失
acks=1: 生产者会等待leader副本确认消息写入日志后才返回，提供了一定可靠性，但是如果leader副本在消息传递给follower之前发生故障，消息可能会丢失。
acks=all(或-1): 生产者会等待所有ISRI(同步副本)确认消息写入后才返回。提供最高的可靠性（即同步投递）

# 关于同步投递的性能优化建议
为了在保证数据可靠性的同时优化性能，可以考虑以下建议：

配置优化：

调整 retries 和 retry.backoff.ms 参数，以适应实际的网络和系统状况，减少消息发送失败的重试次数。
配置 linger.ms 和 batch.size，通过批量发送消息来提高吞吐量。
集群扩展：

根据订单数据的量和并发要求，适当扩展 Kafka 集群，增加 broker 的数量和分区的数量，以提高系统的处理能力。
监控和调优：

通过监控 Kafka 集群的运行状态，及时发现和解决性能瓶颈和故障。
定期调优 Kafka 集群的配置，优化网络和存储性能，以适应不断增长的数据量和并发要求。
```

- 重复消费
- 
