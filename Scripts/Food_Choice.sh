echo "B = Burger"
echo "F = French Fries"
echo "P = Pizza"
echo "S = Sandwiches"
echo "Choice of food?"
read str


case $str in
B)
	echo "Enter Quentity :"
	read n
	echo "Price of Burger is : $((200 * $n))"
	;;
F)
	echo "Enter Quentity :"
	read n
	echo "Price of French Fries is : $((50 * $n))"
	;;
P)
	echo "Enter Quentity :"
	read n
	echo "Price of Pizze is : $((500 * $n))"
	;;
S)
	echo "Enter Quentity :"
	read n
	echo "Price of Sandwiches is : $((150 * $n))"
	;;
*)
	echo "Food is not available"
esac
