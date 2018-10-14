#for循环
for num in 1 2 3 4 5
do 
	echo $num
done


for str in "hello"
do
	echo $str
done

a=(1 2 3)
for x in ${a[*]}
do
	echo $x
done

#while循环
n1=1
while(( $n1<=5 ))
do
	echo $n1
	let "n1++"
done

i=1
sum=0
while [ $i -le 10 ]
do
	sum=$[$sum+$i]
	i=$[$i+1]
done
echo $sum


#until
j=1
until [ $j -gt 10 ]
do 
	echo $j
	let "j++"
done















