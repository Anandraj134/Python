echo "Enter filename "
read n
echo " "
echo "In upper case "
awk '{print	toupper($0)}' $n
echo " "
echo "In lower case "
awk '{print	tolower($0)}' $n

