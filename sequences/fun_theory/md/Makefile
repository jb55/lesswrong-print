
INSTALL_LOC=../../../../sequences/the_fun_theory
INSTALL_NAME=the_fun_theory.md

NAME=the_fun_theory_content.md

content: $(NAME)

install: content
	cp $(NAME) $(INSTALL_LOC)/$(INSTALL_NAME)

FILES= header.md \
	31_laws_of_fun.md \
	prolegomena_to_a_theory_of_fun.md \
	high_challenge.md \
	complex_novelty.md \
	continuous_improvement.md \
	sensual_experience.md \
	living_by_your_own_strength.md \
	free_to_optimize.md \
	harmful_options.md \
	devils_offers.md \
	nonperson_predicates.md \
	nonsentient_optimizers.md \
	cant_unbirth_a_child.md \
	amputation_of_destiny.md \
	dunbars_function.md \
	in_praise_of_boredom.md \
	sympathetic_minds.md \
	interpersonal_entanglement.md \
	failed_utopia_42.md \
	growing_up_is_hard.md \
	changing_emotions.md \
	emotional_involvement.md \
	serious_stories.md \
	eutopia_is_scary.md \
	building_weirdtopia.md \
	justified_expectation_of_pleasant_surprises.md \
	seduced_by_imagination.md \
	the_uses_of_fun_theory.md \
	higher_purpose.md


$(NAME): $(FILES)
	cat $^ | sed 's/\/lw/http:\/\/lesswrong.com\/lw/g' > $@
	
