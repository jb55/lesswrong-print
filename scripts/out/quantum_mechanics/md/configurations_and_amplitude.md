
# Quantum Explanations

So the universe isn't made of little billiard balls, and it isn't
made of crests and troughs in a pool of aether...  Then what is the
stuff that stuff is made of?

(Diagrams stolen from
[qubit.org](http://cam.qubit.org/articles/intros/comp.php) and
edited for my purposes.)

[![Fig1\_4](http://lesswrong.com/static/imported/2008/04/07/fig1_4.gif "Fig1_4")](http://lesswrong.com/static/imported/2008/04/07/fig1_4.gif)
In Figure 1, we see, at **A**, a half-silvered mirror, and two
photon detectors, **1** and **2**.

Early scientists, when they ran experiments like this, became
confused about what the results meant.  They would send a photon
toward the half-silvered mirror, and half the time they would see
the detector at 1 click, and the other half the time they would see
the detector at 2 click.

The early scientists - you're going to laugh at this - thought that
the silver mirror deflected the photon half the time, and let it
through half the time.

Ha, ha!  As if the half-silvered mirror did different things on
different occasions!  I want you to let go of this idea, because if
you cling to what early scientists thought, you will become
extremely confused.  The half-silvered mirror obeys the same rule
every time.

If you were going to write a computer program that *was* this
experiment - not a computer program that *predicted* the result of
the experiment, but a computer program that resembled the
underlying reality - it might look sort of like this:

At the start of the program (the start of the experiment, the start
of time) there's a certain mathematical entity, called a
*configuration.*  You can think of this configuration as
corresponding to "There is one photon heading from the photon
source toward the half-silvered mirror", or just "A photon heading
toward **A**."

A configuration can store a single complex value - "complex" as in
the complex numbers (a + b*i*).  At the start of the program,
there's already a complex number stored in the configuration "A
photon heading toward **A**."  The exact value doesn't matter so
long as it's not zero.  We'll let the configuration "A photon
heading toward **A**" have a value of (-1 + 0*i*).

All this is a fact within the territory, not a description of
anyone's knowledge.  A configuration isn't a proposition or a
possibility or a way the world can be.  A configuration is a
variable in the program - you can think of it as a kind of memory
location whose index is "A photon heading toward **A**" - and it's
out there in the territory.

As the complex numbers that get assigned to configurations are not
positive real numbers between 0 and 1, there is no danger of
confusing them with probabilities.  "A photon heading toward **A**"
has complex value -1, which is hard to see as a degree of belief. 
The complex numbers are values within the program, again out there
in the territory.  We'll call the complex numbers *amplitudes.*

[![Fig1\_4](http://lesswrong.com/static/imported/2008/04/07/fig1_4.gif "Fig1_4")](http://lesswrong.com/static/imported/2008/04/07/fig1_4.gif)

There are two other configurations, which we'll call "A photon
going from **A** to Detector **1**" and "A photon going from **A**
to Detector **2**."  These configurations don't have a complex
value yet; it gets assigned as the program runs.

We are going to calculate the amplitudes of "A photon going from
**A** toward **1**" and "A photon going from **A** toward **2**"
using the value of "A photon going toward **A**", and the rule that
describes the half-silvered mirror at **A**.

Roughly speaking, the half-silvered mirror rule is "Multiply by 1
when the photon goes straight, and multiply by *i* when the photon
turns at a right angle."  This is the universal rule that relates
the amplitude of the configuration of "a photon going in", to the
amplitude that goes to the configurations of "a photon coming out
straight" or "a photon being deflected".

So we pipe the amplitude of the configuration "A photon going
toward **A**", which is (-1 + 0*i*), into the half-silvered mirror
at **A**, and this transmits an amplitude of (-1 + 0*i*)\**i* = (0
+ -*i*) to "A photon going from **A**toward **1**", and also
transmits an amplitude of (-1 + 0*i*)\*1 = (-1 + 0*i*) to "A photon
going from **A** toward **2**".

In the Figure 1 experiment, these are all the configurations and
all the transmitted amplitude we need to worry about, so we're
done.  Or, if you want to think of "Detector **1** gets a photon"
and "Detector **2** gets a photon" as separate configurations,
they'd just inherit their values from "**A**-\>**1**" and
"**A**-\>**2**" respectively.  (Actually, the values inherited
should be multiplied by another complex factor, corresponding from
the distance from **A** to the detector; but we will ignore that
for today, and suppose that all distances traveled in our
experiments happen to correspond to a complex factor of 1.)

So the final program state is:

> Configuration "A photon going toward **A**": (-1 + 0*i*)  
> Configuration "A photon going from **A** toward **1**": (0 +
> -*i*)  
> Configuration "A photon going from **A** toward **2**": (-1 +
> 0*i*)  
>     *and optionally*  
> Configuration "Detector **1** gets a photon": (0 + -*i*)  
> Configuration "Detector **2** gets a photon": (-1 + 0*i*)

This same result occurs - the same amplitudes stored in the same
configurations - every time you run the program (every time you do
the experiment).

Now, for *complicated* reasons that we aren't going to go into
today - considerations that belong on a higher level of
organization than fundamental quantum mechanics, the same way that
atoms are more complicated than quarks - there's no *simple*
measuring instrument that can directly tell us the exact amplitudes
of each configuration.  We can't directly see the program state.

So how do physicists know what the amplitudes are? 

We *do* have a magical measuring tool that can tell us the
*squared modulus* of a configuration's amplitude.  If the original
complex amplitude is (a + b*i*), we can get the positive real
number (a^2^ + b^2^).  Think of the Pythagorean theorem: if you
imagine the complex number as a little arrow stretching out from
the origin on a two-dimensional plane, then the magic tool tells us
the squared length of the little arrow, but it doesn't tell us the
direction the arrow is pointing.

To be more precise, the magic tool actually just tells us the
*ratios* of the squared lengths of the amplitudes in some
configurations.  We don't know how long the arrows are in an
absolute sense, just how long they are relative to each other.  But
this turns out to be enough information to let us reconstruct the
laws of physics - the rules of the program.  And so I can talk
about amplitudes, not just ratios of squared moduli.

When we wave the magic tool over "Detector **1** gets a photon" and
"Detector **2** gets a photon", we discover that these
configurations have the same squared modulus - the lengths of the
arrows are the same.  Thus speaks the magic tool.  By doing more
*complicated* experiments (to be seen shortly), we can tell that
the original complex numbers had a ratio of *i* to 1.  
And what is this magical measuring tool?

Well, from the perspective of everyday life - way, way, way above
the quantum level and a lot more complicated - the magical
measuring tool is that we send some photons toward the
half-silvered mirror, one at a time, and count up how many photons
arrive at Detector 1 versus Detector 2 over a few thousand trials. 
The ratio of these values is the ratio of the squared moduli of the
amplitudes.  But the reason for this is *not* something we are
going to consider yet.  Walk before you run.  It is not possible to
understand what happens *all the way up* at the level of everyday
life, before you understand what goes on in much simpler cases.

For today's purposes, we have a magical squared-modulus-ratio
reader.  And the magic tool tells us that the little
two-dimensional arrow for the configuration "Detector **1** gets a
photon" has the same squared length as for "Detector **2** gets a
photon".  That's all.

You may wonder, "Given that the magic tool works this way, what
motivates us to use quantum theory, instead of thinking that the
half-silvered mirror reflects the photon around half the time?"

Well, that's just begging to be confused - putting yourself into a
historically realistic frame of mind like that and using everyday
intuitions.  Did I say anything about a little billiard ball going
one way or the other and possibly bouncing off a mirror?  That's
not how reality works.  *Reality* is about complex amplitudes
flowing between configurations, and the laws of the flow are
stable.

But if you insist on seeing a more complicated situation that
billiard-ball ways of thinking can't handle, here's a more
complicated
experiment:[![Fig2](http://lesswrong.com/static/imported/2008/04/08/fig2.gif "Fig2")](http://lesswrong.com/static/imported/2008/04/08/fig2.gif)

In Figure 2, **B** and **C** are full mirrors, and **A** and **D**
are half-mirrors.  The line from **D** to **E** is dashed for
reasons that will become apparent, but amplitude is flowing from
**D** to **E** under exactly the same laws.

Now let's apply the rules we learned before:

At the beginning of time "A photon heading toward **A**" has
amplitude (-1 + 0*i*).

We proceed to compute the amplitude for the configurations "A
photon going from **A** to **B**" and "A photon going from **A** to
**C**".

> "A photon going from **A** to **B**" = *i* \* "A photon heading
> toward **A**" = (0 + -*i*)

Similarly,

> "A photon going from **A** to **C**" = 1 \* "A photon heading
> toward **A**" = (-1 + 0*i*)

The full mirrors behave (as one would expect) like half of a
half-silvered mirror - a full mirror just bends things by right
angles and multiplies them by *i*.  (To state this slightly more
precisely:  For a full mirror, the amplitude that flows, from the
configuration of a photon heading in, to the configuration of a
photon heading out at a right angle, is multiplied by a factor of
*i*.)

So:

> "A photon going from **B** to **D**" = *i* \* "A photon going from
> **A** to **B**" = (1 + 0*i*)  
> "A photon going from **C** to **D**" = *i* \* "A photon going from
> **A** to **C**" = (0 + -*i*)

"**B** to **D**" and "**C** to **D**" are two different
configurations - we don't simply write "A photon at **D**" -
because the photons are arriving at two different angles in these
two different configurations.  And what **D** does to a photon,
depends on the angle at which the photon arrives.

Again, the rule (speaking loosely) is that when a half-silvered
mirror bends light at a right angle, the amplitude that flows from
the photon-going-in configuration to the photon-going-out
configuration, is the amplitude of the photon-going-in
configuration multiplied by *i*.  And when two configurations are
related by a half-silvered mirror letting light straight through,
the amplitude that flows from the photon-going-in configuration is
multiplied by 1.

So:

-   From the configuration "A photon going from **B** to **D**",
    with original amplitude (1 + 0*i*)
    -   Amplitude of (1 + 0*i*) \* *i* = (0 + *i*) flows to "A photon
        going from **D** to **E**"
    -   Amplitude of (1 + 0*i*) \* 1 = (1 + 0*i*) flows to "A photon
        going from **D** to **F**".

-   From the configuration "A photon going from **C** to **D**",
    with original amplitude (0 + -*i*)
    -   Amplitude of (0 + -*i*) \* *i* = (1 + 0*i*) flows to "A photon
        going from **D** to **F**"
    -   Amplitude of (0 + -*i*) \* 1 = (0 + -*i*) flows to "A photon
        going from **D** to **E**".


Therefore:

-   The *total* amplitude flowing to configuration "A photon going
    from **D** to **E**" is (0 + *i*) + (0 + -*i*) = (0 + 0*i*) = 0.
-   The total amplitude flowing to configuration "A photon going
    from **D** to **F**" is (1 + 0*i*) + (1 + 0*i*) = (2 + 0*i*).

[![Fig2](http://lesswrong.com/static/imported/2008/04/08/fig2.gif "Fig2")](http://lesswrong.com/static/imported/2008/04/08/fig2.gif)(You
may want to try working this out yourself on pen and paper if you
lost track at any point.)

But the upshot, from that super-high-level "experimental"
perspective that we think of as normal life, is that we see *no*
photons detected at **E**.  Every photon seems to end up at **F**. 
The ratio of squared moduli between "**D** to **E**" and "**D** to
**F**" is 0 to 4.  That's why the line from **D** to **E** is
dashed, in this figure.

This is not something it is possible to explain by thinking of
half-silvered mirrors deflecting little incoming billiard balls
half the time.  You've *got* to think in terms of amplitude flows.

If half-silvered mirrors deflected a little billiard ball half the
time, in this setup, the little ball would end up at Detector 1
around half the time and Detector 2 around half the time.  Which it
doesn't.  So don't think that.

You may say, "But wait a minute!  I can think of another hypothesis
that accounts for this result.  What if, when a half-silvered
mirror reflects a photon, it does something to the photon that
ensures it doesn't get reflected next time?  And when it lets a
photon go through straight, it does something to the photon so it
gets reflected next time."

Now really, there's no need to go making the rules so complicated. 
Occam's Razor, remember.  Just stick with simple, normal amplitude
flows between configurations.

But if you want *another* experiment that disproves your *new*
alternative hypothesis, it's this one:

[![Fig3](http://lesswrong.com/static/imported/2008/04/07/fig3.gif "Fig3")](http://lesswrong.com/static/imported/2008/04/07/fig3.gif)
Here, we've left the whole experimental setup the same, and just
put a little blocking object between **B** and **D**.  This ensures
that the amplitude of "A photon going from **B** to **D**" is 0.

Once you eliminate the amplitude contributions from that
configuration, you end up with totals of (1 + 0*i*) in "A photon
going from **D** to **F**", and (0 + -*i*) in "A photon going from
**D** to **E**".

The squared moduli of (1 + 0*i*) and (0 + -*i*) are both 1, so the
magic measuring tool should tell us that the ratio of squared
moduli is 1.  Way back up at the level where physicists exist, we
should find that Detector 1 goes off half the time, and Detector 2
half the time.

The same thing happens if we put the block between C and D.  The
amplitudes are different, but the ratio of the squared moduli is
still 1, so Detector 1 goes off half the time and Detector 2 goes
off half the time.

This cannot *possibly*happen with a little billiard ball that
either does or doesn't get reflected by the half-silvered mirrors.

Because complex numbers can have opposite directions, like 1 and
-1, or *i* and -*i*, amplitude flows can cancel each other out. 
Amplitude flowing from configuration X into configuration Y can be
canceled out by an equal and opposite amplitude flowing from
configuration Z into configuration Y.  In fact, that's exactly what
happens in this experiment.

In probability theory, when something can either happen one way or
another, X or \~X, then P(Z) = P(Z|X)P(X) + P(Z|\~X)P(\~X).  And
all probabilities are positive.  So if you establish that the
probability of Z happening given X is 1/2, and the probability of X
happening is 1/3, then the total probability of Z happening is
*at least* 1/6 no matter *what* goes on in the case of \~X. 
There's no such thing as negative probability, less-than-impossible
credence, or (0 + *i*) credibility, so *degrees of belief* can't
cancel each other out like amplitudes do.

Not to mention that
[probability is in the mind](/lw/oj/probability_is_in_the_mind/) to
begin with; and we are talking *about* the territory, the
program-that-is-reality, not talking *about* human cognition or
states of partial knowledge.

By the same token, configurations are not *propositions,* not
*statements,* not *ways the world could be.*  Configurations are
not semantic constructs.  Adjectives like *probable*
and*possible** *do not apply to them; they are not beliefs or
sentences or possible worlds.  They are not *true* or *false* but
simply *real.*

[![Fig2](http://lesswrong.com/static/imported/2008/04/08/fig2.gif "Fig2")](http://lesswrong.com/static/imported/2008/04/08/fig2.gif)In
the experiment of Figure 2, at right, do not be tempted to think
anything like:  "The photon goes to either **B** or **C**, but it
*could* have gone the other way, and this possibility interferes
with its ability to go to **E**..."

It makes no sense to think of something that "could have happened
but didn't" exerting an effect on the world.  We can *imagine*
things that could have happened but didn't - like thinking, "Gosh,
that car almost hit me" - and our imagination can have an effect on
our future behavior.  But the event of imagination is a real event,
that actually happens, and *that* is what has the effect.  It's
your imagination of the unreal event - your very real imagination,
implemented within a quite physical brain - that affects your
behavior.

To think that the *actual event* of a car hitting you - this event
which could have happened to you, but in fact didn't - is directly
exerting a *causal* effect on your behavior, is
[mixing up the map with the territory](/lw/oi/mind_projection_fallacy/).

What affects the world is real.  (If things can affect the world
without being "real", it's hard to see what the word "real"
means.)  Configurations and amplitude flows are causes, and they
have visible effects; they are real.  Configurations are not
possible worlds and amplitudes are not degrees of belief, any more
than your chair is a possible world or the sky is a degree of
belief.

So what *is* a configuration, then?

Well, you'll be getting a clearer idea of that in future posts.

But to give you a quick idea of how the real picture differs from
the simplified version we saw today...

Our experimental setup only dealt with one moving particle, a
single photon.  Real configurations are about multiple particles. 
Tomorrow's post will deal with the case of more than one particle,
and that should give you a much clearer idea of what a
configuration is.

Each configuration we talked about, *should*have described a joint
position of all the particles in the mirrors and detectors, not
just the position of one photon bopping around.

In fact, the *really real* configurations are over joint positions
of all the particles in the universe, including the particles
making up the experimenters.  You can see why I'm saving the notion
of*experimental results* for later posts.

In the real world, amplitude is a continuous distribution over a
continuous *space* of configurations.  Today's "configurations"
were blocky and digital, and so were our "amplitude flows".  It was
as if we were talking about a photon teleporting from one place to
another.

We'll get atoms and molecules and humans and all that stuff, out of
a differentiable amplitude distribution in a continuous
configuration space, *later.*

If none of that made sense, don't worry.  It will be cleared up in
future posts.  Just wanted to give you some idea of where this was
heading.
