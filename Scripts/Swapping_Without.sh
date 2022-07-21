echo "enter first number :- "
read a
echo "enter second number :- "
read b
echo "Before swapping"
echo "A = $a"
echo "B = $b"
a=$((a+b))
b=$((a - b))
a=$((a-b))
echo "After swapping"
echo "A = $a"
echo "B = $b"
