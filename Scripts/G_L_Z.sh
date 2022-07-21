echo "Enter a Number"
read num

if [ $num -lt 0 ]
then
    echo "$num is Negative"
elif [ $num -gt 0 ]
then
    echo "$num is Positive"
else
    echo "$num is Zero."
fi
