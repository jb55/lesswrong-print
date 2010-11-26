
# Feynman Paths

At this point I would like to introduce another key idea in quantum
mechanics.  Unfortunately, this idea was introduced so well in
chapter 2 of *QED: The Strange Theory of Light and Matter* by
Richard Feynman, that my mind goes blank when trying to imagine how
to introduce it any other way.  As a compromise with just stealing
his entire book, I stole one diagram - a diagram of how a mirror
*really*works.

[![Feynman1](http://lesswrong.com/static/imported/2008/04/16/feynman1.png "Feynman1")](http://lesswrong.com/static/imported/2008/04/16/feynman1.png)

In elementary school, you learn that the angle of incidence equals
the angle of reflection.  But *actually*, saith Feynman, each part
of the mirror reflects at all angles.

So why is it that, way up at the human level, the mirror seems to
reflect with the angle of incidence equal to the angle of
reflection?

Because in quantum mechanics, amplitude that flows to identical
configurations (particles of the same species in the same places)
is added together, regardless of how the amplitude got there.

To find the amplitude for a photon to go from S to P, you've got to
add up the amplitudes for *all* the different ways the photon could
get there - by bouncing off the mirror at A, bouncing off the
mirror at B...

The rule of the Feynman "path integral" is that each of the paths
from S to P contributes an amplitude of *constant* magnitude but
varying *phase*, and the phase varies with the total *time* along
the path.  It's as if the photon is a tiny spinning clock - the
hand of the clock stays the same length, but it turns around at a
constant rate for each unit of time.

Feynman graphs the time for the photon to go from S to P via A, B,
C, ...  Observe: the *total* time *changes less* between "the path
via F" and "the path via G", then the total time changes between
"the path via A" and "the path via B".  So the phase of the complex
amplitude changes less, too.

And when you add up all the ways the photon can go from S to P, you
find that most of the amplitude comes from the middle part of the
mirror - the contributions from other parts of the mirror tend to
mostly cancel each other out, as shown at the bottom of Feynman's
figure.

There is no answer to the question "Which part of the mirror did
the photon *really* come from?"  Amplitude is flowing from *all*of
these configurations.  But if we were to *ignore* all the parts of
the mirror except the middle, we would calculate essentially the
same amount of *total* amplitude.

This means that a photon, which can get from S to P by striking
*any*part of the mirror, will *behave pretty much as if* only a
tiny part of the mirror exists - the part where the photon's angle
of incidence equals the angle of reflection.

*Unless* you start playing clever tricks using your knowledge of
quantum physics.

For example, you can *scrape away* parts of the mirror at regular
intervals, deleting some little arrows and leaving others.  Keep A
and its little arrow; scrape away B so that it has no little arrow
(at least no little arrow going to P).  Then a distant part of the
mirror can contribute amplitudes that add up with each other to a
big final amplitude, because you've removed the amplitudes that
were out of phase.

In which case you can make a mirror that reflects with the angle of
incidence not equal to the angle of reflection.  It's called a
diffraction grating.  But it reflects different wavelengths of
light at different angles, so a diffraction grating is not quite a
"mirror" in the sense you might imagine; it produces little
rainbows of color, like a droplet of oil on the surface of water.

How fast does the little arrow rotate?  As fast as the photon's
wavelength - that's what a photon's wavelength *is*.  The
wavelength of yellow light is \~570 nanometers:  If yellow light
travels an extra 570 nanometers, its little arrow will turn all the
way around and end up back where it started.

So either Feynman's picture is of a very tiny mirror, or he is
talking about some very big photons, when you look at how fast the
little arrows seem to be rotating.  Relative to the wavelength of
visible light, a human being is a lot bigger than the level at
which you can see quantum effects.

You'll
[recall](http://www.overcomingbias.com/2008/04/quantum-arena.html)
that the first key to recovering the classical hallucination from
the reality of quantum physics, was the possibility of approximate
independence in the amplitude distribution.  (Where the
distribution roughly factorizes, it can look like a subsystem of
particles is evolving on its own, without being entangled with
every other particle in the universe.)

The second key to re-deriving the classical hallucination, is the
kind of behavior that we see in this mirror.  Most of the possible
paths cancel each other out, and only a small group of neighboring
paths add up.  Most of the amplitude comes from a small
neighborhood of histories - the sort of history where, for example,
the photon's angle of incidence is equal to its angle of
reflection.  And so too with many other things you are pleased to
regard as "normal".

My first posts on QM showed amplitude flowing in crude chunks from
discrete situation to discrete situation.  In *real life* there are
continuous amplitude flows between continuous configurations, like
we saw with Feynman's mirror.  But by the time you climb all the
way up from a few hundred nanometers to the size scale of human
beings, most of the amplitude contributions have canceled out
except for a narrow neighborhood around one path through history.

Mind you, this is *not* the reason why a photon only seems to be in
one place at a time.  That's a different story, which we won't get
to today.

The more massive things are - actually the more energetic they are,
mass being a form of energy - the faster the little arrows rotate.
Shorter wavelengths of light having more energy is a special case
of this.  Compound objects, like a neutron made of three quarks,
can be treated as having a collective amplitude that is the
multiplicative product of the component amplitudes - at least to
the extent that the amplitude distribution factorizes, so that you
can treat the neutron as an individual.

Thus the relation between energy and wavelength holds for more than
photons and electrons; atoms, molecules, and human beings can be
regarded as having a wavelength.

But by the time you move up to a human being - or even a single
biological cell - the mass-energy is *really, really* large
relative to a yellow photon.  So the clock is rotating
*really, really fast.*  The wavelength is *really, really* short. 
Which means that the neighborhood of paths where things don't
cancel out is *really, really narrow.*

By and large, a human experiences what seems like a single path
through configuration space - the classical hallucination.

This is not how Schrรถdinger's Cat works, but it is how a regular
cat works.

Just remember that this business of single paths through time is
not *fundamentally* true.  It's merely a good approximation for
modeling a sofa.  The classical hallucination breaks down
completely by the time you get to the atomic level.  It can't
handle quantum computers at all.  It would fail you even if you
wanted a *sufficiently precise* prediction of a brick.  A billiard
ball taking a single path through time is not how the universe
*really, really* works - it is just what human beings have evolved
to easily visualize, for the sake of throwing rocks.

(PS:  I'm given to understand that the Feynman path integral may be
more fundamental than the Schrรถdinger equation: that is, you can
*derive* Schrรถdinger from Feynman.  But as far as I can tell from
examining the equations, Feynman is still differentiating the
amplitude distribution, and so reality doesn't yet break down into
point amplitude flows between point configurations.  Some physicist
please* *correct me if I'm wrong about this, because it is a matter
on which I am quite curious.)
