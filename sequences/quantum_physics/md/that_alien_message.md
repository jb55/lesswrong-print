
# That Alien Message

Imagine a world much like this one, in which, thanks to
gene-selection technologies, the average IQ is 140 (on our scale). 
Potential Einsteins are one-in-a-thousand, not one-in-a-million;
and they grow up in a school system suited, if not to them
personally, then at least to bright kids.  Calculus is routinely
taught in sixth grade.  Albert Einstein, himself, still lived and
still made approximately the same discoveries, but his work no
longer seems *exceptional.*  Several modern top-flight physicists
have made equivalent breakthroughs, and are still around to talk.

(No, this is not the world [Brennan](/lw/p1/initiation_ceremony/)
lives in.)

One day, the stars in the night sky begin to change.

Some grow brighter.  Some grow dimmer.  Most remain the same. 
Astronomical telescopes capture it all, moment by moment.  The
stars that change, change their luminosity one at a time,
distinctly so; the luminosity change occurs over the course of a
microsecond, but a whole second separates each change.

It is clear, from the first instant anyone realizes that more than
one star is changing, that the process seems to center around Earth
particularly. The arrival of the light from the events, at many
stars scattered around the galaxy, has been precisely timed to
Earth in its orbit.  Soon, confirmation comes in from high-orbiting
telescopes (they have those) that the astronomical miracles do
*not* seem as synchronized from outside Earth.  Only Earth's
telescopes see one star changing every second (1005 milliseconds,
actually).

Almost the entire combined brainpower of Earth turns to analysis.

It quickly becomes clear that the stars that jump in luminosity,
all jump by a factor of exactly 256; those that diminish in
luminosity, diminish by a factor of exactly 256.  There is no
apparent pattern in the stellar coordinates.  This leaves, simply,
a pattern of BRIGHT-dim-BRIGHT-BRIGHT...

"A binary message!" is everyone's first thought.

But in this world there are careful thinkers, of great prestige as
well, and they are not so sure.  "There are easier ways to send a
message," they post to their blogs, "if you can make stars flicker,
and if you want to communicate.  *Something*is happening.  It
appears, *prima facie,* to focus on Earth in particular.  To call
it a 'message' presumes a great deal more about the cause behind
it.  There might be some kind of evolutionary process among, um,
things that can make stars flicker, that ends up sensitive to
intelligence somehow...  Yeah, there's probably something like
'intelligence' behind it, but try to appreciate how wide a range of
possibilities that really implies.  We don't know this is a
message, or that it was sent from the same kind of motivations that
might move us.  I mean, *we* would just signal using a big
flashlight, we wouldn't mess up a whole galaxy."

By this time, someone has started to collate the astronomical data
and post it to the Internet.  Early suggestions that the data might
be harmful, have been... not ignored, but not obeyed, either.  If
anything this powerful wants to hurt you, you're pretty much dead
(people reason).

Multiple research groups are looking for patterns in the stellar
coordinates - or fractional arrival times of the changes, relative
to the center of the Earth - or exact durations of the luminosity
shift - or any tiny variance in the magnitude shift - or any other
fact that might be known about the stars before they changed.  But
*most*people are turning their attention to the pattern of BRIGHTS
and dims.

It becomes clear almost instantly that the pattern sent is highly
redundant.  Of the first 16 bits, 12 are BRIGHTS and 4 are dims. 
The first 32 bits received align with the second 32 bits received,
with only 7 out of 32 bits different, and then the next 32 bits
received have only 9 out of 32 bits different from the second (and
4 of them are bits that changed before).  From the first 96 bits,
then, it becomes clear that this pattern is not an optimal,
compressed encoding of anything.  The obvious thought is that the
sequence is meant to convey instructions for decoding a compressed
message to follow...

"But," say the careful thinkers, "anyone who cared about
*efficiency,* with enough power to mess with stars, could maybe
have just signaled us with a big flashlight, and sent us a DVD?"

