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
容器中所有的进程都会存储在这个控制组中`cgroup.procs`这个参数里

#### 通过控制组控制Memory使用量
```shell
# cd /sys/fs/cgroup/memory/system.slice/docker-c5a9ff78d9c1fedd52511e18fdbd26357250719fa0d128349547a50fad7c5de9.scope

# cat cgroup.procs
20731
20787
20788
20789
20791

# echo 2147483648 > memory.limit_in_bytes
# cat memory.limit_in_bytes
2147483648
```


## 容器进程

### 理解init进程
```c
init/main.c

        /*
         * We try each of these until one succeeds.
         *
         * The Bourne shell can be used instead of init if we are
         * trying to recover a really broken machine.
         */
        
        // 如果提供了execute_command命令，即通过内核参数`init=`指定了初始化命令
        // run_init_process会尝试运行这个命令
        if (execute_command) {
                ret = run_init_process(execute_command);
                // 如果命令执行成功，则返回0
                if (!ret)
                        return 0;
                // 命令执行失败，就会触发panic，显示错误，并引发内核恐慌
                panic("Requested init %s failed (error %d).",
                      execute_command, ret);
        }
        // 如果没有指定`execute_command`或它执行失败，代码会尝试
        // 代码会尝试运行常见的初始化进程路径
        // 其中任何一个成功，都会返回0，表示进程启动成功
        // 如果全都失败，就会引发内核恐慌，并输出提示信息
        if (!try_to_run_init_process("/sbin/init") ||
            !try_to_run_init_process("/etc/init") ||
            !try_to_run_init_process("/bin/init") ||
            !try_to_run_init_process("/bin/sh"))
                return 0;


        panic("No working init found.  Try passing init= option to kernel. "
              "See Linux Documentation/admin-guide/init.rst for guidance.");
```

### 如何指定"init="参数
#### 在GRUB引导菜单中指定
如果你的系统使用GRUB作为引导加载程序，你可以在引导时临时指定`init=`参数
- 在启动时进入GRUB菜单（通常通过按下`Esc`，`Shift`或`F2`）
- 选择要启动的内核行，按`e`键进入编辑模式
- 找到以`linux`开头的行，在行末添加`init=/path/to/your/init`
- 按`Ctrl + X`或`F10`启动修改后在内核配置

#### 修改GRUB配置文件
如果你希望永久更改`init`参数，可以修改GRUB配置文件`/etc/default/grub`并更新GRUB配置
```shell
# 编辑/etc/default/grub
# vim /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash init=/path/to/your/init"

```


### `Kill`信号

进程在收到信号后，就会去做相应的处理。对于每个信号，进程对它的处理有下面三个选择
- 第一个选择是`忽略(Ignore)`，就是对这个信号不做任何处理
  - 有两个信号例外：`SIGKILL(9)`和`SIGSTOP(19)`，进程是不能忽略的
  - 他们的主要作用是为Linux Kernel和超级用户提供删除任何进程的特权

- 第二个选择，就是`捕获(Catch)`，这个是指让用户进程可以注册自己针对这个信号的handle。
  - 对于`捕获` `(SIGSTOP)`和`(SIGKILL)`这两个信号也例外，这两个信号不能有用户自己的处理代码，只能执行系统的缺省行为

- 第三个选择，`缺省行为(Default)`,Linux 为每个信号都定义了一个缺省的行为，你可以在 Linux 系统中运行 man 7 signal来查看每个信号的缺省行为。


#### `kill -15`(SIGTERM)
这个信号是Linux命令kill缺省发出的，给一个进程发送信号，在没有别的参数时，这个信号类型默认为SIGTERM

SIGTERM可以被`捕获`，这里的`捕获`指的就是用户进程可以为这个信号注册自己的handler，而这个handler，他可以处理进程的graceful-shutdown问题

#### `kill -1`(SIGHUP)
作用：`kill -1`发送SIGHUP信号，即“挂起”信号(Hangup Signal)

- 重新加载配置：
  - 对于很多守护进程（如`nginx`、`apache`），接收到SIGHUP信号后，它们不会终止进程，而是重新加载配置文件。这对于在不中断服务的情况下，更新配置非常有用
- 终止进程
  - 对与某些进程，SIGHUP信号会导致它们终止。这通常适用于那些没有特别处理SIGUP信号的进程
- 回话终止
  - 最初，SIGHUP信号用于通知终端用户的挂起。例如，当用户断开与中断的连接时，SIGHUP信号会发送到与该终端相关的所有进程，通知它们会话已结束

总结：发送SIGUP信号，通常用于通知守护进程重新加载配置，或者通知会话终止

#### `kill -9`(SIGKILL)
作用：`kill -9`发送SIGKILL信号，即“强制终止”信号(Kill Signal)
- 立即终止进程：
  - SIGKILL信号无法被捕获、阻塞、或忽略。当进程接收到SIGKILL信号时，它会立即被内核终止，无法进行任何清理操作
- 强制杀死进程：
  - 及时进程处于挂起状态，僵尸状态或者无法响应其他信号，SIGKILL也会确保进程被强制终止

总结：强制立即终止进程，不允许进程进行任何清理操作


####
