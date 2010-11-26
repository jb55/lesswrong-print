
# Decoherence is Simple

An epistle to the physicists:

When I was but a little lad, my father, a Ph.D. physicist, warned
me sternly against meddling in the affairs of physicists; he said
that it was hopeless to try to comprehend physics without the
formal math. Period.  No escape clauses.  But I had read in
Feynman's popular books that if you really understood physics, you
ought to be able to explain it to a nonphysicist.  I believed
Feynman instead of my father, because Feynman had won the Nobel
Prize and my father had not.

It was not until later - when I was reading the *Feynman Lectures,*
in fact - that I realized that my father had given me the simple
and honest truth.  No math = no physics.

By vocation I am a Bayesian, not a physicist.  Yet although I was
raised not to meddle in the affairs of physicists, my hand has been
forced by the occasional gross misuse of three terms: 
*Simple, falsifiable,* and *testable*.

The foregoing introduction is so that you don't laugh, and say, "Of
course I know what those words mean!"  There is math here.

Let's begin with the remark that started me down this whole avenue,
of which I have seen several versions; paraphrased, it runs:

> "The Many-Worlds interpretation of quantum mechanics postulates
> that there are vast numbers of other worlds, existing alongside our
> own.  Occam's Razor says we should not multiply entities
> unnecessarily."

Now it must be said, in all fairness, that those who say this will
usually also confess:

> "But this is not a universally accepted application of Occam's
> Razor; some say that Occam's Razor should apply to the laws
> governing the model, not the number of objects inside the model."

So it is good that we are all acknowledging the contrary arguments,
and telling both sides of the story -

But suppose you had to *calculate* the simplicity of a theory.

The original formulation of William of Ockham stated:

> *Lex parsimoniae:  Entia non sunt multiplicanda praeter necessitatem.*

"The law of parsimony:  Entities should not be multiplied beyond
necessity."

But this is qualitative advice.  It is not enough to say whether
one theory seems more simple, or seems more complex, than another -
you have to assign a number; and the number has to be meaningful,
you can't just make it up.  Crossing this gap is like the
difference between being able to eyeball which things are moving
"fast" or "slow", and starting to measure and calculate
velocities.

Suppose you tried saying:  "Count the words - that's how
complicated a theory is."

Robert Heinlein once claimed (tongue-in-cheek, I hope) that the
"simplest explanation" is always:  "The woman down the street is a
witch; she did it."  Eleven words - not many physics papers can
beat that.

Faced with this challenge, there are two different roads you can
take.

First, you can ask:  "The woman down the street is a *what?*" Just
because English has one word to indicate a concept, doesn't mean
that the concept itself is simple.  Suppose you were talking to
aliens who didn't know about witches, women, or streets - how long
would it take you to explain your theory to them?  Better yet,
suppose you had to write a computer program that embodied your
hypothesis, and output what you say are your hypothesis's
predictions - how big would that computer program have to be? 
Let's say that your task is to predict a time series of measured
positions for a rock rolling down a hill.  If you write a
subroutine that simulates witches, this doesn't seem to help narrow
down where the rock rolls - the extra subroutine just inflates your
code.  You might find, however, that your code necessarily includes
a subroutine that squares numbers.

Second, you can ask:  "The woman down the street is a witch; she
did *what?*" Suppose you want to describe some event, as precisely
as you possibly can given the evidence available to you - again,
say, the distance/time series of a rock rolling down a hill.  You
can preface your explanation by saying, "The woman down the street
is a witch," but your friend then says, "What did she *do*?", and
you reply, "She made the rock roll one meter after the first
second, nine meters after the third second..."  Prefacing your
message with "The woman down the street is a witch," doesn't help
to *compress* the rest of your description. On the whole, you just
end up sending a longer message than necessary - it makes more
sense to just leave off the "witch" prefix.  On the other hand, if
you take a moment to talk about Galileo, you may be able to greatly
compress the next five thousand detailed time series for rocks
rolling down hills.

If you follow the first road, you end up with what's known as
Kolmogorov complexity and Solomonoff induction.  If you follow the
second road, you end up with what's known as Minimum Message
Length.

