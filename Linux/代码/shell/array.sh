#定义数组
arr1=(10 20 30 40)
echo $arr1
arr2=(
10
20
30
40
)
echo $arr2

#获取数组中的元素
echo ${arr1[2]}
echo ${arr2[@]}

#获取数组中元素的个数
#方式一
length=${#arr1[@]}
echo $length
#方式二
length=${#arr2[*]}
echo $length
#获取数组中单个元素的长度
len=${#arr1[2]}
echo $len

