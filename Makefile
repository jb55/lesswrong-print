
index.html: readme.md
	pandoc --toc -c "assets/style.css" --section-divs readme.md -o index.html
