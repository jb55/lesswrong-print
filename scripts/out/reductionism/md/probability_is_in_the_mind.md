
# Probability is in the Mind

Yesterday I spoke of the Mind Projection Fallacy, giving the
example of the alien monster who carries off a girl in a torn dress
for intended ravishing - a mistake which I imputed to the artist's
tendency to think that a woman's sexiness is a property of the
woman herself, `woman.sexiness`, rather than something that exists
in the mind of an observer, and probably wouldn't exist in an alien
mind.

The term "Mind Projection Fallacy" was coined by the late great
Bayesian Master, E. T. Jaynes, as part of his long and hard-fought
battle against the accursĂ¨d frequentists.  Jaynes was of the
opinion that probabilities were in the mind, not in the environment
- that probabilities express ignorance, states of partial
information; and if I am ignorant of a phenomenon, that is a fact
about my state of mind, not a fact about the phenomenon.

I cannot do justice to this ancient war in a few words - but the
classic example of the argument runs thus:

You have a coin.  
The coin is biased.  
You don't know which way it's biased or how much it's biased. 
Someone just told you, "The coin is biased" and that's all they
said.  
This is all the information you have, and the only information you
have.

You draw the coin forth, flip it, and slap it down.

Now - before you remove your hand and look at the result - are you
willing to say that you assign a 0.5 probability to the coin having
come up heads?

The frequentist says, "No.  Saying 'probability 0.5' means that the
coin has an inherent propensity to come up heads as often as tails,
so that if we flipped the coin infinitely many times, the ratio of
heads to tails would approach 1:1.  But we know that the coin is
biased, so it can have any probability of coming up heads *except*
0.5."

