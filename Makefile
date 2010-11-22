
index.html: index.md
	pandoc -T 'jb55.com' index.md -o index.html
