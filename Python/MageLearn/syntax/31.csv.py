# csv文件
# csv即逗号分隔值（Comma-Separated Values，CSV，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。
# csv文件是一个纯文本文件，可以使用记事本、文本编辑器等打开，文件内容是以文本形式存储的表格数据，数据之间用逗号分隔。

rows = [
    ('id', 'name', 'age', 'address'),
    (1, 'tom', 18, 'beijing'),
    (2, 'jerry', 20, 'shanghai'),
    (3, 'jack', 22, 'guangzhou')
]

with open('./test1.csv', 'w', newline='') as f: # newline=''表示不换行，windows下需要，否则会多一行空行，因为windows下换行是\r\n
    for line in rows:
        # f.write(",".join(map(str, line)) + '\r\n') # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
        print(",".join(map(str, line)), file=f, end='\r\n') # file参数指定文件对象，end='\r\n'表示换行


# csv模块
# csv.reader(csvfile, dialect='excel', **fmtparams) 用于读取csv文件的内容，返回一个reader对象，reader对象是一个迭代器
'''
默认使用excel方言，也可以自定义方言
delimiter 列分隔符，默认为','（逗号）
lineterminator 行分隔符，默认为'\r\n'（回车换行）
quotechar 引用符，默认为'"'（双引号）
'''

import csv
with open('./test1.csv', 'r', newline='') as f:
    reader = csv.reader(f) # csv.reader()返回一个reader对象,reader对象是一个迭代器,f是一个文件对象
    for row in reader:
        print(row,type(row))

with open('./test2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)