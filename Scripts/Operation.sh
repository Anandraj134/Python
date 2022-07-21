echo "add = addition"
echo "sub = subtraction"
echo "mul = multiplication"
echo "div = division"
echo "Enter operation want to perform"
read op
case $op in
add) echo "Enter number"
	read a
	read b
	echo "Sum is `expr $a + $b `"
	;;
	
sub) echo "Enter number"
	read a
	read b
	echo "Subtraction is `expr $a - $b `"
	;;
mul) echo "Enter number"
	read a
	read b
	echo "Multiplication is `expr $a \* $b `"
	;;
div) echo "Enter number"
	read a
	read b
	echo "Division is `expr $a / $b `"
	;;
*)
	echo "Invalid Option"
esac

