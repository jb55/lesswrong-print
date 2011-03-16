redo-ifchange $1.epub convert-ebook
./convert-ebook $1.epub $1_.mobi > /dev/null
mv $1_.mobi $3
