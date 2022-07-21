echo "Enter number :"
read n
a=0
b=1
c=2
echo "Fibonacci Series :"
echo "$a"
echo "$b"
while [ $c -lt $n ]
do
	c=$(($c+1))
	d=`expr $a + $b`
	echo "$d"
	a=$b
	b=$d
done
