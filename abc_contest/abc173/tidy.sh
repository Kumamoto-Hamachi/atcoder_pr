abc_array=("a" "b" "c" "d" "e" "f")
for i in "${abc_array[@]}"
do
	if test ! -e ${i} -a -e ${i}*.py ; then
		echo "${i}"
		mkdir "${i}"
	fi
	if test -e ${i}*.py ; then
		mv ${i}*.py ${i}/
	fi
done
