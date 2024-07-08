package hw3

func Rm(arr []int, mp map[int]bool) map[int]bool {
	if len(mp) == 0 {
		return mp
	}
	for k, _ := range mp {
		for i := 0; i < len(arr); i++ {
			if arr[i] == k {
				delete(mp, k)
			}
		}
	}
	return mp
}

// 看完6小时视频中的map后，改进写法
func Rm2(arr []int, mp map[int]bool) map[int]bool {
	for _, k := range arr {
		if _, exists := mp[k]; exists {
			delete(mp, k)
		}
	}
	return mp
}
