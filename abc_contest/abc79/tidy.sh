# 全ての値を出力する場合は、インデックスに「@」を指定するんや
# -a: and  -o: or
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
