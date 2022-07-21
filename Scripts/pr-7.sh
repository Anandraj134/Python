echo "a. Display calender of current month"
echo "b. Display today's date and time"
echo "c. Display usernames those are currently logged in the system"
echo "d. Display your name"
echo "e. Display your terminal number"
echo "Enter operation you want to perform"
read op
case $op in
a) echo "Current month calender"
cal
;;
b) echo "Today's date and time is"
date
;;
c) echo "Logged in systems is/are"
who
;;
d) echo "Username "
whoami
;;
e) echo "Terminal number is"
tty
;;
*) echo "Select proper option"

esac 
