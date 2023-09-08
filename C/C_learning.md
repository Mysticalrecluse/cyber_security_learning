# C语言基础
## C语言概述
### C程序的创建
- 编辑
  - 定义：编辑过程就是创建和修改C程序的源代码——我们编写的程序指令称为源代码
- 编译
  - 定义：编译器可以将源代码转换为机器语言，在编译过程中，会找出并报告错误。这个阶段的输入实在编辑期间产生的文件，常称为源文件。
  - 输出结果：编译器的输出结果称为对象代码，存放它们的文件称为对象文件，这些文件的扩展名在Microsoft Windows环境中通常是.obj，在Linux/UNIX环境中通常是.o
  - 编译过程包括两个阶段
    - 第一个阶段称为预处理阶段，在此期间会修改或添加代码
    - 第二个阶段是生成对象代码的实际编译过程。
- 链接
  - 链接过程：链接器将源代码文件中由编译器产生的各种对象模块组合起来，再从C语言提供的程序库中添加必要的代码模块，将它们组合成一个可执行的文件。
  - 链接器也可以检测和报告错误，例如，遗漏了程序的某个部分，或者引用了一个根本不存在的库组件。
- 执行
  - 运行程序
  - 在UNIX和LINUX下，只要键入编辑和链接后的文件名，即可执行程序
### 简单程序剖析
```C
/* Program 1.3 Another Simple C Program - Displaying a Quotation */
#include <stdio.h> // This is a perprocessor directive

int main(void)  // This identifies the function main()
{               // This marks the beginning of main()
    printf("Beware the Ides of March!");  // This line outputs a quotation
    return 0;  // This returns control to the operating system
}              // This marks the end of main()
```
- 注释
  - 多行注释：/* */
  - 单行注释：//

- 预处理指令
  - `#include <stdio.h>`
  - 符号#表示这是一个预处理指令(preprocessing directive)，告诉编辑器在编译源代码之前，要先执行一些操作。
  - 在这个例子中，编译器将stdio.h文件的内容包含进来，这个文件称为头文件(header file),因为它通常放在程序的开头处。
  - 本例要用到标准库中的printf()函数，所以必须包含stdio.h头文件。stdio.h头文件包含了编译器理解printf()以及其他输入/输出函数所需要的信息。名称stdio是标准输入输出（standard input/output）的缩写。C语言中所有头文件的扩展名都是.h

- 定义main()函数
  - 解析：每个C程序都由一个或多个函数组成，每个C程序都必须有一个main()函数——因为每个程序总是从这个函数开始执行。
  - 定义main函数的第一行代码开头是一个关键字int，它表示main()函数的返回值的类型，关键字int表示main()函数返回一个整数值。执行完main()函数后返回的整数值表示返回给操作系统的一个代码，它表示程序的状态。
  - 紧跟在函数名main后的括号，带有函数main()开始执行时传递给它的信息，在这个例子中，括号内是void，表示没有给函数main()传递任何数据。

- 关键字
  - 注意：在C语言中，关键字有特殊意义的字，所以在程序中不能将关键字用于其他目的。

- 函数体
  - 定义：函数体是在函数名称后面位于起始及结束两个大括号之间的代码块。它包含了定义函数功能的所有语句。
  - 每个函数都必须有函数体，但函数体可以是空的，仅有起始及结束两个大括号，里面没有任何语句，在这种情况下，函数什么都不做
    - 作用：事实上，在开发一个包含很多函数的程序时，这种函数是非常有用的。我们可以声明一些用来解决手头问题的空函数，确定需要完成的编程工作，再为每个函数创建程序代码。这个方法有助于条例分明地、系统地建立程序。

- 输出信息
  - 例子中的main()函数体包含了一个调用printf()函数的语句
  - printf()：一个标准的库函数，它将函数名后面引号内的信息输出到命令行（实际上是标准输出流，默认为命令行）。

- 参数
  - 定义：包含在函数名（如上面语句中的printf()函数）后的圆括号内的项称为参数，它指定要传送给函数的数据。当传送给函数的参数多于一个时，要用逗号分开。

