package main


// 准备一个1KB的数组
var arr [1024]byte
// n个hash函数，这里可以是n个hash函数
func hash1(a string) int {}
func hash2(a string) int {}
func hash3(a string) int {}
// ... 可以有很多hash函数

// 一个addBloom函数，将字符串a添加到布隆过滤器中，经过hash函数处理，得到一个整数，然后将整数对应的byte数组的某一位设置为1
func addBloom(a string, hash func(string) int) {

    // 字符串经过hash1函数处理，得到一个整数
    hashNum := hash(a) % (1024 * 8)  // 控制数字范围在0-1024*8之间

    // 通过hashNum/8得到byte数组的索引
    index := hashNum / 8

    // 通过hashNum%8得到byte数组的位索引
    bitIndex := hashNum % 8

    // 通过位运算，将byte数组的index索引的bitIndex位设置为1
    arr[index] |= 1 << bitIndex
}

// 一个checkBloom函数，检查字符串a是否在布隆过滤器中，hash是一个hash函数指针

func checkBloom(a string, hash func(string) int) bool {
    hashNum := hash(a) % (1024 * 8)
    index := hashNum / 8
    bitIndex := hashNum % 8
    return arr[index]&(1<<bitIndex) != 0
}

// 判断一个字符串是否在布隆过滤器中
func judgement() bool {
    addBloom("java", hash1)
    addBloom("python", hash1)
    addBloom("golang", hash1)

    // 等等，假设有很多字符串加入
    
    // 假设有n个hash函数
    return checkBloom("java", hash1) && checkBloom("java", hash2) && checkBloom("java", hash3)...
}