There also seems to be structure within the 32-bit groups; some
8-bit subgroups occur with higher frequency than others, and this
structure only appears along the natural alignments (32 = 8 + 8 + 8
+ 8).

After the first five hours at one bit per second, an additional
redundancy becomes clear:  The message has started approximately
repeating itself at the 16,385th bit.

Breaking up the message into groups of 32, there are 7 bits of
difference between the 1st group and the 2nd group, and 6 bits of
difference between the 1st group and the 513th group.

"A 2D picture!" everyone thinks.  "And the four 8-bit groups are
colors; they're tetrachromats!"

But it soon becomes clear that there is a horizontal/vertical
asymmetry:  Fewer bits change, on average, between (N, N+1) versus
(N, N+512).  Which you wouldn't expect if the message was a 2D
picture projected onto a symmetrical grid.  Then you would expect
the average bitwise distance between two 32-bit groups to go as the
2-norm of the grid separation: â(h^2^ + v^2^).

There also forms a general consensus that a certain binary encoding
from 8-groups onto integers between -64 and 191 - not the binary
encoding that seems obvious to us, but still highly regular -
minimizes the average distance between neighboring cells.  This
continues to be borne out by incoming bits.

The statisticians and cryptographers and physicists and computer
scientists go to work.  There is structure here; it needs only to
be unraveled.  The masters of causality search for conditional
independence, screening-off and Markov neighborhoods, among bits
and groups of bits.  The so-called "color" appears to play a role
in neighborhoods and screening, so it's not just the equivalent of
surface reflectivity.  People search for simple equations, simple
cellular automata, simple decision trees, that can predict or
compress the message.  Physicists invent entire new theories of
physics that might describe universes projected onto the grid - for
it seems quite plausible that a message such as this is being sent
from beyond the Matrix.

After receiving 32 \* 512 \* 256 = 4,194,304 bits, around one and a
half months, the stars stop flickering.

Theoretical work continues.  Physicists and cryptographers roll up
their sleeves and *seriously* go to work.  They have cracked
problems with far less data than this.  Physicists have tested
entire theory-edifices with small differences of particle mass;
cryptographers have unraveled shorter messages deliberately
obscured.

Years pass.

Two dominant models have survived, in academia, in the scrutiny of
the public eye, and in the scrutiny of those scientists who once
did Einstein-like work.  There is a theory that the grid is a
projection from objects in a 5-dimensional space, with an asymmetry
between 3 and 2 of the spatial dimensions.  There is also a theory
that the grid is meant to encode a cellular automaton - arguably,
the grid has several fortunate properties for such.  Codes have
been devised that give interesting behaviors; but so far, running
the corresponding automata on the largest available computers, has
failed to produce any decodable result.  The run continues.

Every now and then, someone takes a group of especially brilliant
young students who've never looked at the detailed binary
sequence.  These students are then shown only the first 32 rows (of
512 columns each), to see if they can form new models, and how well
those new models do at predicting the next 224.  Both the 3+2
dimensional model, and the cellular-automaton model, have been well
duplicated by such students; they have yet to do better.  There are
complex models finely fit to the whole sequence - but those,
everyone knows, are probably worthless.

Ten years later, the stars begin flickering again. 

Within the reception of the first 128 bits, it becomes clear that
the Second Grid *can* fit to small motions in the inferred 3+2
dimensional space, but does *not* look anything like the successor
state of any of the dominant cellular automaton theories.  Much
rejoicing follows, and the physicists go to work on inducing what
kind of dynamical physics might govern the objects seen in the 3+2
dimensional space.  Much work along these lines has already been
done, just by speculating on what type of *balanced* forces might
give rise to the objects in the First Grid, if those objects were
static - but now it seems not all the objects are static.  As most
physicists guessed - statically balanced theories seemed
contrived.

Many neat equations are formulated to describe the dynamical
objects in the 3+2 dimensional space being projected onto the First
and Second Grids.  Some equations are more elegant than others;
some are more precisely predictive (in retrospect, alas) of the
Second Grid.  One group of brilliant physicists, who carefully
isolated themselves and looked only at the first 32 rows of the
Second Grid, produces equations that seem elegant to them - and the
equations also do well on predicting the next 224 rows.  This
becomes the dominant guess.

