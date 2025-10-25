---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- sequences and series
- probability
- expected value
- geometric sequence
is_finished: true
remark: Note for translators. Instead of the amount in CZK, you can enter the currency
  of your country, or some reasonable currency. You can also come up with your own
  names for the lottery tickets.
---

# Which Lottery Ticket Is More Profitable?

In life we very often encounter situations that involve chance and probability. 
Imagine being faced with a choice between several options—for example, when choosing a lottery ticket or investing in a project. 
Each choice has its risks and potential rewards, but how can we determine which one is the most advantageous? 
This is where the so-called *expected value* comes into play.

Expected value tells us the average outcome we can anticipate when choosing a particular option. 
It helps us better estimate which option is likely to pay off in the long run. 
It is not an exact prediction, but a tool that allows us to better understand risk and reward, both in simple games and in real life decisions.

Let's consider two lottery tickets, for example:

* Ticket A: It costs 10 CZK and has a $0{.}1$ probability of winning 100 CZK; otherwise, it wins nothing.
* Ticket B: It costs 10 CZK and has a $0{.}2$ probability of winning 60 CZK; otherwise, it wins nothing.

For ticket A, we expect that if we buy 10 tickets, one of them will win 100 CZK while the reaming nine will win nothing. 
Therefore, we can expect that each lottery ticket will yield an average return of 10 CZK.

Similarly, for lottery ticket B, we expect that if we buy 10 tickets, two of them will win 60 CZK and eight will win nothing. 
We can therefore expect each lottery ticket to yield an average return of 12 CZK.

This shows that ticket B is the better option.

## Expected Value

The average win we just calculated is called the *expected value*.

In general, we can say that for a random variable $X$ that takes on finitely many values $x_1,\,\dots,\,x_k$ with probabilities $p_1,\,\dots,\,p_k$, 
we calculate its expected value using this formula:

$$
EV=\sum_{i=1}^k x_ip_i.
$$

## Which Lottery Ticket Is the Best?

Let's take a look at three lottery tickets. 
The 50 CZK Black Pearl ticket, the 100 CZK Black Pearl ticket and the Rental King lottery ticket worth 50 CZK. 

The prize structure for the 50 CZK Black Pearl lottery tickets, of which there are 13,000,000 in total, is as follows. 

| Prize amount (in CZK) | Number of winning tickets | 
| ------------- | ------------- |  
| $50$  | $1{,}820{,}000$  |
| $100$  | $1\,040{,}000$  |
| $150$  | $260{,}000$  |
| $200$  | $130{,}000$  |
| $300$  | $130{,}000$  |
| $500$  | $104{,}000$  |
| $1{,}000$  | $5{,}550$  |
| $2{,}000$  | $2{,}300$  |
| $4{,}000$  | $480$  |
| $10{,}000$  | $185$  |
| $20{,}000$  | $84$  |
| $100{,}000$  | $14$  |
| $1{,}500{,}000$  | $6$  |
| Total | $3{,}492{,}619$  |

The prize structure for the 100 CZK Black Pearl lottery ticket looks similar, with a total of $15{,}000{,}000$ issued tickets.

| Prize amount (in CZK) | Number of winning tickets | 
| ------------- | ------------- |  
| $100$  | $2{,}400{,}000$  |
| $200$  | $900{,}000$  |
| $300$  | $450{,}000$  |
| $500$  | $150{,}000$  |
| $600$  | $150{,}000$  |
| $900$  | $75{,}000$  |
| $1{,}000$  | $75{,}000$  |
| $1{,}500$  | $20{,}000$  |
| $6{,}000$  | $4{,}000$  |
| $20{,}000$  | $185$  |
| $50{,}000$  | $84$  |
| $100{,}000$  | $30$  |
| $200{,}000$  | $13$  |
| $5{,}000{,}000$  | $6$  |
| Total | $4{,}224{,}318$  |

Last but not least, let's take a look at the Rental King lottery ticket, 
with a total of $8{,}000{,}000$ tickets issued. The prizes are shown in the table below.

| Prize amount (in CZK) | Number of winning tickets | 
| ------------- | ------------- |  
| $50$  | $960{,}000$  |
| $100$  | $720{,}000$  |
| $150$  | $160{,}000$  |
| $250$  | $160{,}000$  |
| $500$  | $70{,}000$  |
| $1{,}000$  | $1{,}300$  |
| $2{,}000$  | $500$  |
| $5{,}000$  | $160$  |
| $10{,}000$  | $80$  |
| $100{,}000$  | $6$  |
| $3{,}500{,}000$  | $3$  |
| Total | $2{,}072{,}049$  |

The top prize of $3{,}500{,}000\,\text{CZK}$ is not paid at once, but consists of an immediate prize of $500{,}000\,\text{CZK}$ 
and an annuity of $50{,}000\,\text{CZK}$ for 5 years.

