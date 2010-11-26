
NAME=Quantum\\\ Physics
MD=quantum_physics.md
OPTS=--toc

all: epub

epub: $(NAME).epub
pdf: $(NAME).pdf

$(NAME).epub: $(MD)
	pandoc $(OPTS) $< -o $@

$(NAME).pdf: $(MD)
	markdown2pdf $(OPTS) $< -o $@
