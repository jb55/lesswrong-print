
# The Born Probabilities

One
[serious mystery of decoherence](/lw/pt/where_experience_confuses_physicists/)
is where the Born probabilities come from, or even what they are
probabilities *of.*  What does the integral over the squared
modulus of the amplitude density have to do with anything?

This was discussed by analogy in
"[Where Experience Confuses Physicists](/lw/pt/where_experience_confuses_physicists/)",
and I won't repeat arguments already covered there.  I will,
however, try to convey exactly what the puzzle *is,* in the real
framework of quantum mechanics.

A professor teaching undergraduates might say:  "The probability of
finding a particle in a particular position is given by the squared
modulus of the amplitude at that position."

This is oversimplified in several ways.

First, for continuous variables like position, amplitude is a
density, not a [point mass](/lw/pw/decoherence_is_pointless/).  You
integrate over it.  The integral over a single point is zero.

(Historical note:  If "observing a particle's position" invoked a
mysterious event that squeezed the amplitude distribution down to a
delta point, or flattened it in one subspace, this would give us a
different future amplitude distribution from what decoherence would
predict.  All interpretations of QM that involve quantum systems
jumping into a point/flat state, which are both testable and have
been tested, have been falsified.  The universe does not have a
"classical mode" to jump into; it's all amplitudes, all the time.)

Second, a single observed particle doesn't *have* an amplitude
distribution.  Rather the system containing yourself, plus the
particle, plus the rest of the universe*,* may approximately
*factor*into the
[multiplicative product](/lw/pj/the_quantum_arena/) of (1) a
sub-distribution over the particle position and (2) a
sub-distribution over the rest of the universe.  Or rather, the
particular blob of amplitude that
[you happen to be in](/lw/pu/on_being_decoherent/), can factor that
way.

So what could it mean, to associate a "subjective probability" with
a component of one *factor* of a combined amplitude distribution
that happens to factorize?

Recall the physics for:

> (Human-BLANK \* Sensor-BLANK) \* (Atom-LEFT + Atom-RIGHT)  
>         =\>  
> (Human-LEFT \* Sensor-LEFT \* Atom-LEFT) + (Human-RIGHT \*
> Sensor-RIGHT \* Atom-RIGHT)

Think of the whole process as reflecting the good-old-fashioned
distributive rule of algebra.  The initial state can be decomposed
- note that this is an *identity*, not an evolution - into:

> (Human-BLANK \* Sensor-BLANK) \* (Atom-LEFT + Atom-RIGHT)  
>     =  
> (Human-BLANK \* Sensor-BLANK \* Atom-LEFT) + (Human-BLANK \*
> Sensor-BLANK \* Atom-RIGHT)

We assume that the distribution factorizes.  It follows that the
term on the left, and the term on the right, initially differ only
by a multiplicative factor of Atom-LEFT vs. Atom-RIGHT.

If you were to *immediately* take the multi-dimensional integral
over the squared modulus of the amplitude density of that whole
system,

Then the *ratio* of the all-dimensional integral of the squared
modulus over the left-side term, *to* the all-dimensional integral
over the squared modulus of the right-side term,

Would equal the *ratio* of the lower-dimensional integral over the
squared modulus of the Atom-LEFT, *to* the lower-dimensional
integral over the squared modulus of Atom-RIGHT,

For essentially the same reason that if you've got (2 \* 3) \* (5 +
7), the ratio of (2 \* 3 \* 5) to (2 \* 3 \* 7) is the same as the
ratio of 5 to 7.

Doing an integral over the squared modulus of a complex amplitude
distribution in N dimensions doesn't change that.

There's also a rule called "unitary evolution" in quantum
mechanics, which says that quantum evolution never changes the
*total* integral over the squared modulus of the amplitude
density.

So if you assume that the initial left term and the initial right
term evolve, without overlapping each other, into the final LEFT
term and the final RIGHT term, they'll have the same ratio of
integrals over etcetera as before.

What all this says is that,

If some roughly independent Atom has got a blob of amplitude on the
left of its factor, and a blob of amplitude on the right,

Then, after the Sensor senses the atom, and *you* look at the
Sensor,

The integrated squared modulus of the whole LEFT blob, and the
integrated squared modulus of the whole RIGHT blob,

Will have the same ratio,

As the ratio of the squared moduli of the original Atom-LEFT and
Atom-RIGHT components.

This is why it's important to remember that apparently individual
particles have amplitude distributions that are
*multiplicative factors* within the total *joint* distribution over
*all* the particles.

If a whole gigantic human experimenter made up of quintillions of
particles,

Interacts with one teensy little atom whose amplitude *factor* has
a big bulge on the left and a small bulge on the right,

Then the resulting amplitude distribution, in the *joint*
configuration space,

Has a big amplitude blob for "human sees atom on the left", and a
small amplitude blob of "human sees atom on the right".

And what *that* means, is that the Born probabilities seem to be
about *finding yourself in a particular blob,* not
*the particle being in a particular place.*

But what does the integral over squared moduli have to do with
anything?  On a straight reading of the data, you would always find
yourself in both blobs, every time.  How can you find yourself in
one blob with greater probability?  What are the Born
probabilities, probabilities *of*?  Here's the map - where's the
territory?

I don't know.  It's an open problem.  Try not to
[go funny in the head](/lw/pt/where_experience_confuses_physicists/)
about it.

