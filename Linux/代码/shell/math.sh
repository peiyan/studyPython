#算术运算符
val=`expr 1 + 2`
echo $val
a=10
b=20
val=`expr $a + $b`
val=`expr $a \* $b`

#关系运算符
#[]中，前后都需要空格
if [ $a -eq $b ]
then 
  echo "相等"
else
  echo "不相等"
fi

#逻辑运算符
if [ 1 -lt 3 ] && [ 2 -lt 3 ]
then
  echo "成立"
else
  echo "不成立"
fi

#文件检测运算符
file="/home/yangyang/Desktop/shell/test.sh"
if [ -r $file ]
then
   echo "可读的"
else
  echo "不可读"
fi