> "Ah, so I can pick and choose among definitions of simplicity?"

No, actually the two formalisms in their most highly developed
forms were proven equivalent.

> "And I suppose now you're going to tell me that both formalisms
> come down on the side of 'Occam means counting laws, not counting
> objects'."

More or less.  In Minimum Message Length, so long as you can tell
your friend an exact recipe they can mentally follow to get the
rolling rock's time series, we don't care how much mental work it
takes to follow the recipe.  In Solomonoff induction, we count bits
in the program code, not bits of RAM used by the program as it
runs.  "Entities" are lines of code, not simulated objects.  And as
said, these two formalisms are ultimately equivalent.

Now before I go into any further detail on formal simplicity, let
me digress to consider the objection:

> "So what?  Why can't I just invent my *own* formalism that does
> things differently?  Why should I pay any attention to the way you
> happened to decide to do things, over in your field? Got any
> *experimental* evidence that shows I should do things this way?"

Yes, actually, believe it or not.  But let me start at the
beginning.

The conjunction rule of probability theory states:

P(X∧Y) ≤ P(X)

For any propositions X and Y, the probability that "X is true, and
Y is true", is *less than or equal to* the probability that "X is
true (whether or not Y is true)".  (If this statement sounds not
terribly profound, then let me assure you that it is easy to find
cases where human probability assessors
[violate this rule](http://www.overcomingbias.com/2007/09/conjunction-fal.html).)

You usually can't apply the conjunction rule P(X∧Y) ≤ P(X) directly
to a conflict between mutually exclusive hypotheses. The
conjunction rule only applies directly to cases where the
left-hand-side strictly implies the right-hand-side.  Furthermore,
the conjunction is just an inequality; it doesn't give us the kind
of quantitative calculation we want.

But the conjunction rule does give us a rule of monotonic decrease
in probability: as you tack more details onto a story, and each
additional detail can potentially be true or false, the story's
probability goes down monotonically.  Think of probability as a
conserved quantity: there's only so much to go around.  As the
number of details in a story goes up, the number of possible
stories increases exponentially, but the sum over their
probabilities can never be greater than 1.  For every story "X∧Y",
there is a story "X∧\~Y".  When you *just* tell the story "X", you
get to *sum over* the possibilities Y and \~Y.

If you add ten details to X, each detail one that could potentially
be true or false, then that story must compete with (2^10^ - 1)
other equally detailed stories for precious probability.  If on the
other hand it suffices to *just* say X, you can sum your
probability over 2^10^ stories ( (X∧Y∧Z∧...) ∨ (X∧\~Y∧Z∧...) ∨
...)

The "entities" counted by Occam's Razor should be individually
costly in probability; this is why we prefer theories with fewer of
them.

Imagine a lottery which sells up to a million tickets, where each
possible ticket is sold only once, and the lottery has sold every
ticket at the time of the drawing.  A friend of yours has bought
one ticket for $1 - which seems to you like a poor investment,
because the payoff is only $500,000.  Yet your friend says, "Ah,
but consider the alternative hypotheses, 'Tomorrow, someone will
win the lottery' and 'Tomorrow, I will win the lottery.'  Clearly,
the latter hypothesis is simpler by Occam's Razor; it only makes
mention of one person and one ticket, while the former hypothesis
is more complicated: it mentions a million people and a million
tickets!"

To say that Occam's Razor only counts laws, and not objects, is not
quite correct: what counts against a theory are the entities it
must mention*explicitly*, because these are the entities that
cannot be *summed over*. Suppose that you and a friend are puzzling
over an amazing billiards shot, in which you are told the starting
state of a billiards table, and which balls were sunk, but not how
the shot was made.  You propose a theory which involves ten
specific collisions between ten specific balls; your friend
counters with a theory that involves five specific collisions
between five specific balls.  What counts against your theories is
not *just* the laws that you claim to govern billiard balls, but
any *specific* billiard balls that had to be in some *particular*
state for your model's prediction to be successful.

If you measure the temperature of your living room as 22° Celsius,
it does not make sense to say:  "Your thermometer is probably in
error; the room is much more likely to be 20° C.  Because, when you
consider all the particles in the room, there are exponentially
vastly more states they can occupy if the temperature is really 22°
C - which makes any *particular* state all the more improbable." 
But no matter which exact 22° C state your room occupies, you can
make the same prediction (for the supervast majority of these
states) that your thermometer will end up showing 22° C, and so you
are not sensitive to the *exact* initial conditions.  You do not
need to specify an exact position of all the air molecules in the
room, so that is not counted against the probability of your
explanation.

On the other hand - returning to the case of the lottery - suppose
your friend won ten lotteries in a row.  At this point you should
suspect the fix is in.  The hypothesis "My friend wins the lottery
every time" is more complicated than the hypothesis "Someone wins
the lottery every time".  But the former hypothesis is predicting
the data much more precisely.

In the Minimum Message Length formalism, saying "There is a single
person who wins the lottery every time" at the beginning of your
message, compresses your description of who won the next ten
lotteries; you can just say "And that person is Fred Smith" to
finish your message.  Compare to, "The first lottery was won by
Fred Smith, the second lottery was won by Fred Smith, the third
lottery was ..."

In the Solomonoff induction formalism, the prior probability of "My
friend wins the lottery every time" is low, because the program
that describes the lottery now needs explicit code that singles out
your friend; but because that program can produce a
*tighter probability distribution* over potential lottery winners
than "Someone wins the lottery every time", it can, by
[Bayes's Rule](http://yudkowsky.net/bayes/technical.html), overcome
its prior improbability and win out as a hypothesis.

Any formal theory of Occam's Razor should quantitatively define,
not only "entities" and "simplicity", but also the "necessity"
part.

Minimum Message Length defines necessity as "that which compresses
the message".

Solomonoff induction assigns a prior probability to each possible
computer program, with the entire distribution, over every possible
computer program, summing to no more than 1.  This can be
accomplished using a binary code where no valid computer program is
a prefix of any other valid computer program ("prefix-free code"),
i.e. because it contains a stop code.  Then the prior probability
of any program P is simply 2^-L(P)^ where L(P) is the length of P
in bits.

P itself can be a program that takes in a (possibly zero-length)
string of bits and outputs the conditional probability that the
*next* bit will be 1; this makes P a probability distribution over
all binary sequences.  This version of Solomonoff induction, for
any string, gives us a mixture of posterior probabilities dominated
by the shortest programs that most precisely predict the string. 
Summing over this mixture gives us a prediction for the next bit.

The upshot is that it takes more Bayesian evidence - more
successful predictions, or more precise predictions - to justify
more complex hypotheses.  But it can be done; the burden of prior
improbability is not infinite.  If you flip a coin four times, and
it comes up heads every time, you don't conclude right away that
the coin produces only heads; but if the coin comes up heads twenty
times in a row, you should be considering it very seriously.  What
about the hypothesis that a coin is fixed to produce "HTTHTT..." in
a repeating cycle?  That's more bizarre - but after a hundred
coinflips you'd be a fool to deny it.

Standard chemistry says that in a gram of hydrogen gas there are
six hundred billion trillion hydrogen atoms.  This is a startling
statement, but there was some amount of evidence that sufficed to
convince physicists in general, and you particularly, that this
statement was true.

Now ask yourself how much evidence it would take to convince you of
a theory with six hundred billion trillion separately specified
physical laws.

Why doesn't the prior probability of a program, in the Solomonoff
formalism, include a measure of how much RAM the program uses, or
the total running time?

The simple answer is, "Because space and time resources used by a
program aren't mutually exclusive possibilities."  It's not like
the program specification, that can only have a 1 or a 0 in any
particular place.

But the even simpler answer is, "Because, historically speaking,
that heuristic doesn't work."

Occam's Razor was raised as an objection to the suggestion that
nebulae were actually distant galaxies - it seemed to vastly
multiply the number of entities in the universe. 
*All those stars!*

Over and over, in human history, the universe has gotten bigger.  A
variant of Occam's Razor which, on each such occasion, would label
the vaster universe as *more unlikely*, would fare less well under
humanity's historical experience.

This is part of the "experimental evidence" I was alluding to
earlier.  While you can justify theories of simplicity on mathy
sorts of grounds, it is also desirable that they actually work in
practice. (The other part of the "experimental evidence" comes from
statisticians / computer scientists / Artificial Intelligence
researchers, testing which definitions of "simplicity" let them
construct computer programs that do empirically well at predicting
future data from past data.  Probably the Minimum Message Length
paradigm has proven most productive here, because it is a very
adaptable way to think about real-world problems.)

Imagine a spaceship whose launch you witness with great fanfare; it
accelerates away from you, and is soon traveling at .9 *c*. If the
expansion of the universe continues, as current cosmology holds it
should, there will come some future point where - according to your
model of reality - you don't expect to be able to interact with the
spaceship even in principle; it has gone over the cosmological
horizon relative to you, and photons leaving it will not be able to
outrace the expansion of the universe.

Should you believe that
[the spaceship literally, physically disappears from the universe](http://www.overcomingbias.com/2008/04/implied-invisib.html)
at the point where it goes over the cosmological horizon relative
to you?

If you believe that Occam's Razor counts the objects in a model,
then yes, you should.  Once the spaceship goes over your
cosmological horizon, the model in which the spaceship instantly
disappears, and the model in which the spaceship continues onward,
give indistinguishable predictions; they have no Bayesian
evidential advantage over one another.  But one model contains many
fewer "entities"; it need not speak of all the quarks and electrons
and fields composing the spaceship.  So it is simpler to suppose
that the spaceship vanishes.

Alternatively, you could say:  "Over numerous experiments, I have
generalized certain laws that govern observed particles.  The
spaceship is made up of such particles.  Applying these laws, I
deduce that the spaceship should continue on after it crosses the
cosmological horizon, with the same momentum and the same energy as
before, on pain of violating the conservation laws that I have seen
holding in every examinable instance.  To suppose that the
spaceship vanishes, I would have to add a new law, 'Things vanish
as soon as they cross my cosmological horizon'."

The decoherence (aka Many-Worlds) version of quantum mechanics
states that measurements obey the same quantum-mechanical rules as
all other physical processes.  Applying these rules to macroscopic
objects in exactly the same way as microscopic ones, we end up with
observers in states of superposition.  Now there are many questions
that can be asked here, such as "But then why don't all binary
quantum measurements appear to have 50/50 probability, since
different versions of us see both outcomes?"

However, the objection that decoherence violates Occam's Razor on
account of multiplying objects in the model is simply wrong.

Decoherence does not require the wavefunction to take on some
complicated exact initial state.  Many-worlds is not specifying all
its worlds by hand, but generating them via the compact laws of
quantum mechanics.  A computer program that directly simulates QM
to make experimental predictions, would require a great deal of RAM
to run - but simulating the wavefunction is exponentially expensive
in *any*flavor of QM!  Decoherence is simply more so. 
*Many*physical discoveries in human history, from stars to
galaxies, from atoms to quantum mechanics, have vastly increased
the apparent CPU load of what we believe to be the universe.

Many-Worlds is not a zillion worlds worth of complicated, any more
than the atomic hypothesis is a zillion atoms worth of
complicated.  For anyone with a quantitative grasp of Occam's Razor
that is simply not what the term "complicated" means.

As with the historical case of galaxies, it may be that people have
mistaken their *shock* at the notion of a universe that large, for
a probability penalty, and invoked Occam's Razor in justification. 
But if there are probability penalties for decoherence, the
*largeness of the implied universe*, per se, is definitely not
their source!

The notion that decoherent worlds are additional entities penalized
by Occam's Razor, is just plain mistaken.  It is not
sort-of-right.  It is not an argument that is weak but still
valid.  It is not a defensible position that could be shored up
with further arguments.  It is entirely defective as probability
theory.  It is not fixable.  It is bad math.  2 + 2 = 3.

**Continued in**: 
[Decoherence is Falsifiable and Testable](http://www.overcomingbias.com/2008/05/mwi-is-falsifia.html).
