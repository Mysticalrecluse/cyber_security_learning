## Prometheus监控应用

Prometheus基于http的方式采集
- 被采集应用需要提供一个http访问路径
- `http:/xxx:port/metrics`
- 通过上述方式将待采集数据暴露出来

## 解决操作系统的数据指标暴露问题
### nodeexporter


## pushgateway采集自定义数据
### 安装pushgateway

```shell
# 官网：https://prometheus.io/download/#pushgateway
wget https://github.com/prometheus/pushgateway/releases/download/v1.9.0/pushgateway-1.9.0.linux-amd64.tar.gz

tar xf pushgateway-1.9.0.linux-amd64.tar.gz -C /usr/local/
ln -s pushgateway-1.9.0.linux-amd64/ pushgateway
mkdir /usr/local/pushgateway/bin
mv /usr/local/pushgateway/pushgateway /usr/local/pushgateway/bin
useradd -r -s /sbin/nologin prometheus
ln -s /usr/local/pushgateway/bin/pushgateway /usr/local/bin/
```

- 准备service
```shell
[Unit]
Description=Prometheus Pushgateway
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/pushgateway/bin/pushgateway
#ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
User=prometheus
Group=prometheus

[Install]
WantedBy=multi-user.target
```

### 配置Prometheus收集Pushgateway数据
#### 静态发现
```yaml
# vim /usr/local/prometheus/conf/prometheus.yml
- job_name: "pushgateway"
  honor_labels: true   # 可选项，设置为true，那么Prometheus将使用Pushgateway上的job和instance标签。如果设置为false那么它将重命名这些值，在它们前面加上exported_前缀，并在服务器上为这些标签附加新值
  scrape_interval: 10s # 可选项
  static_config:
    - targets: # 可以写在同一行：比如：["pushgateway.wang.org:9091"]
      - "pushgateway.wang.org:9091"
```
```shell
# 使用promtool check config /usr/local/promtheus/conf/prometheus.yml 检查配置文件语法
```

#### 基于文件形式自动发现形式
```yaml
# vim /usr/local/prometheus/conf/prometheus.yml
- job_name: pushgateway
  honor_labels: true
  file_sd_configs:
  - files:
    - targets/pushgateway/*.json
    refresh_interval: 5m
```

### 配置客户端发送数据给Pushgateway

#### 方法1：向执行url标准输入指定数据
- 推送Metric格式
```shell
http://<pushgateway_address>:<push_port>/metrics/job/<jpb_name>/[<label_name>/<label_value>][<label_name>/<label_value>]

# <job_name> 在Prometheus中指标的新加标签exported_job的值，在pushgateway中是job的指标值
# <label_name>/<label_value> 将成为额外的标签/值对

# 示例：echo "age 18" | curl --data-binary @- http://10.0.0.118:9091/metrics/job/pushgateway/instance/`hostname -I`
# --data-binary：表示提交的是二进制数据
# @- 表示读取标准输入
```

- 通用脚本`pushgateway_metric.sh`
```shell
#!/bin/bash
METRIC_NAME=mem_free
METRIC_VALUE_CMD="free -b | awk 'NR==2{print \$4}'"
METIRC_TYPE=gauge
METIRC_HELP="free memory"

PUSHGATEWAY_HOST=10.0.0.205:9091
EXPORITED_JOB=pushgateway_test
INSTANCE=`hostname -I| awk '{print $1}'`
SLEEP_TIME=1

CURL_URL="curl --data-binary @- http://${{PUSHGATEWAY_HOST}}/metrics/job/${EXPORITED_JOB}/instance/${INSTANCE}"

push_metric() {
    while true ;do
      VALUE=`eval "$METRIC_VALUE_CMD"`
      echo $VALUE
      cat << EOF | $CURL_URL  # 这里是将cat的内容，利用管道发送给$CURL_URL
# HELP ${METRIC_NAME} ${METRIC_HELP}
# TYPE ${METRIC_NAME} ${METRIC_TYPE}
${METRIC_NAME} ${VALUE}
EOF
      sleep $SLEEP_TIME
    done
}
push_metric
```

## PromQL
### 指标数据

Prometheus基于指标名称(metrics name)以及附属的标签集(labelset)唯一定义一条时间序列
- 指标名称代表着监控目标上某类可测量属性的基本特征标识
- 标签则是这个基本特征上再次细分的多个可测量维度
- 示例
```shell
request_total{path="/status",method="GET"}
request_total{path="/",method="POST"}
```

