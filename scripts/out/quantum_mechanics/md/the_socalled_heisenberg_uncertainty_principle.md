
# The So-Called Heisenberg Uncertainty Principle

As touched upon [earlier](/lw/pj/the_quantum_arena/), Heisenberg's
"Uncertainty Principle" is horribly misnamed.

Amplitude distributions in configuration space evolve over time. 
When you specify an amplitude distribution over joint positions,
you are also necessarily specifying how the distribution will
evolve.  If there are blobs of position, you know where the blobs
are going.

In classical physics, where a particle is, is a separate fact from
how fast it is going.  In quantum physics this is not true.  If you
*perfectly* know the amplitude distribution on position, you
*necessarily know* the evolution of any blobs of position over
time.

So there is a theorem which *should* have been called the
Heisenberg Certainty Principle, or the Heisenberg Necessary
Determination Principle; but what does this theorem actually say?

[![Ampl1](http://lesswrong.com/static/imported/2008/04/22/ampl1.png "Ampl1")](http://lesswrong.com/static/imported/2008/04/22/ampl1.png)

At left is an image I previously used to illustrate a possible
amplitude distribution over positions of a 1-dimensional particle.

[![Helix](http://lesswrong.com/static/imported/2008/04/22/helix.png "Helix")](http://lesswrong.com/static/imported/2008/04/22/helix.png)Suppose
that, instead, the amplitude distribution is actually a
*perfect helix**.*  (I.e., the amplitude at each point has a
constant modulus, but the complex phase changes linearly with the
position.)  And neglect the effect of potential energy on the
system evolution; i.e., this is a particle out in intergalactic
space, so it's not near any gravity wells or charged particles.

If you started with an amplitude distribution that looked like a
perfect spiral helix, the laws of quantum evolution would make the
helix seem to rotate / move forward at a constant rate.  Like a
corkscrew turning at a constant rate.

This is what a physicist views as *a single particular momentum*.

And you'll note that a "single particular momentum" corresponds to
an amplitude distribution that is *fully spread out* - there's no
bulges in any particular position.

Let me emphasize that I have *not* just described a
[real situation you could find a particle in](http://dresdencodak.com/cartoons/dc_014.htm).

The physicist's notion of "a single particular momentum" is a
*mathematical tool* for analyzing quantum amplitude distributions.

The evolution of the amplitude distribution involves things like
taking the second derivative in space and multiplying by *i* to get
(one component of) the first derivative in time.  Which turns out
to give rise to a [wave](/lw/iq/guessing_the_teachers_password/)
mechanics - blobs that can propagate themselves across space, over
time.

One of the basic tools in wave mechanics is taking apart
complicated waves into a sum of simpler waves.

If you've got a wave that bulges in particular places, and thus
changes in pitch and diameter, then you can take apart that ugly
wave into a *sum* of prettier waves.

A sum of simpler waves whose individual behavior is easy to
calculate; and then you just add those behaviors back together
again.

A sum of nice neat waves, like, say, those perfect spiral helices
corresponding to precise
momenta.[![Posmomdual\_2](http://lesswrong.com/static/imported/2008/04/22/posmomdual_2.png "Posmomdual_2")](http://lesswrong.com/static/imported/2008/04/22/posmomdual_2.png)

A physicist can, for mathematical convenience, decompose a position
distribution into an integral over (infinitely many) helices of
different pitches, phases, and diameters.

Which integral looks like assigning a complex number to each
possible pitch of the helix.  And each pitch of the helix
corresponds to a different momentum.  So you get a complex
distribution over momentum-space.

It happens to be a fact that, when the position distribution is
more concentrated - when the position distribution bulges more
sharply - the integral over momentum-helices gets more widely
distributed.

Which has the physical consequence, that anything which is very
sharply in one place, tends to soon spread itself out.  Narrow
bulges don't last.

Alternatively, you might find it convenient to think, "Hm, a narrow
bulge has sharp changes in its second derivative, and I know the
evolution of the amplitude distribution depends on the second
derivative, so I can sorta imagine how a narrow bulge might tend to
propagate off in all directions."

Technically speaking, the distribution over momenta is the Fourier
transform of the distribution over positions.  And it so happens
that, to go *back* from momenta to positions, you just do another
Fourier transform.  So there's a precisely symmetrical argument
which says that anything moving at a very definite speed, has to
occupy a very spread-out place.  Which goes back to what was shown
before, about a perfect helix having a "definite momentum"
(corkscrewing at a constant speed) but being equally distributed
over all positions.

That's Heisenberg's Necessary Relation Between Position
Distribution And Position Evolution Which Prevents The Position
Distribution And The Momentum Viewpoint From Both Being Sharply
Concentrated At The Same Time Principle in a nutshell.

So now let's talk about some of the assumptions, issues, and common
misinterpretations of Heisenberg's Misnamed Principle.

> **The effect of observation on the observed**

Here's what actually happens when you "observe a particle's
position":

[![Heisensplit](http://lesswrong.com/static/imported/2008/04/22/heisensplit.png "Heisensplit")](http://lesswrong.com/static/imported/2008/04/22/heisensplit.png)

[Decoherence](/lw/pp/decoherence/), as discussed yesterday, can
take apart a formerly coherent amplitude distribution into
noninteracting blobs.

Let's say you have a particle X with a fairly definite position and
fairly definite momentum, the starting stage shown at left above. 
And then X comes into the neighborhood of another particle S, or
set of particles S, where S is highly sensitive to X's exact
location - in particular, whether X's position is on the left or
right of the black line in the middle.  For example, S might be
poised at the top of a knife-edge, and X could tip it off to the
left or to the right.

The result is to decohere X's position distribution into two
noninteracting blobs, an X-to-the-left blob and an X-to-the-right
blob.  Well, now the position distribution *within* each blob, has
become sharper.  (Remember:  Decoherence is a process of increasing
quantum entanglement that masquerades as increasing quantum
independence.)

So the Fourier transform of the more definite position distribution
*within*each blob, corresponds to a more spread-out distribution
over momentum-helices.

Running the particle X past a sensitive system S, has decohered X's
position distribution into two noninteracting blobs.  Over time,
each blob spreads itself out again, by Heisenberg's Sharper Bulges
Have Broader Fourier Transforms Principle.

[![Singleslitheisenberg](http://lesswrong.com/static/imported/2008/04/22/singleslitheisenberg.png "Singleslitheisenberg")](http://lesswrong.com/static/imported/2008/04/22/singleslitheisenberg.png)All
this gives rise to very real, very observable effects.

In the system shown at right, there is a light source, a screen
blocking the light source, and a single slit in the screen.

Ordinarily, light seems to go in straight lines (for
[less straightforward reasons](/lw/pk/feynman_paths/)).  But in
this case, the screen blocking the light source decoheres the
photon's amplitude.  Most of the Feynman paths hit the screen.

The paths that *don't* hit the screen, are concentrated into a very
narrow range.  All positions except a very narrow range have
decohered away from the blob of possibilities for "the photon goes
through the slit", so, within this blob, the position-amplitude is
concentrated very narrowly, and the spread of momenta is vey
large.

Way up at the level of human experimenters, we see that when
photons strike the second screen, they strike over a broad range -
they don't just travel in a straight line from the light source.

[Wikipedia](http://en.wikipedia.org/wiki/Uncertainty_principle),
and at least some physics textbooks, claim that it is misleading to
ascribe Heisenberg effects to an "observer effect", that is,
perturbing interactions between the measuring apparatus and the
measured system:

> "Sometimes it is a *failure* to measure the particle that produces
> the disturbance.  For example, if a perfect photographic film
> contains a small hole, and an incident photon is *not* observed,
> then its momentum becomes uncertain by a large amount.  By not
> observing the photon, we discover that it went through the hole."

However, the most technical treatment I've actually read was by
Feynman, and Feynman seemed to be saying that, whenever measuring
the position of a particle increases the spread of its momentum,
the measuring apparatus must be delivering enough of a "kick" to
the particle to account for the change.

In other words, Feynman seemed to assert that the decoherence
perspective actually *was* dual to the observer-effect perspective
- that an interaction which produced decoherence would always be
able to physically account for any resulting perturbation of the
particle.

Not grokking the math, I'm inclined to believe the Feynman
version.  It sounds pretty, and physics has a known tendency to be
pretty.

> **The alleged effect of conscious knowledge on particles**

One thing that the Heisenberg Student Confusion Principle
DEFINITELY ABSOLUTELY POSITIVELY **DOES NOT SAY** is that KNOWING
ABOUT THE PARTICLE or CONSCIOUSLY SEEING IT will MYSTERIOUSLY MAKE
IT BEHAVE DIFFERENTLY because THE UNIVERSE CARES WHAT YOU THINK.

Decoherence works exactly the same way whether a system is
decohered by a human brain or by a rock.  Yes, physicists tend to
construct very sensitive instruments that slice apart amplitude
distributions into tiny little pieces, whereas a rock isn't that
sensitive.  That's why your camera uses photographic film instead
of mossy leaves, and why replacing your eyeballs with grapes will
not improve your vision.  But *any*sufficiently sensitive physical
system will produce decoherence, where "sensitive" means
"developing to widely different final states *depending on* the
interaction", where "widely different" means "the blobs of
amplitude don't interact".

Does this description say anything about *beliefs?*  No, just
amplitude distributions.  When you jump up to a higher level and
talk about cognition, you realize that
[forming accurate beliefs](/lw/o6/perpetual_motion_beliefs/)[requires](/lw/o6/perpetual_motion_beliefs/)[sensors](/lw/o6/perpetual_motion_beliefs/). 
But the decohering power of sensitive interactions can be analyzed
on a purely physical level.

There is a legitimate "observer effect", and it is this:  Brains
that see, and pebbles that are seen, are part of a unified physics;
they are both built out of atoms.  To gain new empirical knowledge
about a thingy, the particles in you have to interact with the
particles in the thingy.  It so happens that, in our universe, the
laws of physics are pretty symmetrical about how particle
interactions work - conservation of momentum and so on: if you pull
on something, it pulls on you.

So you can't, in fact, observe a rock without affecting it, because
to observe something is to depend on it - to let *it* affect *you*,
and shape your beliefs.  And, in our universe's laws of physics,
any interaction in which the rock affects your brain, tends to have
consequences for the rock as well.

Even if you're looking at light that left a distant star 500 years
ago, then 500 years ago, emitting the light affected the star.

That's how the observer effect works.  It works *because*
everything is particles, and all the particles obey the same
unified mathematically simple physics.

It does *not* mean the physical interactions we happen to call
"observations" have a basic, fundamental, privileged effect on
reality.

To suppose that physics contains a basic account of "observation"
is like supposing that physics contains a basic account of being
Republican.  It [projects](/lw/oi/mind_projection_fallacy/) a
complex, intricate, high-order biological cognition onto
fundamental physics. 
[It sounds like a simple theory to humans, but it's not simple.](/lw/pg/where_philosophy_meets_science/)

> **Linearity**

One of the foundational assumptions physicists used to figure out
quantum theory, is that time evolution is *linear*.  If you've got
an amplitude distribution X1 that evolves into X2, and an amplitude
distribution Y1 that evolves into Y2, then the amplitude
distribution (X1 + Y1) should evolve into (X2 + Y2).

(To "add two distributions" means that we just add the complex
amplitudes at every point.  Very simple.)

Physicists assume you can take apart an amplitude distribution into
a sum of nicely behaved individual waves, add up the time evolution
of those individual waves, and get back the actual correct future
of the total amplitude distribution.

Linearity is why we can take apart a bulging blob of
position-amplitude into perfect momentum-helices, without the whole
model degenerating into complete nonsense.

The linear evolution of amplitude distributions is a theorem in the
Standard Model of physics.  But physicists didn't just stumble over
the linearity principle; it was used to invent the hypotheses, back
when quantum physics was being figured out.

I talked earlier about taking the second derivative of position;
well, taking the derivative of a differentiable distribution is a
linear operator.  F'(x) + G'(x) = (F + G)'(x).  Likewise,
integrating the sum of two integrable distributions gets you the
sum of the integrals.  So the amplitude distribution evolving in a
way that depends on the second derivative - or the equivalent view
in terms of integrating over Feynman paths - doesn't mess with
linearity.

Any "non-linear system" you've ever heard of is linear on a quantum
level.  Only the high-level simplifications that we humans use to
model systems are nonlinear.  (In the same way, the lightspeed
limit requires physics to be local, but if you're thinking about
the Web on a very high level, it looks like any webpage can link to
any other webpage, even if they're not neighbors.)

Given that quantum physics is strictly linear, you may wonder how
the *hell* you can build *any possible physical instrument* that
detects a
[ratio of squared moduli](/lw/pd/configurations_and_amplitude/) of
amplitudes, since
[the squared modulus operator is not linear](/lw/pe/joint_configurations/):
the squared modulus of the sum is not the sum of the squared moduli
of the parts.

This is a *very good question*.

We'll get to it *shortly*.

Meanwhile, physicists, in their daily mathematical practice, assume
that quantum physics is linear.  It's one of those important little
assumptions, like CPT invariance.
