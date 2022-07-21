array1[0]=0 
array1[1]=10
array1[2]=20
array1[3]=30
array1[4]=40
array1[5]=50
array1[6]=60
array1[7]=70
array1[8]=80
array1[9]=90 
SUM=0
echo "Values is :"
for i in ${array1[@]}
do 
	echo "$i"
	SUM=$(( SUM + i ))
done

avg=$((SUM / 10))
echo "Average is : $avg"
