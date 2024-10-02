# 入门
## linux程序设计
### 应用程序

应用程序通常存放在系统为之保留的特定目录中。
```shell
# 系统为正常使用提供的程序，包括用于程序开发的工具，都可在/usr/bin中找到
/usr/bin
# 系统管理员为某个特定的主机或本地网路添加的程序，通常可在/usr/local/bin或/opt中找到
/usr/local/bin    # 建议放系统级的应用工程
/opt/

~/                # 对于开发用和个人的应用程序，最好在你的家目录中使用一个文件夹来存放它
```

### 头文件

用C语言及其他语言进行程序设计时，你需要用头文件来提供对常量的定义和对系统函数及库函数的调用的声明
```shell
# 这些头文件几乎总是位于/usr/include目录及其子目录中
/usr/include

# 那些依赖于特定Linux版本的头文件通常可在下列目录中找到
/usr/include/sys
/usr/include/linux
```

在调用C语言编译器时，你可以使用-I标志来包含保存在子目录或非标准中的头文件
```shell
gcc -I/usr/openwin/include fred.c
```

用grep命令来搜包含某些特定定义和函数原型的头文件是很方便的
- 假设想知道用于程序中返回退出状态的#define定义的名字，你可以使用下列命令查找
```shell
grep EXIT_ /usr/include/*.h
```

### 库文件

库是一组预先编译好的函数的集合，这些函数都是按照可重用的原则编写的。

```shell
# 标准系统库文件一般存储在/lib和/usr/lib目录中
/lib/
/usr/lib/
```

库文件必须遵循特定的命名规范并且需要在命令行中明确指定。
- 命名规范：
  - 库文件的名字总是以lib开头，随后部分执行这是什么库
    - 例如：c代表C语言库
    - m代表数学库
    - 文件名最后部分以`.`开始，然后给出库文件的类型

库文件的类型

- `.a`代表传统的静态函数库
- `.so`代表共享函数库

可以通过给出完整的库文件路径名用-l标志来告诉编译器要搜索的库文件
```shell
gcc -o fred fred.c /usr/lib/libm.a

# 等价
gcc -o fred fred.c -lm  # 简写方式，它代表的标准库目录中名为libm.a的函数库
# -lm标志的另一个好处是如果有共享库，编译器会自动选择共享库
```

可以使用`-L`（大写字母）标志为编译器增加库的搜索路径
```shell
gcc -o x11fred -L/usr/openwin/ x11fred.c -lX11
```

### 静态库

静态库，也称作归档文件(archive)，按惯例它们的文件名都以`.a`结尾。比如，标准C语言函数库`/usr/lib/libc.a`和X11函数库`/usr/lib/libX11.a`

#### 实验：创建静态库

(1) 为两个函数`fred`,`bill`分别创建各自的源文件

fred.c
```C
#include <stdio.h>

void fred(int arg) {
    printf("fred: we passed %d\n", arg);
    return ;
}
```

bill.c
```C
#include <stdio.h>

void bill(char *arg) {
    printf("bill: we passwd %s\n", arg);
}
```

(2) 分别编译这些函数以产生要包含在库文件中的目标文件。这可以通过调用带有-c选项的C语言编译器来完成，-c选项的作用是阻止编译器创建一个完整的程序。【如果此时试图创建一个完整的程序将不会成功，因为你还未定义main函数】

```shell
gcc -c bill.c fred.c

ls *.o
bill.o fred.o
```

(3) 现在编写一个调用bill函数的程序。首先，为你的库文件创建一个头文件。这个头文件将声明你的库文件中的函数，它应该被所希望使用你的库文件的应用程序所包含。把这个头文件包含在源文件fred.c和bill.c中是一个好主意，它将帮助编译器发现所有错误
```C
/*
    This is lib.h. It declares the functions fred and bill users
*/

void bill(char *);
void fred(int);
```

(4) 调用程序(program.c)非常简单。它包含库的头文件并且调用库中的一个函数
```C
#include <stdlib.c>
#include "lib.h"

int main() {
    bill("Hello World");
    exit(0);
}
```

(5) 现在，可以编译并测试这个程序了。暂时为编译器显示指定目标文件，然后要求编译器编译你的文件并将其与先前编译好的目标模块bill.o连接
```shell
gcc -c program.c
gcc -o program program.o bill.o
./program
```

(6) 创建并使用一个库文件。使用ar程序创建一个归档文件并将你的目标文件添加进去。这个程序之所以成为ar，是因为它将若干单独的文件归并到一个大的文件中以创建归档文件或集【注意：可以用ar程序来创建任何类型的文件的归档文件】
```shell
ar crv libfoo.a bill.o fred.o
a - bill.o
a - fred.o
```

(7) 库文件建好后，两个目标文件也已经添加进去。【在某些系统中，要想成功地使用函数库，还需要为函数库生成一个库。可以通过ranlib命令来完成这一工作】
```shell
ranlib libfoo.a
```

现在可以在编译器使用的文件列表中添加该库文件以创建你的程序
```shell
gcc -o program program.c libfoo.a

# 使用-l选项来访问函数库，但因其未保存在标准位置，所以必须使用-L选项来告诉编译器在何处可以找到它
gcc -o program program.o -L. -lfoo

# 查看标准位置
gcc --print-search-dirs
```

要查看哪些函数被包含在目标文件、函数库或可执行文件里，你可以使用nm命令
```shell
nm libfoo.a
```

### 共享库

共享库的保存位置与静态库是一样的，但共享库有不同的文件名后缀。在一个典型的Linux系统中，标准数学库的共享版本是`/usr/lib/libm.so`

当一个程序使用共享库时，它的链接方式是这样的：程序本身不再包含函数代码，而是引用运行时可访问的共享代码。当编译好的程序被装载到内存中执行时，函数引用被解析并产生对共享库的调用，如果有必要，共享库才被加载到内存中。

对Linux系统来说，负责装载共享库并解析客户程序函数引用的程序（动态装载器）是ld.so,也可能是ld-linux.so.2、ld-lsb.so.2或ld-lsb.so.3

用于搜索共享库的额外位置可以在文件/etc/ld.so.conf中配置，如果修改了这个文件，你需要执行ldconfig来处理它

可以通过运行工具ldd来查看一个程序需要的共享库
```shell
ldd program
    linux-vdso.so.1 (0x00007ffd9eb7a000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f65d300d000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f65d3243000)
```

在本例中，你看到标准C语言函数库（libc）是共享的(.so)。程序需要的主版本号是6。

共享库在许多方面类似于Windows中使用的动态链接库。`.so`库对应于`DLL`文件，它们都是在程序运行时加载，而`.a`库类似于`.LIB`文件，它们都包含在可执行程序中


## Shell程序设计

```shell
# 复制重定向操作对一个已有文件的覆盖
set -o noclobber  # 或者set -C

set +o noclobber   # 取消该选项
```

如果想对标准错误输出进行重定向，需要把想要重定向的文件描述符编号加在`>`操作符的前面,比如`2>`

把标准输出和标准错误输出分别重定向到不同的文件中
```shell
kill -HUP 1234 > killout.txt 2>killer.txt
```

把两组输出都重定向到一个文件中，可以用>&操作符来结合两个输出
```shell
# 这里 1> 省略为 >
kill -1 1234 > killouterr.txt 2>&1
```

