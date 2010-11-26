
# Decoherence as Projection

[![Heisensplit](http://lesswrong.com/static/imported/2008/05/01/heisensplit.png "Heisensplit")](http://lesswrong.com/static/imported/2008/05/01/heisensplit.png)
In
"[The So-Called Heisenberg Uncertainty Principle](http://www.overcomingbias.com/2008/04/heisenberg.html)"
we got a look at how decoherence can affect the apparent surface
properties of objects:  By measuring whether a particle is to the
left or right of a dividing line, you can decohere the part of the
amplitude distribution on the left with the part on the right. 
Separating the amplitude distribution into two parts affects its
future evolution (within each component) because the two components
can no longer interfere with each other.

Yet there are more subtle ways to take apart amplitude
distributions than by splitting the position basis down the
middle.  And by exploring this, we rise further up the rabbit
hole.

(Remember, the classical world is Wonderland, the quantum world is
reality.  So when you get deeper into quantum physics, you are
going *up* the rabbit hole, not *down* the rabbit hole.)

Light has a certain quantum property called "polarization".  Of
course, all known physical properties are "quantum properties", but
in this case I mean that polarization neatly exhibits fundamental
quantum characteristics.  I mention this, because polarization is
often considered part of "classical" optics.  Why?  Because the
quantum nature of polarization is so simple that it was
accidentally worked out as part of classical mechanics, back when
light was thought to be a wave.

(Nobody tell the marketers, though, or we'll be wearing "quantum
sunglasses".)

I don't usually begin by discussing the astronomically high-level
phenomena of macroscopic physics, but in this case, I think it will
be helpful to begin with a human-world example...

I hand you two little sheets of semi-transparent material, looking
perhaps like dark plastic, with small arrows drawn in marker along
the sides.  When you hold up one of the sheets in front of you, the
scene through it is darker - it blocks some of the light.

[![2polaroids](http://lesswrong.com/static/imported/2008/05/01/2polaroids.png "2polaroids")](http://lesswrong.com/static/imported/2008/05/01/2polaroids.png)Now
you hold up the second sheet in front of the first sheet...

When the two arrows are aligned, pointing in the same direction,
the scene is no darker than before - that is, the two sheets in
series block the same amount of light as the first sheet alone.

But as you rotate the second sheet, so that the two arrows point in
increasingly different directions, the world seen through both
sheets grows darker.  When the arrows are at 45° angles, the world
is half as bright as when you were only holding up one sheet.

When the two arrows are perpendicular (90°) the world is completely
black.

Then, as you continue rotating the second sheet, the world gets
lighter again.  When the two arrows point in opposite directions,
again the lightness is the same as for only one sheet.

Clearly, the sheets are selectively blocking light.  Let's call the
sheets "polarized filters".

Now, you might reason something like this:  "Light is built out of
two components, an up-down component and a left-right component. 
When you hold up a single filter, with the arrow pointing up, it
blocks out the left-right component of light, and lets only the
up-down component through.  When you hold up another filter in
front of the first one, and the second filter has the arrow
pointing to the left (or the right), it only allows the left-right
component of light, and we already blocked that out, so the world
is completely dark.  And at intermediate angles, it, um, blocks
some of the light that wasn't blocked already."

So I ask, "Suppose you've already put the second filter at a 45°
angle to the first filter.  Now you put up the third filter at a
45° angle to the second filter.  What do you expect to see?"

"That's ambiguous," you say.  "Do you mean the third filter to end
up at a 0° angle to the first filter, or a 90° angle to the first
filter?"

"Good heavens," I say, "I'm surprised I forgot to specify that! 
Tell me what you expect either way."

"If the third filter is at a 0° angle to the first filter," you
say, "It won't block out anything the first filter hasn't blocked
already.  So we'll be left with the half-light world, from the
second filter being at a 45° angle to the first filter.  And if the
third filter is at a 90° angle to the first filter, it will block
out everything that the first filter didn't block, and the world
will be completely dark."

I hand you a third filter.  "Go ahead," I say, "Try it."

First you set the first filter at 0° and the second filter at 45°,
as your reference point.  Half the light gets through.

[![3polaroids](http://lesswrong.com/static/imported/2008/05/01/3polaroids.png "3polaroids")](http://lesswrong.com/static/imported/2008/05/01/3polaroids.png)Then
you set the first filter at 0°, the second filter at 45°, and the
third filter at 0°.  Now one quarter of the light gets through.

"Huh?" you say.

"Keep going," I reply.

With the first filter at 0°, the second filter at 45°, and the
third filter at 90°, one quarter of the light goes through. 
Again.

"Umm..." you say.  You quickly take out the second filter, and find
that the world goes completely dark.  Then you put in the second
filter, again at 45°, and the world resumes one-quarter
illumination.

Further investigation quickly verifies that all three filters seem
to have the same basic properties - it doesn't matter what order
you put them in.

"All right," you say, "that just seems weird."  You pause.  "So
it's probably something quantum."

Indeed it is.

Though light may seem "dim" or "bright" at the macroscopic level,
you can't split it up indefinitely; you can always send a single
photon into the series of filters, and ask what happens to that
single photon.

As you might suspect, if you send a single photon through the
succession of three filters, you will find that - assuming the
photon passes the first filter (at 0°) - the photon is observed to
pass the second filter (at 45°) with 50% probability, and, if the
photon does pass the second filter, then it seems to pass the third
filter (at 90°) with 50% probability.

The appearance of "probability" in deterministic amplitude
evolutions, as we now know, is due to
[decoherence](http://www.overcomingbias.com/2008/04/on-being-decohe.html). 
Each time a photon was blocked, some other you saw it go through. 
Each time a photon went through, some other you saw it blocked.

But what exactly is getting decohered?  And why does an intervening
second filter at 45°, let some photons pass that would otherwise be
blocked by the 0° filter plus the 90° filter?

First:  We can represent the polarization of light as a complex
amplitude for up-down plus a complex amplitude for left-right.  So
polarizations might be written as (1 ; 0) or (0 ; -i) or (√.5 ;
√.5), with the units (up-down ; left-right).  It is more customary
to write these as column vectors, but row vectors are easier to
type.

(Note that I say that this is a way to "represent" the polarization
of light.  There's nothing magical about picking up-down vs.
left-right, instead of upright-downleft vs. upleft-downright.  The
vectors above are written in an arbitrary but convenient basis. 
This will become clearer.)

Let's say that the first filter has its little arrow pointing
right.  This *doesn't* mean that the filter blocks any photon whose
polarization is not *exactly* (0 ; 1) or a multiple thereof.  But
it nonetheless happens that all the photons which we see leave the
first filter, will have a polarization of (0 ; 1) or some
irrelevantly complex multiple thereof.  Let's just take this for
granted, for the moment.  Past the first filter at 0°, we're
looking at a stream of photons purely polarized in the left-right
direction.

Now the photons hit a second filter.  Let's say the second filter
is at a 30° angle to the first - so the arrow written on the second
filter is pointing 30° above the horizontal.

Then each photon has a 25% probability of being blocked at the
second filter, and a 75% probability of going through.

How about if the second filter points to 20° above the horizontal? 
12% probability of blockage, 88% probability of going through.

45°, 50/50.

The general rule is that the probability of being blocked is the
squared sine of the angle, and the probability of going through is
the squared cosine of the angle.

Why?

First, remember two rules we've picked up about quantum mechanics: 
The evolution of quantum systems is
[linear](http://www.overcomingbias.com/2008/04/heisenberg.html) and
[unitary](http://www.overcomingbias.com/2008/04/the-born-prob-1.html). 
When an amplitude distribution breaks into parts that then evolve
separately, the components must (1) add to the original
distribution and (2) have squared moduli adding to the squared
modulus of the original distribution.

So now let's consider the photons leaving the first filter, with
"polarizations", quantum states, of (0 ; 1).

To understand what happens when the second filter is set at a 45°
angle, we observe... and think of this as a purely abstract
statement about 2-vectors... that:

> (0 ; 1) = (.5 ; .5) + (-.5 ; .5)

[![Polardecomp](http://lesswrong.com/static/imported/2008/05/01/polardecomp.png "Polardecomp")](http://lesswrong.com/static/imported/2008/05/01/polardecomp.png)Okay,
so the two vectors on the right-hand-side sum to (0 ; 1) on the
left-hand-side.

But what about the squared modulus? Just because two vectors sum to
a third, doesn't mean that the squares of the first two vectors'
lengths sum to the square of the third vector's length.

The *squared* length of the vector (.5 ; .5) is (.5)^2^ + (.5)^2^ =
.25 + .25 = 0.5.  And likewise the squared length of the vector
(-.5 ; .5) is (-.5)^2^ + (.5)^2^ = 0.5.  The sum of the squares is
0.5 + 0.5 = 1.  Which matches the squared length of the vector (0 ;
1).

[![Polarpythagorean](http://lesswrong.com/static/imported/2008/05/01/polarpythagorean.png "Polarpythagorean")](http://lesswrong.com/static/imported/2008/05/01/polarpythagorean.png)
So when you decompose (0 ; 1) into (.5 ; .5) + (-.5 ; .5), this
obeys both linearity and unitarity:  The two parts sum to the
original, and the squared modulus of the parts sums to the squared
modulus of the original.

When you interpose the second filter at an angle of 45° from the
first, it decoheres the incoming amplitude of (0 ; 1) into an
amplitude of (.5 ; .5) for being transmitted and an amplitude of
(-.5 ; .5) for being blocked.  Taking the squared modulus of the
amplitudes gives us the observed Born probabilities, i.e.
fifty-fifty.

[![Polar3060](http://lesswrong.com/static/imported/2008/05/01/polar3060.png "Polar3060")](http://lesswrong.com/static/imported/2008/05/01/polar3060.png)
What if you interposed the second filter at an angle of 30° from
the first?  Then that would decohere the incoming amplitude vector
of (0 ; 1) into the vectors (.433 ; .75) and (-.433, .25).  The
squared modulus of the first vector is .75, and the squared modulus
of the second vector is .25, again summing to one.

A polarized filter *projects* the incoming amplitude vector into
the two sides of a right triangle that sums to the original vector,
and *decoheres* the two components.  And so, under Born's rule, the
transmission and absorption probabilities are given by the
Pythagorean Theorem.

(!)

[![3polaroids\_2](http://lesswrong.com/static/imported/2008/05/01/3polaroids_2.png "3polaroids_2")](http://lesswrong.com/static/imported/2008/05/01/3polaroids_2.png)
A filter set at 0° followed by a filter set at 90° will block all
light - any photon that emerges from the first filter will have an
amplitude vector of (0 ; 1), and the component in the direction of
(1 ; 0) will be 0.  But suppose that instead you put an
intermediate filter at 45°.  This will decohere the vector of (0 ;
1) into a transmission vector of (.5 ; .5) and an absorption
amplitude of (-.5 ; .5).

A photon that *is* transmitted through the 45° filter will have a
polarization amplitude vector of (.5 ; .5).  (The (-.5 ; .5)
component is decohered into another world where you see the photon
absorbed.)

This photon then hits the 90° filter, whose transmission amplitude
is the component in the direction of (1 ; 0), and whose absorption
amplitude is the component in the direction of (0 ; 1).  (.5 ; .5)
has a component of (.5 ; 0) in the direction of (1 ; 0) and a
component of (0 ; .5) in the direction of (0 ; 1).  So it has an
amplitude of (.5 ; 0) to make it through both filters, which
translates to a Born probability of .25.

Likewise if the second filter is at -45°.  Then it decoheres the
incoming (0 ; 1) into a transmission amplitude of (-.5 ; .5) and an
absorption amplitude of (.5 ; .5).  When (-.5 ; .5) hits the third
filter at 90°, it has a component of (-.5 ; 0) in the direction of
(1 ; 0), and because these are complex numbers we're talking about,
(-.5 ; 0) has a squared modulus of 0.25, that is, 25% probability
to go through both filters.

It may seem surprising that putting in an extra filter causes more
photons to go through, even when you send them one at a time; but
that's quantum physics for you.

"But wait," you say, "Who needs the second filter?  Why not just
use math?  The initial amplitude of (0 ; 1) breaks into an
amplitude of (-.5 ; .5) + (.5 ; .5) whether or not you have the
second filter there.  By linearity, the evolution of the parts
should equal the evolution of the whole."

Yes, indeed!  So, with no second filter - just the 0° filter and
the 90° filter - here's how we'd do that analysis:

First, the 0° filter decoheres off all amplitude of any incoming
photons except the component in the direction of (0 ; 1).  Now we
look at the photon - which has some amplitude (0 ; x) that we've
implicitly been renormalizing to (0 ; 1) - and, in a purely
mathematical sense, break it up into (.5x ; .5x) and (-.5x ; .5x)
whose squared moduli will sum to x^2^.

Now first we consider the (.5x ; .5x) component; it strikes the 90°
filter which transmits the component (.5x ; 0) and absorbs the (0 ;
.5x) component.

Next we consider the (-.5x ; .5x) component.  It also strikes the
90° filter, which transmits the component (-.5x ; 0) and absorbs
the component (0 ; .5x).

[![Polarbreakdown](http://lesswrong.com/static/imported/2008/05/01/polarbreakdown.png "Polarbreakdown")](http://lesswrong.com/static/imported/2008/05/01/polarbreakdown.png)
Since no other particles are entangled, we have some
[identical configurations](http://www.overcomingbias.com/2008/04/distinct-config.html)
here:  Namely, the two configurations where the photon is
transmitted, and the two configurations where the photon is
absorbed.

Summing the amplitude vectors of (.5x ; 0) and (-.5x ; 0) for
transmission, we get a total amplitude vector of (0 ; 0).

Summing the amplitude vectors of (0 ; .5x) and (0 ; .5x) for
absorption, we get an absorption amplitude of (0 ; x).

So all photons that make it through the first filter are blocked.

Remember
[Experiment 2](http://www.overcomingbias.com/2008/04/configurations.html)
from way back when?  *Opening up a new path* to a detector can
cause *fewer* photons to be detected, because the new path has an
amplitude of opposite sign to some existing path, and they cancel
out.

In an exactly analogous manner, having a filter that sometimes
absorbs photons, can cause more (individual) photons to get through
a series of filters.  Think of it as decohering off a component of
the amplitude that would otherwise destructively interfere with
another component.

> A word about choice of basis:

You could just as easily create a new basis in which (1 ; 0) =
(.707 ; .707) and (0 ; 1) = (.707 ; -.707).  This is the
upright-downleft and upleft-downright basis of which I spoke
before.  .707 = √.5, so the basis vectors individually have length
1; and the dot product of the two vectors is 0, so they are
orthogonal.  That is, they are "orthonormal".

The new basis is just as valid as a compass marked NW, NE, SE, SW
instead of N, E, S, W.  There isn't an absolute basis of the
photon's polarization amplitude vector, any more than there's an
absolute three-coordinate system that describes your location in
space.  Ideally, you should see the photon's polarization as a
purely abstract 2-vector in complex space.

(One of my great "Ahas!" while reading the Feynman Lectures was the
realization that, rather than a 3-vector being made out of an
ordered list of 3 scalars, a 3-vector was just a pure mathematical
object in a vector algebra.  If you wanted to take the 3-vector
apart for some reason, you could generate an arbitrary orthonormal
basis and get 3 scalars that way.  In other words, you didn't build
the vector space by composing scalars - you built the decomposition
from within the vector space.  I don't know if that makes any sense
to my readers out there, but it was the great turning point in my
relationship with linear algebra.)

Oh, yes, and what happens if you have a complex polarization in the
up-down/left-right basis, like (.707*i* ; .707)?  Then that
corresponds to "circular polarization" or "elliptical
polarization".  All the polarizations I've been talking about are
"linear polarizations", where the amplitudes in the
up-down/left-right basis happen to be real numbers.

When things decohere, they decohere into pieces that add up to the
original (linearity) and whose squared moduli add up to the
original squared modulus (unitarity).  If the squared moduli of the
pieces add up to the original squared modulus, this implies the
pieces are *orthogonal* - that the components have
[inner products](http://plato.stanford.edu/entries/qm/#VecVecSpa)
of zero with each other.  That is why the title of this blog post
is "Decoherence as Projection".

> A word about how *not* to see this whole business of polarization:

Some ancient textbooks will say that when you send a photon through
a 0° filter, and it goes through, you've learned that the photon is
polarized left-right rather than up-down.  Now you measure it with
another filter at a 45° angle, and it goes through, so you've
learned that the photon is polarized upright-downleft rather than
upleft-downright.  And (says the textbook) this second measurement
"destroys" the first, so that if you want to know the up-down /
left-right polarization, you'll have to measure it all over again.

*Because you can't know both at the same time.*

And some of your more strident ancient textbooks will say something
along the lines of: the up-down / left-right polarization
*no longer exists* after the photon goes through the 45° filter. 
It's not just unknown, it *doesn't exist*, and -* *

(you might think that wasn't too far from the truth)

- *it is meaningless to even talk about it.*

Okay.  That's going a bit too far.

There are ways to use a polarizer to split a beam into two
components, rather than absorbing a component and transmitting a
component.

Suppose you first send the photons through a 0° filter.  Then you
send them through a 45° splitter.  Then you *recombine the beams*. 
Then you send the photons through a 0° filter again.  All the
photons that made it past the first filter, will make it past the
third filter as well.  Because, of course, you've put the
components back together again, and (.5 ; .5) + (-.5 ; .5) = (0 ;
1).

This doesn't seem to square with the idea that measuring the 45°
polarization *automatically destroys* the up-down/left-right
polarization, that it *isn't even meaningful* to talk about it.

Of course the one will say, "Ah, but now you no longer *know*which
path the photon took past the splitter.  When you recombined the
beams, you unmeasured the photon's 45° polarization, and the
original 0° polarization popped back into existence again, and it
was always meaningful to talk about it."

O RLY?

Anyway, that's all talk about classical surface appearances, and
you've *seen* the underlying quantum reality.  A photon with
polarization of (-.707 ; .707) has a component of (.707 ; 0) in the
up-down direction and a component of (0 ; .707) in the left-right
direction.  If you happened to feed it into an apparatus that
decohered these two components - like a polarizing filter - then
you would be able to predict the decoherent evolution as a
deterministic fact about the amplitude distribution, and the Born
probabilities would (deterministically if mysteriously) come out to
50/50.

Now someone comes along and says that the result of this
measurement you may or may not perform, *doesn't exist* or, better
yet, *isn't meaningful*.

It's hard to see what this startling statement could *mean*, let
alone how it could improve your experimental predictions.  How
would you
[falsify](http://www.overcomingbias.com/2007/07/bayesian-judo.html)
it?
