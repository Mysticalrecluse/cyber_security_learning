# 二进制安全学习规划
## Hacking三步曲
### 理解系统（Understanding）
- 系统性地基础课程学习，深入理解计算机系统运作机制

- 基础课程学习
  - 核心基础课程-计算机的工作原理
    - 体系结构
      - CPU的设计与实现
        - 机器指令与汇编语言
        - 指令的解码、执行
        - 内存管理
      - CMU 18-447 Introduction to Computer Architecture
        - https://www.ece.cmu.edu/~ece447/s15/doku.php
        - 视频：https://course.ece.cmu.edu/~ece447/s15/doku.php?id=schedule
        - Labs: Implement a MIPS CPU using Verilog
    - 编辑原理
      - 编辑器的设计与实现
        - 自动机、词法分析、语法分析
        - 运行时
        - 程序静态分析
      - Stanford CS143-Compilers
        - http://web.stanford.edu/class/cs143
        - PA: Compilers for Cool language
    - 操作系统
      - 操作系统的设计与实现
        - 系统的加载与引导
        - 用户态与内核态、系统调用、中断和驱动
        - 进程与内存管理、文件系统
        - 虚拟机
      - MIT 6.828-Operating System Engineering
        - https://pdos.csail.mit.edu/6.828/2016
        - Labs:Implement jos
        - Xv6. a simple Unix-like teaching operating system
  - 系统软件开发基础
    - 编程语言
    - 网络协议
    - 算法与数据结构
### 破环系统（Breaking）
- 学习与创造漏洞挖掘与利用技巧
- CTF历史资料库：https://github.com/ctfs

- Wargames
  - http://pwnable.kr/
  - http://smashthestack.org/

- 漏洞挖掘与利用实战-目标
  - 网络协议的实现
    - HTTP/SMB/DNS/UPnP Server
  - 脚本引擎
    - JavaScript Engine
    - ActionScript Engine
    - PHP/Java Sandbox Escape
  - 内核
    - Linux/Android
    - Freebsd
    - Apple iOS
    - Sony PS4
### 重构系统（Reconstruction）
- 设计与构造系统防护