
# On Being Decoherent

"A human researcher only sees a particle in one place at one
time."  At least that's what everyone goes around repeating to
themselves.  Personally, I'd say that when a human researcher looks
at a quantum computer, they quite clearly see particles *not*
behaving like they're in one place at a time.  In fact, you have
*never in your life* seen a particle "in one place at a time"
because they aren'*t.*

Nonetheless, when you construct a big measuring instrument that is
sensitive to a particle's location - say, the measuring
instrument's behavior depends on whether a particle is to the left
or right of some dividing line - then you, the human researcher,
see the screen flashing "LEFT", or "RIGHT", but not a mixture like
"LIGFT".

As you might have guessed from reading about
[decoherence](/lw/pp/decoherence/) and
[Heisenberg](/lw/pq/the_socalled_heisenberg_uncertainty_principle/),
this is because we *ourselves* are governed by the laws of quantum
mechanics and subject to decoherence.

The standpoint of the
[Feynman path integral](/lw/pk/feynman_paths/) suggests viewing the
evolution of a quantum system as a sum over histories, an integral
over ways the system "could" behave - though the quantum evolution
of each history still depends on things like the second derivative
of that component of the amplitude distribution; it's not a sum
over classical histories.  And "could" does not mean *possibility*
in the logical sense; all the amplitude flows are real events...

Nonetheless, a human being can try to grasp a quantum system by
imagining all the ways that something could happen, and then adding
up all the [little arrows](/lw/pk/feynman_paths/) that flow to
[identical outcomes](/lw/pf/distinct_configurations/).  That gets
you something of the flavor of the real quantum physics, of
amplitude flows between volumes of configuration space.

Now apply this mode of visualization to a sensor measuring an atom
- say, a sensor measuring whether an atom is to the left or right
of a dividing line.

