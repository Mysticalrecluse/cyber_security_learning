# C语言应试部分
## 环境配置
### Windows
- 相关软件安装
  - DEV CPP 6.7.5
    - 安装时，直接根据引导，走默认配置，即可安装成功
    - 安装后，软件配置
    ```
    工具 -> 编辑器选项 -> 更改tab缩进，改为自动计算缩进量，1个tab等于4个空格

    原因：不同的编译环境，tab键的宽度可能不同，为了让代码在不同的环境下显示不一样，因此统一改为一个tab等于4个space
    ```
    - 注意事项：如果后期发现，代码逻辑和程序执行结果不一致，在代码正确的情况下，删除之前生成的可执行程序，重新编译运行即可
### Linux
- 配置云主机
```bash
在购买云主机(Ubuntu2004)，安装好tabby，并实现远程连接之后

1. 执行以下命令，确保自己在root用户下执行命令
sudo -i

2. 执行下面的命令
apt update
apt upgrade -y
apt install wget -y
wget http://123.57.102.65/data/init_env.sh

3. 执行下面的命令，完成环境配置
bash init_env.sh
```

- 查看C语言使用方法
  - man手册
  ```bash
  man -f < C_command >

  man -K command # 查看带command关键字的命令

  # 在vim中直接查看man手册
  shift + [n]K # 默认n=1，查看第n章手册

  # 彩色man手册
  - 配置 ~.bashrc
  搜索：plugins
  插入新插件
  plugins=(... colored-man-pages)
  ```
  - tldr (too long don't read)
    - 更好用的命令手册，只能查询shell命令

## C语言参考
- 查询手册网站：`zh.cppreference.com`

## 编码规范

## 类型、运算符与表达式
### 类型与变量
#### 计算机中的数据存储方式
- 计算机存储数据的基本单位：字节（byte）

- 计算机中表示数据的基本单位：位（bit）
  - 1byte = 8bit
  - 一个整型数据(int)占4个字节，相当于需要4个连续的地址来存储一个整型数据，共32位
  ```
  系统会分配4个连续的字节来存储这个整型的值。每个字节有一个唯一的内存地址，所以这个整型变量的值将占据这四个连续地址
  ```
#### 整型
- 整型(int)
  - int -> 4个字节   
  - 占位符：%d
  - 大小：4字节，32位
  - 范围：-2^31(-2147483648) ~ 2^31-1(2147483647)
  - 计算机中表示整型数据的相关规则
  ```
  00000000 00000000 00000000 00000000

  1. 第一位是符号位
  2. 负数：补码表示法，即取反加1
  3. 补码的优势：
     把十进制的减法等价于二进制的加法
      7 - 2 = 7 + (-2)
     (0111) + (1110) 结果截断后4位：0101
  4. 所以在计算机中，不管是减法还是加法，本质上都是加法
  ```

- 整型(long long)
  - 格式占位符：%d
  - 大小：8字节，64位
  - 范围：-2^63 ~ 2^63-1

#### 浮点型
- 单精度浮点数(float)
  - 格式占位符：%f
  - 大小：4字节，32位
  - 有效数字：7位
  ```
  有效数字：从第一个非0数字开始算，一共多少位
  例如；0.000123  有效数字为3位
  ```

- 双精度浮点型(double)
  - 格式占位符：%lf
  - 大小：8字节，64位
  - 有效数字：15位

#### 字符型
- 字符型(char)
  - 格式占位符：%c
  - 大小：1字节，8位
  - 编码方式：ASCII编码
    - 字符到数字的对应关系：即：编码规则 
  - C语言中，字符用单引号括起来（例如：'a'）
  ```
  需记忆的知识点
  1. 'A' -> 65
  2. 'a' -> 97
  3. '0' -> 48
  ```

#### 示例：
```C
#include<stdio.h>
#include<inttypes.h>

int main() {
    int a = 123, b = 97, c, d;
    c = 100062;
    d = 9651;
    printf("%d %d %d %d\n",a,b,c,d);
    a = 2147483647 + 1;
    printf("%d\n",a);
    printf("INT32_MIN = %d\n", INT32_MIN);
    printf("INT32_MAX = %d\n", INT32_MAX);
    long long e;
    e = INT32_MAX + 1;
    printf("%lld\n", e);  //-2147483648
    // 疑问点1
    float f = e2 + 0.1;
    double ff = e2 + 0.123456789;
    double fff = e2 + 0.123456789;
    printf("float : %f\n", f);
    printf("double : %lf\n", ff); //2147483648.123457
    // 疑问点2
    printf("double : %.9lf\n",fff); //2147483648.123456955
    char g = 'a';
    printf("g = %c\n",g);
    printf("g = %d\n",g); // 97，用整型占位符表示字符
    printf("g + 5= %c\n", g + 5); // 'f'
    printf("sizeof(int) = %lu\n", sizeof(int)); // 4 sizeof()查看类型大小
    printf("sizeof(long long) = %lu\n", sizeof(long long)); //8
    printf("sizeof(float) = %lu\n", sizeof(float)); //4
    printf("sizeof(double) = %lu\n", sizeof(double)); //8
    printf("sizeof(char) = %lu\n", sizeof(char)); //1
    // %lu 是unsigned long int类型的占位符
    return 0;
}
```
- 疑问点1：变量e声明了长整型，为什么下面的公式命名结果不超范围，却没有得到准确的值
  - 答：因为计算机在计算下面公式`INT32_MAX + 1`的时候，默认将两个数按`int32_t`的类型进行的计算，计算出的结果，因为超出了int32_t的范围，因此得到`-2147483648`然后赋值给长整型`变量e`
  - 更改后代码
  ```C
  #include<stdio.h>
  #include<inttypes.h>

  int main() {
    long long e;
    e = 2147483647LL + 1;
    // 将其中一个数字标记为长整型
    // 如果一个公式中有个较大数据类型，那么计算规则就会按较大数据类型的进行计算
    printf("%d",e); //2147483648
  }
  ```
- 疑问点2：为什么`double ff`的值小数点后面只有6位：
  - 答：默认情况下，float和double在计算机中，小数点后只显示6位，如果想全部显示小数位，需要在` %f | %lf `前加`.n`，即`%.nf | %.nlf`
### 输出&输入函数
#### 输出函数
- printf函数
  - 头文件：<stdio.h>
  - 原型：int printf(const char *format,...);
    - format : 格式控制字符串
    - ... : 可变参数
    - 返回值：输出字符的数量

- 示例：
```C
#include<stdio.h>

int main() {
    int n1, n2;
    n1 = printf("hello world\n");
    printf("%d\n",'\n');
    int a = 123;
    n2 = printf("hello world: %d\n",a);
    printf("%d,%d\n",n1,n2);

    return 0;
}
```

#### 输入函数说明
- scanf函数
  - 头文件：stdio.h
  - 原型：int scanf(const char *format, ...);
  - format : 格式控制字符串
  - ... : 可变参数列表
  - 返回值：<font color=tomato>成功读入的参数个数</font>
    - 当scanf读到文件末尾，没有任何返回值时，返回-1
    - `printf("EOF=%d",EOF); // -1`
    - EOF的返回值也为-1
    - 在交互模式下，按ctrl+d也表示告诉计算机程序结束，后面所有scanf返回值都为-1
    - Linux和Mac中是ctrl+d; Windows中是ctrl+z

- 代码示例
```C
#include<stdio.h>

int main() {
    int a, b, n;
    n = scanf("%d%d",&a, &b); //'&' is address
    printf("a=%d,b=%d,n=%d\n",a,b,n);
    n = scanf("%dabc%d",&a, &b);
    printf("a = %d, b = %d, n = %d\n",a,b);
    printf("format scanf, input %%dabc%%d: ");
    n = scanf("%dabc%d",&a, &b);
    // input 124abc345
    printf("a = %d, b = %d, n = %d\n",a ,b ,n);
    // output a = 124, b = 345, n = 2
    return 0;
}
```

#### 扩展1：字符串
- 定义字符串
```C
#include<stdio.h>

int main() {
  // 给字符数组赋值
  // 方式1：
  char s[100] = "hello world";
  // 定义了一个能存储99个字符的字符串数组
  // 之所以是99，是因为字符串数组通常以\0结尾，所以是100-1
  printf("%s\n",s); // hello world

  // 方式2：
  scanf("%s",s);
  printf("scanf s : %s\n",s);
  // 输入：hello bilibili
  // 输出；hello
  // 原因：scanf遇到空格会截断
  return 0;
}
```
- 解决scanf读取字符数组遇空格截断的问题
```C
#include<stdio.h>

int main() {
  char s[100];
  scanf("%[^\n]",s);
  // %[],表示格式占位符集合，只有集合中的元素可以被读入到字符数组
  printf("s = %s\n",s);

  return 0;
}
```
- 字符串本质
```
当你声明了一个如 char s[100]; 的数组，无论你存储了什么数据，或者是否完全使用了数组的所有元素，这个数组分配的空间都是100个字节。数组 s 将占据100个连续的字节的内存空间，从 s[0] 到 s[99]。

在你声明数组之后，每个元素都会被分配存储空间，即使你没有显式地初始化它们。如果数组是自动存储类（在函数内部声明而没有用 static 修饰），那么它的元素默认是未初始化的，它们的值是未定义的，可以包含任何垃圾值。如果数组是静态或全局的，所有的元素将默认初始化为0。
```
#### 扩展2：sscanf & ssprintf
- sscanf
```C
#include<stdio.h>

int main() {
  char s[100] = "123 456 789";
  int a, b, c;
  sscanf(s,"%d%d%d", &a, &b, &c);
  // 从字符串中读取数据
  printf("a = %d, b = %d, c = %d\n",a,b,c);

  return 0;
}

// 输出：a = 123, b = 456, c = 789
```

- sprintf
```C
#include<stdio.h>

int main() {
  char str[100] = "192.168.1.245";
  int a, b, c, d;
  sscanf(str,"%d.%d.%d.%d", &a, &b, &c, &d); // 格式化读入
  sprintf(str,"%d:%d:%d:%d", a, b, c, d);
  // 将打印的值输入到str[100]数组中，而不会输出到屏幕上
  printf("str = %s\n",str);

  return 0;
}

// 输出：str = 192:168:1:245
```

- 总结：
  - sscanf 本质上是将字符串信息 --> 转换成 --> 其他类型信息
    - 上述示例(ip转换)中：将字符串信息转换为4个整型信息
  - sprintf 本质上是将其他类型信息 --> 转换成 --> 其他类型信息

####  扩展练习：
- 给输出的内容加一个漂亮的框框
```C
#include<stdio.h>

int main() {
  char s[100], t[100];
  scanf("%[^\n]", s);
  printf("%s\n", s);
  int n = 0;
  n = sprintf(t, "| %s |", s); // 得到上边沿的长度
  for (int i = 0; i < n; i++) printf("-");
  printf("\n");
  printf("| %s |\n",s);
  for (int i = 0; i < n; i++) printf("-");  
  printf("\n");

  return 0;
}
```
- 扩展中出现的提示
```C
p3.soild.c: In function ‘main’:
p3.soild.c:14:21: warning: ‘%s’ directive writing up to 99 bytes into a region of size 98 [-Wformat-overflow=]
   14 |   n = sprintf(t, "| %s |", s); // 得到上边沿的长度
      |                     ^~     ~
p3.soild.c:14:7: note: ‘sprintf’ output between 5 and 104 bytes into a destination of size 100
   14 |   n = sprintf(t, "| %s |", s); // 得到上边沿的长度
      |       ^~~~~~~~~~~~~~~~~~~~~~~

// 这个提示的含义是警告可能出现缓冲区溢出的风险
// 因为s[100]一共能保存0-99个字符
// sprintf(t,"| %s |",s);
// 这里s中的字符串+5（这里因为是接收一个字符数组，加上t本身一共是2个\0的截断字符）个字符返回给t，导致t最多可以存放5-104个字符
// 因此t[100]就可能出现溢出，建议改为t[105],此时就不会出现报错
```
### 运算符与表达式
#### 算术运算符
- 重点：`除法`
  - 向0取整
  ```C
  #include<stdio.h>

  int main() {
    int a = 7, b = 2;
    printf("%d",a/b); // 3
    printf("%d",(-a)/2); // -3
  }
  ```
  
#### 位运算
- 按位与 '&'
```C
0110
1011
---- &(都为1，结果才为1)
0010

// 总结：按位与运算：遇1不变，遇0归0
```
- 按位或 '|'
```C
0110
1011
---- &(都为0，结果才为0)
1111

// 总结：按位或运算：遇0不变，遇1归1
```
- 异或 '^'
```C
0110
1011
---- ^(相同为0，不同为1)
1101

// 总结：异或运算：统计相应二进制位上1的奇偶性
// 总结2：异或运算：自己是自己的逆运算
// a ^ b = c; a ^ c = b; b ^ c = a(即，任意两个数可以得到第三个数)
```
- 异或运算的扩展应用：两数交换
```C
// 两数交换
a ^= b; b ^= a; a ^= b; 
```
- 取反 '~'
```C
a = 101
~a = 010 

//用法：原码取反+1 = 负数
```
- 应用2：取得二进制中最后一位1的位权
```C
示例：
原数：01011001000
负数：10100111000（取反+1）
------------------------- & 按位与计算
得到：00000001000

// 成功得到最后一个1的位权
```
- 左移 '<<'
```
向左移位，末尾补0

// 相应的数字*2
```
- 右移 '>>'
```
向右移位，末尾补符号位

// 相应的数字/2（向下取整）
// 比如：a = -5; a >> 1 = -3
```
#### 运算符优先级
![Alt text](images/image01.png)
- 结合性：
  - 即同等级运算符情况下的计算顺序
- 示例：
```C
#include<stdio.h>

int main() {
  int a = 1, b = 2, c = 3, d = 4;
  a = b = c = d; // a = 4, b = 4, c = 4, d = 4
  // 从右到左，依次赋值
  return 0;
}
```

#### 常用数学函数库
- 头文件：math.h

- pow:指数函数
  - 头文件：math.h
  - 原型：`double pow(double a, double b);`
  - a: 底数
  - b: 指数
  - 返回值: 返回a^b的结果
  - 例子：`pow(2,3) = 8`

- sqrt: 开平方函数
  - 头文件: math.h
  - 原型: double sqrt(double x);
  - x: 被开放数
  - 返回值: 返回x^1/2的结果
  - 例子：sqrt(16) = 4

- ceil: 向上取整
  - 头文件: math.h
  - 原型: double ceil(double x);
  - x: 某个实数
  - 返回值: 返回[x]的结果
  - 例子: ceil(4.1) = 5

- floor: 向下取整
  - 头文件: math.h
  - 原型: double floor(double x);
  - x: 某个实数
  - 返回值: 返回[x]的结果
  - 例子: floor(-4.6) = -5

- abs: <font color=tomato>整数</font>绝对值函数
  - 头文件: stdlib.h
  - 原型: int abs(int x);
  - x: 某个整数
  - 返回值: 返回|x|的结果
  - 例子：abs(-4) = 4
  - 注意: <font color=tomato>x的取值必须是整数</font>

- fabs: 实数绝对值函数
  - 头文件: math.h
  - 原型: double fabs(double x);
  - x: 某个实数
  - 返回值: 返回|x|的结果
  - 例子: fabs(-4.65) = 4.65

- acos: 角度余弦值换算弧度值
  - 头文件: math.h
  - 原型: double acos(double x);
  - x: 角度的余弦值
  - 返回值: 以弧度值返回arccos(x)的结果
  - 例子：acos(-1) = 3.1415926...
  - 应用：使用acos可以得到精确的PI值，180°的余弦是-1，对应的弧度是PI
### 实战题
- HZOJ已提交

## 控制流
### 短路原则
- 概述：通过前面的表达式就可以确定整体表达式的值，就不再计算后面的表达式

- 短路表达式的合法性：即&&，||，左右两边的表达式能判断boolean值即可

- 示例：
```C
#include<stdio.h>

int main() {
    int a, b;
    scanf("%d%d", &a, &b);
    a < b && printf("YES\n");
    a < b || printf("NO\n");

    return 0;
}
```

### 分支结构
#### if语句
- 基础用法示例：
```C
#include<stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n == 0) printf("HEHE\n");
    else if (n > 0 && n < 60) printf("FALL\n");
    else if (n >= 60 && n < 75) printf("MEDIUM\n");
    else if (n >= 75 && n <= 100) printf("GOOD\n");
    else printf("It's Wrong\n");
    return 0;
}
// 注意：if (表达式) 不加大括号的前提下，只能执行“一条语句”
```
- if (表达式) 后跟复合语句示例
```C
if (表达式) {
    代码段;
}
```
```C
if (表达式) {
    代码段;
} else {
    代码段：
}
```
```C
if (表达式1) {
    代码段1;
} else if (表达式2) {
    代码段2;
} else {
    代码段3;
}
```

#### switch case 语句
- 基础结构示例
```C
switch (a) {          // a 为表达式
  case v1: 代码块1;   // v1 为值
  case v2: 代码块2;   // v2 为值
  case v3: 代码块3;   // v3 为值
  ...
  default: 代码块n;
}
// 每个代码块以break;结束
```
- 代码示例：
```C
#include<stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    switch (a) {
        case 1: printf("case a = 1\n"); break;
        case 2: printf("case a = 2\n"); break;
        case 3: printf("case a = 3\n"); break;
        case 4: printf("case a = 4\n"); break;
        default: printf("default value\n"); break;
    }
    return 0;
}
```
- 综合示例（判断某年某月天数）：
```C
#include<stdio.h>

int main() {
    int y, m;
    scanf("%d%d", &y, &m);
    switch (m) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12: printf("31\n"); break;
        case 2: {
            if ((0 == y % 4 && y % 100 != 0) || (0 == y % 400)) {
                // 闰年
                printf("29\n");

            } else {
               // 不是闰年
                printf("28\n");
            }
        }
        break;
        case 4:
        case 6:
        case 9:
        case 11: printf("30\n"); break;
        default: printf("error\n"); break;
    }
    return 0;
}
// 在C语言中, case不支持多选一
```
- 综合示例（判断某年某月天数）解法2：
```C
#include<stdio.h>

int main() {
    int y, m, a;
    scanf("%d%d", &y, &m);
    a = (y % 4 == 0 && y % 100) || y % 400 == 0; // 重点
    if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) {
        printf("31\n");
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
        printf("30\n");
    } else {
        printf("%d\n", 28 + a);
    }
    return 0;
}
```

#### CPU的分支预测
- 知识点1：逻辑值的归一化
```C
!!(x)  // 无论x值为多少，经过两次！，值都为1

#define likely(x)
// __builtin_expect(!!(x), 1)，
// 1是告诉CPUx的值大概率为真，优先把x作为真值去计算
#define unlikely(x)
// __builtin_expect(!!(x), 0)
// 0是告诉CPUx的值大概率为假
// likely 代表x经常成立
// unlikely(x) 代表x不经常成立
```
- 知识点2：CPU执性一条语句的5个步骤解析
```
对于程序中的每一条语句的执行
对应到CPU内部，就是CPU在执行这条语句
CPU执行一条语句需要5个步骤：
1. F(Fetch)     
取指
意义：取指阶段涉及从内存中读取指令。CPU 使用程序计数器（Program Counter, PC）来跟踪当前正在执行的指令的内存地址。
运行方式：程序计数器指向下一条要执行的指令。CPU 读取这个地址上的数据，这些数据就是要执行的指令。读取完成后，程序计数器更新为下一条指令的地址。

1. D1(Decode 2) 译码器是CPU的组件之一
译码阶段1
意义：译码阶段涉及解析取出的指令，确定它是什么操作并了解所需的操作数。
运行方式：指令被送往译码器，译码器分析指令的各个部分，如操作码（OpCode，指示执行何种操作）和操作数地址。

1. D2（D2, Decode 2 或 Operand Fetch）
译码阶段2-操作数读取
意义：这个阶段是为了从寄存器或内存中获取指令操作的数据。
运行方式：CPU 根据译码阶段确定的地址，从寄存器文件或内存中读取操作数。这些操作数是执行指令所需的数据。

1. EX （Execute） 
执行
执行（EX）阶段：执行阶段是流水线中的一个关键步骤，此时 ALU 或其他专用硬件执行实际的操作。具体来说，这可能包括算术运算、逻辑运算、地址计算、数据比较等。例如，如果指令是一个加法指令，ALU 将完成加法运算；如果是一个分支指令，可能涉及到比较运算并根据结果改变程序计数器的值。

控制信号：控制单元在 EX 阶段发出的控制信号确保 ALU 执行正确的运算，并确保数据从正确的源（如寄存器或内存）传送到 ALU，并将运算结果传送到正确的目的地。

控制单元的角色：在整个指令执行过程中，控制单元（Control Unit, CU）负责解释指令并生成相应的控制信号。这些控制信号决定了 CPU 的其他部件如何响应当前执行的指令。

编译器的角色：编译器在程序被执行之前起作用，它负责将高级语言代码转换成机器指令。在指令被执行时，编译器的工作已经完成，此时 CPU 正在执行编译器生成的机器指令。

5. WB  
写回
意义：写回阶段涉及将执行结果写回到寄存器或内存。
运行方式：执行的结果（如计算的数据或处理的状态信息）被写回到指定的寄存器或内存地址中，以便后续指令使用。

```
- 总结现代 CPU 中的指令处理流程
  - <font color=tomato>指令取出</font>：程序计数器（PC）指向下一条将要执行的指令的内存地址。CPU 根据这个地址从内存中取出指令并将其存储到指令寄存器（IR）中。
  - <font color=tomato>指令译码：</font>译码器接收来自指令寄存器的指令，并解析这条指令以确定其操作码（Opcode）、操作数地址、寄存器编号等。这个过程涉及识别指令要执行的操作类型和所涉及的数据。
  - <font color=tomato>控制信号生成：</font>控制单元接收到译码器解析后的指令信息，并生成相应的控制信号。这些控制信号协调 CPU 内部的数据流动，管理 ALU 的操作，并控制 CPU 与内存、输入/输出设备的交互。
  - <font color=tomato>指令执行：</font>根据控制单元的指令，ALU 或其他处理单元执行计算或其他操作。这可能涉及从寄存器或内存读取数据、执行算术或逻辑运算、以及将结果写回寄存器或内存。
  - <font color=tomato>重复过程：</font>一旦当前指令执行完毕，PC 更新为下一条指令的地址，CPU 重复上述过程，继续执行程序中的下一条指令。

- 知识点3：流水线操作：
```
如果向CPU的运行过程的5个阶段，假设为相同的单位时间，那么
| F | D1 | D2 | EX | WB |
    | F | D1 | D2 | EX | WB |
        | F | D1 | D2 | EX | WB |
            | F | D1 | D2 | EX | WB |
                | F | D1 | D2 | EX | WB | 
以这种方式，更有效率的对多条语句进行并行操作
```
- 知识点4：分支预测
- 分支预测的详细说明
  - <font color=tomato>遇到分支指令：</font>
    - 当 CPU 执行到一个分支指令（如 if 语句）时，此时条件表达式的结果可能还未知。但由于指令流水线的设计，CPU 需要知道下一步执行哪条指令。
  - <font color=tomato>分支预测：</font>
    - CPU 使用分支预测器来预测分支将如何解决（即条件表达式的结果是真还是假）。基于这个预测，它决定接下来执行哪条指令的地址。
  - <font color=tomato>继续执行：</font>
    - 如果分支预测为真（即预测条件为满足），CPU 将继续执行if块中的指令；如果预测为假，则跳过if块。在这个过程中，CPU 不会等待条件表达式的实际计算结果，而是继续执行其预测的路径。
  - <font color=tomato>实际条件表达式结果：</font>
    - 一旦条件表达式的实际结果计算出来，CPU 会检查其预测是否正确。
  - <font color=tomato>预测正确或错误：</font>
    - 如果预测正确，那么流水线中已经执行的操作是有效的，CPU 将继续执行。
    - 如果预测错误，CPU 需要撤销或丢弃自预测点以来执行的所有操作，并从正确的分支重新开始执行。

```
CPU以流水线模式执行指令时
当遇到分支语句
在if后面的表达式的值还没执行时，根据CPU的流水线操作流程，PC指向下一指令的内存地址，此时由于未得到表达式的值，因此需要CPU提前对结果进行预测，来控制PC执行下一条指令的内存地址的值

当表达式的值计算出来后，如果预测错误，则之前的执行作废，重新在正确的结果进行语句执行

而下面的代码，就是人工告诉CPU，来增加CPU分支预测的准确率，从侧面提高CPU的运行效率

#define likely(x)
// __builtin_expect(!!(x), 1)，
// 1是告诉CPUx的值大概率为真，优先把x作为真值去计算
#define unlikely(x)
// __builtin_expect(!!(x), 0)
// 0是告诉CPUx的值大概率为假，优先把x作为假值去计算
// likely 代表x经常成立
// unlikely(x) 代表x不经常成立
```

### 循环结构
#### while 语句
- 基础语法示例：
```C
while (expression) {
    code block;
}
// 先判断在执行
```
```C
do {
    code block;
} while (expression);
// 先执行在判断，至少执行一次
```
- 代码示例（判断数字位数）
```C
#include<stdio.h>

int main() {
    int n, m = 0;
    scanf("%d", &n);
    do {
        n /= 10;
        ++m;
    } while (n); // 考虑0，所以不能直接使用while(){}
    printf("%d\n", m);
}
```
- 代码示例：
```C
#include<stdio.h>

int main() {
    int x;
    while (scanf("%d", &x) != EOF) {
      // EOF表示程序执行过程中，按ctrl+d,程序返回的值，通常值为-1
        printf("2 * x = %d\n", x);
    }

    return 0;
}
```

#### for 语句
- 语法结构
```C
for (初始化; 循环条件; 执行后操作) {
    代码块;
}
```
- for语句永久执行：
```C
for (;;) {
  // code block;
}
// 等同于
while (true) {
  // code block;
}
```
- 示例代码（f0 = 1,f1 = 1）求斐波那契数列
```C
#include<stdio.h>

int main() {
    int n = 0;
    int first = 1, second = 1, next;
    scanf("%d", &n);
    printf("%d\n", 1);
    printf("%d\n", 1);
    for (int i = 0; i < n - 2; i++) {
        next = first + second;
        first = second;
        second = next; 
        printf("%d\n", next);
    }

    return 0;
}
```

#### break 和 continue
- break 语句
  - 跳出switch-case语句
  - 跳出最近的一层循环

- continue 语句
  - 结束本次循环，继续下一次循环


#### goto 语句
- 基础语法结构
```C
goto lab_1;
    code block1;
lab_1:
    code block2;

// 跳转到lab_1标记处，code block1被跳过，直接执行block2
```
- 示例：
```C
#include<stdio.h>

int main() {
    goto lab_1;
    printf("hello world\n");
lab_1:
    printf("hello Harbin\n");

    return 0;
} // result: hello Harbin
```
- 问题1：
```C
#include<stdio.h>

int main() {
    goto lab_2;
    int a = 0, b = 0;
    scanf("%d%d", &a, &b);
lab_2:
    printf("%d\n", a * b);

    return 0;
} // 不报错，但结果不可知

// 在使用goto语句跳过变量声明时，变量的定义可以在后续使用
// 但是初始值，和赋值行为不会执行
```
- 示例：使用goto模拟if分支语句(脱裤子放屁)
```C
#include<stdio.h>

int main() {
    int n, x;
    scanf("%d", &n);
    n & 1 && ({
        goto if_stmt;
        1;
    });
    n & 1 || ({
        goto else_stmt;
        1;
    });
// &&两边必须是有返回值的表达式
// {}将多条语句合并成一条复合语句
// ()将复合语句转换为表达式
if_stmt:
    printf("%d is odd\n", n);
    goto if_end;
else_stmt:
    printf("%d is even\n", n);
if_end:
    return 0;
}
```
- 示例：使用goto模拟while
```C
#include<stdio.h>

int main() {
    int n, i = 0;
    scanf("%d", &n);
start:
    if (i < n) {
        printf("%d ", ++i);
        goto start;
    } else {
        goto end;
    }
end:
    printf("\n");
    return 0;
}
```
- 示例：使用goto模拟for
```C
#include<stdio.h>

int main() {
    int n = 0;
    scanf("%d", &n);
    int i = 1;
for_1:
    goto for_2;
for_2:
    if (i <= n) goto for_4;
    else goto for_end;
for_3:
    i++;
    goto for_2;
for_4:
    if (i % 3 == 0) goto for_3;
    else printf("%d ", i);
    goto for_3;
for_end:
    return 0;
}
```
### 重识一条语句
- 分类
  - 复合语句
    - { statement; }
  - 表达式语句
    - expression;
  - 选择(分支)语句
    - if-else
    - switch-case
  - 循环语句
    - while / do-while
    - for
  - 跳转语句
    - return 跳出当前函数
    - break 跳出当前循环
    - continue 跳出本次循环
    - goto 跳到标识处
  - 空语句
    - ;
