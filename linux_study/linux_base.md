# LINUX 基础
## 文本处理
### Awk
#### Awk基础
- Awk语法
```shell
awk [option] 'pattern[action]' file ...
# options：awk可选参数
# pattern：模式
# {action}：动作； 最常用的动作是 print 和 printf
# file：文件/数据
```
- Awk场景
```shell
[Mon Aug 14 09:16:05 -bash 24] root@parrot:Storage #cat prac1.txt
root x 0 0 root /root /bin/bash
daemon x 1 1 daemon /usr/sbin /usr/sbin/nologin
bin x 2 2 bin /bin /usr/sbin/nologin
sys x 3 3 sys /dev /usr/sbin/nologin
sync x 4 65534 sync /bin /bin/sync
games x 5 60 games /usr/games /usr/sbin/nologin
man x 6 12 man /var/cache/man /usr/sbin/nologin
lp x 7 7 lp /var/spool/lpd /usr/sbin/nologin
mail x 8 8 mail /var/mail /usr/sbin/nologin
news x 9 9 news /var/spool/news /usr/sbin/nologin
inetsim x 132 138  /var/lib/inetsim /usr/sbin/nologin
_gvm x 133 140  /var/lib/openvas /usr/sbin/nologin
beef-xss x 134 141  /var/lib/beef-xss /usr/sbin/nologin
mystical x 1000 1003 mystical /home/mystical /bin/bash
saned x 135 142  /var/lib/saned /usr/sbin/nologin
[Mon Aug 14 09:16:21 -bash 25] root@parrot:Storage #cat prac1.txt | awk '{print $1}'
root
daemon
bin
sys
sync
games
man
lp
mail
news
inetsim
_gvm
beef-xss
mystical
saned
```
- 简单规则：
  - awk默认以空格为分隔符，且多个空格也识别为一个空格，作为分隔符
  - awk是按行处理文件，一行处理完毕，处理下一行，根据用户指定的分隔符去工作，没有指定则默认空格

- awk内置变量
<table>
    <thead>
        <th style="background-color: darkred; color: white;">内置变量</th>
        <th style="background-color: darkred; color: white;">解释</th>
    </thead>
    <tbody>
        <tr>
            <td>$n</td>
            <td>指定分隔符后，当前记录的第n个字段</td>
        </tr>
        <tr>
            <td>$0</td>
            <td>表示整行</td>
        </tr>
        <tr>
            <td>FS</td>
            <td>字段分隔符，默认是空格</td>
        </tr>
        <tr>
            <td>NF(Number of fields)</td>
            <td>分割后，当前一共有多少个字段</td>
        </tr>
        <tr>
            <td>NR(Number of records)</td>
            <td>当前记录数，行数</td>
        </tr>
        <tr>
            <td>更多详情查看man手册</td>
            <td>man awk</td>
        </tr>
    </tbody>
</table>

- 一次性输出多列信息
  - 示例：awk '{print $1,$4,$5}' prac1.txt
  - ',' 逗号代表空格分隔显示

- 自定义输出内容
  - awk，必须外层用单引号，内层用双引号
  - 示例：awk '{print "第一列",$1,"第二列",$2}' prac1.txt
  - 内层双引号代表字符串

- awk参数
<table>
    <thead>
        <th style="background-color: darkred; color: white;">参数</th>
        <th style="background-color: darkred; color: white;">解释</th>
    </thead>
    <tbody>
        <tr>
            <td>-F</td>
            <td>指定分割字段符</td>
        </tr>
        <tr>
            <td>-v</td>
            <td>定义或修改一个awk内部的变量</td>
        </tr>
        <tr>
            <td>-f</td>
            <td>从脚本文件中读取awk命令</td>
        </tr>
    </tbody>
</table>

- 输出指定行信息
  - 示例：awk 'NR==5{print $0}' prac1.txt 输出第5行数据
  - 示例2：awk 'NR==5,NR==10{print $0}' prac1.txt 输出第5-10行数据
  - 示例3：awk 'NR==5,NR==10{print NR,$0}' prac1.txt 输出第5-10行数据，并给每一行的内容添加行号

