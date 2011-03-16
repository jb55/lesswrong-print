MDS=$(cat $1/filelist | sed "s/\(.*\)/$1\/md\/\1/g")
redo-ifchange $1/header $MDS
cat $1/header $MDS > $3
