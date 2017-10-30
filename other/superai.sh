#!/bin/bash
clear
sleep 0.5
for value in {1..2}
do
	echo -n "BOOTING UP."
	sleep 0.5
	clear
	echo -n "BOOTING UP.."
	sleep 0.5
	clear
done

sleep 2
clear

read -p "ENTER COMMAND: " mainmenuinput
sleep 1

echo "COMMAND ACCEPTED"
sleep 2
clear
echo "CURRENTLY PROCESSING 'hack russia'"
sleep 1

for value in "CREATING HACK" "INFILTRATING KREMLIN" "FIGHTING A BEAR" "WRESTLING NAKED PUTIN" "ELIMINATING ISIS" "DEFEATING ELITE 4" "ERASING TRACES"
do
	echo -en "$value"
	for num in {1..3}
	do
		echo -en "\r\033[K$value.";
		sleep 0.5
		echo -en "\r\033[K$value..";
		sleep 0.5
		echo -en "\r\033[K$value...";
		sleep 0.5
	done
	echo -en "\r$value...DONE\n"
done

sleep 3
clear

for num in {1..3}
do
		echo -en "\r\033[KCOMPILING RESULTS.."
		sleep 0.5
		echo -en "\r\033[KCOMPILING RESULTS.."
		sleep 0.5
		echo -en "\r\033[KCOMPILING RESULTS.."
		sleep 0.5
done
	
sleep 0.5
clear
sleep 2

echo "  _               _           _ _     _    ___    ____ __ ";
echo " | |             | |         | (_)   | |  / _ \  / /_ /_ |";
echo " | |__  _   _ ___| |__     __| |_  __| | | (_) |/ / | || |";
echo " | '_ \| | | / __| '_ \   / _\` | |/ _\` |  \__, / /  | || |";
echo " | |_) | |_| \__ \ | | | | (_| | | (_| |    / / /   | || |";
echo " |_.__/ \__,_|___/_| |_|  \__,_|_|\__,_|   /_/_/    |_||_|";
echo "                                                          ";
echo "                                                          ";


sleep 1
clear

