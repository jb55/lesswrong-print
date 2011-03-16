redo-ifchange $1.md
pandoc --toc -f markdown -t epub $1.md -o $1_
mv $1_ $3
