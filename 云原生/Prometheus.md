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
- 算数运算
  - 略

- 比较运算
  - 略

- 逻辑运算
  - and
  - or
  - unless

- 正则表达式
```shell
node_memory_MemAvailable_bytes{instance =~ "10.0.0.20[12]:9100"}
node_memory_MemAvailable_bytes{instance =~ "10.0.0.20[1-3]:9100"}
...
```

- 集合处理
  - 并集or
  - 交集and
  - 补集unless

### 聚合运算
```shell
sum()
avg()
count()
min()
max()
...
```

### without和by
- without
  - 表示显示信息的时候，排除此处指定的标签列表，对以外额标签进行分组统计，即，使用除此标签之外的其他标签进行分组统计

- by
  - 表示显示信息的时候，仅显示指定的标签的分组统计，即针对哪些标签分组统计

```shell
# 两种格式：先从所有数据中利用数据表达式过滤出部分数据，进行分组后，再进行聚合运算，最终得出结果
# 格式1
聚合操作符(数据选择表达式) without|by (<label list>)
# 格式2
聚合操作符 without|by (<label list>) (数据选择表达式)
```

```shell
# 示例
# 按instance分组统计内存总量
sum(node_memory_MemTotal_bytes) by (instance)

# 按handle,instance分组统计
max(prometheus_http_requests_total) by (handle,instance)

# 获取前5个最大值
topk(5, prometheus_http_requests_total)
```

### 功能函数
示例
```shell
# increase(): 增长量，即last值-last前一个值
# 示例：最近1分钟内CPU处于空闲状态时间
increase（node_cpu_seconds_total {cpu"=0", nod="idle"})

# rate(): 平均变化率：计算在指定时间范围内，计数器每次增加量的平均值，即（last值-first值）时间差的秒数，常用语counter

# irate(): 查看瞬时变化率（last值-first值）/ 时间戳插值，
# 示例
irate(promethous_http_requests_total{code="200"}, handle="/-/ready"...}[1m]
```

### 定制开发Exporter
#### python

#### Golang

## 标签管理
### 增加标签
```yaml
scrape_config:
  - job_name: "node exporter"
    metrics_path: /metrics
    scheme: http
    static_configs:
      - targets:
        - "10.0.0.100:9100"
        - "10.0.0.101:9100"
        - "10.0.0.102:9100"
        labels:
          node: "worker node"
          type: "test"
          class: "M58"
```

### 基于source_labels的值赋值给新的标签名
```yaml
scrape_configs:
  ...
  - job_name: 'consul'
    honor_labels: true  # 如果抓取的原有标签和Prometheus配置的标签冲突，保留原有标签，避免标签冲突
    consul_sd_configs:
      - server: 'consul-node1.wang.org.8500'
        service: []
    relabel_configs:
      - source_labels: ['__meta_consul_service'] # 基于source_labels的值赋值给新的标签consul_service
        target_label: 'consul_servcie'
      - source_labels: ['__meta.consul_dc'] # 基于source_labels的值赋值给新的标签datacente
        target_label: 'consul_servcie'
      - source_label: ['__meta_consul_tags']
        regex: "consul" 
          action: drop 
```

### 将Target的默认标签修改为定制的新标签
```yaml
scrape_config:
...
  - job_name: 'k8s-node'
    statuc_configs:
    - targets: [10.0.0.104:9100]
    relabe_configs:
    - source_labels:
      - __Scheme__
      - __addressh
      - __cemetric_path__
      regex: "(http|https)(.*)"
      separator: ""  #将source_labels指定的label连接在还一起，成为一个字符串，每个label间没有分隔符
      target_label: "endpoint"
      replacement: "${1}://${2}"
      action: replace 
      # 基于默认属性，重写了一个新的标签

    - regex: "(job|app)"
      replacement: ${1}_name
      action: labelmap  
      # labelmap: 一般用于生成新的标签，将regex对source labels中指定的标签名称进行匹配，而后将匹配到的标签的值赋值给replacement字段指定的标签；通常用于取出匹配的签名的一部分生成新标签，旧的标签仍然存在
      # 本质就是拷贝一个标签，然后更改标签名，值不变
    metric_relabel_configs:
      - source_labels:
        - __name__    # 删除指标
        regex: 'go.*'
        action: drop
```

