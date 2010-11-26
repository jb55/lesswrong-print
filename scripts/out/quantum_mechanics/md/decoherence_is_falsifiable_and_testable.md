
# Decoherence is Falsifiable and Testable

The words "falsifiable" and "testable" are sometimes used
interchangeably, which imprecision is the price of speaking in
English.  There are two different probability-theoretic qualities I
wish to discuss here, and I will refer to one as "falsifiable" and
the other as "testable" because it seems like the best fit.

As for the math, it begins, as so many things do, with:

![Bayestheorem](http://lesswrong.com/static/imported/2008/05/06/bayestheorem.png "Bayestheorem")
This is Bayes's Theorem.  I own at least two distinct items of
clothing printed with this theorem, so it must be important.

I am going to assume you are familiar with elementary probability
theory; should the above theorem fail to be transparently
meaningful, you should stop here and read an
[introduction to Bayes](http://www.google.com/search?q=bayes+introduction). 
(I've [written one](http://yudkowsky.net/bayes/bayes.html), but
it's aimed at not-physicists.)

To review quickly, B here refers to an item of evidence, A~i~ is
some hypothesis under consideration, and the A~j~ are competing,
mutually exclusive hypotheses.  P(B|A~i~) means "the probability of
seeing B, if hypothesis A~i~ is true" and P(A~i~|B) means "the
probability hypothesis A~i~ is true, if we see B".

The mathematical phenomenon that I will call "falsifiability" is
the scientifically desirable property of a hypothesis that it
should concentrate its probability mass into preferred outcomes,
which implies that it must also assign low probability to some
un-preferred outcomes; probabilities must sum to 1 and there is
only so much probability to go around.  Ideally there should be
possible observations which would drive down the hypothesis's
probability to nearly zero:  There should be things the hypothesis
*cannot* explain, conceivable experimental results with which the
theory is *not* compatible.  A theory that can explain everything,
prohibits nothing, and so gives us no advice about what to expect.

[![Bayestheorem\_3](http://lesswrong.com/static/imported/2008/05/06/bayestheorem_3.png "Bayestheorem_3")](http://lesswrong.com/static/imported/2008/05/06/bayestheorem_3.png)In
terms of Bayes's Theorem, if there is at least some observation B
that the hypothesis A~i~can't explain", i.e., P(B|A~i~) is tiny,
then the numerator P(B|A~i~)P(A~i~) will also be tiny, and likewise
the posterior probability P(A~i~|B).  Updating on having seen the
impossible result B has driven the probability of A~i~ down to
nearly zero.  A theory which refuses to make itself vulnerable in
this way, will need to spread its probability widely, so that it
has no holes; it will not be able to strongly concentrate
probability into a few preferred outcomes; it will not be able to
offer precise advice.

Thus is the rule of science derived in probability theory.

As depicted here, "falsifiability" is something you evaluate by
looking at a *single* hypothesis, asking, "How narrowly does it
concentrate its probability distribution over possible outcomes? 
How narrowly does it tell me what to expect?  Can it explain some
possible outcomes much better than others?"

Is the decoherence interpretation of quantum mechanics
*falsifiable?*  Are there experimental results that could drive its
probability down to an infinitesimal?

Sure:  We could measure entangled particles that should always have
opposite spin, and find that if we measure them far enough apart,
they sometimes have the same spin.

Or we could find apples falling upward, the planets of the Solar
System zigging around at random, and an atom that kept emitting
photons without any apparent energy source.  Those observations
would also falsify decoherent quantum mechanics.  They're things
that, on the hypothesis that decoherent QM governs the universe, we
should definitely *not expect* to see.

So there do exist observations B whose P(B|A~deco~~ ~) is
infinitesimal, which would drive P(A~deco~|B) down to an
infinitesimal.

> "But that's just because decoherent quantum mechanics is still
> quantum mechanics!  What about the decoherence part, per se, versus
> the collapse postulate?"

[![Bayestheorem\_3](http://lesswrong.com/static/imported/2008/05/06/bayestheorem_3.png "Bayestheorem_3")](http://lesswrong.com/static/imported/2008/05/06/bayestheorem_3.png)
We're getting there.  The point is that I just defined a test that
leads you to think about one hypothesis at a time (and called it
"falsifiability").  If you want to distinguish decoherence *versus*
collapse, you have to think about at least *two* hypotheses at a
time.

Now really the "falsifiability" test is not quite *that* singly
focused, i.e., the sum in the denominator has got to contain *some*
other hypothesis.  But what I just defined as "falsifiability"
pinpoints the kind of problem that Karl Popper was complaining
about, when he said that Freudian psychoanalysis was
"unfalsifiable" because it was equally good at coming up with an
explanation for every possible thing the patient could do.

If you belonged to an alien species that had never invented the
collapse postulate or Copenhagen Interpretation - if the only
physical theory you'd *ever* heard of was decoherent QM - if *all*
you had in your head was the differential equation for the
wavefunction's evolution plus the Born probability rule - you would
still have sharp expectations of the universe.  You would not live
in a magical world where anything was probable.

> "But you could say exactly the same thing about quantum mechanics
> *without* (macroscopic) decoherence."

Well, yes!  Someone walking around with the differential equation
for the wavefunction's evolution, plus a collapse postulate that
obeys the Born probabilities and is triggered before superposition
reaches macroscopic levels, still lives in a universe where apples
fall down rather than up.

> "But where does decoherence make a *new*prediction, one that lets
> us *test*it?"

A "new" prediction relative to what?  To the state of knowledge
possessed by the ancient Greeks?  If you went back in time and
showed them decoherent QM, they would be enabled to make many
experimental predictions they could not have made before.

When you say "new prediction", you mean "new" relative to some
other hypothesis that defines the "old prediction".  This gets us
into the theory of what I've chosen to label *testability*; and the
algorithm inherently considers at least two hypotheses at a time. 
You cannot call something a "*new* prediction" by considering only
one hypothesis in isolation.

In Bayesian terms, you are looking for an item of evidence B that
will produce evidence for one hypothesis over another,
distinguishing between them, and the process of producing this
evidence we could call a "test".  You are looking for an
experimental result B such that:

> p(B|A~d~) != p(B|A~c~)

that is, some outcome B which has a different probability,
conditional on the decoherence hypothesis being true, versus its
probability if the collapse hypothesis is true.  Which in turn
implies that the posterior odds for decoherence and collapse, will
become different from the prior odds:

[](http://lesswrong.com/static/imported/2008/05/06/bayesodds.png)

[![Bayesodds\_2](http://lesswrong.com/static/imported/2008/05/06/bayesodds_2.png "Bayesodds_2")](http://lesswrong.com/static/imported/2008/05/06/bayesodds_2.png)

This equation is symmetrical (assuming no probability is
[literally equal to 0](http://www.overcomingbias.com/2008/01/0-and-1-are-not.html)). 
There isn't one A~j~ labeled "old hypothesis" and another A~j~
labeled "new hypothesis".

This symmetry is a feature, not a bug, of probability theory!  If
you are designing an artificial reasoning system that arrives at
different beliefs depending on the order in which the evidence is
presented, this is labeled "hysteresis" and considered a Bad
Thing.  I hear that it is also frowned upon in Science.

From a probability-theoretic standpoint we have various trivial
theorems that say it shouldn't matter whether you update on X first
and then Y, or update on Y first and then X.  At least they'd be
trivial if human beings didn't violate them so often and so
lightly.

If decoherence is "untestable" relative to collapse, then so too,
collapse is "untestable" relative to decoherence.  What if the
history of physics had transpired differently - what if Hugh
Everett and John Wheeler had stood in the place of Bohr and
Heisenberg, and vice versa?  Would it then be right and proper for
the people of that world to look at the collapse interpretation,
and snort, and say, "Where are the *new* predictions?"

What if someday we meet an alien species which invented decoherence
before collapse?  Are we each bound to keep the theory we invented
first?  Will Reason have nothing to say about the issue, leaving no
recourse to settle the argument but interstellar war?

> "But if we revoke the requirement to yield new predictions, we are
> left with scientific chaos.  You can add arbitrary untestable
> complications to old theories, and get experimentally equivalent
> predictions.  If we reject what you call 'hysteresis', how can we
> defend our current theories against every crackpot who proposes
> that electrons have a new property called 'scent', just like quarks
> have 'flavor'?"

Let it first be said that I quite agree that you should reject the
one who comes to you and says:  "Hey, I've got this brilliant new
idea!  Maybe it's not the electromagnetic field that's tugging on
charged particles.  Maybe there are tiny little angels who actually
push on the particles, and the electromagnetic field just tells
them how to do it.  Look, I have all these successful experimental
predictions - the predictions you used to call your own!"

So yes, I agree that we shouldn't buy this amazing new theory, but
it is not the *newness* that is the problem.

Suppose that human history had developed only slightly differently,
with the Church being a primary grant agency for Science.  And
suppose that when the laws of electromagnetism were first being
worked out, the phenomenon of magnetism had been taken as proof of
the existence of unseen spirits, of angels.  James Clerk becomes
Saint Maxwell, who described the laws that direct the actions of
angels.

A couple of centuries later, after the Church's power to burn
people at the stake has been restrained, someone comes along and
says:  "Hey, do we really need the angels?"

"Yes," everyone says.  "How else would the mere numbers of the
electromagnetic field, translate into the actual motions of
particles?"

"It might be a fundamental law," says the newcomer, "or it might be
something other than angels, which we will discover later.  What I
am suggesting is that interpreting the numbers
*as the action of angels* doesn't really add anything, and we
should just keep the numbers and throw out the angel part."

And they look one at another, and finally say, "But your theory
doesn't make any new experimental predictions, so why should we
adopt it?  How do we test your assertions about the absence of
angels?"

From a normative perspective, it seems to me that if we should
reject the crackpot angels in the first scenario,
*even without being able to distinguish the two theories experimentally,*
then we should also reject the angels of established science in the
second scenario, even without being able to distinguish the two
theories experimentally.

It is ordinarily the crackpot who adds on new useless
complications, rather than scientists who accidentally build them
in at the start.  But the problem is not that the complications are
new, but that they are useless whether or not they are new.

A Bayesian would say that the extra complications of the angels in
the theory, lead to penalties on the prior probability of the
theory.  If two theories make equivalent predictions, we keep the
one that can be described with the shortest message, the smallest
program.  If you are evaluating the prior probability of each
hypothesis by counting bits of code, and then applying Bayesian
updating rules on all the evidence available, then it makes no
difference which hypothesis you hear about first, or the order in
which you apply the evidence.

It is usually not possible to apply formal probability theory in
real life, any more than you can predict the winner of a tennis
match using quantum field theory.  But if probability theory can
serve as a guide to practice, this is what it says:  Reject
*useless*complications *in general*, not just when they are
*new*.* *

> "Yes, and *useless* is precisely what the many worlds of
> decoherence are!  There are supposedly all these worlds alongside
> our own, and they don't *do* anything to our world, but I'm
> supposed to believe in them anyway?"

No, according to decoherence, what you're supposed to believe are
the general laws that govern wavefunctions - and these general laws
are very visible and testable.

I have argued elsewhere that
[the imprimatur of science should be associated with general laws, rather than particular events](http://www.overcomingbias.com/2007/08/scientific-evid.html),
because it is the general laws that, in principle, anyone can go
out and test for themselves.  I assure you that I happen to be
wearing white socks right now as I type this.  So you are probably
*rationally* justified in believing that this is a historical
fact.  But it is not the specially strong kind of statement that we
canonize as a provisional belief of science, because there is no
experiment that you can do for yourself to determine the truth of
it; you are stuck with my authority.  Now, if I were to tell you
the mass of an electron in general, you could go out and find your
own electron to test, and thereby see for yourself the truth of the
general law in that particular case.

The ability of anyone to go out and verify a general scientific law
for themselves, by constructing some particular case, is what makes
our belief in the general law specially reliable.

What decoherentists say they believe in, is the differential
equation that is observed to govern the evolution of wavefunctions
- which you can go out and test yourself any time you like; just
look at a hydrogen atom.

Belief in the existence of separated portions of the universal
wavefunction is not *additional,* and it is not *supposed*to be
explaining the price of gold in London; it is just a deductive
consequence of the wavefunction's evolution.  If the evidence of
many particular cases gives you cause to believe that X-\>Y is a
general law, and the evidence of some particular case gives you
cause to believe X, then you should have P(Y) ≥ P(X∧(X-\>Y)).

Or to look at it another way, if P(Y|X) ≈ 1, then P(X∧Y) ≈ P(X).

Which is to say, believing extra details doesn't cost you extra
probability when they are *logical implications* of general beliefs
you already have.  Presumably the general beliefs themselves are
falsifiable, though, or why bother?

This is why we don't believe that
[spaceships blink out of existence when they cross the cosmological horizon](http://www.overcomingbias.com/2008/04/implied-invisib.html)
relative to us.  True, the spaceship's continued existence doesn't
have an impact on our world.  The spaceship's continued existence
isn't helping to explain the price of gold in London.  But we get
the invisible spaceship for free as a consequence of general laws
that imply conservation of mass and energy.  If the spaceship's
continued existence were *not* a deductive consequence of the laws
of physics as we presently model them, *then* it would be an
additional detail, cost extra probability, and we would have to
question why our theory must include this assertion.

The part of decoherence that is supposed to be testable is not the
many worlds per se, but just the general law that governs the
wavefunction.  The decoherentists note that, applied universally,
this law implies the existence of entire superposed worlds.  Now
there are critiques that can be leveled at this theory, most
notably "But then where do the Born probabilities come from?".  But
within the internal logic of decoherence, the many worlds are not
offered as an explanation for anything, nor are they the substance
of the theory that is meant to be tested; they are simply a logical
consequence of those general laws that constitute the substance of
the theory.

If A-\>B then \~B-\>\~A.  To deny the existence of superposed
worlds, is necessarily to deny the universality of the quantum laws
formulated to govern hydrogen atoms and every other examinable
case; it is this denial that seems to the decoherentists like the
extra and untestable detail.  You can't see the other parts of the
wavefunction - why postulate *additionally* that they don't exist?

The events surrounding the decoherence controversy may be unique in
scientific history, marking the first time that serious scientists
have come forward and said that by historical accident humanity has
developed a powerful, successful, mathematical physical theory that
includes angels.  That there is an entire law, the collapse
postulate, which can simply be thrown away, leaving the theory
*strictly*simpler.

To this discussion I wish to contribute the assertion that, in the
light of a mathematically solid understanding of probability
theory, decoherence is not ruled out by Occam's Razor, nor is it
unfalsifiable, nor is it untestable.

We may consider e.g. decoherence and the collapse postulate, side
by side, and evaluate critiques such as "Doesn't decoherence
definitely predict that quantum probabilities should always be
50/50?" and "Doesn't collapse violate Special Relativity by
implying influence at a distance?"  We can consider the relative
merits of these theories on grounds of their compatibility with
experience and the apparent character of physical law.

To assert that decoherence is not even in the game - because the
many worlds themselves are "extra entities" that violate Occam's
Razor, or because the many worlds themselves are "untestable", or
because decoherence makes no "new predictions" - all this is, I
would argue, an outright error of probability theory.  The
discussion should simply discard those particular arguments and
move on.
