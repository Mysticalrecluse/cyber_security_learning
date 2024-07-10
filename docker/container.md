# 容器实现原理
```dockerfile
# 创建实验用镜像
# cat Dockerfile
FROM centos:8.1.1911
RUN yum install -y httpd
COPY file1 /var/www/html/
ADD  file2.tar.gz /var/www/html/
CMD ["/sbin/httpd", "-D", "FOREGROUND"]

# docker build -t <name> -f ./Dockerfile .
```

上述不成功的话，直接运行`docker pull centos/httpd-24-centos8`

```shell
root@ubuntu2204:~/dockerfile$docker exec myhttpd2 ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
default        1  0.4  0.4 350976 18820 ?        Ss   18:57   0:00 httpd -D FOREGROUND
default       36  0.0  0.1 331432  5060 ?        S    18:57   0:00 httpd -D FOREGROUND
default       37  0.1  0.4 1998428 16184 ?       Sl   18:57   0:00 httpd -D FOREGROUND
default       39  0.0  0.4 1867292 16136 ?       Sl   18:57   0:00 httpd -D FOREGROUND
default       41  0.1  0.4 1867292 16136 ?       Sl   18:57   0:00 httpd -D FOREGROUND
default      251  0.0  0.0  44600  3380 ?        Rs   18:58   0:00 ps aux
```

```shell
root@ubuntu2204:~/dockerfile$ps aux|grep httpd
1001       13365  0.1  0.4 350976 18820 ?        Ss   18:57   0:00 httpd -D FOREGROUND
1001       13417  0.0  0.1 331432  5060 ?        S    18:57   0:00 httpd -D FOREGROUND
1001       13418  0.1  0.4 1998428 16184 ?       Sl   18:57   0:00 httpd -D FOREGROUND
1001       13420  0.0  0.4 1867292 16136 ?       Sl   18:57   0:00 httpd -D FOREGROUND
1001       13422  0.0  0.4 1867292 16136 ?       Sl   18:57   0:00 httpd -D FOREGROUND
```

Namespace 其实就是一种隔离机制，主要目的是隔离运行在同一个宿主机上的容器，让这些容器之间不能访问彼此的资源。这种隔离有两个作用：第一是可以充分地利用系统的资源，也就是说在同一台宿主机上可以运行多个用户的容器；第二是保证了安全性，因为不同用户之间不能访问对方的资源。

## Cgroups

主要作用：资源限制

### Cgroups的原理
Cgroups 通过不同的子系统限制了不同的资源，每个子系统限制一种资源。每个子系统限制资源的方式都是类似的，就是把相关的一组进程分配到一个控制组里，然后通过树结构进行管理，每个控制组都设有自己的资源控制参数。

### Cgroups常见子系统
- CPU 子系统，用来限制一个控制组（一组进程，你可以理解为一个容器里所有的进程）可使用的最大 CPU。
- memory 子系统，用来限制一个控制组最大的内存使用量。
- pids 子系统，用来限制一个控制组里最多可以运行多少个进程。
- cpuset 子系统， 这个子系统来限制一个控制组里的进程可以在哪几个物理 CPU 上运行。

对于启动的每个容器，都会在 Cgroups 子系统下建立一个目录，在 Cgroups 中这个目录也被称作控制组
```shell
root@ubuntu2204:~/dockerfile$ll /sys/fs/cgroup/system.slice/|grep docker
drwxr-xr-x  2 root root 0 Jul 10 18:57 docker-765574dfc55276ba79d41f5615b19011ac19d0b3a4b1ddb348eb004f952315fc.scope/
```