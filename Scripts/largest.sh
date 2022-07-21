echo "Enter Num1"
read num1
echo "Enter Num2"
read num2
echo "Enter Num3"
read num3

if [ $num1 -gt $num2 ] && [ $num1 -gt $num3 ]
then
    largest=$num1
elif [ $num2 -gt $num1 ] && [ $num2 -gt $num3 ]
then
    largest=$num2
else
    largest=$num3
fi
echo "Largest number is :- $largest"
