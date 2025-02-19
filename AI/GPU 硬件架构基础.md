# GPU 硬件架构基础

```ABAP
在运行拥有极致逼真画面的游戏时，显卡每秒需要执行多少次计算
```

**每秒一亿次运算？**

每秒一亿次运算仅仅是**1996年的游戏《超级马里奥64》**所需要的运算量

![image-20250219170541793](D:\git_repository\cyber_security_learning\markdown_img\image-20250219170541793.png)

**每秒一千亿次运算？**你拥有的电脑可以在**2011年运行《我的世界》**

![image-20250219170923894](D:\git_repository\cyber_security_learning\markdown_img\image-20250219170923894.png)

如果你想运行画质逼真的**《赛博朋克2077》**，你需要一块显卡，它每秒能够运行大约**36万亿次运算**

![image-20250219171131464](D:\git_repository\cyber_security_learning\markdown_img\image-20250219171131464.png)



36万亿次计算，这个难以想象的庞大数字，需要我们花点时间去理解它

想象一下，你每秒做一道长乘法题。（例如：4689732 * 2764569），现在假设地球上的每个人都需要做类似的计算，但用的数字各不相同，为了达到这块显卡**每秒36万亿次运算**的计算能力，我们**需要大约4400个住满了地球的人，所有人一起工作，每人每秒完成一次计算**

![image-20250219171631681](D:\git_repository\cyber_security_learning\markdown_img\image-20250219171631681.png)

很难想象一个设备能完成所有这些计算，下面我们将了解，为何显卡能做到如此快速的计算，以及显卡是如何工作的？



## GPU 应用场景



-  **运行游戏画面**
- **比特币挖矿**
- **神经网络**
- **人工智能**







## GPU 物理设计和架构



### GPU 和 CPU 的区别

![image-20250219172437807](D:\git_repository\cyber_security_learning\markdown_img\image-20250219172437807.png)

**GPU，拥有超过1万个核心（10496 Cores），而CPU仅有24 Cores**

![image-20250219172540250](D:\git_repository\cyber_security_learning\markdown_img\image-20250219172540250.png)

GPU核心数远超CPU，看似GPU理所当然的比CPU强大，但是实际情况要比这复杂的多

如果把GPU想象成一艘巨型游轮，而CPU则是一架大型喷气式飞机，货轮的载货量相当于可以处理的计算量和数据量，而船或飞机的速度则代表这些计算和数据被处理的速率。

本质上，这是一个权衡：大量计算以较慢的速度执行，相较于少量的计算，以极快的速度执行

另一个关键区别是飞机要灵活的多，因为它可以运载乘客，包裹，或者集装箱，而且可以在数以万计的任何一个机场起降。同样的**CPU也很灵活**，它们可以运行各种各样的程序和指令

![image-20250219173216267](D:\git_repository\cyber_security_learning\markdown_img\image-20250219173216267.png)

然后，巨型货轮只能运载货物的集装箱，而且只能在港口之间航行，类似地，GPU比CPU的灵活性要差得多，它们只能运行简单的指令，比如基本的算术运算。

![image-20250219173420850](D:\git_repository\cyber_security_learning\markdown_img\image-20250219173420850.png)

此外GPU不能运行操作系统，也不能与输入设备或网络交互



#### 那么GPU和CPU哪一个更快

这个问题，本质上，如果你想对海量数据运行一系列计算，那么GPU完成任务的速度会更快

然而，如果你需要处理的数据少得多，而且需要快速得到结果，那么CPU会更快。

此外，如果你需要运行操作系统，或支持网络连接，以及各种不同的应用或硬件，那么你需要的会是CPU





### GPU 的 物理结构

#### 印刷电路板（PCB）

各种各样的组件都安装在上面

![image-20250219173932078](D:\git_repository\cyber_security_learning\markdown_img\image-20250219173932078.png)



#### 图形化处理区（GPU）

![image-20250219174035577](D:\git_repository\cyber_security_learning\markdown_img\image-20250219174035577.png)



打开它时，会看到一块名**为GA102的大型芯片或晶粒，它由283亿个晶体管构成**，![image-20250219174230758](D:\git_repository\cyber_security_learning\markdown_img\image-20250219174230758.png)

芯片的大部分区域都被处理核心占据，这些核心具有**分层的组织结构**，具体来说，这块芯片，被**分为7个图形处理集群，简称GPC**

![image-20250219174659069](D:\git_repository\cyber_security_learning\markdown_img\image-20250219174659069.png)

**每个处理集群内有12个流式多处理器，简称SM**

![image-20250219174759796](D:\git_repository\cyber_security_learning\markdown_img\image-20250219174759796.png)

**每个流式处理器内部有4个Warp和1个光线追踪核心**

![image-20250219174913196](D:\git_repository\cyber_security_learning\markdown_img\image-20250219174913196.png)

**每个Warp内有32个CUDA核心，也叫着色核心，和1张量核心**

![image-20250219174959379](D:\git_repository\cyber_security_learning\markdown_img\image-20250219174959379.png)**整个GPU共有10752个CUDA核心，336个量核心，以及84个光线追踪核心。这三个核心执行GPU的所有**

![image-20250219175222656](D:\git_repository\cyber_security_learning\markdown_img\image-20250219175222656.png)

这三种核心执行GPU的所有计算任务，而且每种核心都有不同的功能。



#### CUDA核心 

CUDA核心可以被看做是简单的计算任务，有加法按钮，乘法按钮等等，通常在运行游戏时使用的最多

![image-20250219175609616](D:\git_repository\cyber_security_learning\markdown_img\image-20250219175609616.png)



#### 张量核心 TENSOR

张量核心是矩阵乘法和加法计算器，用于几何变换，以及处理神经网络和人工智能。

![image-20250219175752926](D:\git_repository\cyber_security_learning\markdown_img\image-20250219175752926.png)



#### 光线追踪器 Ray Tracing Cores

光线追踪核心是体积最大的，但数量最少，它们用于执行光线追踪算法

![image-20250219175909274](D:\git_repository\cyber_security_learning\markdown_img\image-20250219175909274.png)



**事实是，3080,3090,3080ti和3090ti显卡都使用相同的GA102芯片设计作为它们的GPU**

![image-20250219180027518](D:\git_repository\cyber_security_learning\markdown_img\image-20250219180027518.png)







## GPU 计算架构