[![Superposition2](http://lesswrong.com/static/imported/2008/04/26/superposition2.png "Superposition2")](http://lesswrong.com/static/imported/2008/04/26/superposition2.png)
Which is to say:  The sensor and the atom undergo some physical
interaction in which the final state of the sensor depends heavily
on whether the atom is to the left or right of a dividing line.  (I
am reusing some [previous diagrams](/lw/pp/decoherence/), so this
is not an exact depiction; but you should be able to use your own
imagination at this point.)

[![Entanglecloud](http://lesswrong.com/static/imported/2008/04/26/entanglecloud.png "Entanglecloud")](http://lesswrong.com/static/imported/2008/04/26/entanglecloud.png)You
may recognize this as the *entangling interaction* described in
"[Decoherence](/lw/pp/decoherence/)". A quantum system that starts
out highly factorizable, looking plaid and rectangular, that is,
independent, can evolve into an entangled system as the
formerly-independent parts interact among themselves.

So you end up with an amplitude distribution that contains two
blobs of amplitude - a blob of amplitude with the atom on the left,
and the sensor saying "LEFT"; and a blob of amplitude with the atom
on the right, and the sensor saying "RIGHT".

For a sensor to *measure* an atom is to *become entangled* with it
- for the state of the sensor to depend on the state of the atom -
for the two to become correlated.  In a classical system, this is
true only on a probabilistic level.  In quantum physics it is a
physically real state of affairs.

To *observe* a thing is to *entangle yourself* with it. You may
recall my having previously said things that sound a good deal like
this, in describing how
[cognition obeys the laws of thermodynamics](/lw/o5/the_second_law_of_thermodynamics_and_engines_of/),
and, much earlier, talking about how
[rationality is a phenomenon within causality](/lw/jl/what_is_evidence/). 
It is possible to appreciate this in a purely philosophical sense,
but quantum physics helps drive the point home.

[![Ampl1](http://lesswrong.com/static/imported/2008/04/26/ampl1.png "Ampl1")](http://lesswrong.com/static/imported/2008/04/26/ampl1.png)
Let's say you've got an Atom, whose position has amplitude bulges
on the left and on the right.  We can regard the Atom's
distribution as a *sum* (addition, not multiplication) of the left
bulge and the right bulge:

> Atom = (Atom-LEFT + Atom-RIGHT)

Also there's a Sensor in a ready-to-sense state, which we'll call
BLANK:

> Sensor = Sensor-BLANK

By hypothesis, the system starts out in a state of quantum
independence - the Sensor hasn't interacted with the Atom yet. 
So:

> System = (Sensor-BLANK) \* (Atom-LEFT + Atom-RIGHT)

Sensor-BLANK is an amplitude sub-distribution, or sub-factor, over
the [joint positions](/lw/pe/joint_configurations/) of all the
particles in the sensor.  Then you multiply this distribution by
the distribution (Atom-LEFT + Atom-RIGHT), which is the sub-factor
for the Atom's position.  Which gets you the *joint* configuration
space over *all* the particles in the system, the Sensor *and* the
Atom.

Quantum evolution is linear, which means that Evolution(A + B) =
Evolution(A) + Evolution(B).  We can understand the behavior of
this whole distribution by understanding its parts.  Not its
multiplicative factors, but its additive components.  So now we use
the distributive rule of arithmetic, which, because we're just
adding and multiplying complex numbers, works just as usual:

> System = (Sensor-BLANK) \* (Atom-LEFT + Atom-RIGHT)  
>            = (Sensor-BLANK \* Atom-LEFT) + (Sensor-BLANK \*
> Atom-RIGHT)

Now, the volume of configuration space corresponding to
(Sensor-BLANK \* Atom-LEFT) evolves into (Sensor-LEFT \*
Atom-LEFT).

Which is to say:  Particle positions for the sensor being in its
initialized state *and* the Atom being on the left, end up sending
their amplitude flows to final configurations in which the Sensor
is in a LEFT state, and the Atom is still on the left.

So we have the evolution:

> (Sensor-BLANK \* Atom-LEFT) + (Sensor-BLANK \* Atom-RIGHT)  
>         =\>  
> (Sensor-LEFT \* Atom-LEFT) + (Sensor-RIGHT \* Atom-RIGHT)

By hypothesis, Sensor-LEFT is a different state from Sensor-RIGHT -
otherwise it wouldn't be a very sensitive Sensor.  So the final
state doesn't factorize any further; it's entangled.

But this entanglement is not likely to manifest in difficulties of
calculation.  Suppose the Sensor has a little LCD screen that's
flashing "LEFT" or "RIGHT". This may seem like a relatively small
difference to a human, but it involves avogadros of particles -
photons, electrons, entire molecules - occupying different
positions.

So, since the states Sensor-LEFT and Sensor-RIGHT are widely
separated in the configuration space, the volumes (Sensor-LEFT \*
Atom-LEFT) and (Sensor-RIGHT \* Atom-RIGHT) are even more widely
separated.

The LEFT blob and the RIGHT blob in the amplitude distribution can
be considered separately; they won't interact.  There are no
plausible Feynman paths that end up with both LEFT and RIGHT
sending amplitude to the *same joint configuration.*  There would
have to be a Feynman path from LEFT, and a Feynman path from RIGHT,
in which *all* the quadrillions of differentiated particles ended
up in the *same places*.  So the amplitude flows from LEFT and
RIGHT don't intersect, and don't interfere.

[![Precohered](http://lesswrong.com/static/imported/2008/04/25/precohered.png "Precohered")](http://lesswrong.com/static/imported/2008/04/25/precohered.png)You
may recall this principle from
"[Decoherence](/lw/pp/decoherence/)", for how a sensitive
interaction can decohere two interacting blobs of amplitude, into
two noninteracting
blobs.[![Decohered](http://lesswrong.com/static/imported/2008/04/25/decohered.png "Decohered")](http://lesswrong.com/static/imported/2008/04/25/decohered.png)

Formerly, the Atom-LEFT and Atom-RIGHT states were close enough in
configuration space, that the blobs could interact with each other
- there would be Feynman paths where an atom on the left ended up
on the right.  Or Feynman paths for both an atom on the left, and
an atom on the right, to end up in the middle.

Now, however, the two blobs are decohered.  For LEFT to interact
with RIGHT, it's not enough for just the *Atom* to end up on the
right.  The *Sensor* would have to spontaneously leap into a state
where it was flashing "RIGHT" on screen.  Likewise with any
particles in the environment which previously happened to be hit by
photons for the screen flashing "LEFT".  Trying to reverse
decoherence is like trying to unscramble an egg.

And when a *human being* looks at the Sensor's little display
screen... or even just stands nearby, with quintillions of
particles slightly influenced by gravity... then, under
*exactly the same laws,* the system evolves into:

> (Human-LEFT \* Sensor-LEFT \* Atom-LEFT) + (Human-RIGHT \*
> Sensor-RIGHT \* Atom-RIGHT)

Thus, any *particular version* of yourself only sees the sensor
registering one result.

That's it - the big secret of quantum mechanics.  As physical
secrets go, it's actually pretty damn big.  Discovering that the
Earth was not the center of the universe, doesn't hold a candle to
realizing that you're twins.

That *you, yourself,* are made of particles, is the fourth and
final key to recovering the classical hallucination.  It's why you
only ever see the universe from *within* one blob of amplitude, and
not the vastly entangled whole.

Asking why you can't see Schrodinger's Cat as simultaneously dead
and alive, is like an
[Ebborian](/lw/ps/where_physics_meets_experience/) asking:  "But if
my brain really splits down the middle, why do I only ever remember
finding myself on either the left *or* the right?  Why don't I find
myself on both sides?"

Because you're not outside and above the universe, looking down. 
You're *in* the universe.

Your eyes are not an empty window onto the soul, through which the
true state of the universe leaks in to your mind.  What you *see,*
you see because your brain represents it: because your brain
becomes entangled with it: because your eyes and brain are part of
a continuous physics with the rest of reality.

You only see nearby objects, not objects light-years away, because
photons from those objects can't reach you, therefore you can't see
them.  By a similar locality principle, you don't interact with
distant configurations.

When you open your eyes and
[see your shoelace is untied](/lw/jl/what_is_evidence/), that event
happens within your brain.  A brain is made up of interacting
neurons.  If you had two separate groups of neurons that never
interacted with each other, but did interact among themselves, they
would not be a single computer.  If one group of neurons thought
"My shoelace is untied", and the other group of neurons thought "My
shoelace is tied", it's difficult to see how these two brains could
possibly contain the same consciousness.

And if you think all this sounds
[obvious](/lw/im/hindsight_devalues_science/), note that,
historically speaking, it took more than two decades after the
invention of quantum mechanics for a physicist to publish that
little suggestion.  People *really aren't used* to thinking of
themselves as particles.

The [Ebborians](/lw/ps/where_physics_meets_experience/) have it a
bit easier, when they split.  They can see the other sides of
themselves, and talk to them.

But the only way for two widely separated blobs of amplitude to
communicate - to have causal dependencies on each other - would be
if there were at least some [Feynman paths](/lw/pk/feynman_paths/)
leading to
[identical configurations](/lw/pf/distinct_configurations/) from
both starting blobs.

Once one entire human brain thinks "Left!", and another entire
human brain thinks "Right!", then it's *extremely unlikely* for all
of the particles in those brains, and all of the particles in the
sensors, and all of the nearby particles that interacted, to
coincidentally end up in approximately the same configuration
again.

It's around the same likelihood as your brain spontaneously erasing
its memories of seeing the sensor and going back to its exact
original state; while nearby, an egg unscrambles itself and a
hamburger turns back into a cow.

So the decohered amplitude-blobs don't interact.  And we never get
to talk to our other selves, nor can they speak to us.

Of course, this doesn't mean that the other
amplitude-blobs* **aren't there any more,* any more than we should
think that
[a spaceship suddenly ceases to exist](/lw/pb/belief_in_the_implied_invisible/)
when it travels over the cosmological horizon (relative to us) of
an expanding universe.

> (Oh, you thought that post on
> [belief in the implied invisible](/lw/pb/belief_in_the_implied_invisible/)was
> part of the Zombie sequence?  No, that was covert preparation for
> the coming series on quantum mechanics.
> 
> You can go through line by line and substitute the arguments, in
> fact.
> 
> Remember that the next time some commenter snorts and says, "But
> what do all these posts have to do with your Artificial
> Intelligence work?")

Disturbed by the prospect of there being more than one version of
you?  But as
[Max Tegmark points out](http://arxiv.org/abs/astro-ph/0302131),
living in a spatially infinite universe *already* implies that an
exact duplicate of you exists somewhere, with probability 1.  In
all likelihood, that duplicate is no more than 10\^(10^29^)
lightyears away.  Or 10\^(10^29^) meters away, with numbers of that
magnitude it's pretty much the same thing.

> (Stop the presses!  Shocking news!  Scientists have announced that
> *you* are actually the duplicate of yourself 10\^(10^29^)
> lightyears away!  What you *thought* was "you" is really just a
> duplicate of you.)

You also get the same Big World effect from the inflationary
scenario in the Big Bang, which buds off multiple universes.  And
both spatial infinity and inflation are more or less standard in
the current model of physics.  So living in a Big World, which
contains more than one person who resembles you, is a bullet you've
pretty much got to bite - though none of the guns are certain,
physics is firing that bullet at you from at least three different
directions.

Maybe later I'll do a post about why you shouldn't panic about the
Big World.  You shouldn't be drawing many epistemic implications
from it, let alone moral implications.  As Greg Egan put it, "It
all adds up to normality."  Indeed, I sometimes think of this as
Egan's Law.
