#-e开启转义，\n表示换行，\c表示不换行
echo -e "ok! \n"
echo -e "ok! \c"
echo `date`



printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" 张三 男 66.124
printf "%-10s %-8s %-4.2f\n" 李四 女 48.6667


num1=100
num2=200
if test $[num1] -eq $[num2]
then 
   echo ""
else
  echo ""
fi

cd /bin
if test -e ./bash
then
 echo ""
else
 echo ""
fi
