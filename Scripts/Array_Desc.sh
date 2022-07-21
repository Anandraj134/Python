arr=(18 8 22 130 14)
  
echo "Array in original order"
echo ${arr[*]}
  

for ((i = 0; i<5; i++))
do
      
    for ((j = 0; j<5-i-1; j++))
    do
      
        if [ ${arr[j]} -lt ${arr[$((j+1))]} ]
        then
            temp=${arr[j]}
            arr[$j]=${arr[$((j+1))]}  
            arr[$((j+1))]=$temp
        fi
    done
done
  
echo "Array in Desending order :"
echo ${arr[*]}
