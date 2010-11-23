
INSTALL_LOC=../../../../sequences/map_and_territory
INSTALL_NAME=map_and_territory.md

NAME=map_and_territory_content.md

content: $(NAME)

install: content
	cp $(NAME) $(INSTALL_LOC)/$(INSTALL_NAME)

FILES= header.md \
simple_truth.md \
what_do_we_mean_by_rationality.md \
why_truth_and.md \
what_is_evidence.md \
how_much_evidence_does_it_take.md \
how_to_convince_me_that_2_2_3.md \
occams_razor.md \
the_lens_that_sees_its_flaws.md

$(NAME): $(FILES)
	cat $^ | sed 's/\/lw/http:\/\/lesswrong.com\/lw/g' > $@
	
