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
  - 关于给数值类型赋值是，常量后面加后缀，如：L,LL,UL,ULL等的意义
    - 一般来说，由于前面已经声明了变量类型，后面的后缀在大多数情况下是多余的，但是在一些编辑器中，并不能完全识别前面如：long int ,long long int 类似这种的说明，因此在这种情况下，需要加后缀防止数值溢出。 

- 浮点数
  - 浮点数在内存中的表现形式，参照 C++中的浮点数在内存中的表现形式（C++_learning.md） 
  - 浮点数大致共3种类型：float；double；long double
    - 字节数及精确位数
      - float       占4个字节，  7位有效位
      - double      占8个字节，  15位有效位
      - long double 占12个字节， 18个有效位
    - 编写一个类型为float的常量，需要在数值的末尾添加一个f，以区别double类型
      - 例如：`float redius = 2.5f`
    - 当用E或e指定指数值时，这个常量就不需要包含小数点
      - 例如：`float num = 1E3f`和`double biggest = 123E30`
  - 浮点数的格式说明符：%f
    - 控制输出中的小数位数：`%.3f`(小数点后3位)
    - 用于浮点数的格式说明符的一般形式：`%[width][.precision][modifier]f`
      - width: 是一个整数，指定输出的总字符串（包括空格），即字段宽度，数值默认右对齐，即在前面补空格。如果希望左对齐（即在后面补空格），可以用负数
      - .precision: 指定小数点后的位数
      - modifier: 当输出值的类型是long double时，modifier部分就是L，否则省略

### 简单介绍scanf() 后续会更详细的说明
- 语法格式：`scanf(a,&b)`, 共两个参数
- 简介：scanf()是一个需要包含头文件stdio.h的函数。它专门处理键盘输入，提取通过键盘输入的数据
  - 第一个参数：放在双引号内的一个控制字符串，用来声明输入的数据类型
  - 第二个参数：&是寻址运算符，它允许scanf()函数将读入的数值存进指定变量中。
    - 例如：`scanf("%f", &diameter)` 将输入的浮点数存入变量diameter中
- scanf()中的更多参数和应用将在后续讲解

### 定义命名常量
- 定义一个固定不变的值（即常量），有两种方法：
  - 方法1：是将PI定义为一个符号，此时PI不是一个变量，而是它表示的值的一个别名
    - 语法：`#define PI 3.14159f`
    - 注意：#define语句中的标识符都是大写，只要在程序里的表达式中引用PI，预处理器就会用#define指令中的值取代它
  - 方法2：将Pi定义成变量，但告诉编译器，它的值是固定的，不能改变 （推荐）
    - 语法：`const float Pi = 3.14159f`
  - 区别：
    - 方法1中PI只是一个字符序列，替代代码中的所有PI。
    - 方法2中Pi为指定类型的一个常量值，在Pi的声明中添加关键字const，会使编译器检查代码是否试图改变它的值，如果改变则会报错。

### 极限值
- 整数类型的极限值：头文件`<limits.h>`定义的符号表示每种类型的极限值
<table>
  <thead>
    <th style="background-color:darkred;color:white">类 型</th>
    <th style="background-color:darkred;color:white">下 限</th>
    <th style="background-color:darkred;color:white">上 限</th>
  </thead>
  <tbody>
    <tr>
      <td>char</td>
      <td>CHAR_MIN</td>
      <td>CHAR_MAX</td>
    </tr>
    <tr>
      <td>short</td>
      <td>SHRT_MIN</td>
      <td>SHRT_MAX</td>
    </tr>
    <tr>
      <td>int</td>
      <td>INT_MIN</td>
      <td>INT_MAX</td>
    </tr>
    <tr>
      <td>long</td>
      <td>LONG_MIN</td>
      <td>LONG_MAX</td>
    </tr>
    <tr>
      <td>long long</td>
      <td>LLONG_MIN</td>
      <td>LLONG_MAX</td>
    </tr>
  </tbody>
</table>

- 浮点数类型的极限值：头文件`<float.h>`定义了表示浮点数的符号
<table>
  <thead>
    <th style="background-color:darkred;color:white">类 型</th>
    <th style="background-color:darkred;color:white">下 限</th>
    <th style="background-color:darkred;color:white">上 限</th>
  </thead>
  <tbody>
    <tr>
      <td>float</td>
      <td>FLT_MIN</td>
      <td>FLT_MAX</td>
    </tr>
    <tr>
      <td>double</td>
      <td>DBL_MIN</td>
      <td>DBL_MAX</td>
    </tr>
    <tr>
      <td>long double</td>
      <td>LDBL_MIN</td>
      <td>LDBL_MAX</td>
    </tr>
  </tbody>