- 转义序列
<table>
    <thead>
        <th style="background-color:darkred;color:white">转义序列</th>
        <th style="background-color:darkred;color:white">说明</th>
    </thead>
    <tbody>
        <tr>
            <td>\n</td>
            <td>换行</td>
        </tr>
        <tr>
            <td>\r</td>
            <td>回车键</td>
        </tr>
        <tr>
            <td>\b</td>
            <td>退后一格</td>
        </tr>
        <tr>
            <td>\f</td>
            <td>换页</td>
        </tr>
        <tr>
            <td>\t</td>
            <td>制表符</td>
        </tr>
        <tr>
            <td>\v</td>
            <td>垂直制表符</td>
        </tr>
        <tr>
            <td>\a</td>
            <td>发出鸣响</td>
        </tr>
        <tr>
            <td>\?</td>
            <td>插入问好(?)</td>
        </tr>
        <tr>
            <td>\"</td>
            <td>插入双引号(")</td>
        </tr>
        <tr>
            <td>\'</td>
            <td>插入单引号(')</td>
        </tr>
        <tr>
            <td>\\</td>
            <td>插入反斜杠(\)</td>
        </tr>
    </tbody>
</table>

- 预处理器（宏）
  - 宏定义：宏是提供给预处理器的指令，来添加或修改程序中的C语句。
    - 宏可以很简单，只定义一个符号：`define INCHES_PER_FOOT 12`
      - 在源文件中包含这个指令，则代码中只要出现INCHES_PER_FOOT，就用12代替它。
    - 宏也可以很复杂，根据特定的条件把大量代码添加到源文件中。后续会详细解读


## 编程初步
- 本章主要内容
  - 内存的用法及变量的概念
  - 在C中如何计算
  - 变量的不同类型及其用途
  - 强制类型转换的概念及其使用场合

### 计算机的内存
- 内存的最小单位是位(bit)，将8个位组合为一组，称为字节(byte)。每个字节都有唯一的地址，字节地址从0开始。位只能是0或1。
- 内存的单位
  - 1KB 是 1024字节
  - 1MB 是 1024KB，也是1 048 576字节。
  - 1GB 是 1024MB，也是1 073 741 841字节
  - 1TB 是 1024GB，也是1 099 511 627 776字节

### 变量
- 定义：变量是计算机里一块特定的内存，它是由一个或多个连续的字节所组成，一般是1、2、4、8或16字节。每个变量都有一个名称，可以用该名称表示内存的这个位置，以提取它包含的数据或存储一个新的数值。
- 注意：变量可以有一个或多个字节，那么，计算机如何知道变量有多少个字节？每个变量都有类型来指定变量可以存储的数据种类。变量的类型决定了为它分配多少个变量。
```C
#include <stdio.h>

int main(void)
{
    int salary; // 变量声明，它分配了一些存储空间，来存储整数值，该整数可以用变量名salary来引用。
    // 此刻还未指定变量salary的值，所以此刻该变量包含一个垃圾之，即上次使用这块内存空间时遗留在此的值。
    salary = 10000;
    printf("My salary is %d.\n",salary); // %d, 转换说明符：指定最初二进制值转换为什么形式显示在屏幕上。
    // 这里%d是应用于整数值的十进制说明符
    return 0;
}
```

```C
/* 多个变量的使用 */
#include <stdio.h>

int main(void)
{
    int brothers;
    int brides;

    brothers = 7;
    brides = 7;

    // Display some output
    printf("%d bridges for %d brothers\n",brides,brothers);
    return 0;
}
```

- 变量的初始化
  - 建议在声明变量的同时，初始化变量值，防止后续没有给变量赋值，导致使用垃圾值得情况发生。
  - 基本算数运算
    - 在C语言中，算术语句的格式：`变量名 = 算数表达式;`
    - 深入了解整数除法：
      - 当一个操作数是负数时，在执行除法运算时，如果操作数不同号，结果就为负数，如果同号，则结果为正。
      - 在执行模数运算符，不管操作数是否同号，其结果总是和左操作数的符号相同 `45 % -7 = 3` `-45 % 7 = -3`

- 变量与内存
  - 带符号的整数类型
  <table>
    <thead>
        <th style="background-color:darkred;color:white">类型名称</th>
        <th style="background-color:darkred;color:white">字节数</th>
    </thead>
    <tbody>
        <tr>
            <td>signed char</td>
            <td>1</td>
        </tr>
         <tr>
            <td>short int</td>
            <td>2</td>
        </tr>
         <tr>
            <td>int</td>
            <td>4</td>
        </tr>
         <tr>
            <td>long int</td>
            <td>4</td>
        </tr>
         <tr>
            <td>long long int</td>
            <td>8</td>
        </tr>
    </tbody>
  </table>

  - 上述表格中，int和signed，在一般情况下，可以省略。
  - 无符号整数类型
  <table>
    <thead>
        <th style="background-color:darkred;color:white">类型名称</th>
        <th style="background-color:darkred;color:white">字节数</th>
    </thead>
    <tbody>
        <tr>
            <td>unsigned char</td>
            <td>1</td>
        </tr>
         <tr>
            <td>unsigned short int 或 unsigned short</td>
            <td>2</td>
        </tr>
         <tr>
            <td>unsigned int</td>
            <td>4</td>
        </tr>
         <tr>
            <td>unsigned long int 或 unsigned long</td>
            <td>4</td>
        </tr>
         <tr>
            <td>unsigned long long int 或 unsigned long long</td>
            <td>8</td>
        </tr>
    </tbody>
  </table>

  - 注意：如果变量的类型不同，但占用相同的字节数，则它们仍是不同的。Long 和 int类型占用相同的内存量，但它们仍是不同的类型。

- 浮点数
  - 浮点数在内存中的表现形式，参照 C++中的浮点数在内存中的表现形式（C++_learning.md） 