## 记录和告警规则

### 记录规则
规则语法检查
```shell
promtool check rules promtheus_rues_file.yml
```
可以在promtheus.yaml配置文件中通过rule_files属性进行导入
```yaml
# vim prometheus.yaml
rule_files:
  - "first_rules.yml"
  - "second_fules.yml"
  - "../rules/" ".yml"
```

```yaml
# 规则文件的语法
groups:
  [ - <rule_group> ]

# 简单的规则文件示例
groups:
  - name: example
    interval: 10s # 定制规则执行的间隔时间
    limit: <init> | default=0
    rules:
    - record: job:http_inprogress_requests:sum  # 记录规则
      expr: sum(http_inprogress_requests) by (job)
      labels: 
        [ <labelname>:<labelvalue> ]
```

## 告警
### 告警组件
告警能力在Prometheus的架构中被划分为两个独立的部分
- 通过在Prometheus中定义AlertRule(告警规则)，Prometheus会周期性的对告警规则进行计算，如果满足告警触发条件，就会向Alertmanager发送告警信息
- 然后，Alertmanager管理这些告警，包括进行重复数据删除，分组和路由，以及告警的静默和抑制等

### 告警种类
- 去重
- 分组
- 抑制（告警信息之间的依赖关系）
- 静默(暂时不告警)
- 路由(根据不同条件，发送给不同的目标)
### alertmanager部署

```shell
#软件安装
wget https://github.com/prometheus/alertmanager/releases/download/v0.23.0/alertmanager-0.23.0.linux-amd64.tar.gz

# 解压软件
tar xf alertmanager-0.23.0.linux-amd64.tar.gz -C /usr/local
ln -s /usr/local/alertmanager-0.23.0.linux-amd64 /usr/local/alertmanager

# 准备工作
cd /usr/local/alertmanager
mkdir {bin,conf,data}
mv alertmanager amtool bin/
cp alertmanager.yaml conf/
useradd -r -s /sbin/nologin prometheus
chown -R prometheus.prometheus /usr/local/alertmanager
```
创建服务文件
```shell
[Unit]
Description=alertmanager project
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/alertmanager/bin/alertmanager --config.file=/usr/local/alertmanager/conf/alertmanager.yml --storage.path=/usr/local/alertmanager/data --web.listen-address=0.0.0.0:9093
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
User=prometheus
Group=prometheus

[Install]
WantedBy=multi-user.target
```
#### 容器部署

#### Prometheus集成
```shell
vim prometheus.yml
- job_name: "alertmanager"
  static_configs:
    - target:
      - "10.0.0.100:9093"
```
### 告警规则
在Prometheus中一条告警规则主要由以下几部分组成
- 告警名称：用户需要为告警规则命名，当然对于命名而言，需要能够直接表达出该告警的主要内容
- 告警规则：告警规则实际上主要由PromQL进行定义，其实际意义是当表达式查询结果持续多长时间后发出告警

在Prometheus中，还可以通过Group(告警组)对一组相关的告警进行统一定义

#### 告警规则文件示例
```yaml
# 确认包含rules目录中的yaml文件
cat /usr/local/prometheus/conf/prometheus.yml
rule_files:
  - "../rules/*.yml"

# 准备告警rule文件
vim /usr/local/prometheus/rules/prometheus_alert_rules.yml
groups:
  - name: example
    rules:
    - alert: HighRequestLatency
      #expr: up == 0
      expr: job:request_latency_seconds:mean5m{job="myjob"} > 0.5
      for: 10m
      labels:
        severity: warning
        project: myproject
      annotations:
        summary: "Instance {{ $labels.instance }} down"
        description: "{{ $labels.instance }} of job {{ $labels.job }} has been down for more than 1 minutes"
```