> **Exercise 1.** Which ticket has the highest chance of winning?

\iffalse

*Solution.* In the case of the 50 CZK Black Pearl ticket, there are $3{,}492{,}619$ winning tickets 
out of the total number of $13{,}000{,}000$ (see the last row of the table).
The probability that a randomly selected ticket is a winning one can be calculated as

$$
P(V_1)=\frac{3{,}492{,}619}{13{,}000{,}000}=0{.}268633.
$$

We can say that if we buy one lottery ticket, we have a chance of winning about $26{.}86\%$. 
By manipulating the fraction, we can also see that the chance of getting a winning lottery ticket is $1\colon 3{.}72$.

Similarly, in the case of the 100 CZK Black Pearl lottery ticket we get
$$
P(V_2)=\frac{4{,}224{,}318}{15{,}000{,}000}=0{.}2816212.
$$
That means that the chance of winning is $28{.}16\%$ or $1\colon 3{.}55$.

In the case of the Rental King ticket, we get
$$
P(V_3)=\frac{2{,}072{,}049}{8{,}000{,}000}=0{.}259,
$$
so the chance of winning is $25{.}9\%$ or $1\colon 3{.}86$.

Comparing the individual probabilities of winning, we find that the highest chance of winning comes with the 100 CZK Black Pearl ticket.

In this context, we can also consider what we mean by a winning ticket.
A ticket is usually considered winning if it yields any amount of money. 
But when we paid 100 CZK for the ticket, then a win of 100 CZK will pay us back, but we haven't actually won anything. 
In order to get the probability of actually winning more than we paid, we won't consider the first row in our winning tables. 
This way we get adjusted winning probabilities
$$
\begin{aligned}
P(V_1)&=\frac{1{,}672{,}619}{13{,}000{,}000}=0{.}128633,\\
P(V_2)&=\frac{1{,}824{,}318}{15{,}000{,}000}=0{.}1216212,\\
P(V_3)&=\frac{1{,}112{,}049}{8{,}000{,}000}=0{.}139.
\end{aligned}
$$
We can see that when we only consider the lottery tickets that return more than their purchase cost, 
the best option is the Rental King lottery ticket that has a $13{.}9\%$ chance of such win.

\fi

> **Exercise 2.** What is the expected value of each ticket?

\iffalse

*Solution.* To calculate the expected value, by definition, we need to know the probabilities of individual wins:

| Prize amount (in CZK) | Winning probability | 
| ------------- | ------------- |  
| $50$  | $0{.}14$  |
| $100$  | $0{.}08$  |
| $150$  | $0{.}02$  |
| $200$  | $0{.}01$  |
| $300$  | $0{.}01$  |
| $500$  | $0{.}008$  |
| $1{,}000$  | $0{.}0004269$  |
| $2{,}000$  | $0{.}000176923$  |
| $4{,}000$  | $0{.}000036923$  |
| $10{,}000$  | $0{.}000014231$  |
| $20{,}000$  | $0{.}000006461538$  |
| $100{,}000$  | $0{.}000006461538$  |
| $1{,}500{,}000$  | $0{.}000000461538$  |

Let the values of individual winnings be denoted by $n_1$ to $n_{13}$ and their corresponding probabilities $p_1$ to $p_{13}$. 
Then, the expected value $EV(L_1)$ of the Black Pearl ticket is

$$
EV(L_1)=\sum_{k=1}^{13}n_kp_k=29\,\text{CZK}.
$$

Given how the individual probabilities are calculated, we can also calculate the expected value as follows:
$$
EV(L_1)=\frac{1}{13{,}000{,}000}\left(50\cdot 1{,}820{,}000+100\cdot1{,}040{,}000+ \cdots + 100{,}000\cdot14+1{,}500{,}000\cdot6 \right).
$$

This approach is more convinient because we don't have to calculate the probability of each possible prize in the table. 
For the 100 CZK Black Pearl ticket, we get the expected value $EV(L_2)$:
$$
EV(L_2)=\frac{1}{15{,}000{,}000}\left(100\cdot 2{,}400{,}000+200\cdot 900{,}000+ \cdots + 200{,}000\cdot 13+5{,}000{,}000 \cdot 6 \right)=64\,\text{CZK}.
$$
And for the Rental King lottery ticket we get the expected value $EV(L_3)$:
$$
EV(L_3)=\frac{1}{8{,}000{,}000}\left(50\cdot 960{,}000+100\cdot 720{,}000+ \cdots + 100{,}000\cdot 6+3{,}500{,}000\cdot 3 \right)=29{.}25\,\text{CZK}.
$$

*Note.* 

