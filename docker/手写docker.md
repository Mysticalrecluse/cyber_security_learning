# 学习目标
所有容器化底层基于libcontainer

# 容器核心技术

隔离： namespace

资源限制：cgroups

联合文件系统：OverlayFS

# 名称空间Namespace

## PID Namespace
```shell
# unshare: 创建新的命名空间
unshare --uts /bin/bash
```