# Git基础概念
## 版本控制软件的基础功能
- 保存和管理文件
- 提供客户端工具进行访问
- 提供不同版本文件的比对功能

## 集中式版本控制
- 所有的资源放在一个服务器中，所有人的上传下载都和同一个服务器交互， 如果该服务器宕机，则所有人受到影响

- 集中式版本控制对于多人合作中文件冲突的解决
  - 利用锁的概念，参考php的flock()读写锁
  - 利用约定，提前约定好，每个人对于文件指定位置的修改


## 分布式版本控制
- 依然是有一个中央服务器，放置所有的资源，但是在本地也有一个资源库，两个资源库中的内容同步
- 版本控制工具不直接对中央服务器进行操做（读写）， 而是对本地资源库进行操做

# Git基本操做
