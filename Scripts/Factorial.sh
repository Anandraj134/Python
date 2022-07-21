echo "Enter Number"
read END
FACT=1
for i in $(seq $END)
do 
	FACT=$((FACT * i))	
done

echo "Factorial of $END is $FACT"