This problem is even worse than it looks, because the
squared-modulus business is
*the only non-linear rule in all of quantum mechanics.*  Everything
else - *everything* else - obeys the
[linear](/lw/pq/the_socalled_heisenberg_uncertainty_principle/)
rule that the evolution of amplitude distribution A, plus the
evolution of the amplitude distribution B, equals the evolution of
the amplitude distribution A + B.

When you think about the weather in terms of clouds and flapping
butterflies, it may not *look* linear on that higher level.  But
the amplitude distribution for weather (plus the rest of the
universe) is linear on
[the only level that's fundamentally real](/lw/on/reductionism/).

Does this mean that the squared-modulus business *must* require
additional physics beyond the linear laws we know - that it's
*necessarily* futile to try to derive it on any higher level of
organization?

But even this doesn't follow.

Let's say I have a computer program which computes a sequence of
positive integers that encode the successive states of a sentient
being.  For example, the positive integers might describe a
Conway's-Game-of-Life universe containing sentient beings (Life is
Turing-complete) or some other cellular automaton.

Regardless, this sequence of positive integers represents the time
series of a discrete universe containing conscious entities.  Call
this sequence Sentient(n).

Now consider another computer program, which computes the negative
of the first sequence:  -Sentient(n).  If the computer running
Sentient(n) instantiates conscious entities, then so too should a
program that computes Sentient(n) and then negates the output.

Now I write a computer program that computes the sequence {0, 0,
0...} in the obvious fashion.

This sequence happens to be equal to the sequence Sentient(n) +
-Sentient(n).

So does a program that computes {0, 0, 0...} necessarily
instantiate as many conscious beings as both Sentient programs put
together?

Admittedly, this isn't an exact analogy for "two universes add
linearly and cancel out".  For that, you would have to talk about a
universe with linear physics, which excludes Conway's Life.  And
then in this linear universe, two states of the world both
containing conscious observers - world-states equal but for their
opposite sign - would have to cancel out.

It doesn't work in Conway's Life, but it works in our own
universe!  Two quantum amplitude distributions can contain
components that *cancel each other out,* and this demonstrates that
the number of conscious observers in
*the sum of two distributions*, need not equal the sum of conscious
observers *in each distribution separately.*

So it actually *is* possible that we could pawn off
*the only non-linear phenomenon in all of quantum physics* onto a
better understanding of consciousness.  The question "How many
conscious observers are contained in an evolving amplitude
distribution?" has obvious reasons to be non-linear.

(!)

Robin Hanson has made
[a suggestion along these lines](http://hanson.gmu.edu/mangledworlds.html).

(!!)

Decoherence is a physically continuous process, and the interaction
between LEFT and RIGHT blobs may never actually become *zero.*

So, Robin suggests, any blob of amplitude which gets small enough,
becomes dominated by stray flows of amplitude from many larger
worlds.

A blob which gets too small, cannot sustain coherent inner
interactions - an internally driven chain of cause and effect -
because the amplitude flows are dominated from outside.  Too-small
worlds fail to support computation and consciousness, or are ground
up into chaos, or merge into larger worlds.

Hence Robin's cheery phrase, "mangled worlds".

The cutoff point will be a function of the squared modulus, because
unitary physics preserves the squared modulus under evolution; if a
blob has a certain total squared modulus, future evolution will
preserve that integrated squared modulus so long as the blob
doesn't split further.  You can think of the squared modulus as the
amount of amplitude available to internal flows of causality, as
opposed to outside impositions.

The seductive aspect of Robin's theory is that quantum physics
wouldn't need *interpreting.*  You wouldn't have to stand off
beside the mathematical structure of the universe, and say, "Okay,
now that you're finished computing all the mere numbers, I'm
furthermore telling you that the squared modulus is the 'degree of
existence'."  Instead, when you run any program that computes the
*mere numbers,* the program *automatically* contains people who
experience the same physics we do, with the same probabilities.

A major problem with Robin's theory is that it seems to predict
things like, "We should find ourselves in a universe in which
lots of
very few decoherence events have already taken place," which
tendency does not seem especially apparent.
The main thing that would support Robin's theory would be if you
could show from first principles that mangling does happen; and
that the cutoff point is somewhere around the median amplitude
density (the point where half the total amplitude density is in
worlds above the point, and half beneath it), which is apparently
what it takes to reproduce the Born probabilities in any particular
experiment.

What's the probability that Hanson's suggestion is right?  I'd put
it under fifty percent, which I don't think Hanson would disagree
with.  It would be much lower if I knew of a single alternative
that seemed equally... [reductionist](/lw/on/reductionism/).

But *even if* Hanson is wrong about what causes the Born
probabilities, I would guess that the final answer still comes out
*equally non-mysterious*.  Which would make me
[feel very silly](/lw/iy/my_wild_and_reckless_youth/), if I'd
embraced a more
[mysterious-seeming "answer"](/lw/iu/mysterious_answers_to_mysterious_questions/)
up until then.  As a general rule, it is questions that are
mysterious, not answers.

When I began reading Hanson's paper, my initial thought was: 
*The math isn't beautiful enough to be true.*

By the time I finished processing the paper, I was thinking: 
*I don't know if this is the real answer, but the real answer has got to be at least this normal.*

This is still my position today.
