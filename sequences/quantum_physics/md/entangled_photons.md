
# Entangled Photons

Today we shall analyze the phenomenon of "entangled particles". 
We're going to make heavy use of polarized photons here, so you'd
better have read
[yesterday's post](http://www.overcomingbias.com/2008/05/projection.html).

If a particle at rest decays into two other particles, their *net*
momentum must add up to 0.  The two new particles may have
amplitudes to head off in all directions, but in each *joint*
configuration, the directions will be opposite.

By a similar method you can produce two entangled photons which
head off in opposite directions, and are guaranteed to be polarized
oppositely (at right angles to each other), but with a 50% prior
probability of going through any given polarized filter.

You might think that this would involve amplitudes over a
continuous spectrum of opposite configurations - an amplitude for
photon A to be polarized at 0° and for photon B to be polarized at
90°, an amplitude for A to be 1° polarized and for B to be 91°
polarized, etc.  But in fact it's possible to describe the quantum
state "unknown but opposite polarizations" much more compactly.

First, note that the two photons are heading off in opposite
directions.  This justifies calling one photon A and one photon B;
they aren't likely to get their
[identities](http://www.overcomingbias.com/2008/04/identical-parti.html)
mixed up.

As with yesterday, the polarization state (1 ; 0) is what passes a
90° filter.  The polarization state (0 ; 1) is what passes a 0°
filter.  (1 ; 0) is polarized up-down, (0 ; 1) is polarized
left-right.

If A is in the polarization state (1 ; 0), we'll write that as A=(1
; 0).

If A=(1 ; 0) and B=(0 ; 1), we'll write that as

> [ A=(1 ; 0) ∧ B=(0 ; 1) ]

The state for "unknown opposite polarization" can be written as:

> √(1/2) \* ( [ A=(1 ; 0) ∧ B=(0 ; 1) ] - [ A=(0 ; 1) ∧ B=(1; 0) ] )

Note that both terms are being multiplied by the square root of
1/2.  This ensures that the squared modulus of both terms sums to
1. Also, don't overlook the minus sign in the center, we'll need
it.

If you measure the A photon's polarization in the
up-down/left-right basis, the result is pretty straightforward. 
Your measurement decoheres the entanglement, creating one evolution
out of the A=(1 ; 0) ∧ B=(0 ; 1) configuration, and a second,
noninteracting evolution out of the A=(0 ; 1) ∧ B=(1; 0)
configuration.

If you find that the A photon is polarized up-down, i.e., (1 ; 0),
then you know you're in the A=(1 ; 0) ∧ B=(0 ; 1) blob of
amplitude. So you know that if you or anyone else measures B,
they'll report to you that they found B in the (0 ; 1) or
left-right polarization.  The version of you that finds A=(1 ; 0),
and the version of your friend that finds B=(0 ; 1), always turn
out to live in the same blob of amplitude.

On the other side of
[configuration space](http://www.overcomingbias.com/2008/04/quantum-arena.html),
another version of you finds themselves in the A=(0 ; 1) ∧ B=(1; 0)
blob.  If a friend measures B, the other you will expect to hear
that B was polarized up-down, just as you expect to meet the
version of your friend that measured B left-right.

But what if you measure the system in a slanted basis - test a
photon with a 30° polarized filter?  Given the specified starting
state, in the up-down / left-right basis, what happens if we
measure in the 30° basis instead?  Will we still find the photons
having opposite polarizations?  Can this be demonstrated?

Yes, but the math gets a little more interesting.

Let's review, from yesterday, the case where a photon previously
polarized in the up-down/left-right basis encounters a 30° filter.

[![Polar3060](http://lesswrong.com/static/imported/2008/05/02/polar3060.png "Polar3060")](http://lesswrong.com/static/imported/2008/05/02/polar3060.png)
A 30-60-90 triangle has a hypotenuse of 1, a small side of 1/2, and
a longer side of (√3)/2, in accordance with the Pythagorean
Theorem.

If a photon passes a 0° filter, coming out with polarization (0 ;
1), and then encounters another filter at 30°, the vector that
would be *transmitted*through the 30° filter is

> (√3)/2 \* (1/2 ; (√3)/2) = (.433 ; .75)

and the polarization vector that would be *absorbed* is

> 1/2 \* (-(√3)/2 ; 1/2) = (-.433 ; .25)

Note that the polarization states (1/2 ; (√3)/2) and (-(√3)/2 ;
1/2) form an *orthonormal basis:*  The
[inner product](http://plato.stanford.edu/entries/qm/#VecVecSpa) of
each vector with itself is 1, and the inner product of the two
vectors with each other is 0.

Then we had (√3)/2 of one basis vector plus 1/2 of the other,
guaranteeing the squared moduli would sum to 1.  ((√3)/2)^2^  +
(1/2)^2^  = 3/4 + 1/4 = 1.

So we can say that in the 30° basis, the incoming (0 ; 1) photon
had a (√3)/2 amplitude to be transmitted, and a 1/2 amplitude to be
absorbed.

Symmetrically, suppose a photon had passed a 90° filter, coming out
with polarization (1 ; 0), and then encountered the same 30°
filter.  Then the transmitted vector would be

> 1/2 \* (1/2 ; (√3)/2) = (.25 ; .433)

and the absorbed vector would be

> -(√3)/2 \* (-(√3)/2 ; 1/2) = (.75 ; -.433)

Now let's consider again with the entangled pair of photons

> √(1/2) \* ( [ A=(1 ; 0) ∧ B=(0 ; 1) ] - [ A=(0 ; 1) ∧ B=(1; 0) ] )

and measure photon A with a 30° filter.

Suppose we find that we see photon A absorbed.

Then we know that there was a -(√3)/2 amplitude for this event to
occur if the original state had A=(1 ; 0), and a 1/2 amplitude for
this event to occur if the original state had A=(0 ; 1).

So, if we see that photon A is absorbed, we learn that *we* are in
the now-decoherent blob of amplitude:

> ( -(√3)/2 \* √(1/2) \* [ A=(-(√3)/2 ; 1/2) ∧ B=(0 ; 1) ] )  
> - ( 1/2 \* √(1/2) \* [ A=(-(√3)/2 ; 1/2) ∧ B=(1; 0) ] )

You might be tempted to add the two amplitudes for A being absorbed
- the -(√3)/2 \* √(1/2) and the -1/2 \* √(1/2) - and get a total
amplitude of -.966, which, squared, comes out as .933.

But if this were true, there would be a 93% prior probability of A
being absorbed by the filter - a huge prior expectation to see it
absorbed.  There should be a 50% prior chance of seeing A
absorbed.

What went wrong is that, even though we haven't yet measured B, the
configurations with B=(0 ; 1) and B=(1 ; 0) are
[distinct](http://www.overcomingbias.com/2008/04/distinct-config.html).
B could be light-years away, and unknown to us; the configurations
would still be distinct.  So we don't add the amplitudes for the
two terms; we keep them separate.

When the amplitudes for the terms are *separately* squared, and the
squares added together, we get a prior absorption probability of
1/2 - which is exactly what we should expect.

Okay, so we're in the decoherent blob where A is absorbed by a 30°
filter.  Now consider what happens over at B, within our blob, if a
friend measures B with another 30° filter.

The new starting amplitude distribution is:

> ( -(√3)/2 \* √(1/2) \* [ A=(-(√3)/2 ; 1/2) ∧ B=(0 ; 1) ] )  
> - ( 1/2 \* √(1/2) \* [ A=(-(√3)/2 ; 1/2) ∧ B=(1; 0) ] )

In the case where B=(0 ; 1), it has an amplitude of (√3)/2 to be
transmitted through a 30° filter; being transmitted through a 30°
filter corresponds to the polarization state (1/2 ; (√3)/2). 
Likewise, a 1/2 amplitude to be absorbed (polarization state
(-(√3)/2 ; 1/2).)

In the case where B=(1 ; 0) it has an amplitude of 1/2 to be
transmitted with state (1/2 ; (√3)/2).  And an amplitude of -(√3)/2
to occupy the state (-(√3)/2 ; 1/2) and be absorbed.

So add up four terms:

> ( -(√3)/2 \* √(1/2) ) \* [ A=(-(√3)/2 ; 1/2) ∧ B=(0 ; 1) ]   
> *  breaks down into*  
>     ( -(√3)/2 \* √(1/2) ) \* (√3)/2 \* [ A=(-(√3)/2 ; 1/2) ∧ B=(1/2
> ; (√3)/2) ] +  
>     ( -(√3)/2 \* √(1/2) ) \* 1/2     \* [ A=(-(√3)/2 ; 1/2) ∧
> B=(-(√3)/2 ; 1/2) ]  
> *and*  
> - ( 1/2 \* √(1/2) ) \* [ A=(-(√3)/2 ; 1/2) ∧ B=(1; 0) ] )  
> *   breaks down into*  
>     - ( 1/2 \* √(1/2) ) \*  1/2      \* [ A=(-(√3)/2 ; 1/2) ∧
> B=(1/2 ; (√3)/2) ] +  
>     - ( 1/2 \* √(1/2) ) \* -(√3)/2 \* [ A=(-(√3)/2 ; 1/2) ∧
> B=(-(√3)/2 ; 1/2) ]

These four terms occupy only two distinct configurations.

Adding the amplitudes, the configuration [ A=(-(√3)/2 ; 1/2) ∧
B=(-(√3)/2 ; 1/2) ] ends up with zero amplitude, while [ A=(-(√3)/2
; 1/2) ∧ B=(1/2 ; (√3)/2) ] ends up with a final amplitude of
√(1/2).

So, within the blob in which you've found yourself, the probability
of your friend seeing that a 30° filter blocks both A and B, is 0. 
The probability of seeing that a 30° filter blocks A and transmits
B, is 50%.

Symmetrically, there's another blob of amplitude where your other
self sees A transmitted and B blocked, with probability 50%.  And A
transmitted and B transmitted, with probability 0%.

So you and your friend, when you compare results in some particular
blob of decohered amplitude, always find that the two photons have
opposite polarization.

And in general, if you use two equally oriented polarization
filters to measure a pair of photons in the inital state:

> √(1/2) \* ( [ A=(1 ; 0) ∧ B=(0 ; 1) ] - [ A=(0 ; 1) ∧ B=(1; 0) ] )

then you are guaranteed that one filter will transmit, and the
other filter absorb - regardless of how you set the filters, so
long as you use the same setting.  The photons *always* have
opposite polarizations, even though the prior probability of any
*particular* photon having a *particular* polarization is 50%.

What if I measure one photon with a 0° filter, and find that it is
transmitted (= state (0 ; 1)), and then I measure the other photon
with a 30° filter?

The probability works out to just the same as if I knew the other
photon had state (1 ; 0) - in effect, it now does.

Over on my side, I've decohered the amplitude over the *joint*
distribution, into blobs in which A has been transmitted, and A
absorbed.  I am in the decoherent blob with A transmitted:  A=(0 ;
1). Ergo, the amplitude vector / polarization state of B,
*in my blob,* behaves as if it starts out as (1 ; 0).  This is just
as true whether I measure it with another 0° filter, or a 30°
filter.

With symmetrically entangled particles, each particle *seems* to
know the state the other particle has been measured in.  But
"seems" is the operative word here.  Actually we're just dealing
with decoherence that happens to take place in a very symmetrical
way.

Tomorrow (if all goes according to plan) we'll look at Bell's
Theorem, which rules out the possibility that each photon already
has a fixed, non-quantum state that locally determines the result
of any possible polarization measurement.
