echo "Enter Number"
read END
SUM=0
for i in $(seq $END)
do 
	SUM=$(( SUM + i))
done
echo "$SUM"