- awk变量
  - 内置变量
  <table>
    <thead>
        <th style="background-color: darkred; color: white;">内置变量</th>
        <th style="background-color: darkred; color: white;">解释</th>
    </thead>
    <tbody>
        <tr>
            <td>$n</td>
            <td>指定分隔符后，当前记录的第n个字段</td>
        </tr>
        <tr>
            <td>$0</td>
            <td>表示整行</td>
        </tr>
        <tr>
            <td>NF(Number of fields)</td>
            <td>分割后，当前一共有多少个字段</td>
        </tr>
        <tr>
            <td>NR(Number of records)</td>
            <td>当前记录数，行数</td>
        </tr>
        <tr>
            <td>FS</td>
            <td>输入字段分隔符，默认为空格</td>
        </tr>
        <tr>
            <td>OFS</td>
            <td>输出字段分隔符，默认为空格</td>
        </tr>
        <tr>
            <td>RS</td>
            <td>输入记录分隔符，指定输入时的换行符</td>
        </tr>
        <tr>
            <td>ORS</td>
            <td>输出记录分隔符，输出指定的换行符</td>
        </tr>
        <tr>
            <td>FNR</td>
            <td>各文件分别计数的行号</td>
        </tr>
        <tr>
            <td>FILENAME</td>
            <td>FILENAME：当前文件名</td>
        </tr>
        <tr>
            <td>ARGC</td>
            <td>命令行参数个数</td>
        </tr>
        <tr>
            <td>ARGV</td>
            <td>数组，保存命令行所给定的各参数</td>
        </tr>

    </tbody>
  </table>

  - 自定义变量
    - 方法一：-v varName=value
    - 示例：awk -v myname="峰哥" 'BEGIN{print "我的名字是？",myname}'
    - 方法二：在程序中直接定义

- awk格式化
  - printf 格式化输出
  - printf 和 print 的区别
  ```
  format的使用

  要点：
  1.其与print命令的最大不同是，printf需要指定format
  2.format用于指定后面的每个item的输出格式
  3.printf语句不会自动打印换行符；\n

  format格式的指示符都以%开头，后跟一个字符；如下：
  %c: 显示字符的ASCLL码；
  %d, %i：十进制整数；
  %e, %E：科学计数法显示数值；
  %f：显示浮点数；
  %s：显示字符串；
  %u：显示无符号整数；
  %%：显示%自身

  printf修饰符
  -：左对齐，默认右对齐；
  +：显示数值符号； printf"%+d"

  ```

- awk模式pattern
  - BEGIN：处理文本前，先执行BEGIN模式指定的动作
  - END：处理完指定文本后，需要执行的动作
    <table>
        <thead>
            <th style="background-color: darkred; color: white;">关系运算符</th>
            <th style="background-color: darkred; color: white;">解释</th>
            <th style="background-color: darkred; color: white;">示例</th>
        </thead>
        <tbody>
            <tr>
                <td><</td>
                <td>小于</td>
                <td>x < y </td>
            </tr>
            <tr>
                <td><=</td>
                <td>小于等于</td>
                <td> x <= y </td>
            </tr>
            <tr>
                <td>==</td>
                <td>等于</td>
                <td> x == y </td>
            </tr>
            <tr>
                <td>!=</td>
                <td>不等于</td>
                <td> x != y </td>
            </tr>
            <tr>
                <td> >= </td>
                <td>大于等于</td>
                <td> x >= y </td>
            </tr>
            <tr>
                <td>></td>
                <td>大于</td>
                <td> x > y </td>
            </tr>
            <tr>
                <td>~</td>
                <td>匹配正则</td>
                <td>x~/正则/</td>
            </tr>
            <tr>
                <td>!~</td>
                <td>不匹配正则</td>
                <td> x!~/正则/ </td>
            </tr>
        </tbody>
    </table>

- awk使用正则语法
  - awk '/正则表达式/{动作}' file


### sed
#### sed基本用法
