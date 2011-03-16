exec 2>&1
CONV=`locate ebook-convert | grep "ebook-convert$"`

if [ -z "$CONV" ]; then
  echo "warning: calibre's ebook-convert was not found, .mobi formats will be ignored"
  echo "" > $3
else
  echo "$CONV \$1 \$2" > $3
fi

chmod a+x "$3"