#### Alertmanager配置文件
Alertmanager配置文件格式说明
```yaml
# 配置文件总共定义了五个模块：global, templates, route, receivers, inhibit_rules
```
### 告警模版编辑
模版文件使用标准go语法，并暴露了一些包含时间标签和值的变量
该模版必须在alertmanager所在的机器上创建目录，以及建立模版文件
```shell
mkdir /usr/lcoal/alermanager/tmpl

# 基于go的模版内容
vim /usr/local/alertmanager/tmpl/email.tmpl
```
### 告警路由

新版中使用指令`matchers`替换了`match`和`match_re`指令

路由示例
```yaml
route:
  group_by: ['alertname', 'cluster']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 10s
  receiver: 'email'    # 兜底规则，默认路由, 所有规则都不匹配走默认路由
```

通过在Prometheus中给不同的告警规则添加不同的label，再在Alertmanager中添加针对不同的label使用不同的路由至不同的receiver,即可实现路由的分组功能

Alertmanager的相关配置
```yaml
matchers:
  - alertname = Watchdog
  - severity =~ "warning|critical"
```

配置示例
```yaml
# 1.在Prometheus上定制告警规则
groups:
- name: example
  ...

- name: nodes_alerts
  rules:
  - alert: DiskWillFillIn12Hours
    expr: predict_linear(node_filesystem_free_bytes{mountpoint="/"}[1h], 12*3600)
    for: 1m
    labels:
      severity: critital
    annotations: 
      discription: Disk on {{ $label.instance }} will fill in approximately 12 hours
- name: prometheus_alerts
  rules:
  - alert: PrometheusConfigReloadFailed
    expr: prometheus_config_last_reload_successful == 0
    for: 3m
    labels:
      severity: warning
    annotations: 
      discription: Reloading Prometheus configuration has failed on {{ $label.instance }}

# 2.在alertmanager 定制路由
global:
  ...
templates:
  ...
route:
  group_by: ['instance']
  ...
  receiver: email-receiver
  routes:
  - match：
      severity: critical
    receiver: leader-team
  - match_re:
      severity: ^(warning)$
      # project: myproject
    receiver: ops-team
# 新版
#- receiver: 'leader-team'
#  matchers:
#  - severity = "critical"
#- receiver: 'leader-team'
#  matchers:
#  - severity = ^(warning)$

receivers:
  - name: 'leader-team'
    email_configs:
    - to: 'XXXXX@qq.com'
  - name: 'ops-team'
    email_configs:
    - to: 'XXXXX@qq.com'
```

### 抑制告警
配置实例
```yaml

```


### 邮件告警实现
- vim /usr/local/alertmanager/conf/alertmanager.yml
```yaml
# 全局配置
global:
  resolve_timeout: 5m  # 解析的超时时长
  smtp_smarthost: 'smpt.qq.cm:25或465'  # 基于全局块指定发件人信息
  smtp_from: '3140394153@qq.com'
  smtp_auth_username: '3140394153@qq.com'
  smtp_auth_password: 'XXXXXXXXXXX'  # 授权码
  smtp_hello: 'qq.com'
  smtp_require_tls: false     # 启用tls安全，默认true, 此处为false

# 定义模版路径
templates:
  - "../tmpl/*.tmpl" # 相对路径是相对于altermanager.yml文件的路径

# 路由配置
route:
  group_by: ['alertname', 'cluster']  # 分组依据
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 10s  # 此值不要过低，否额短期内会收到大量邮件
  receiver: 'email'  # 指定接收者名称

# 收信人员
receivers:
- name: 'email'  # 这个地方和route->receiver的值匹配
  email_configs:
  - to: 'root@XXXX.com'  # 收件人邮箱 
  send_resolved: true    # 问题解决后也会发送恢复通知

# 抑制规则（可选）
inhibit_rules
```

告警规则语法检查
```shell
amtool check-config /usr/local/alertmanager/conf/alertmanager.ymlj
```

### 微信告警实现

### 钉钉告警实现


## 服务发现

### 文件发现

### DNS发现

### 基于consul集群实现服务发现