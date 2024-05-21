# Nginx Error
```shell
nginx: [error] open() "/apps/nginx/logs/nginx.pid" failed (2: No such file or directory)

# 问题：nginx未启动
# 解决：nginx && systemctl start nginx
```

```shell
nginx: [emerg] getgrnam("nobody") failed in /apps/nginx/conf/nginx.conf:1

# 问题：nginx中，main模块的属主属组有问题
# 解决：更改属主属组
```

```shell
0: *110586 open() "/apps/nginx/html/50x.html" failed (24: Too many opoen files). client: 10.0.0.7, server: localhost, request: "GET / HTTP/1.0", host:"10.0.0.8"

# 问题：默认nginx配置不支持高并发，会出现该错误日志
# 解决：扩大连接数，启用防惊群优化，启动多路复用（multi_accpet on）
# 扩大链接数，要同时扩大外面的内核参数和nginx本身的进程最大连接数，避免nginx的最大连接数没问题，但是内核参数限制出现问题
```