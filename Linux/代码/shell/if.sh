#简单if语句
if [ 1 -lt 3 ]
then
  echo "ok"
fi


#双分支
num1=$[2*3]
num2=$[1+5]
#if-else语句一般会结合test使用
if test $[num1] -eq $[num2]
then 
  echo "两个数相等"
else
  echo "两个数不相等"
fi

#多分支
a=10
b=20
if [ $a -eq $b ]
then 
  echo "a 等于 b"
elif [ $a -gt $b ]
then
  echo "a 大于 b"
elif [ $a -lt $b ]
then
  echo "a 小于  b"
else
  echo "没有符合条件的操作"
fi

