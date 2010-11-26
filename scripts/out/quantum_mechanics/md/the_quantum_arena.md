
# The Quantum Arena

Yesterday, we looked at configuration spaces in classical physics. 
In classical physics, configuration spaces are a useful, but
optional, point of view.

Today we look at quantum physics, which *inherently* takes place
inside a configuration space, and *cannot be taken out*.

[![Ampl1](http://lesswrong.com/static/imported/2008/04/15/ampl1.png "Ampl1")](http://lesswrong.com/static/imported/2008/04/15/ampl1.png)For
a start, as you might guess, in quantum physics we deal with
distributions of complex amplitudes, rather than probability
distributions made up of positive real numbers.  At left, I've used
up 3 dimensions drawing a complex distribution over the position of
*one* particle, A.

You may recall that yesterday, 3 dimensions let us display the
position of two 1-dimensional particles plus the system evolution
over time.  Today, it's taking us 3 dimensions just to visualize an
amplitude distribution over the position of one 1-dimensional
particle at a single moment in time.  Which is why we did classical
configuration spaces first.

[![Ampl2](http://lesswrong.com/static/imported/2008/04/15/ampl2.png "Ampl2")](http://lesswrong.com/static/imported/2008/04/15/ampl2.png)
To clarify the meaning of the above diagram, the left-to-right
direction is the position of A.

The up-and-down direction, and the invisible third dimension that
leaps out of the paper, are devoted to the complex amplitudes. 
Since a complex amplitude has a real and imaginary part, they use
up 2 of our 3 dimensions.

Richard Feynman said to just imagine the complex amplitudes as
little 2-dimensional arrows.  This is as good a representation as
any; little 2D arrows behave just the same way complex numbers do. 
(You add little arrows by starting at the origin, and moving along
each arrow in sequence.  You multiply little arrows by adding the
angles and multiplying the lengths.  This is isomorphic to the
complex field.)  So we can think of each position of the A particle
as having a little arrow associated to it.

As you can see, the position of A bulges in two places - a big
bulge to the left, and a smaller bulge at right.  Way up at the
level of classical observation, there would be a large probability
(integrating over the squared modulus) of finding A somewhere to
the left, and a smaller probability of finding it at the small
bulge to the right.

Drawing a neat little graph of the A+B system would involve having
a complex amplitude for each joint position of the A and B
particles, which you could visualize as a hypersurface in 4
dimensions.  I'd draw it for you, but I left my 4-dimensional
pencil in the pocket of the 3rd leg of my other pants.

[![Conf6\_2](http://lesswrong.com/static/imported/2008/04/15/conf6_2.png "Conf6_2")](http://lesswrong.com/static/imported/2008/04/15/conf6_2.png)
You may recall from yesterday that a plaid rectangular probability
distribution factorizes into the product of two independent
probability distributions.

This kind of independence-structure is one of several keys to
recovering the illusion of individual particles from quantum
amplitude distributions.   If the amplitude distribution roughly
factorizes, has subsystems A and B with Amplitude(X,Y) \~
Amplitude(X) \* Amplitude(Y), then X and Y will seem to evolve
roughly independently of each other.

But maintaining the illusion of individuality is harder in quantum
configuration spaces, because of the identity of particles.  This
identity cuts down the size of a 2-particle configuration space by
1/2, cuts down the size of a 3-particle configuration space by 1/6,
and so on.  Here, the diminished configuration space is shown for
the 2-particle case:



[![Ampl3\_3](http://lesswrong.com/static/imported/2008/04/15/ampl3_3.png "Ampl3_3")](http://lesswrong.com/static/imported/2008/04/15/ampl3_3.png)

The quantum configuration space is over joint possibilities like "a
particle here, a particle there", not "this particle here, that
particle there".  What would have been a neat little plaid pattern
gets folded in on itself.

You might think that you could recover the structure by figuring
out which particle is "really which" - i.e. if you see a "particle
far forward, particle in middle", you can guess that the first
particle is A, and the second particle is B, because only A can be
far forward; B just stays in the middle.  (This configuration would
lie in at the top of the original plaid pattern, the part that got
folded over).

The problem with this is the little triangular region, where the
folded plaid intersects itself.  In this region, the folded-over
amplitude distribution gets superposed, added together.  Which
makes an experimental difference, because the squared modulus of
the sum is not the sum of the squared moduli.

In that little triangular region of quantum configuration space,
there is simply no fact of the matter as to "which particle is
which".  Actually, there *never was* any such fact; but there was
an illusion of individuality, which in this case has broken down.

But even *that* isn't the ultimate reason why you can't take
quantum physics out of configuration space.

In classical configuration spaces, you can take a *single* point in
the configuration space, and the single point describes the entire
state of a classical system.  So you can take a single point in
classical configuration space, and ask how the corresponding system
develops over time.  You can take a single point in classical
configuration space, and ask, "Where does this one point go?"

The development over time of *quantum* systems depends on things
like the second derivative of the amplitude distribution.  Our laws
of physics describe how amplitude distributions develop into new
amplitude distributions.  They do not describe,
*even in principle,* how one configuration develops into another
configuration.

(I pause to observe that physics books make it way, way, way too
hard to figure out this extremely important fact.  You'd think
they'd tell you up front, "Hey, the evolution of a quantum system
depends on stuff like the second derivative of the amplitude
distribution, so you can't *possibly* break it down into the
evolution of individual configurations*.*"  When I first saw the
Schrรถdinger Equation it confused the hell out of me, because I
thought the equation was supposed to apply to single
configurations.)

If I've understood the laws of physics correctly, quantum mechanics
still has an extremely important property of *locality:*  You can
determine the instantaneous change in the amplitude of a single
configuration using only the infinitesimal neighborhood.  If you
forget that the space is continuous and think of it as a mesh of
computer processors, each processor would only have to talk to its
immedatien neighbors to figure out what to do next.  You do have to
talk to your neighbors - but *only* your next-door neighbors, no
telephone calls across town.  (Technical term: 
"[Markov neighborhood.](http://en.wikipedia.org/wiki/Markov_blanket)")

[Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life)
has the discrete version of this property; the future state of each
cell depends only on its own state and the state of neighboring
cells.

The second derivative -
[Laplacian](http://en.wikipedia.org/wiki/Laplace_operator),
actually - is not a *point* property.  But it is a *local*
property, where knowing the immediate neighborhood tells you
everything, regardless of what the rest of the distribution looks
like.  Potential energy, which also plays a role in the evolution
of the amplitude, can be computed at a *single* positional
configuration (if I've understood correctly).

There are mathematical transformations physicists use for their
convenience, like viewing the system as an amplitude distribution
over momenta rather than positions, which throw away this
neighborhood structure (e.g. by making potential energy a
non-locally-computable property).  Well, mathematical convenience
is a fine thing.  But I *strongly suspect* that the physically real
wavefunction has local dynamics.  This kind of locality seems like
an *extremely* important property, a candidate for something
hardwired into the nature of reality and the structure of
causation.  Imposing locality is part of the jump from Newtonian
mechanics to Special Relativity.

The temporal behavior of each amplitude in configuration space
depends only on the amplitude at neighboring points.  But you
cannot figure out what happens to the amplitude of a point in
quantum configuration space, by looking *only* at that *one*
point.  The *future* amplitude depends on the *present* second
derivative of the amplitude distribution.

So you can't say, as you can in classical physics, "If I had
infinite knowledge about the system, all the particles would be in
one definite position, and then I could figure out the exact future
state of the system."

If you had a point mass of amplitude, an infinitely sharp spike in
the quantum arena, the amplitude distribution would not be twice
differentiable and the future evolution of the system would be
undefined.  The known laws of physics would crumple up like
tinfoil.  Individual configurations don't have quantum dynamics;
amplitude distributions do.

A point mass of amplitude, concentrated into a single exact
position in configuration space, does not correspond to a precisely
known state of the universe.  It is *physical nonsense*.

It's like asking, in Conway's Game of Life:  "What is the future
state of this one cell, regardless of the cells around it?"  The
immediate future of the cell depends on its immediate neighbors;
its distant future may depend on distant neighbors.

Imagine trying to say, in a classical universe, "Well, we've got
this probability distribution over this classical configuration
space... but to find out where the system evolves, where the
probability flows from each point, we've got to twice differentiate
the probability distribution to figure out the dynamics."

In classical physics, the position of a particle is a separate fact
from its momentum.  You can know exactly where a particle is, but
not know exactly how fast it is moving.

In Conway's Game of Life, the velocity of a glider is not a
separate, additional fact about the board.  Cells are only "alive"
or "dead", and the *apparent* motion of a glider arises from a
configuration that repeats itself as the cell rules are applied. 
If you know the life/death state of all the cells in a glider, you
know the glider's velocity; they are not separate facts.

In quantum physics, there's an amplitude distribution over a
configuration space of particle positions.  Quantum dynamics
specify how that amplitude distribution evolves over time.  Maybe
you start with a blob of amplitude centered over position X, and
then a time T later, the amplitude distribution has evolved to have
a similarly-shaped blob of amplitude at position X+D.  Way up at
the level of human researchers, this looks like a particle with
velocity D/T.  But at the quantum level this behavior arises
*purely* out of the amplitude distribution over *positions,* and
the laws for how amplitude distributions evolve over time.

In quantum physics, if you know the exact current amplitude
distribution over particle positions, you know the exact future
behavior of the amplitude distribution.  Ergo, you know how blobs
of amplitude appear to propagate through the configuration space. 
Ergo, you know how fast the "particles" are "moving".  Full
knowledge of the amplitude distribution over positions implies full
knowledge of momenta.

Imagine trying to say, in a classical universe, "I twice
differentiate the probability distribution over these particles'
positions, to *physically determine* how fast they're going.  So if
I learned new information about where the particles were, they
might end up moving at different speeds.  If I got very precise
information about where the particles were, this would physically
cause the particles to start moving very fast, because the second
derivative of probability would be very large."  Doesn't sound all
that sensible, does it?  Don't try to interpret this nonsense -
it's not even analogously correct.  We'll look at the horribly
misnamed "Heisenberg Uncertainty Principle" later.

But that's why you can't take quantum physics out of configuration
space.  Individual configurations don't *have* physics.  Amplitude
distributions have physics.

(Though you can regard the *entire* state of a quantum system - the
whole amplitude distribution - as a single point in a space of
infinite dimensionality:  "Hilbert space."  But this is just a
convenience of visualization.  You imagine it in N dimensions, then
let N go to infinity.)