### 数据模型
Prometheus中，每个时间序列都由指标名称(Metric Name)和标签(Label)来唯一标识
Metric Name的表示方法有下面两种
```shell
# 方式1
<metric name>{<label name>=<label value>,...}

# 示例
http_requests_total{status="200", method="GET"}

# 方式2
<__name__="metric name",<label name>=<label value>,...> #通常用于Prometheus内部

# 示例
{__name__="http_requests_total",status="200",method="GET"}
```
### 样本数据
Prometheus的每个数据样本由两部分组成
- key:包括三部分：
  - Metric名称
  - Label
  - Timestamp(毫秒精度的时间戳)
- value: float64格式的数据

- 示例
```shell
...
http_requests_total{status="200",method="GET"} @1434317560938  94355
...
```

### PromQL基础
- Prometheus提供一个内置的函数表达式语言PromQL，可以帮助用户实现实时地查找和聚合时间序列数据
- 默认情况下，是以当前时间为基准点，来进行数据的获取操作

#### 表达式形式
每一个PromQL其实都是一个表达式，这些语句表达式或子表达式的计算结果可以为以下`四种类型`
- `instant vector` 即时向量，瞬时数据
- `range vector` 范围向量
- `scalar`标量
  - 一个简单的浮点类型数值
- `string`字符串(用的比较少)

#### 使用url查询数据
- 访问即时数据，指定时间点的数据`--data time="timestmp"`
```shell
curl --data 'query=<指标>' --data time="<时间戳>" '<Prometheus_address:port>/api/v1/query'

# 示例
[root@ubuntu2204 conf]#curl --data 'query=up' --data time=1720451038 'http://10.0.0.206:9090/api/v1/query'|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   395  100   371  100    24  36522   2362 --:--:-- --:--:-- --:--:-- 39500
```
```json
{
  "status": "success",
  "data": {
    "resultType": "vector",
    "result": [
      {
        "metric": {
          "__name__": "up",
          "instance": "localhost:9090",
          "job": "prometheus"
        },
        "value": [
          1720451038,
          "1"
        ]
      },
      {
        "metric": {
          "__name__": "up",
          "instance": "10.0.0.206:9100",
          "job": "node_exporter"
        },
        "value": [
          1720451038,
          "1"
        ]
      },
      {
        "metric": {
          "__name__": "up",
          "instance": "10.0.0.205:9091",
          "job": "pushgateway"
        },
        "value": [
          1720451038,
          "1"
        ]
      }
    ]
  }
}
```

- 范围数据，指定时间前1分钟的数据
```shell
curl --data 'query=node_memory_MemFree_bytes{instance=~"10.0.0.(101|102):9100"}[1m]' --data time=<时间戳> 'http://10.0.0.206:9090/api/v1/query'|jq
```
```json
{
  "status": "success",
  "data": {
    "resultType": "matrix",
    "result": [
      {
        "metric": {
          "__name__": "node_memory_MemFree_bytes",
          "instance": "10.0.0.206:9100",
          "job": "node_exporter"
        },
        "values": [ // 刮擦的时间是15s
          [
            1720450988.082,
            "1343700992"
          ],
          [
            1720451003.085,
            "1343700992"
          ],
          [
            1720451018.082,
            "1343700992"
          ],
          [
            1720451033.085,
            "1343700992"
          ]
        ]
      }
    ]
  }
}
```

#### 数据选择器
所谓的数据选择器，其实指的是获取实时数据或者历史数据的一种方法
```shell
metrics_name{筛选label=值,...}<时间范围> offset <偏移>
```
#### 即时向量选择器
示例
```shell
node_memory_MemFree_bytes{instance=~"10.0.0.(101|102):9100"}
```
#### 范围选择器
示例
```shell
prometheus_http_requests_total{job="prometheus"}[5m]
# 表示过去5分钟之内的监控数据
```


#### 指标的类型
- counter(计数器)
  - counter特点是，值一定是不断增大
- gauge（计量器）
  - 当前的值大小，一种度量标准
- histogram
  - 直方图
- summary
  - 摘要

### PromQL运算

## 标签管理

### relabel_configs和metric_relabel_configs

### relabel_configs和metric_relabel_configs的区别和各自的应用场景

#### relabel_config实现

#### metric_relable_configs实现


## 记录和告警规则

### 记录规则

### alertmanager部署

#### 二进制部署
#### 容器部署

#### Prometheus集成
### 告警规则


### 告警模版编辑


### 告警路由


### 抑制告警


### 邮件告警实现

### 微信告警实现

### 钉钉告警实现