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

### 配置客户端发送数据给Pushgateway
- 推送Metric格式
```shell
http://<pushgateway_address>:<push_port>/metrics/job/<jpb_name>/[<label_name>/<label_value>][<label_name>/<label_value>]

# <job_name> 在Prometheus中指标的新加标签exported_<job_name>的值，在Prometheus中是job名称
# <label_name>/<label_value> 将成为额外的标签/值对

# 示例：echo "age 18" | curl --data-binary @- http://10.0.0.118:9091/metrics/job/pushgateway/instance/`hostname -I`
```

- 通用脚本
```shell

```
