
# How Much Evidence Does It Take?

[Previously](/lw/jl/what_is_evidence/), I defined *evidence* as "an
event entangled, by links of cause and effect, with whatever you
want to know about", and *entangled* as "happening differently for
different possible states of the target".  So how much entanglement
- how much evidence - is required to support a belief?

Let's start with a question simple enough to be mathematical: how
hard would you have to entangle yourself with the
[lottery](/lw/hl/lotteries_a_waste_of_hope/) in order to win? 
Suppose there are seventy balls, drawn without replacement, and six
numbers to match for the win.  Then there are 131,115,985 possible
winning combinations, hence a randomly selected ticket would have a
1/131,115,985 probability of winning (0.0000007%).  To win the
lottery, you would need evidence *selective* enough to visibly
favor one combination over 131,115,984 alternatives.

Suppose there are some tests you can perform which discriminate,
probabilistically, between winning and losing lottery numbers.  For
example, you can punch a combination into a little black box that
always beeps if the combination is the winner, and has only a 1/4
(25%) chance of beeping if the combination is wrong.  In
[Bayesian](http://yudkowsky.net/bayes/bayes.html) terms, we would
say the *likelihood ratio* is 4 to 1.  This means that the box is 4
times as likely to beep when we punch in a correct combination,
compared to how likely it is to beep for an incorrect combination.

There are still a whole lot of possible combinations.  If you punch
in 20 incorrect combinations, the box will beep on 5 of them by
sheer chance (on average).  If you punch in all 131,115,985
possible combinations, then while the box is certain to beep for
the one winning combination, it will also beep for 32,778,996
losing combinations (on average).

So this box doesn't let you win the lottery, but it's better than
nothing.  If you used the box, your odds of winning would go from 1
in 131,115,985 to 1 in 32,778,997.  You've made some progress
toward finding your target, the truth, within the huge space of
possibilities.

Suppose you can use another black box to test combinations *twice,*
*independently.*  Both boxes are certain to beep for the winning
ticket.  But the chance of a box beeping for a losing combination
is 1/4 *independently* for each box; hence the chance of *both*
boxes beeping for a losing combination is 1/16.  We can say that
the *cumulative* evidence, of two independent tests, has a
likelihood ratio of 16:1.  The number of losing lottery tickets
that pass both tests will be (on average) 8,194,749.

Since there are 131,115,985 possible lottery tickets, you might
guess that you need evidence whose strength is around 131,115,985
to 1 - an event, or series of events, which is 131,115,985 times
more likely to happen for a winning combination than a losing
combination.  Actually, this amount of evidence would only be
enough to give you an *even* chance of winning the lottery.  Why? 
Because if you apply a filter of that power to 131 million losing
tickets, there will be, on average, one losing ticket that passes
the filter.  The winning ticket will also pass the filter.  So
you'll be left with two tickets that passed the filter, only one of
them a winner.  50% odds of winning, if you can only buy one
ticket.

A better way of viewing the problem:  In the beginning, there is 1
winning ticket and 131,115,984 losing tickets, so your odds of
winning are 1:131,115,984.  If you use a single box, the odds of it
beeping are 1 for a winning ticket and 0.25 for a losing ticket. 
So we multiply 1:131,115,984 by 1:0.25 and get 1:32,778,996. 
Adding another box of evidence multiplies the odds by 1:0.25 again,
so now the odds are 1 winning ticket to 8,194,749 losing tickets.

It is convenient to measure evidence in bits - not like bits on a
hard drive, but mathematician's bits, which are conceptually
different.  Mathematician's bits are the logarithms, base 1/2, of
probabilities.  For example, if there are four possible outcomes A,
B, C, and D, whose probabilities are 50%, 25%, 12.5%, and 12.5%,
and I tell you the outcome was "D", then I have transmitted three
bits of information to you, because I informed you of an outcome
whose probability was 1/8.

It so happens that 131,115,984 is slightly less than 2 to the 27th
power.  So 14 boxes or 28 bits of evidence - an event 268,435,456:1
times more likely to happen if the ticket-hypothesis is true than
if it is false - would shift the odds from 1:131,115,984 to
268,435,456:131,115,984, which reduces to 2:1.  Odds of 2 to 1 mean
two chances to win for each chance to lose, so the *probability* of
winning with 28 bits of evidence is 2/3.  Adding another box,
another 2 bits of evidence, would take the odds to 8:1.  Adding yet
another two boxes would take the chance of winning to 128:1.

So if you want to license a *strong belief* that you will win the
lottery - arbitrarily defined as less than a 1% probability of
being wrong - 34 bits of evidence about the winning combination
should do the trick.

In general, the rules for weighing "how much evidence it takes"
follow a similar pattern:  The larger the *space of possibilities*
in which the hypothesis lies, or the more unlikely the hypothesis
seems *a priori* compared to its neighbors, or the more confident
you wish to be, the more evidence you need.

You cannot defy the rules; you cannot form accurate beliefs based
on inadequate evidence.  Let's say you've got 10 boxes lined up in
a row, and you start punching combinations into the boxes.  You
cannot stop on the first combination that gets beeps from all 10
boxes, saying, "But the odds of that happening for a losing
combination are a million to one!  I'll just ignore those
ivory-tower Bayesian rules and stop here."  On average, 131 losing
tickets will pass such a test for every winner.  Considering the
space of possibilities and the prior improbability, you jumped to a
too-strong conclusion based on insufficient evidence.  That's not a
pointless bureaucratic regulation, it's math.

Of course, you can still *believe* based on inadequate evidence, if
that is your whim; but you will not be able to believe
*accurately. *It is like trying to drive your car without any fuel,
because you don't believe in the silly-dilly fuddy-duddy concept
that it ought to take fuel to go places.  It would be so much more
*fun,* and so much less expensive, if we just decided to repeal the
law that cars need fuel.  Isn't it just obviously better for
everyone?  Well, you can try, if that is your whim.  You can even
shut your eyes and pretend the car is moving.  But to *really*
arrive at accurate beliefs requires evidence-fuel, and the further
you want to go, the more fuel you need.