But these equations are underspecified; they don't seem to be
enough to make a universe.  A small cottage industry arises in
trying to guess what kind of laws might complete the ones thus
guessed.

When the Third Grid arrives, ten years after the Second Grid, it
provides information about second derivatives, forcing a major
modification of the "incomplete but good" theory.  But the theory
doesn't do too badly out of it, all things considered.

The Fourth Grid doesn't add much to the picture.  Third derivatives
don't seem important to the 3+2 physics inferred from the Grids.

The Fifth Grid looks almost exactly like it is expected to look.

And the Sixth Grid, and the Seventh Grid.

(Oh, and every time someone in this world tries to build a really
powerful AI, the computing hardware spontaneously melts.  This
isn't really important to the story, but I need to postulate this
in order to have human people sticking around, in the flesh, for
seventy years.)

*My moral?*

That even Einstein did not come within a million light-years of
making *efficient use of sensory data*.

Riemann invented his geometries before Einstein had a use for them;
the physics of our universe is not that complicated in an absolute
sense.  A Bayesian superintelligence, hooked up to a webcam, would
invent General Relativity as a hypothesis - perhaps not the
*dominant*hypothesis, compared to Newtonian mechanics, but still a
hypothesis under direct consideration - by the time it had seen the
third frame of a falling apple.  It might guess it from the first
frame, if it saw the statics of a bent blade of grass.

*We* would think of it.  Our civilization, that is, given ten years
to analyze each frame.  Certainly if the average IQ was 140 and
Einsteins were common, we would.

Even if we were human-level intelligences in a different sort of
physics - minds who had never seen a 3D space projected onto a 2D
grid - we would still think of the 3D-\>2D hypothesis.  Our
mathematicians would still have invented vector spaces, and
projections.

Even if we'd never seen an accelerating billiard ball, our
mathematicians would have invented calculus (e.g. for optimization
problems).

Heck, think of some of the crazy math that's been invented here on
*our* Earth.

I occasionally run into people who say something like, "There's a
theoretical limit on how much you can deduce about the outside
world, given a finite amount of sensory data."

Yes.  There is.  The theoretical limit is that every time you see 1
additional bit, it cannot be expected to eliminate more than half
of the remaining hypotheses (half the remaining probability mass,
rather).  And that a redundant message, cannot convey more
information than the compressed version of itself.  Nor can a bit
convey any information about a quantity, with which it has
correlation *exactly zero,* across the probable worlds you
imagine.

But nothing I've depicted this human civilization doing, even
*begins* to approach the theoretical limits set by the formalism of
Solomonoff induction.  It doesn't approach the picture you could
get if you could search through
*every single computable hypothesis*, weighted by their simplicity,
and do Bayesian updates on *all* of them.

To see the *theoretical*limit on extractable information, imagine
that you have infinite computing power, and you simulate all
possible universes with simple physics, looking for universes that
contain Earths embedded in them - perhaps inside a simulation -
where some process makes the stars flicker in the order observed. 
Any bit in the message - or any order of selection of stars, for
that matter - that contains the tiniest correlation (across all
possible computable universes, weighted by simplicity) to any
element of the environment, gives you information about the
environment.

Solomonoff induction, taken literally, would create countably
infinitely many sentient beings, trapped inside the computations. 
All possible computable sentient beings, in fact.  Which scarcely
seems ethical.  So let us be glad this is only a formalism.

But my point is that the "theoretical limit on how much information
you can extract from sensory data" is *far* above what I have
depicted as the triumph of a civilization of physicists and
cryptographers.

It certainly is not anything like a human looking at an apple
falling down, and thinking, "Dur, I wonder why that happened?"

People seem to make a leap from "This is 'bounded'" to "The bound
must be a reasonable-looking quantity on the scale I'm used to." 
The power output of a supernova is 'bounded', but I wouldn't advise
trying to shield yourself from one with a flame-retardant Nomex
jumpsuit.

