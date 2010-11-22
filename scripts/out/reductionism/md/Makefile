
INSTALL_LOC=../../../../sequences/reductionism
INSTALL_NAME=Reductionism.md

NAME=reductionism_content.md

content: $(NAME)

install: content
	cp $(NAME) $(INSTALL_LOC)/$(INSTALL_NAME)

FILES= header.md \
	dissolving_the_question.md \
	wrong_questions.md \
	righting_a_wrong_question.md \
	mind_projection_fallacy.md \
	probability_is_in_the_mind.md \
	the_quotation_is_not_the_referent.md \
	qualitatively_confused.md \
	reductionism.md \
	explaining_vs_explaining_away.md \
	fake_reductionism.md \
	savanna_poets.md \
	joy_in_the_merely_real.md \
	joy_in_discovery.md \
	bind_yourself_to_reality.md \
	if_you_demand_magic_magic_wont_help.md \
	mundane_magic.md \
	the_beauty_of_settled_science.md \
	amazing_breakthrough_day_april_1st.md \
	is_humanism_a_religionsubstitute.md \
	scarcity.md \
	to_spread_science_keep_it_secret.md \
	initiation_ceremony.md \
	awww_a_zebra.md \
	hand_vs_fingers.md \
	angry_atoms.md \
	heat_vs_motion.md \
	brain_breakthrough_its_made_of_neurons.md \
	reductive_reference.md \
	zombies_zombies.md \
	zombie_responses.md \
	the_generalized_antizombie_principle.md \
	gazp_vs_glut.md \
	belief_in_the_implied_invisible.md \
	zombies_the_movie.md \
	excluding_the_supernatural.md \
	psychic_powers.md

$(NAME): $(FILES)
	cat $^ | sed 's/\/lw/http:\/\/lesswrong.com\/lw/g' > $@
	
