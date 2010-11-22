
NAME=Reductionism
MD=$(NAME).md
OPTS=--toc

all: epub pdf

epub: $(NAME).epub
pdf: $(NAME).pdf

$(NAME).epub: $(MD)
	pandoc $(OPTS) $< -o $@

$(NAME).pdf: $(MD)
	markdown2pdf $(OPTS) $< -o $@
