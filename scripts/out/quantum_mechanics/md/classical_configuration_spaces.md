
# Classical Configuration Space

>   Once upon a time, there was a student who went to a math
> lecture.  When the lecture was over, he approached one of the other
> students, and said, "I couldn't follow that at all.  The professor
> was talking about rotating 8-dimensional objects!  How am I
> supposed to visualize something rotating in 8 dimensions?"  
>     "Easy," replied the other student, "you visualize it rotating
> in N dimensions, then let N go to 8."  
>             -- old joke

Quantum configuration space isn't quite like classical
configuration space. But in this case, considering that 8
dimensions is peanuts in quantum physics, even I concede that you
ought to start with classical configuration space first.

(I apologize for the homemade diagrams, but this blog post already
used up all available time...)

In classical physics, a configuration space is a way of visualizing
the state of an entire system as a single point in a
higher-dimensional space.

[![Conf1](http://lesswrong.com/static/imported/2008/04/14/conf1.png "Conf1")](http://lesswrong.com/static/imported/2008/04/14/conf1.png)
Suppose that a system is composed of two particles, A and B, each
on the same 1-dimensional line.  (We'll call the two directions on
the line, "forward" and "back".)

Then we can view the state of the complete system A+B as a single
point in 2-dimensional space.

If you look at state 1, for example, it describes a state of the
system where B is far forward and A is far back.  We can view state
1 as being embodied either in two 1-dimensional positions (the
representation on the right), or view it as one 2-dimensional
position (the representation on the left).

[![Conf2](http://lesswrong.com/static/imported/2008/04/14/conf2.png "Conf2")](http://lesswrong.com/static/imported/2008/04/14/conf2.png)
To help grasp the idea of viewing a *system* as a point, this
alternate graph shows A and B on the same line.

When A and B are far apart, they both move toward each other.
However, B moves slower than A.  Also, B wants to be closer to A
than A wants to be close to B, so as B gets too close, A runs
away...

(At least that's what I had in mind while trying to draw the system
evolution.)

The system evolution can be shown as a discrete series of states: 
Time=1, Time=2, Time=3...  But in configuration space, I can draw
the system evolution as a smooth trajectory.

[![Conf3](http://lesswrong.com/static/imported/2008/04/14/conf3.png "Conf3")](http://lesswrong.com/static/imported/2008/04/14/conf3.png)
If I had the time (to learn to use the appropriate software), I'd
be drawing neat-o 3D diagrams at this point.  Like the diagram at
right, only with, like, actual graphics.

You may have previously heard the phrase, "time is the 4th
dimension".  But the diagram at right shows the evolution over time
of a 1-dimensional universe with two particles.  So time is the
third dimension, the first dimension being the position of particle
A, and the second dimension being the position of particle B.

All these neat pictures are simplified, even relative to classical
physics.

In classical physics, each particle has a 3-dimensional position
and a 3-dimensional velocity.  So to specify the complete state of
a 7-particle system would require 42 real numbers, which you could
view as one point in 42-dimensional space.

Hence the joke.

Configuration spaces get very high-dimensional, very fast.  That's
why we're sticking with 2 particles in a 1-dimensional universe. 
Anything more than that, I can't draw on paper - you've just got to
be able to visualize it in N dimensions.

So far as classical physics is concerned, it's a matter of taste
whether you would want to imagine a system state as a point in
configuration space, or imagine the individual particles.
Mathematically, the two systems are isomorphic - in classical
physics, that is.  So what's the benefit of imagining a classical
configuration space?

[![Conf4](http://lesswrong.com/static/imported/2008/04/14/conf4.png "Conf4")](http://lesswrong.com/static/imported/2008/04/14/conf4.png)
Well, for one thing, it makes it possible to visualize joint
probability distributions.

The grey area in the diagram represents a
*probability distribution* over potential states of the A+B
system.

If this is my state of knowledge, I think the system is somewhere
in the region represented by the grey area.  I believe that if I
knew the actual states of both A and B, and visualized the A+B
system as a point, the point would be inside the grey.

Three sample possibilities within the probability distribution are
shown, and the corresponding systems.

And really the probability distribution should be lighter or
darker, corresponding to volumes of decreased or increased
probability *density*.  It's a *probability* distribution, not a
*possibility* distribution.  I didn't make an effort to represent
this in the diagram - I probably should have - but you can imagine
it if you like.  Or pretend that the slightly darker region in the
upper left is a volume of increased probability density, rather
than a fluke of penciling.

Once you've hit on the idea of using a bounded volume in
configuration space to represent possibility, or a cloud with
lighter and darker parts to represent probability, you can ask how
your *knowledge about* a system develops over time.  If you know
how each system state (point in configuration space) develops
dynamically into a future system state, and you draw a little cloud
representing your current probability distribution, you can project
that cloud into the future.

[![Conf5](http://lesswrong.com/static/imported/2008/04/14/conf5.png "Conf5")](http://lesswrong.com/static/imported/2008/04/14/conf5.png)
Here I start out with uncertainty represented by the squarish grey
box in the first configuration space, at bottom right.

All the points in the first grey box, correspond to system states,
that dynamically develop over time, into new system states,
corresponding to points in the grey rectangle in the second
configuration space at middle right.

Then, my little rectangle of uncertainty develops over time into a
wiggly figure, three major possibility-nodes connected by thin
strings of probability density, as shown at top right.

In this figure I also tried to represent the idea of conserved
probability volume - the same total volume of possibility, with
points evolving to other points with the same local density, at
each successive time.  This is Liouville's Theorem, which is the
key to the
[Second Law of Thermodynamics](/lw/o5/the_second_law_of_thermodynamics_and_engines_of/),
as I have previously described.

Neat little compact volumes of uncertainty develop over time, under
the laws of physics, into big wiggly volumes of uncertainty.  If
you want to describe the new volumes of uncertainty *compactly,* in
less than a gazillion gigabytes, you've got to draw larger
boundaries around them.  Once you draw the new larger boundary,
your uncertainty never shrinks, because probability flow is
conservative.  So entropy always increases.  That's the second law
of thermodynamics.

Just figured I'd mention that, as long as I was drawing diagrams...
you can see why this "visualize a configuration space" trick is
useful, even in classical physics.

[![Conf6](http://lesswrong.com/static/imported/2008/04/15/conf6.png "Conf6")](http://lesswrong.com/static/imported/2008/04/15/conf6.png)
Another idea that's easier to visualize in configuration space is
the idea of conditional independence between two probabilistic
variables.

Conditional independence happens when the joint probability
distribution is the product of the individual probability
distributions:

P(A,B) = P(A) x P(B)

The vast majority of possible probability distributions are not
conditionally independent, the same way that the vast majority of
shapes are not rectangular.  Actually, this is oversimplifying: 
It's not enough for the volume of possibilities to be rectangular. 
The probability density has to *factorize* into a product of
probability densities on each side.

The vast majority of shapes are not rectangles, the vast majority
of color patterns are not plaid.  It's conditional *independence,*
not conditional dependence, that is the unusual special case.

(I bet when you woke up this morning, you didn't think that today
you would be visualizing plaid patterns in N dimensions.)

[![Conf4\_2](http://lesswrong.com/static/imported/2008/04/14/conf4_2.png "Conf4_2")](http://lesswrong.com/static/imported/2008/04/14/conf4_2.png)
In the figure reprised here at right, my little cloud of
uncertainty is not rectangular.

Hence, my uncertainty about A and my uncertainty about B are not
independent.

If you tell me A is far forward, I will conclude B is far back.  If
you tell me A is in the middle of its 1-dimensional universe, I
will conclude that B is likewise in the middle.

If I tell you A is far back, what do you conclude about B?

Aaaand that's classical configuration space, folks.  It doesn't add
anything mathematically to classical physics, but it can help human
beings visualize system dynamics and probability densities.  It
seemed worth filtering into a separate post, because configuration
space is a modular concept, useful for
[other](/lw/nl/the_cluster_structure_of_thingspace/)
[ideas](/lw/o5/the_second_law_of_thermodynamics_and_engines_of/).

Quantum physics *inherently* takes place in a configuration space. 
You can't take it out.  Tomorrow, we'll see why.
