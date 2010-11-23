
index.html: readme.md
	pandoc -T 'jb55.com' readme.md -o index.html
