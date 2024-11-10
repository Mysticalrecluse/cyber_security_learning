# 时间模块

# 常见时间名词
## GMT: 格林尼治标准时间（Greenwich Mean Time, GMT）, 指的是太阳在格林尼治天文台经过的平均子午线时间，是最早的世界标准时间。

## 时区：地球上共有24个时区，每个时区相差1小时，东西两个时区相差12小时。中国属于东八区，即东八时区。

## UTC：协调世界时（Coordinated Universal Time, UTC）, 是目前的世界标准时间
## UTC由全球很多国家的铯原子钟的平均时间计算而成，是世界上最准确的时间标准之一。
## UTC与GMT的区别：UTC是以原子时秒长为基础的，而GMT是以地球自转为基础的。

## 简单的说，GMT可以看做UTC+0, 中国时间可以看做UTC+8

## CST(China Standard Time)：中国标准时间，即北京时间，是UTC+8，CST(Central Standard Time)是美国中部时间。UTC-6

# 时间模块
import datetime  # datetime, timezone, timedelta, time

# datetime模块
# datetime模块提供了多个类，用于处理日期和时间
# 1. 构造器
d1 = datetime.datetime(2024,3,5,20,18,5)
print(d1) # 2024-03-05 20:18:05

# 2. now()方法，取当前时间
d2 = datetime.datetime.now()  # 无时区时间
print(d2) #2024-10-18 00:33:47.820892

# Unix时间戳, 从1970年1月1日0时0分0秒开始计算的秒数
d2_stamp = d2.timestamp()
print(d2_stamp, type(d2_stamp))

# 3. fromtimestamp()方法，从时间戳创建datetime对象
d3 = datetime.datetime.fromtimestamp(d2_stamp)
print(d3, type(d3)) # 2024-10-18 00:33:47.820892

# 4. 基于字符串创建datetime对象
datestring = "2024-10-18 00:33:47"
d4 = datetime.datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
print(d4) # 2024-10-18 00:33:47

# 5. strftime()方法，将datetime对象转换为字符串
d5 = d4.strftime("%Y-%m-%d %H:%M:%S")
print(d5, type(d5)) # 2024-10-18 00:33:47 <class 'str'>

# 构建带时区的datetime对象
# 1. timezone类
# tzinfo是一个抽象类，datetime模块中的timezone类是tzinfo的子类，用于表示时区
d6 = datetime.datetime(2024,10,18,0,33,47, tzinfo=datetime.timezone.utc)
# 等价于
# d6 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=0)))
print(d6, type(d6))

d7 = datetime.datetime.now(datetime.timezone.utc)
print(d7, type(d7))

## 取当前时间
# 中国时间, UTC+8, 东八区
d8 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))

# datetime.timedelta类
# timedelta类表示两个datetime对象之间的时间差
print(d8 + datetime.timedelta(days=1)) # 2024-10-19 09:33:47.820892

year = datetime.timedelta(days=365)
print(year, type(year)) # 365 days, 0:00:00 <class 'datetime.timedelta'>

# total_seconds()方法
# 返回时间差的秒数
print(year.total_seconds()) # 31536000.0

# datetime.datetime.utcnow()方法
# 返回当前的UTC时间
print(datetime.datetime.utcnow()) # 2024-10-18 01:33:47.820892 # 默认0时区

print("================================")

# 取时间成分
print(d8.year)
print(d8.month)
print(d8.day)
print(d8.isoweekday())



#import time
#time.sleep(5) # 休眠5秒