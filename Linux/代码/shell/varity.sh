your_name="zhangsan"
echo $your_name
num=10
echo ${num}
echo "your name is ${your_name}"
your_name="jack"
echo $your_name
#定义一个只读变量
url="www.baidu.com"
readonly url
#url="www.1000phone.com"
#删除变量
age=18
unset age
echo $age
