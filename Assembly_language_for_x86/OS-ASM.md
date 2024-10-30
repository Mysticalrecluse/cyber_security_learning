# 汇编篇1
## 汇编、CPU架构、硬编码之间的关系
### CPU架构
#### CISC
CISC 复杂指令集
- (Intel、AMD CPU)
  - x86架构     32位CPU
  - x64架构     64位CPU

#### RISC
RISC 精简指令集
- ARM
  - MAC、Intel x86 -> ARM架构（M1、M2）

### 汇编
指令集 --> 汇编 <-- 机器码
```asm
; C
int a = 10
; CISC


; RISC
```

### 硬编码
CPU只认识0101...，0101是什么


硬编码、机器码
- 指令集的本质是硬编码（即机器码）
```C
// ConsoleApplication1.cpp : 定义控制台应用程序的入口点。
// 反汇编

#include "stdafx.h"
#include <stdlib.h>

//001513C0 内存地址
// 55机器码 
void test() {
001513C0 55                   push        ebp  
001513C1 8B EC                mov         ebp,esp  
001513C3 81 EC CC 00 00 00    sub         esp,0CCh  
001513C9 53                   push        ebx  
001513CA 56                   push        esi  
001513CB 57                   push        edi  
001513CC 8D BD 34 FF FF FF    lea         edi,[ebp-0CCh]  
001513D2 B9 33 00 00 00       mov         ecx,33h  
001513D7 B8 CC CC CC CC       mov         eax,0CCCCCCCCh  
001513DC F3 AB                rep stos    dword ptr es:[edi]  
	int a = 10;
001513DE C7 45 F8 0A 00 00 00 mov         dword ptr [a],0Ah  
}

// Windows 0x55 --> push ebp
// Linux 0x55 --> push ebp
// CPU架构是一样的(X64兼容X86)
// 只要是同一个CPU，干同一个事情，汇编风格随便，生成的机器码都一样
```
硬编码是如何生成的(指令集的规范)
```asm
; 推荐文章（了解硬编码规范）
https://blog.51cto.com/u_15127590/4549268
```

汇编 --> 机器码  编译
机器码 --> 汇编  反汇编

总结：不同CPU架构的指令集不同，而汇编到硬编码之间的对应关系即使指令集的表现形式


## 使用工具
### OD(ollydbg)
下载链接
```
https://pan.baidu.com/s/1EZUBZwR4d2CbT2UDSsp4rg
```

#### OD的使用


### Windows: Visual Studio 2013
```
https://pan.baidu.com/s/1RWWIqO9ft88SynKrp11i6Q
```

## MASM、NASM、ATT、ARM之间的关系
MASM(CISC)：
- Windows默认的汇编风格

NASM(CISC)：后续主要学习风格
- 对MASM做了优化：比如大小写敏感，主要用于Linux平台
- 我们Windows内核的汇编风格就是NASM

ATT(CISC)
- Linux默认的汇编风格
  - Windows内核，使用的是.asm结尾的汇编文件编写
  - linux内核，使用的是.s结尾的汇编文件编写
  - 在Linux平台下，单纯的写汇编：NASM，ATT都可以
  - C语言中内联汇编，只能使用ATT
  - 扩展
  ```
  内联汇编（Inline Assembly）是一种在高级编程语言（如C/C++）中嵌入汇编指令的技术，允许程序员在高级代码中直接编写和执行汇编代码。这样可以在特定的代码部分精细控制底层硬件，或者优化代码性能。
  ```

ARM(RISC)
- IOT设备，非PC

## 汇编、C语言、C++、Java之间的关系

- 打孔机时代：只能做简单的事情，编码很困难 1001 1001
- 机器码时代：55 88 12
- 汇编时代：push ebp + 汇编编译器
- C时代(1950)： int a = 10; + C编译器（GCC），面向过程
- C++时代：已经基本比较成熟了，但是学习成本高，因为可以直接操作内存，需要学习指针，内存，很容易出现内存错误，而通常内存错误难以排查，因为它有时候正确，有时候又不正确
  - C和C++时代，程序员之间的水平差异很大很明显

- 2010年（前后）：三大语言鼎力：PHP，.net，Java
  - php的虚拟机：zend engine(中东写的)，高级语言，屏蔽了内存操作
  - .net:
  - java：Hotspot，高级语言，编译型语言

- go,java云原生
  - go --> 机器码

## 寄存器、CPU缓存、内存之间的关系
- CPU
  - 寄存器: 中间存储单元
  - CPU缓存
  - 内存

## CPU三组寄存器及常用汇编指令
### 通用寄存器
通用寄存器可以看到

- EAX
- EBX
- ECX
- EDX
- ESI
- EDI


- EIP

- ESP
- EBP


### 段寄存器
段寄存器可以看到
指向一个内存段

- CS: code segment 代码段
- SS: Stack segment 栈段

### 控制寄存器 
控制寄存器看不奥
- CRO
  - CPU最开始从实模式 --> 进入保护模式，CPU想进入保护模式，就得操控CRO寄存器
