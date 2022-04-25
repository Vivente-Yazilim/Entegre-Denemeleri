#!/bin/bash

echo  "1.Read Date and Time"
echo "2.Set Date"
echo "3.Set Time"
echo "4.Quick Set"
read command
read_time=1
set_date=2
set_time=3
quick_set=4
if (($command == $read_time))
then 
	read _DATE_TIME[{1..2}]<<<$(python3 /home/pi/Desktop/rtc/ds1307.py)
	echo ${_DATE_TIME[1]}
	echo ${_DATE_TIME[2]}

elif(($command == $set_date))
then
	echo "Enter Year(YYYY)"
	read YEAR
	echo "Enter Month(MM)"
	read MONTH
	echo "Enter Date(DD)"
	read DATE
	python3 /home/pi/Desktop/rtc/set_date_ds1307.py $YEAR $MONTH $DATE
	sudo date +%Y%m%d -s "$YEAR$MONTH$DATE"	
elif(($command == $set_time))
then
	echo "Enter Hour(HH)"
	read HOUR
	echo "Enter Minute(MM)"
	read MINUTE
	echo "Enter Second(SS)"
	read SECOND

	python3 /home/pi/Desktop/rtc/set_time_ds1307.py $HOUR $MINUTE $SECOND
	
	sudo date +%T -s "$HOUR:$MINUTE:$SECOND"

elif(($command == $quick_set))
then
	read _DATE_TIME[{1..2}]<<<$(python3 /home/pi/Desktop/rtc/ds1307.py)
	sudo date +%Y%m%d -s "${_DATE_TIME[1]}"
	sudo date +%T -s "${_DATE_TIME[2]}"
	
fi