* Lotteries usually state the total prize pool and the number of tickets. The expected value is, of course, the ratio of these two numbers.
* The stated values ​​are often even lower in reality, since lottery prizes are usually taxed.
* The same approach can be used to calculate the expected value of a pack of various trading card games (Pokémon, Lorcana, Magic the Gathering or sports cards).

\fi

> **Exercise 3.** In the previous examples, we considered the top prize of the Rental King lottery to be $3{,}500{,}000\,\text{CZK}$.
> But is this really the actual value of the prize, given that it is not paid out all at once? 

\iffalse

*Solution.* The simple answer is that it is not. 

It is important to remember that if we got the money immediately, we could save it or invest it somehow.
To determine the value of $50{,}000\,\text{CZK}$ recieved one month from now, we can use a concept known as *present value*. 
When using this concept, we ask ourselves how much money we would have to invest today to get the amount we want in one month (e.g. considered $50{,}000\,\text{CZK}$). 
This amount is what we call the present value.

Let's suppose we could save the given amount $P_0$ for a month with a monthly interest rate of $0{.}5\%$. 
We would then get $P_1=1{,}005P_0$ after one month. The present value is then the amount $P_0$ that we must deposit so that $P_1$ is $50{,}000\,\text{CZK}$, i.e. 
$$
P_0=\frac{50{,}000}{1{.}005}=49{,}751{.}24\,\text{CZK}.
$$

To determine the present value of an amount to be received in $n$ months, 
we assume that we will keep the given amount deposited for the entire time. 
Using compound interest, we obtain the present value $P_0$ of the amount $P_n$ recieved after $n$ months as follows:
$$
P_0=\frac{P_n}{1{.}005^n}.
$$
Let us recall that the top prize of the Rental King lottery consists of $500{,}000\,\text{CZK}$ and thirty monthly payments of $50{,}000\,\text{CZK}$. 
Considering a monthly interest rate of $0{.}5\,\%$, the present value $PV$ of these payments is
$$
PV=\frac{50{,}000}{1{.}005}+\frac{50{,}000}{1{.}005^2}+\cdots+\frac{50{,}000}{1{.}005^{29}}+\frac{50{,}000}{1{.}005^{30}}.
$$
Notice that this is the sum of the terms of a geometric sequence and thus the calculation can be significantly shortened.
$$
PV=\frac{50{,}000}{1{.}005}\cdot\frac{1-\left(\frac{1}{1{.}005}\right)^{30}}{1-\frac{1}{1{.}005}}=1{,}389{,}702{.}7\,\text{CZK}.
$$
Therefore, we assume that the value of the top prize is only $1{,}889{,}702{.}7\,\text{CZK}$.

When we use this amount to calculate the expected value of the Rental King lottery ticket, we get 
$$
EV(L_3)=28{.}65\,\text{CZK}.
$$

*Note.* Previous considerations were still very simplistic, as they did not include, for example, the effect of inflation.

\fi

> **Exercise 4.** Based on the results of the previous tasks, choose the best lottery ticket.

\iffalse

*Solution.* Based on the previous tasks, we can compare the lottery tickets according to various criteria:

1. By probability of winning.

According to this criterion, the best ticket is the 100 CZK Black Pearl with a $28{.}16\%$ chance of winning, 
followed by the 50 CZK Black Pearl ticket with $26{.}86\%$ a chance of winning and the worst is the Rental King ticket with a chance of winning at $25{.}9\%$.

2. By probability of actual winning.

When we instead consider the chance of winning more than we paid, we get a different ranking. 
The best is the Rental King ticket with a $13{.}9\%$ chance of winning, then the 50 CZK Black Pearl ticket with a $12{.}86\%$ chance of winning 
and the last is the 100 CZK Black Pearl ticket with a $12{.}16\%$ chance of winning.

3. By expected value.

The expected value of the 50 CZK Black Pearl ticket is $29\,\text{CZK}$. On average, we lose $21\,\text{CZK}$ buying one ticket. 
Similarly, the expected value of the 100 CZK Black Pearl ticket is $64\,\text{CZK}$. On average we lose $36\,\text{CZK}$. 
And in the case of the 50 CZK Rental King ticket, the adjusted expected value is $28{.}65\,\text{CZK}$, so on average we lose $21{.}35\,\text{CZK}$.

We can therefore say that, as expected, all of the tickets result in a loss. However, the 50 CZK Black Pearl ticket can be considered the best, since it yields the smallest loss.


\fi

## Literature

* Novák, J., *Střední hodnota v úlohách na střední škole.* Učitel matematiky, 2, JČMF, 2024. 
* *Herní plán loterií SAZKA* [online] Dostupné z https://static.sazka.cz/kentico-media/sazka/media/content/herni-plany/hp-sazka-od-17-7-24-komplet-sazka.pdf, [cit. 1. 9. 2024]
