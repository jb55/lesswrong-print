
# Joint Configurations

The key to understanding configurations, and hence the key to
understanding quantum mechanics, is realizing on a truly gut level
that configurations are about more than one particle.

[![Fig4\_2](http://lesswrong.com/static/imported/2008/04/10/fig4_2.gif "Fig4_2")](http://lesswrong.com/static/imported/2008/04/10/fig4_2.gif)
Continuing from [yesterday](/lw/pd/configurations_and_amplitude/),
here's an altered version of the experiment where we send in *two*
photons toward **D** at the same time, from the sources **B** and
**C**.

The starting configuration then is:

"A photon going from **B** to **D**, and a photon going from **C**
to **D**."

Again, let's say the starting configuration has amplitude (-1 +
0*i*).

And remember, the rule of the half-silvered mirror (at **D**) is
that a right-angle deflection multiplies by *i*, and a straight
line multiplies by 1.

So the amplitude flows from the starting configuration, separately
considering the four cases of deflection/non-deflection of each
photon, are:

1.  The "**B** to **D**" photon is deflected and the "**C** to
    **D**" photon is deflected.  This amplitude flows to the
    configuration "A photon going from **D** to **E**, and a photon
    going from **D** to **F**".  The amplitude flowing is (-1 + 0*i*)
    \* *i* \* *i* = (1 + 0*i*).
2.  The  "**B** to **D**" photon is deflected and the  "**C** to
    **D**" photon goes straight.  This amplitude flows to the
    configuration "Two photons going from **D** to **E**".  The
    amplitude flowing is (-1 + 0*i*) \* *i* \* 1 = (0 + -*i*).
3.  The  "**B** to **D**" photon goes straight and the  "**C** to
    **D**" photon is deflected.  This amplitude flows to the
    configuration "Two photons going from **D** to **F**".  The
    amplitude flowing is (-1 + 0*i*) \* 1 \* *i* = (0 + -*i*).
4.  The "**B** to **D**" photon goes straight and the "**C** to
    **D**" photon goes straight.  This amplitude flows to the
    configuration "A photon going from **D** to **F**, and a photon
    going from **D** to **E**".  The amplitude flowing is (-1 + 0*i*)
    \* 1 \* 1 = (-1 + 0*i*).

Now - and this is a
*very important and fundamental idea in quantum mechanics* - the
amplitudes in cases 1 and 4 are flowing to the *same*
configuration.  Whether the **B** photon and **C** photon both go
straight, or both are deflected, the resulting configuration is
*one photon going toward **E** and another photon going toward **F***.

So we add up the two incoming amplitude flows from case 1 and case
4, and get a total amplitude of (1 + 0*i*) + (-1 + 0*i*) = 0.

When we wave our magic squared-modulus-ratio reader over the three
final configurations, we'll find that "Two photons at Detector 1"
and "Two photons at Detector 2" have the same squared modulus, but
"A photon at Detector 1 and a photon at detector 2" has squared
modulus zero.

Way up at the level of experiment, we never find Detector 1 and
Detector 2 both going off.  We'll find Detector 1 going off twice,
or Detector 2 going off twice, with equal frequency.

(Assuming I've gotten the math and physics right.  I didn't
actually perform the experiment.  If I got this wrong, I'm sure 50
commenters will tell me so in very short order.)

The configuration's identity is *not,* "The **B** photon going
toward **E** and the **C** photon going toward **F**."  Then the
resultant configurations in case 1 and case 4 would not be equal. 
Case 1 would be, "**B** photon to **E**, **C** photon to **F**" and
case 4 would be "**B** photon to **F**, **C** photon to **E**". 
These would be two distinguishable configurations, *if*
configurations had photon-tracking structure.

So we would not add up the two amplitudes and cancel them out.  We
would keep the amplitudes in two separate configurations.  The
total amplitudes would have non-zero squared moduli.  And when we
ran the experiment, we would find (around half the time) that
Detector 1 and Detector 2 each registered one photon.  Which
doesn't happen, if my calculations are correct.

Configurations don't keep track of where particles come from.  A
configuration's identity is just, "A photon here, a photon there;
an electron here, an electron there."  No matter how you get into
that situation, so long as there are the same species of particles
in the same places, it counts as the same configuration.

I say again that the question "What kind of information does the
configuration's structure incorporate?" has
*experimental consequences.*  You can deduce, from experiment, the
way that reality itself must be treating configurations.

In a classical universe, there would be no experimental
consequences.  If the photon were like a little billiard ball that
either went one way or the other, and the configurations were our
beliefs about possible states the system could be in, and instead
of amplitudes we had probabilities, it would not make a difference
whether we tracked the origin of photons or threw the information
away.

In a classical universe, I could assign a 25% probability to both
photons going to **E**, a 25% probability of both photons going to
**F**, a 25% probability of the **B** photon going to **E** and the
**C** photon going to **F**, and 25% probability of the **B**
photon going to **F** and the **C** photon going to **E**.  Or,
since I *personally* don't care which of the two latter cases
occurred, I could decide to collapse the two possibilities into one
possibility and add up their probabilities, and just say, "A 50%
probability that each detector gets one photon."

With probabilities, we can aggregate events as we like - draw our
boundaries around sets of possible worlds as we please - and the
numbers will still work out the same.

But you can't arbitrarily collapse configurations together, or
split them apart, in your model, and get the same experimental
predictions.  Our magical tool tells us the ratios of squared
moduli.  When you add two complex numbers, the squared modulus of
the sum is not the sum of the squared moduli of the parts:

> Squared\_Modulus(C1 + C2) != Squared\_Modulus(C1) +
> Squared\_Modulus(C2)

E.g:

> S\_M((2 + *i*) + (1 + -*i*)) = S\_M(3 + 0*i*) = 3\^2 + 0\^2 = 9  
> (S\_M(2 + *i*) + S\_M(1 + -*i*)) = ((2\^2 + 1\^2) + (1\^2 +
> (-1)\^2)) = ((4 + 1) + (1 + 1)) = 7

Or in today's experiment of discourse, we had flows of (1 + 0*i*)
and (-1 + 0*i*) cancel out, adding to 0 whose squared modulus is 0,
where the squared modulus of the parts would have been 1 and 1.

Because the squared modulus of the sum does not equal the squared
modulus of the parts, the question of which configurations are the
same or distinct is experimentally distinguishable; a matter of
objective fact.  You cannot merge configurations that should be
distinct, or split configurations that should be identical, without
ending up with different results.

The *probability* of two mutually exclusive events equals the
probability of the first event plus the probability of the second
event.  This is what lets us group *possible worlds* however we
like during our calculations, without affecting our final
probabilities.

Suppose I roll two six-sided dice (all the way up at the level of
everyday life, where something like a classical level emerges). 
Then, when I calculate the probability of events like "both dice
will show odd numbers", it does not depend whether I make a table
of 36 possible outcomes for the exact numbers, or if I decide to
think about 1, 3, 5 as "odd faces" and 2, 4, 6 as "even faces" and
make a table of 4 possible outcomes. I can split up my knowledge
any way I like - throw away information that doesn't make a
difference to my current calculations, or keep the information,
depending on my whim - and my predictions will
[always come out the same](/lw/mt/beautiful_probability/).

If in place of Squared\_Modulus, our magical tool was some linear
function - any function where F(X + Y) = F(X) + F(Y) - then all the
quantumness would instantly vanish and be replaced by a classical
physics.  (A *different*classical physics, not the same illusion of
classicality we hallucinate from inside the higher levels of
organization in our own quantum world.)

If amplitudes were just probabilities, they couldn't cancel out
when flows collided.  If configurations were just states of
knowledge, you could reorganize them however you liked.

But the configurations are nailed in place, indivisible and
unmergeable without changing the laws of physics.

And part of what is nailed, is the way that configurations treat
multiple particles.  A configuration says, "A photon here, a photon
there", not "*This* photon here, *that* photon there".  "*This*
photon here, *that* photon there" does not have a different
identity from "*That* photon here, *this* photon there."

The result - we'll talk more about this in future posts, but it's
visible already in today's experiment - is that you can't factorize
the physics of our universe to be about particles with individual
identities.

Part of the reason why humans have trouble coming to grips with
*perfectly normal* quantum physics, is that humans bizarrely keep
trying to factor reality into a sum of individually real billiard
balls.

Ha ha!  Silly humans.
