# UNIX环境高级编程
## UNIX概要
### Unix基础概要
#### Unix的系统架构
- kernel（内核）
- shell（命令解释器）：/bin/sh->bash
- system call（系统调用）
- library routines（库函数）
  - 一定程度上对系统调用（system call）进行封装
- application（应用程序）

#### APUE的实验环境的搭建
- APUE2源代码下载：http://www.apuebook.com
- 保存到你自己的工作目录下（这里以/root为例）解压缩`tar -xvf src.tar.gz`
- `cd apue2e`进入apue2e目录，查看READDME告诉我们linux系统只要修改Make.defines.linux
- `vi Make defines.linux` 修改`WKDIR=/root/apue.2e`就是说工作目录为WKDIR=`/root/apue.2e`
- `cd lib && make -f linux.mk`(生成静态库lib.apue.a，并且复制到/usr/lib目录中)
- 把apue.2e/include/apue.h复制到/usr/include目录中，让gcc编译期间顺利找到头文件apue.h
- 编译单一源文件成功，则gcc -o myls.ls1.c -lapue fig1.3

#### Unix基础知识
- I/O(输入和输出)
  - file descripters
  - unbuffered I /O -------> fig1.4
    - 解释：（无缓冲I/O），每个read和write操做都直接与底层的硬件设备进行通信
    - open
    - read
    - write
    - close
  - buffered I/O --------> fig1.5
    - 解释：（有缓冲I/O），操作系统或运行时库（如C的标准I/O库）为每个文件操作维护一个内存缓冲区，当应用程序执行read和write操作时，它实际上是在读写这个内存缓冲区
    - fopen
    - fread
    - fwrite
  
- Processes(进程)
  - ProcessID(进程号) -------> fig1.6
  - Process Control(进程控制) -----> fig1.7(模拟shell，简单解读)

- Signals(信号)
  - ignored(忽略)
  - allowed to causes the default action(默认行为)
  - caught and transferred to a user defined funcgtion(捕获信号来处理)-------> fig1.10

- User Identification(用户标识)
  - UserID & GroupID

- UNIX Times(时间)
  - Calend ar time date +%s
  - Process time: time grep -r _POSIX /usr/include > /dev/null (常用于测量一个命令的运行时间)

## 文件IO和标准IO
### 文件IO
#### 不带缓冲的IO
- 概念：指每个read和write这些文件IO操作都调用的是系统调用，属于内核态的操作

#### 文件描述符
- 对于内核而言，所有打开的文件，都是通过所谓的文件描述符来进行引用的

- Operations on file descriptors: 
  - The following lists typicals operations on file descriptors on modern Unix-like systems.Most of these functions are declared in the <unistd.h>header,but some are in the <fcntl.h>header instead.


- Creating file descriptors
  - open()
  - create()
  - socket()
  - accept()
  - socketpair()
  - pipe()
  - opendir()

- Deriving(推导) file descriptors
  - dirfd()
  - fileno()

- Operations on a single file descriptor
  - read(), write()
  - readv(), writev()
  - pread(), pwrite()
  - recv(), send()
  - recvmsg(), sendmsg()
  - sendfile()
  - lseek()
  - fstat()
  - fchmod()
  - fdopen()
  - fchown()
  - fsync()
  - fdatasync()
  - fstatvfs()
  - dprintf()


- Operations on multiple file descriptors
  - select(), pselect()
  - poll()
  - epoll()
  - kqueue()

- Operations on the file descriptor table
  - close()
  - closefrom() [BSD and Solaris only; deletes all file descriptors greater than or equal to specitied number]
  - dup() [duplicates and existing file descriptor guaranteeing to be  the lowest number available file descriptor]
  - dup2() (the new file descriptor will have the value passed as an argument)
  - fcntl (F_DUPFD)

- operations the modify process state
  - fchdir
  - mmap()

- File locking
  - flock()
  - fcntl()
  - lockf()

- Sockets----(网络编程中讲解，这里不展开)


- cat示例
```C
#include "apue.h"

#define BUFFSIZE      4096
int main() {
    int n;
    char buf[BUFFSIZSE];
    // 这里STDIN_FILENO的宏，在/usr/include/unistd.h
    // #define STDIN_FILENO  0  /* Standard input */
    // #define STDOUT_FILENO  1  /* Standard output */
    // #define STDERR_FILENO  2  /* Standard error */
    while((n = read(STDIN_FILENO, buf, BUFFSIZE)) > 0)
        if (write(STDOUT_FILEON, buf, n) != n)
            err_sys("write error");
    if (n < 0)
        err_sys("read error");
    exit(0);
}
```