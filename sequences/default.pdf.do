redo-ifchange $1.md
markdown2pdf --toc -f markdown $1.md -o $1_
mv $1_.pdf $3
