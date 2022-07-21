echo "Enter iteration Number"
read END
SUM=0
for i in $(seq $END)
do 
	echo "Enter $i number"
	read n
	SUM=$(( SUM + n))
done
echo "$SUM"
