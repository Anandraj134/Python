echo "Enter 5 subject marks :"
i=0
while [ $i -lt 5 ]
do
	read a[$i]
	i=`expr $i + 1`
done
for i in ${a[@]}
do 
	SUM=$(( SUM + i ))
done

per=$((SUM / 5 ))

echo "Percentage is : $per%"

if [ $per -ge 90 ]
then
	echo "Grade : A"
	echo "Excellent"
elif [ $per -ge 80 ] && [ $per -lt 90 ]
then
	echo "Grade : B"
	echo "Well Done!"
elif [ $per -ge 70 ] && [ $per -lt 80 ]
then
	echo "Grade : C"
	echo "Very Good"
elif [ $per -ge 60 ] && [ $per -lt 70 ]
then
	echo "Grade : D"
	echo "Good"
elif [ $per -ge 50 ] && [ $per -lt 60 ]
then
	echo "Grade : E"
	echo "Need Improvement"
fi
