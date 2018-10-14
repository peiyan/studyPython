#定义字符串
name="zhangsan"
str='hello world'
#字符串拼接
strr="you name is ${name}"

#获取字符串的长度
string='abcd'
echo ${#string}


#提取子字符串
#包头包尾
stri='today is agood day'
echo ${stri:1:4}

echo `expr index "$stri" is`


