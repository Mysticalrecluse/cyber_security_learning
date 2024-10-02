# 第三章：访问控制与超级权限
## 文件系统访问控制
为什么chown可以随便更改文件属主，属组的UID和GID，但是不能更改为不存在的用户名和组名

> 答：
因为内核和文件系统以数字形式跟踪属主及组，它们并不使用文本名称。在最基本的情况下，用户标识号（User Identification Number, UID）会在/etc/passwd文件中被映射为用户名，组标识号（Group Identification Number, GID）会在/etc/group文件中被映射为组名（17章中描述了更复杂的选项）
UID和GID所对应的文本名仅仅是为了方便系统的人类用户（human user）使用。如果命令需要以人类可读的格式显示所有权信息，必须在相应的文件或数据库中查找每个名字


### <p style="color:red">待解决问题1</p>
进程所有权：即`real UID/GID`,`effective UID/GID`,`saved UID/GID`
文件系统UID（一般作为网络文件系统 Network File System, NFS的实现细节讲解）通常和effective UID相同