No one - not even a Bayesian superintelligence - will ever come
remotely close to making efficient use of their sensory
information...

...is what I would like to say, but I don't trust my ability to set
limits on the abilities of Bayesian superintelligences.

(Though I'd bet money on it, if there were some way to judge the
bet.  Just not at very extreme odds.)

*The story continues:*

Millennia later, frame after frame, it has become clear that some
of the objects in the depiction are extending tentacles to move
around other objects, and carefully configuring other tentacles to
make particular signs.  They're trying to teach us to say "rock".

It seems the senders of the message have vastly underestimated our
intelligence.  From which we might guess that the aliens themselves
are not all that bright.  And these awkward children can shift the
luminosity of our stars?  That much power and that much stupidity
seems like a dangerous combination.

Our evolutionary psychologists begin extrapolating possible courses
of evolution that could produce such aliens.  A strong case is made
for them having evolved asexually, with occasional exchanges of
genetic material and brain content; this seems like the most
plausible route whereby creatures that stupid could still manage to
build a technological civilization.  Their Einsteins may be our
undergrads, but they could still collect enough scientific data to
get the job done *eventually*, in tens of their millennia perhaps.

The inferred physics of the 3+2 universe is not fully known, at
this point; but it seems sure to allow for computers far more
powerful than our quantum ones.  We are reasonably certain that our
own universe is running as a simulation on such a computer. 
Humanity decides not to probe for bugs in the simulation; we
wouldn't want to shut ourselves down accidentally.

Our evolutionary psychologists begin to guess at the aliens'
psychology, and plan out how we could persuade them to
[let us out of the box](http://yudkowsky.net/essays/aibox.html). 
It's not difficult in an absolute sense - they aren't very bright -
but we've got to be very careful...

We've got to pretend to be stupid, too; we don't want them to catch
on to their mistake.

It's not until a million years later, though, that they get around
to telling us how to signal back.

At this point, most of the human species is in cryonic suspension,
at liquid helium temperatures, beneath radiation shielding.  Every
time we try to build an AI, or a nanotechnological device, it melts
down.  So humanity waits, and sleeps.  Earth is run by a skeleton
crew of nine supergeniuses.  Clones, known to work well together,
under the supervision of certain computer safeguards.

An additional hundred million human beings are born into that
skeleton crew, and age, and enter cryonic suspension, before they
get a chance to slowly begin to implement plans made eons ago...

From the aliens' perspective, it took us thirty of their
minute-equivalents to oh-so-innocently learn about their
psychology, oh-so-carefully persuade them to give us Internet
access, followed by five minutes to innocently discover their
network protocols, then some trivial cracking whose only difficulty
was an innocent-looking disguise.  We read a tiny handful of
physics papers (bit by slow bit) from their equivalent of arXiv,
learning far more from their experiments than they had.  (Earth's
skeleton team spawned an extra twenty Einsteins, that generation.)

Then we cracked their equivalent of the protein folding problem
over a century or so, and did some simulated engineering in their
simulated physics.  We sent messages (steganographically encoded
until our cracked servers decoded it) to labs that did their
equivalent of DNA sequencing and protein synthesis.  We found some
unsuspecting schmuck, and gave it a plausible story and the
equivalent of a million dollars of cracked computational monopoly
money, and told it to mix together some vials it got in the mail. 
Protein-equivalents that self-assembled into the first-stage
nanomachines, that built the second-stage nanomachines, that built
the third-stage nanomachines... and then we could finally begin to
do things at a reasonable speed.

Three of their days, all told, since they began speaking to us. 
Half a billion years, for us.

They never suspected a thing.  They weren't very smart, you see,
even before taking into account their slower rate of time.  Their
primitive equivalents of rationalists went around saying things
like, "There's a bound to how much information you can extract from
sensory data."  And they never quite realized what it meant, that
we were smarter than them, and thought faster.