- CR1
- CR2
  - 一旦程序发生了内存错误，他肯定是调到中断里面，中断如何知道哪段内存发生错误？这个只有CPU知道，CPU会把那个内存地址写到CR2中，如果要修复内存错误，必须会这个寄存器
- CR3
  - 虚拟内存，页表的位置
- CR4
  - 控制大小页

### 状态寄存器 eflags
状态寄存器可以看到

EFL：eflags，

### 浮点寄存器

### 使用工具
- OD(ollydbg)
  - 逆向分析软件
  - 调试器
    - 以调试的方式打开
    - attach
  - OD快捷指令
    - F2 下断点
    - F7 单步步入


- VS
- Clion(重要)
  - Clion里看寄存器，实际就是使用gdb：info registers，缩写I R
- GDB(重要)


## 数据宽度
![alt text](images\image1.png)

64位寄存器         32位寄存器       16位寄存器     8位寄存器
%rax  ------------ %eax ---------- %ax ----------%ah,%al

上述位数就是数据宽度

### mov
mov: 将数据存入寄存器
```asm
mov eax, 0x12345678   ;向eax放入0x12345678
; ax = 0x5678 ah = 0x56 al=0x78
add
```

### xor
给寄存器清零
```asm
xor eax, eax
```

### jmp
jmp + 地址：程序跳转到指定的内存地址
```asm
jmp <addr>
```

### sub
示例
```asm
sub eax, 0
; 将eax的值和0相减，结果存储到eax中，但结果不会影响eflags
```
### JCC
任何语言的底层，循环结果及条件判断，都是基于eflags寄存器 + JCC指令实现的

- JZ/JE
  - 中文含义：若为0则跳转，若相等则跳转
  - 英文原义：jump if zero; jump if equal
  - 检查符号位：ZF = 1
  - 对应C语言：if(i == j); if(i == 0);

- JNZ/JNE
  - 中文含义：若不为0则跳转，若不相等则跳转
  - 英文原意：jump if not zero; jump if not equal
  - 检查符号位：ZF=0
  - if(!i == j); if(!i == 0);

- JS
  - 中文含义：若为负则跳转
  - 英文原意：jump if sign
  - 检查符号位：SF = 1
  - if(i < 0);

- JNS
  - 中文含义：若为正则跳转
  - 英文含义：jump if not sign
  - 检查符号位：SF = 0
  - if(i > 0);

- JP/JPE
  - 中文含义：若1出现次数为偶数则跳转
  - 英文含义：jump if Parity (Even)
  - 检查符号位：PF = 1
  - (NULL)

- JNP/JPO
  - 中文含义：若1出现次数为奇数则跳转
  - 英文原意：jump if not parity (ODD)
  - 检查符号位：PF = 0
  - (NULL)

- JO
  - 中文含义：若溢出则跳转
  - 英文原意：jump if overflow
  - 检查符号位：OF = 1
  - (NULL)

- JNO
  - 中文含义：若无溢出则跳转
  - 英文原意：jump if not overflow
  - 检查符号位：OF = 0
  - (NULL)

- JC/JB/JNAE
  - 中文含义：若进位则跳转；若低于则跳转；若不高于等于则跳转
  - 英文原意：jump if carry; jump if below ; jump not above equal
  - 检查符号位：CF = 1
  - if(i < j)

- JNC/JNB/JAE
  - 中文含义：若无进位则跳转；若不低于则跳转，若高于等于则跳转；
  - 英文原意：jump if not carry; jump if not below; jump above equal
  - 检查符号位：CF = 0
  - if(i >= j)

- JBE/JNA
  - 中文含义：若低于等于则跳转，若不高于则跳转
  - 英文原意：jump if below equal; jump if not above
  - 检查符号位：ZF = 1 或 CF = 1 
  - if(i <= j);

- JNBE/JA
  - 中文含义：若不低于等于则跳转，若高于则跳转
  - 英文原意：jump if not below equal; jump if above
  - 检查符号位：ZF = 0 或 CF = 0
  - if(i > j);

- JL/JNGE
  - 中文原意

### cmp
本质上做减法运算
cmp eax, 0等价于sub eax, 0
差别是cmp的运算结果只会改eflags寄存器，不会修改eax寄存器
通常配合JCC指令使用实现条件跳转



### test
本质上做与运算


### 练习
1. 用一个寄存器实现加法：1+2、1+2+3
```asm
mov ah, 1
mov al, 2
add al, ah
```

```asm
xor eax eax
mov ax, 1
add ax, 2
add ax, 3
```
2. 用多个寄存器实现加法：1+2+3+4
```asm

```

3. 实现C语言中的if...else...
```C
int i = 10
if (i == 10) {
    i = 11;
}
i = 12;
```

```asm
xor eax, eax
mov eax, 10
cmp eax, 10
je  <addr>     ;+3
mov eax, 12    ;3
mov eax, 11
```

4. 实现while true;
