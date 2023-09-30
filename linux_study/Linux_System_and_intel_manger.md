# 操做系统安装与虚拟机基础配置
## Linux操做系统镜像下载
- ubuntu官网下载
  - 网址：ubuntu.com/download
  - 网址：cdimage.ubuntu.com
  
- ubuntu历史版本：
  - old-releases.ubuntu.com/releases/

- 镜像文件版本选择
```
<OS_name>-<version-number>-<type>-<cpu_arch>.iso
```

## 安装后网卡配置
- 选择版本：ubuntu18.04.6
- 编辑 sudo vim /etc/netplan/01-netcfg.yaml
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: yes
      dhcp6: yes
    enp0s8:
      dhcp4: yes
      dhcp6: yes
      dhcp-identifier: mac
```
- 编辑成功后，执行sudo netplan apply


- https://pan.baidu.com/s/1gjzqIxxF85fctbCHGKhz0A