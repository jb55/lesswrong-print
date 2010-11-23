
# Continuous Improvement

When is it
[adaptive](/lw/l0/adaptationexecuters_not_fitnessmaximizers/) for
an organism to be satisfied with what it has?  When does an
organism have enough children *and* enough food?  The answer to the
second question, at least, is obviously "never" from an
evolutionary standpoint.  The first proposition might be true if
the reproductive risks of all available options exceed their
reproductive benefits.  In general, though, it is a rare organism
in a rare environment whose reproductively optimal strategy is to
rest with a smile on its face, feeling happy.

To a first approximation, we might say something like "The
evolutionary purpose of emotion is to direct the cognitive
processing of the organism toward achievable, reproductively
relevant goals".  *Achievable*goals are usually located in the
Future, since you can't affect the Past.  Memory is a useful trick,
but *learning the lesson* of a success or failure isn't the same
goal as the original event - and usually the emotions associated
with the memory are less intense than those of the original event.

Then the way organisms and brains are built right now, "true
happiness" might be a chimera, a carrot dangled in front of us to
make us take the next step, and then yanked out of our reach as
soon as we achieve our goals.

This hypothesis is known as the
[hedonic treadmill](http://www.subjectpool.com/ed_teach/msc/personality/wellbeing/2006_Diener_Am_Psychologist_happiness_beyond_the_hedonic_treadmill.pdf).

The famous pilot studies in this domain demonstrated e.g. that past
lottery winners' stated subjective well-being was not significantly
greater than that of an average person, after a few years or even
months.  Conversely, accident victims with severed spinal cords
were not as happy as before the accident after six months - around
0.75 sd less than control groups - but they'd still adjusted much
more than they had expected to adjust.

This being the transhumanist form of Fun Theory, you might perhaps
say:  "Let's get rid of this effect.  Just delete the treadmill, at
least for positive events."



I'm not *entirely* sure we can get away with this.  There's
[the possibility that comparing good events to not-as-good events is what gives them part of their subjective quality](/lw/xi/serious_stories/). 
And on a moral level, it sounds perilously close to tampering with
Boredom itself.

So suppose that instead of modifying minds and values, we first ask
what we can do by modifying the environment.  Is there enough fun
in the universe, sufficiently accessible, for a transhuman to
*jog off the hedonic treadmill* - improve their life
*continuously*, at a sufficient rate to leap to an even higher
hedonic level before they had a chance to get bored with the
previous one?

This question leads us into great and interesting difficulties.

I had a nice vivid example I wanted to use for this, but
unfortunately I couldn't find the exact numbers I needed to
illustrate it.  I'd wanted to find a figure for the total mass of
the neurotransmitters released in the pleasure centers during an
average male or female orgasm, and a figure for the density of
those neurotransmitters - density in the sense of mass/volume of
the chemicals themselves.  From this I could've calculated
*how long a period of exponential improvement* would be possible -
how many years you could have "the best orgasm of your life" by a
margin of at least 10%, at least once per year - before your orgasm
collapsed into a black hole, the total mass having exceeded the
mass of a black hole with the density of the neurotransmitters.

Plugging in some random/Fermi numbers instead:

Assume that a microgram of additional neurotransmitters are
released in the pleasure centers during a standard human orgasm. 
And assume that neurotransmitters have the same density as water. 
Then an orgasm can reach around 10^8^ solar masses before it
collapses and forms a black hole, corresponding to 10^47^ baseline
orgasms.  If we assume that a 100mg dose of crack is as pleasurable
as 10 standard orgasms, then the street value of your last orgasm
is around a hundred billion trillion trillion trillion dollars.

I'm sorry.  I just had to do that calculation.

Anyway... requiring an *exponential* improvement eats up a factor
of 10^47^ in short order.  Starting from human standard and
improving at 10% per year, it would take less than 1,200 years.

Of course you say, "This but shows the folly of brains that use an
analog representation of pleasure.  Go digital, young man!"

If you redesigned the brain to represent the intensity of pleasure
using IEEE 754 double-precision floating-point numbers, a mere 64
bits would suffice to feel pleasures up to 10\^308 hedons...  in,
um, whatever base you were using.

This still represents less than 7500 years of 10% annual
improvement from a 1-hedon baseline, but after that amount of time,
you can switch to larger floats.

Now we *have* lost a bit of fine-tuning by switching to
IEEE-standard hedonics.  The 64-bit double-precision float has an
11-bit exponent and a 52-bit fractional part (and a 1-bit sign). 
So we'll only have 52 bits of precision (16 decimal places) with
which to represent our pleasures, however great they may be.  An
original human's orgasm would soon be lost in the rounding error...
which raises the question of how we can *experience* these
invisible hedons, when the finite-precision bits are the whole
substance of the pleasure.

We also have the odd situation that, starting from 1 hedon,
flipping a single bit in your brain can make your life 10^154^
times more happy.

And Hell forbid you flip the sign bit.  Talk about a need for
cosmic ray shielding.

But really - if you're going to go so far as to use imprecise
floating-point numbers to represent pleasure, why stop there?  Why
not move to
[Knuth's up-arrow notation](/lw/kn/torture_vs_dust_specks/)?

For that matter, IEEE 754 provides special representations for +/-
INF, that is to say, positive and negative infinity.  What happens
if a bit flip makes you experience infinite pleasure?  Does that
mean you [Win The Game](/lw/wv/prolegomena_to_a_theory_of_fun/)?

Now all of these questions I'm asking are in some sense unfair,
because right now I don't know exactly what I have to do with
*any*structure of bits in order to turn it into a
"[subjective experience](/lw/x4/nonperson_predicates/)".  Not that
this is
[the right way to phrase the question](/lw/oh/righting_a_wrong_question/). 
It's not like there's a ritual that summons some incredible density
of positive qualia that could collapse in its own right and form
[an epiphenomenal black hole](/lw/pn/zombies_the_movie/).

But don't laugh - or at least, don't *only* laugh - because in the
long run, these are *extremely*important questions.

To give you some idea of what's at stake here, Robin, in
"[For Discount Rates](http://www.overcomingbias.com/2008/01/protecting-acro.html)",
pointed out that an investment earning 2% annual interest for
12,000 years adds up to a googol (10\^100) times as much wealth;
therefore, "very distant future times are ridiculously easy to help
via investment".

I observed that there weren't a googol atoms in the observable
universe, let alone within a 12,000-lightyear radius of Earth.

And Robin replied, "I know of no law limiting economic value per
atom."

If you've got an increasingly large number of bits - things that
can be one or zero - and you're doing a proportional number of
computations with them... then how fast can you grow the amount of
fun, or pleasure, or value?

This echoes back to the questions in
[Complex Novelty](/lw/wx/complex_novelty/), which asked how many
kinds of problems and novel solutions you could find, and how many
deep insights there were to be had.  I argued there that the growth
rate is *faster than linear* in bits, e.g., humans can have much
more than four times as much fun as chimpanzees even though our
absolute brain volume is only around four times theirs.  But I
don't think the growth in "depth of good insights" or "number of
unique novel problems" is, um, *faster than exponential* in the
size of the pattern.

Now... it might be that the Law simply permits outright that we can
create very large amounts of subjective pleasure, every bit as
substantial as the sort of subjective pleasure we get now, by the
expedient of writing down very large numbers in a digital pleasure
center.  In this case, we have got it made.  Have we *ever* got it
made.

In one sense I can definitely see where Robin is coming from. 
Suppose that you had a specification of the first 10,000
[Busy Beaver](/lw/wx/complex_novelty/) machines - the
longest-running Turing machines with 1, 2, 3, 4, 5... states.  This
list could easily fit on a small flash memory card, made up of a
few measly avogadros of atoms.

And that small flash memory card would be worth...

Well, let me put it this way:  If a mathematician said to me that
the value of this memory card, was worth more than the rest of the
entire observable universe minus the card...  I wouldn't
necessarily *agree with him outright.*  But I would understand his
point of view.

Still, I don't know if you can truly grok the fun contained in that
memory card, without an unbounded amount of computing power with
which to understand it.  Ultradense information does not give you
ultradense economic value or ultradense fun unless you can also
*use* that information in a way that consumes few resources. 
Otherwise it's just More Fun Than You Can Handle.

Weber's Law of Just Noticeable Difference says that stimuli with an
intensity scale, typically require a fixed fraction of proportional
difference, rather than any fixed interval of absolute intensity,
in order for the difference to be noticeable to a human or other
organism.  In other words, we may demand exponential increases
because our *imprecise* brains can't *notice* smaller differences. 
This would suggest that our existing pleasures might already in
effect possess a floating-point representation, with an exponent
and a fraction - the army of actual neurons being used only to
transmit an analog signal most of whose precision is lost.  So we
might be able to get away with using floats, even if we can't get
away with using up-arrows.

But suppose that the inscrutable rules governing the substantiality
of "subjective" pleasure actually require one neuron per hedon, or
something like that.

Or suppose that we
[only choose to reward ourselves](/lw/ww/high_challenge/) when we
find a *better solution,* and that we don't choose to game the
betterness metrics.

And suppose that we don't discard the Weber-Fechner law of "just
noticeable difference", but go on demanding *percentage* annual
improvements, year after year.

Or you might need to improve at a fractional rate
[in order to assimilate your own memories](/lw/wx/complex_novelty/). 
Larger brains would lay down larger memories, and hence need to
grow exponentially - efficiency improvements suiting to
*moderate*the growth, but not to eliminate the exponent.

If fun or intelligence or value can only grow as fast as the mere
*cube*of the brain size... and yet we demand a 2% improvement every
year...

Then 350 years will pass before our resource consumption grows a
single order of magnitude.

And yet there are only around 10^80^ atoms in the observable
universe.

Do the math.

(It works out to a lifespan of around 28,000 years.)

Now... before everyone gets all depressed about this...

We can still hold out a fraction of hope for *real immortality*,
aka "emortality".  As Greg Egan put it, "Not dying after a very
long time.  Just not dying, period."

The laws of physics as we know them prohibit emortality on multiple
grounds.  It is a fair historical observation that, over the course
of previous centuries, civilizations have become able to do things
that previous civilizations called "physically impossible".  This
reflects a change in knowledge about the laws of physics, not a
change in the actual laws; and we cannot do *everything* once
thought to be impossible.  We violate Newton's version of
gravitation, but not conservation of energy.  It's a good
historical bet that the future will be able to do at least *one*
thing our physicists would call impossible.  But you can't bank on
being able to violate any *particular* "law of physics" in the
future.

There is just... a shred of reasonable hope, that our physics might
be *much* more incomplete than we realize, or that we are wrong in
exactly the right way, or that anthropic points I don't understand
might come to our rescue and let us escape these physics (also
*a la* Greg Egan).

So I haven't lost hope.  But I haven't lost despair, either;
*that*would be faith.

In the case where our resources really are limited and there is no
way around it...

...the question of how fast a rate of *continuous improvement*you
demand for an acceptable quality of life - an annual percentage
increase, or a fixed added amount - and the question of *how much*
improvement you can pack into patterns of linearly increasing size
- adding up to the fun-theoretic question of how fast you have to
expand your resource usage over time to lead a life worth
living...

...determines the maximum lifespan of sentient beings.

If you can get by with increasing the size *in bits* of your mind
at a linear rate, then you can last for quite a while.  Until the
end of the universe, in many versions of cosmology.  *And* you can
have a child (or two parents can have two children), and the
children can have children.  Linear brain size growth \* linear
population growth = quadratic growth, and cubic growth at
lightspeed should be physically permissible.

But if you have to grow exponentially, in order for your
ever-larger mind and its ever-larger memories not to end up
uncomfortably squashed into too small a brain - squashed down to a
point, to the point of it being pointless - then a transhuman's
life is measured in subjective eons at best, and more likely
subjective millennia.  Though it would be a merry life indeed.

My own eye has trouble enough looking ahead a mere century or two
of growth.  It's not like I can imagine any sort of *me* the size
of a galaxy.  I just want to live one more day, and tomorrow I will
still want to live one more day.  The part about "wanting to live
forever" is just an induction on the positive integers, not an
instantaneous vision whose desire spans eternity.

If I can see to the fulfillment of all my present self's goals that
I can concretely envision, shouldn't that be enough for me?  And my
century-older self will also be able to see that far ahead.  And so
on through thousands of generations of selfhood until some distant
figure the size of a galaxy has to depart the physics we know, one
way or the other...  Should that be *scary?*

Yeah, I hope like hell that emortality is possible.

Failing that, I'd at least like to find out one way or the other,
so I can get on with my life instead of having that lingering
uncertainty.

For now, one of the reasons
[I care about people alive today](/lw/ws/for_the_people_who_are_still_alive/)
is the thought that if creating new people just divides up a finite
pool of resource available *here*, but we live in a Big World where
there are plenty of people *elsewhere*with their own resources...
then we might not want to create so many new people *here*.  Six
billion now, six trillion at the end of time?  Though this is more
an idiom of linear growth than exponential - with exponential
growth, a factor of 10 fewer people just buys you another 350 years
of lifespan per person, or whatever.

But I do hope for emortality.  Odd, isn't it?  How abstract should
a hope or fear have to be, before a human can stop thinking about
it?

Oh, and finally - there's an idea in the literature of hedonic
psychology called the "hedonic set point", based on identical twin
studies showing that identical twins raised apart have highly
similar happiness levels, more so than fraternal twins raised
together, people in similar life circumstances, etcetera.  There
are things that do seem to shift your set point, but not much (and
permanent downward shift happens more easily than permanent upward
shift, what a surprise).  Some studies have suggested that up to
80% of the variance in happiness is due to genes, or something
shared between identical twins in different environments at any
rate.

If *no*environmental improvement ever has much effect on subjective
well-being, the way you are now, because you've got a more or less
genetically set level of happiness that you drift back to, then...

Well, my usual heuristic is to imagine messing with environments
before I imagine messing with minds.

But in this case?  Screw that.  That's just *stupid.*  Delete it
without a qualm.
