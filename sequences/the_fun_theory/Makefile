
NAME=The\\\ Fun\\\ Theory
MD=the_fun_theory.md
OPTS=--toc

all: epub pdf

epub: $(NAME).epub
pdf: $(NAME).pdf

$(NAME).epub: $(MD)
	pandoc $(OPTS) $< -o $@

$(NAME).pdf: $(MD)
	markdown2pdf $(OPTS) $< -o $@