</table>

### sizeof()运算符
- 使用sizeof运算符可以确定给定的类型占据多少字节。当然，在C语言中sizeof是一个关键字。表达式sizeof(int)会得到int类型的变量所占的字节数，所得的值是一个size_t类型的整数。
  - 例句：`size_t size = sizeof(long long);`
- 除了确定某个基本类型的值占用的内存空间之外，sizeof运算符还有其他用途，但这里只使用它确定每种类型占用的字节数
```C
// Program 2.12 Finding the size of a type
#include <stdio.h>

int main(void) {
  printf("Variables of type char occupy %u bytes\n", sizeof(char));
  printf("Variables of type short occupy %u bytes\n", sizeof(short));
  printf("Variables of type int occupy %u bytes\n", sizeof(int));
  ...
}
```
- 注意：如果希望把sizeof运算符应用于一个类型，则该类型名必须放在括号中，例如sizeof(long double)。将sizeof运算符应用于表达式时，括号就是可选的。

### 强制类型转换
- 要把变量从一种类型转换为另一种类型，应把目标类型放在变量前面的括号里，和java的强制类型转换相同
- 例如：`RevQuarter = (float)QuarterSold/150*Revenue_Per_150;`

### 隐式转换
- 转换规则：
  - 将值域较小的操作数类型转换为另一个操作数类型（这里和java一致），但在一些情况下，两个操作数都要转换类型

### 字符类型 char
- 概述
  - char类型的变量可以存储单个字符的代码。他只能存储一个字符代码（即一个整数），所以也可以看作整数类型。可以像其他整数类型那样处理char类型存储的值。因此可以在算术运算中使用它。
  - char类型的变量有双重性：可以把它解释为一个字符，也可以解释为一个整数
    - `char letter = 'C'; letter = letter + 3;`

- 字符的输入输出
  - scanf()函数和格式说明符%c，可以从键盘上读取单个字符，将它存储在char类型的变量中
  ```C
  char ch = 0;
  scanf("%c",&ch);  // Read One character
  ```

### 枚举
- 概述：
  - 使用场景：在编程时，常常希望变量存储一组可能值中的一个。例如：一个变量存储表示当前月份的值。这时就可以使用枚举
  - 利用枚举，可以定义一个新的整数类型，该类型变量的值域是我们指定的几个可能值
    - 例：`enum Weekday {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};`
    - 解析：
      - 这个语句定义了一个类型，而不是变量。新类型的名称Weekday跟在关键字enum的后面，这个类型名称称为枚举的标记
      - Weekday类型的变量值可以是类型名称后面的大括号中的名称指定的任意值。这些名称叫做枚举器或枚举常量，其数量可任意。
      - 每个枚举器都用我们赋予的唯一名称来指定，编译器会把int类型的整数值赋予每个名称。枚举是一个整数类型，因为指定的枚举器对应不同的整数值，这些整数值默认从0开始，即索引。
      - 可以声明Weekday类型的一个新变量，并初始化它：`enum Weekday today = Wednesday; //2`
      - 也可以在定义枚举类型时，声明该类型的变量，并初始化变量：`enum Weekday {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday} today = Monday, tomorrow = Tuesday;`
      - 枚举类型的变量是整数类型，所以可以在算术表达式中使用：`enum Weekday {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday} today = Monday, tomorrow = today + 1;`

- 选择枚举值：
  - 可以给任意或所有枚举器明确指定自己的整数值。尽管枚举器使用的名称必须唯一，但枚举器的值不要求是唯一的。（除非有特殊的原因让某些枚举器的值相同，否则一般应确保这些值也是唯一的）
  - 例：`enum Weekday {Monday = 1, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};`
  - 枚举值相同的例子：`enum Weekday {Monday = 5, Tuesday = 4, Wednesday, Thursday = 10, Friday = 3, Saturday, Sunday};`

### 存储布尔值的变量
- _Bool类型存储布尔值。
  - _Bool类型的变量值可以是0或1，对应于布尔值false和true。由于值0和1是整数，所以_Bool类型也被看为整数类型。
  - 例：`_Bool vaild = 1; // Boolean variable initialized to true`
  - 在包含使用`<stdbool.h>`头文件后，可以用bool代替_Bool


