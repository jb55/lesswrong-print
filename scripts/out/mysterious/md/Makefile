
INSTALL_LOC=../../../../sequences/mysterious
INSTALL_NAME=mysterious.md

NAME=mysterious_content.md

content: $(NAME)

install: content
	cp $(NAME) $(INSTALL_LOC)/$(INSTALL_NAME)

FILES=making_beliefs_pay_rent_in_anticipated_experiences.md \
	belief_in_belief.md \
	bayesian_judo.md \
	professing_and_cheering.md \
	belief_as_attire.md \
	focus_your_uncertainty.md \
	the_virtue_of_narrowness.md \
	your_strength_as_a_rationalist.md \
	absence_of_evidence_is_evidence_of_absence.md \
	conservation_of_expected_evidence.md \
	hindsight_bias.md \
	hindsight_devalues_science.md \
	fake_explanations.md \
	guessing_the_teachers_password.md \
	science_as_attire.md \
	fake_causality.md \
	semantic_stopsigns.md \
	mysterious_answers_to_mysterious_questions.md \
	the_futility_of_emergence.md \
	say_not_complexity.md \
	positive_bias_look_into_the_dark.md \
	my_wild_and_reckless_youth.md \
	failing_to_learn_from_history.md \
	making_history_available.md \
	explainworshipignore.md \
	science_as_curiositystopper.md \
	applause_lights.md \
	chaotic_inversion.md

$(NAME): $(FILES)
	cat $^ | sed 's/\/lw/http:\/\/lesswrong.com\/lw/g' > $@
	
