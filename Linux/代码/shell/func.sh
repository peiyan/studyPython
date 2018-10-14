#午餐无返回值的函数
demo(){
	echo "hello world"
}
demo

#有返回值
funWithReturn(){
	echo "输入第一个数字："
	read aNum
	echo "输入第二个数字："
	read anotherNum
	return $(($aNum + $anotherNum))
}

funWithReturn
echo $?