The Bayesian says, "Uncertainty exists in the map, not in the
territory.  In the real world, the coin has either come up heads,
or come up tails.  Any talk of 'probability' must refer to the
*information* that I have about the coin - my state of partial
ignorance and partial knowledge - not just the coin itself. 
Furthermore, I have all sorts of theorems showing that if I don't
treat my partial knowledge a
[certain way](http://www.overcomingbias.com/2008/01/something-to-pr.html),
I'll make stupid bets.  If I've got to plan, I'll plan for a 50/50
state of uncertainty, where I don't weigh outcomes conditional on
heads any more heavily in my mind than outcomes conditional on
tails.  You can call that number whatever you like, but it has to
obey the probability laws on pain of stupidity.  So I don't have
the slightest hesitation about calling my outcome-weighting a
probability."

I side with the Bayesians.  You may have noticed that about me.

Even before a fair coin is tossed, the notion that it has an
*inherent* 50% probability of coming up heads may be just plain
wrong.  Maybe you're holding the coin in such a way that it's just
about guaranteed to come up heads, or tails, given the force at
which you flip it, and the air currents around you.  But, if you
don't know which way the coin is biased on this one occasion, so
what?

I believe there was a lawsuit where someone alleged that the draft
lottery was unfair, because the slips with names on them were not
being mixed thoroughly enough; and the judge replied, "To whom is
it unfair?"

To make the coinflip experiment repeatable, as frequentists are
wont to demand, we could build an automated coinflipper, and verify
that the results were 50% heads and 50% tails.  But maybe a robot
with extra-sensitive eyes and a good grasp of physics, watching the
autoflipper prepare to flip, could predict the coin's fall in
advance - not with certainty, but with 90% accuracy.  Then what
would the *real* probability be?

There is no "real probability".  The robot has one state of partial
information.  You have a different state of partial information. 
The coin itself has no mind, and doesn't assign a probability to
anything; it just flips into the air, rotates a few times, bounces
off some air molecules, and lands either heads or tails.

So that is the Bayesian view of things, and I would now like to
point out a couple of classic brainteasers that derive their
brain-*teasing* ability from the tendency to think of probabilities
as inherent properties of objects.

Let's take the old classic:  You meet a mathematician on the
street, and she happens to mention that she has given birth to two
children on two separate occasions.  You ask:  "Is at least one of
your children a boy?"  The mathematician says, "Yes, he is."

What is the probability that she has two boys?  If you assume that
the prior probability of a child being a boy is 1/2, then the
probability that she has two boys, on the information given, is
1/3.  The prior probabilities were:  1/4 two boys, 1/2 one boy one
girl, 1/4 two girls.  The mathematician's "Yes" response has
probability \~1 in the first two cases, and probability \~0 in the
third.  Renormalizing leaves us with a 1/3 probability of two boys,
and a 2/3 probability of one boy one girl.

But suppose that instead you had asked, "Is your eldest child a
boy?" and the mathematician had answered "Yes."  Then the
probability of the mathematician having two boys would be 1/2. 
Since the eldest child is a boy, and the younger child can be
anything it pleases.

Likewise if you'd asked "Is your youngest child a boy?"  The
probability of their being both boys would, again, be 1/2.

Now, if at least one child is a boy, it must be either the oldest
child who is a boy, or the youngest child who is a boy.  So how can
the answer in the first case be different from the answer in the
latter two?

Or here's a very similar problem:  Let's say I have four cards, the
ace of hearts, the ace of spades, the two of hearts, and the two of
spades.  I draw two cards at random.  You ask me, "Are you holding
at least one ace?" and I reply "Yes."  What is the probability that
I am holding a pair of aces?  It is 1/5.  There are six possible
combinations of two cards, with equal prior probability, and you
have just eliminated the possibility that I am holding a pair of
twos.  Of the five remaining combinations, only one combination is
a pair of aces.  So 1/5.

Now suppose that instead you asked me, "Are you holding the ace of
spades?"  If I reply "Yes", the probability that the other card is
the ace of hearts is 1/3.  (You know I'm holding the ace of spades,
and there are three possibilities for the other card, only one of
which is the ace of hearts.)  Likewise, if you ask me "Are you
holding the ace of hearts?" and I reply "Yes", the probability I'm
holding a pair of aces is 1/3.

But then how can it be that if you ask me, "Are you holding at
least one ace?" and I say "Yes", the probability I have a pair is
1/5?  Either I must be holding the ace of spades or the ace of
hearts, as you know; and either way, the probability that I'm
holding a pair of aces is 1/3.

How can this be?  Have I miscalculated one or more of these
probabilities?

If you want to figure it out for yourself, do so now, because I'm
about to reveal...

That all stated calculations are correct.

As for the paradox, there isn't one.  The *appearance*of paradox
comes from thinking that the probabilities must be properties of
the cards themselves.  The ace I'm holding has to be either hearts
or spades; but that doesn't mean that your *knowledge about* my
cards must be the same as if you *knew* I was holding hearts, or
*knew* I was holding spades.

It may help to think of Bayes's Theorem:

> P(H|E) = P(E|H)P(H) / P(E)

That last term, where you divide by P(E), is the part where you
throw out all the possibilities that have been eliminated, and
renormalize your probabilities over what remains.

Now let's say that you ask me, "Are you holding at least one ace?" 
*Before* I answer, your probability that I say "Yes" should be
5/6.

But if you ask me "Are you holding the ace of spades?", your prior
probability that I say "Yes" is just 1/2.

So right away you can see that you're *learning* something very
different in the two cases.  You're going to be eliminating some
different possibilities, and renormalizing using a different P(E). 
If you learn two different items of evidence, you shouldn't be
surprised at ending up in two different states of partial
information.

Similarly, if I ask the mathematician, "Is at least one of your two
children a boy?" I expect to hear "Yes" with probability 3/4, but
if I ask "Is your eldest child a boy?" I expect to hear "Yes" with
probability 1/2.  So it shouldn't be surprising that I end up in a
different state of partial knowledge, depending on which of the two
questions I ask.

The only reason for seeing a "paradox" is thinking as though the
probability of holding a pair of aces is *a property of cards* that
have at least one ace, or a property *of cards* that happen to
contain the ace of spades.  In which case, it would be paradoxical
for card-sets containing at least one ace to have an inherent
pair-probability of 1/5, while card-sets containing the ace of
spades had an inherent pair-probability of 1/3, and card-sets
containing the ace of hearts had an inherent pair-probability of
1/3.

Similarly, if you think a 1/3 probability of being both boys is an
*inherent property* of child-sets that include at least one boy,
then that is not consistent with child-sets of which the eldest is
male having an *inherent* probability of 1/2 of being both boys,
and child-sets of which the youngest is male having an inherent 1/2
probability of being both boys.  It would be like saying, "All
green apples weigh a pound, and all red apples weigh a pound, and
all apples that are green or red weigh half a pound."

That's what happens when you start thinking as if probabilities are
*in* things, rather than probabilities being states of partial
information *about*things.

Probabilities express uncertainty, and it is only agents who can be
uncertain.  A blank map does not correspond to a blank territory. 
Ignorance is in the mind.
