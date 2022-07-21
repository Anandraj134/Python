echo "Enter number :"
read n
i=0
echo "Enter $n numbers :"
while [ $i -lt $n ]
do
	read arr[$i]
	i=`expr $i + 1`
done

for ((i=0; i<${#arr[@]}; i++))
do
	for ((j=0;j<${#arr[@]};j++))
	do
		if [[ ${arr[$j]} -lt ${arr[$i]} ]]
		then
			temp=${arr[$i]}
			arr[$i]=${arr[$j]}
			arr[$j]=${temp}
		fi
	done
done

echo "Largest element is : ${arr[0]}"

echo "Second largest element is : ${arr[1]}"
