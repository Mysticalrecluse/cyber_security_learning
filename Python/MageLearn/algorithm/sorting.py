# 排序算法
## 1. 冒泡排序
x = [1, 3, 2, 5, 4]
y = [5,8,5,2,9]
#
def bubblesort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-1-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    print(x)

bubblesort(x)


## 2. 选择排序
x = [1, 3, 2, 5, 4]
y = [5,8,5,2,9]
# 选择排序
# 1. 选择排序是一种简单的排序算法，每次找到最小的元素，然后放到前面
# 2. 选择排序的时间复杂度是O(n^2)
# 3. 选择排序是不稳定的排序算法, 例如：[5, 8, 5, 2, 9], 第一次排序后，第一个5和第二个5的位置发生了变化, 5 5 8 2 9, 两个5的相对位置发生了变化, 所以选择排序是不稳定的排序算法
# 4. 适用于小型数组排序（数组元素个数<1000）
# 4. 选择排序是原地排序算法
def selectionsort(x):
    n = len(x)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if x[j] < x[min_index]:
                min_index = j
        x[i], x[min_index] = x[min_index], x[i]
    print(x)

selectionsort(x)


## 3. 插入排序
### 核心算法
# 1. 结果可为升序或降序，默认升序，以升序为例
# 2. 将待排序数插入到已排序数列中

nums = [1,9,8,5,6,7,4,3,2]
nums2 = [1,19,8,52,6,37,4,13,2]


def insertsort(x):
    x = [0] + x
    n = len(x)
    for i in range(2, n):
        x[0] = x[i]
        j = i - 1
        while x[j] > x[0]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = x[0]
    return x[1:]


print(insertsort(nums))

