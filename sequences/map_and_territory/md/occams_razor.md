
# Occam's Razor

The more complex an explanation is, the more evidence you need just
to find it in belief-space.  (In Traditional Rationality this is
often phrased [misleadingly](/lw/jo/einsteins_arrogance/), as "The
more complex a proposition is, the more evidence is required to
argue for it.")  How can we measure the complexity of an
explanation? How can we determine how much evidence is required?

Occam's Razor is often phrased as "The simplest explanation that
fits the facts."  Robert Heinlein replied that the simplest
explanation is "The lady down the street is a witch; she did it."

One observes that the length of an English sentence is not a good
way to measure "complexity".  And "fitting" the facts by merely
*failing to prohibit* them is insufficient.

Why, exactly, is the length of an English sentence a poor measure
of complexity?  Because when you speak a sentence aloud, you are
using *labels* for concepts that the listener shares - the receiver
has already stored the complexity in them.  Suppose we abbreviated
Heinlein's whole sentence as "Tldtsiawsdi!" so that the entire
explanation can be conveyed in one word; better yet, we'll give it
a short arbitrary label like "Fnord!"  Does this reduce the
complexity?  No, because you have to tell the listener in advance
that "Tldtsiawsdi!" stands for "The lady down the street is a
witch; she did it."  "Witch", itself, is a label for some
extraordinary assertions - just because we all know what it means
doesn't mean the concept is simple.

An enormous bolt of electricity comes out of the sky and hits
something, and the Norse tribesfolk say, "Maybe a really powerful
agent was angry and threw a lightning bolt."* *The human brain is
the most complex artifact in the known universe.  If *anger* seems
simple, it's because we don't see all the neural circuitry that's
implementing the emotion.  (Imagine trying to explain why
*Saturday Night Live* is funny, to an alien species with no sense
of humor.  But don't feel superior; you yourself have no sense of
fnord.)  The complexity of anger, and indeed the complexity of
intelligence, was glossed over by the humans who hypothesized Thor
the thunder-agent.

*To a human,* Maxwell's Equations take much longer to explain than
Thor.  Humans don't have a built-in vocabulary for calculus the way
we have a built-in vocabulary for anger.  You've got to explain
your language, and the language behind the language, and the very
concept of mathematics, before you can start on electricity.

And yet it seems that there should be some sense in which Maxwell's
Equations are *simpler* than a human brain, or Thor the
thunder-agent.

There is:  It's *enormously* easier (as it turns out) to write a
computer program that simulates Maxwell's Equations, compared to a
computer program that simulates an intelligent emotional mind like
Thor.

The formalism of Solomonoff Induction measures the "complexity of a
description" by the length of the shortest computer program which
produces that description as an output.  To talk about the
"shortest computer program" that does something, you need to
specify a space of computer programs, which requires a language and
interpreter. Solomonoff Induction uses Turing machines, or rather,
bitstrings that specify Turing machines.   What if you don't like
Turing machines? Then there's only a constant complexity penalty to
design your own Universal Turing Machine that interprets whatever
code you give it in whatever programming language you like. 
Different inductive formalisms are penalized by a worst-case
constant factor relative to each other, corresponding to the size
of a universal interpreter for that formalism.

In the better (IMHO) versions of Solomonoff Induction, the computer
program does not produce a deterministic prediction, but assigns
probabilities to strings.  For example, we could write a program to
explain a fair coin by writing a program that assigns equal
probabilities to all 2\^N strings of length N.  This is Solomonoff
Induction's approach to *fitting* the observed data.  The higher
the probability a program assigns to the observed data, the better
that program *fits* the data.  And probabilities must sum to 1, so
for a program to better "fit" one possibility, it must steal
probability mass from some other possibility which will then "fit"
much more poorly.  There is no superfair coin that assigns 100%
probability to heads and 100% probability to tails.

How do we trade off the fit to the data, against the complexity of
the program?  If you ignore complexity penalties, and think *only*
about fit, then you will always prefer programs that claim to
deterministically predict the data, assign it 100% probability.  If
the coin shows "HTTHHT", then the program which claims that the
coin was fixed to show "HTTHHT" fits the observed data 64 times
better than the program which claims the coin is fair.  Conversely,
if you ignore fit, and consider *only* complexity, then the "fair
coin" hypothesis will always seem simpler than any other
hypothesis.  Even if the coin turns up "HTHHTHHHTHHHHTHHHHHT..." 
Indeed, the fair coin *is* simpler and it fits this data exactly as
well as it fits any other string of 20 coinflips - no more, no less
- but we see another hypothesis, seeming not too complicated, that
fits the data much better.

If you let a program store one more binary bit of information, it
will be able to cut down a space of possibilities by half, and
hence assign twice as much probability to all the points in the
remaining space.  This suggests that one bit of program complexity
should cost *at least* a "factor of two gain" in the fit.  If you
try to design a computer program that explicitly stores an outcome
like "HTTHHT", the six bits that you lose in complexity must
destroy all plausibility gained by a 64-fold improvement in fit. 
Otherwise, you will sooner or later decide that all fair coins are
fixed.

Unless your program is being smart, and *compressing* the data, it
should do no good just to move one bit from the data into the
program description.

The way Solomonoff induction works to predict sequences is that you
sum up over all allowed computer programs - if any program is
allowed, Solomonoff induction becomes uncomputable - with each
program having a prior probability of (1/2) to the power of its
code length in bits, and each program is further weighted by its
fit to all data observed so far.  This gives you a weighted mixture
of experts that can predict future bits.

The Minimum Message Length formalism is nearly equivalent to
Solomonoff induction.  You send a string describing a code, and
then you send a string describing the data in that code.  Whichever
explanation leads to the shortest *total* message is the best. If
you think of the set of allowable codes as a space of computer
programs, and the code description language as a universal machine,
then Minimum Message Length is nearly equivalent to Solomonoff
induction.  (Nearly, because it chooses the *shortest* program,
rather than summing up over all programs.)

This lets us see clearly the problem with using "The lady down the
street is a witch; she did it" to explain the pattern in the
sequence "0101010101".  If you're sending a message to a friend,
trying to describe the sequence you observed, you would have to
say:  "The lady down the street is a witch; she made the sequence
come out 0101010101."  Your accusation of witchcraft wouldn't let
you *shorten* the rest of the message; you would still have to
describe, in full detail, the data which her witchery caused.

Witchcraft may fit our observations in the sense of qualitatively
*permitting* them; but this is because witchcraft permits
*everything*, like saying "[Phlogiston!](/lw/is/fake_causality/)" 
So, even after you say "witch", you still have to describe all the
observed data in full detail.  You have not
*compressed the total length of the message describing your observations*
by transmitting the message about witchcraft; you have simply added
a useless prologue, increasing the total length.

The real sneakiness was concealed in the word "it" of "A witch did
it".  A witch did *what?*

Of course, thanks to [hindsight bias](/lw/il/hindsight_bias/) and
[anchoring](/lw/j7/anchoring_and_adjustment/) and
[fake explanations](/lw/ip/fake_explanations/) and
[fake causality](/lw/is/fake_causality/) and
[positive bias](/lw/iw/positive_bias_look_into_the_dark/) and
[motivated cognition](/lw/he/knowing_about_biases_can_hurt_people/),
it may seem all too obvious that if a woman is a witch, of *course*
she would make the coin come up 0101010101.  But of this I have
already spoken.
