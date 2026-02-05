---
workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- sequences and series
- geometric sequence
- financial literacy
is_finished: true
---
# Pyramid Scheme

Imagine that someone, claiming to represent an investment company, offers you a quick way to multiply your money. The only thing you need to do is persuade three of your friends to invest as well. In reality, however, your money will not be used to purchase gold or stocks. Instead, it will be divided among the people who joined the company before you.  

If you manage to convince three friends, you will receive a share of their money, and also from the people they recruit — until the entire system collapses due to a lack of new investors and the company’s owner mysteriously flies off to the Bahamas. It should be noted that situations like this usually do not benefit friendships.

You have just fallen for one of the most widespread fraudulent business models — a *pyramid scheme*.

![Pyramid Scheme](pyramida.png)

### Assignment

The founder of the company (the first level of the pyramid) recruits three investors (the second level of the pyramid) and collects a fixed entry fee of $20\,000\,\text{CZK}$ from each of them. Each of these three investors must then recruit three new investors (the third level of the pyramid) and again collect an entry fee of $20\,000\,\text{CZK}$ from each. The same process continues at the following levels.  

For simplicity, we assume that recruitment for a new level begins only after the previous level has been completely filled. For example, recruitment into the fourth level begins only after all nine investors in the third level have joined.

The entry fee paid by each new member is distributed among the existing participants as follows: $6\,000\,\text{CZK}$ goes to person A, who recruited the new member; $1\,000\,\text{CZK}$ goes to person B, who recruited person A; another $1\,000\,\text{CZK}$ goes to person C, who recruited person B; another $1\,000\,\text{CZK}$ goes to person D, who recruited person C; and so on, until the entire entry fee has been distributed. If the distribution reaches the founder of the company, the founder receives the remaining amount.

> **Task 1.**  
> When does a newly joined participant recover the money paid as the entry fee?

\iffalse

*Solution.* A newly joined participant pays an entry fee of $20\,000\,\text{CZK}$. To recover this amount, they must recruit three new members (from whom they receive a total of $18\,000\,\text{CZK}$), and these members must collectively recruit at least two additional members (from whom the participant receives the remaining $2\,000\,\text{CZK}$).

\fi

> **Task 2.**  
> At a certain level of the pyramid, it happens for the first time that the founder of the company receives no money from the entry fees of new members.
>
> 1. At which level of the pyramid are these new members?  
> 2. How many people are in the entire pyramid after this level has been filled? Compare this number with the population of your school or your town.  
> 3. Determine the percentage of people who are at a loss after this level has been filled.

\iffalse

*Solution.*

*Solution to part 2.1.* If the founder of the company receives no money for the first time from the entry fee of a newly joined member, this means that there are $16$ levels above this member ($6\,000\,\text{CZK}$ goes to the person one level above, $14 \cdot 1\,000\,\text{CZK}$ goes to people in the next fourteen higher levels, and the founder in the first level receives nothing). Therefore, the newly joined member is at the $17$th level.

*Solution to part 2.2.* The number of people at each level forms a geometric sequence with first term $a_1 = 1$ and common ratio $q = 3$.  

The total number of people in a pyramid with seventeen levels is the sum of the first seventeen terms of this sequence. Recall that the sum of the first $n$ terms of a geometric sequence is given by

$$
\tag{1}
 s_n = a_1 \cdot \frac{q^n - 1}{q - 1}.
$$

In our case ($a_1 = 1$, $q = 3$, and $n = 17$), we obtain

$$
s_{17} = 1 \cdot \frac{3^{17} - 1}{3 - 1} = 64\,570\,081.
$$

We see that the scheme would require the entire population of a larger country (approximately the population of France).

*Solution to part 2.3.* From Task 1 it follows that the loss-making part of the pyramid consists of the last two levels. The number of people at a loss is therefore equal to the sum of the sixteenth and seventeenth terms of the geometric sequence:

$$
a_{16} + a_{17} = 3^{15} + 3^{16} = 57\,395\,628.
$$

Now we determine the percentage of people at a loss:

$$
P = 100 \cdot \frac{57\,395\,628}{64\,570\,081} \doteq 88.89\,\%.
$$

\fi

Pyramid schemes, also known as airplane games, have a long and unfortunately dark history in the Czech Republic. One of the most well-known cases is the Avalanche affair (2000–2006), in which managers of a certain company, promising high returns, collected over $400$ million CZK from nearly $6\,000$ investors. The money was used to pay earlier participants from the contributions of new ones — the classic principle of a pyramid scheme — which later collapsed.

> **Task 3.**  
> In real cases in the Czech Republic, the number of participants was typically in the thousands. In this task, assume that after filling a certain level, the total number of participants in our pyramid is between $3\,000$ and $4\,000$.
>
> 1. Which level is it?  
> 2. Determine the percentage of people who are at a loss at this stage.  
> 3. Determine the total profit of the founder of the company.  
> 4. Determine the total profit of an investor at the second level of the pyramid.  
> 5. What percentage of all collected entry fees will be paid to the people in the first three levels of the pyramid?

\iffalse

*Solution.*

*Solution to part 3.1.* The problem can be solved by testing natural numbers in the formula for the sum of the first $n$ terms of a geometric sequence. Here we present a solution using exponential inequalities. According to the assignment,

$$
3\,000 \leq s_n \leq 4\,000.
$$

Substituting $a_1 = 1$ and $q = 3$ into formula (1), we obtain

$$
3\,000 \leq \frac{3^n - 1}{2} \leq 4\,000,
$$

$$
6\,001 \leq 3^n \leq 8\,001,
$$

$$
\log_3 6\,001 \leq n \leq \log_3 8\,001.
$$

Since
$\log_3 6\,001 \doteq 7.92$ and $\log_3 8\,001 \doteq 8.18$,
the pyramid has eight levels (by substituting into $s_8$, we verify that the total number of people is $3\,280$).

*Solution to part 3.2.* The loss-making part again consists of the last two levels. Similarly to Task 2.3, the number of people at a loss is

$$
a_7 + a_8 = 3^6 + 3^7 = 2\,916.
$$

We determine the percentage:

$$
P' = 100 \cdot \frac{2\,916}{3\,280} \doteq 88.90\,\%.
$$

We may notice that the result differs only slightly from the result in Task 2.3, even though the numbers of people considered are of different orders of magnitude.

*Solution to part 3.3.* The founder receives the full entry fee ($20\,000\,\text{CZK}$) from each person at the second level, $14\,000\,\text{CZK}$ from each person at the third level, $13\,000\,\text{CZK}$ from each person at the fourth level, and so on. Since the pyramid now has eight levels, the total profit $Z_1$ of the founder is

$$
Z_1 = 3 \cdot 20\,000 + 3^2 \cdot 14\,000 + 3^3 \cdot 13\,000 + \cdots + 3^7 \cdot 9\,000 = 31\,155\,000\,\text{CZK}.
$$

*Solution to part 3.4.* For clarity, we illustrate the situation of an investor at the second level in a diagram. The red investor at the second level receives $6\,000\,\text{CZK}$ from each of the three blue investors at the third level. These three investors then recruit additional participants into the scheme, and from each green participant the red investor receives $1\,000\,\text{CZK}$. Similarly, the red investor receives $1\,000\,\text{CZK}$ from participants recruited by the green investors and from all other participants in “their” branch of the pyramid.

![Illustration for Task 3.4](pyramida2.png)

Now we determine the profit $Z_2$ of the red investor. The number of people from whom they receive $1\,000\,\text{CZK}$ equals

$$
3^2 + 3^3 + 3^4 + 3^5 + 3^6
$$

(the pyramid has eight levels). We must also subtract the entry fee. Therefore,

$$
Z_2 = 3 \cdot 6\,000 + (3^2 + 3^3 + 3^4 + 3^5 + 3^6) \cdot 1\,000 - 20\,000 = 1\,087\,000\,\text{CZK}.
$$

*Solution to part 3.5.* From part 3.1 we know that the pyramid contains $3\,280$ people in total; everyone except the founder paid an entry fee of $20\,000\,\text{CZK}$. Therefore, the total amount $S$ of collected money is

$$
S = 3\,279 \cdot 20\,000 = 65\,580\,000\,\text{CZK}.
$$

From parts 3.3 and 3.4 we know the profit of the founder and of an investor at the second level. We now compute the profit $Z_3$ of an investor at the third level (similarly to part 3.4):

$$
Z_3 = 3 \cdot 6\,000 + (3^2 + 3^3 + 3^4 + 3^5) \cdot 1\,000 - 20\,000 = 358\,000\,\text{CZK}.
$$

We can now determine the percentage of funds paid to participants in the first three levels (where $S$ is the total collected amount):

$$
P'' = 100 \cdot \frac{Z_1 + 3 \cdot Z_2 + 9 \cdot Z_3}{S}
= 100 \cdot \frac{37\,638\,000}{65\,580\,000}
\doteq 57.39\,\%.
$$

For better understanding, it is important to realize that this share of the total “company revenue” is paid to only $13$ people out of $3\,280$. Approximately $0.4\,\%$ of the participants receive more than half of the collected money. It is therefore not surprising that pyramid schemes are banned as a business model in many countries around the world.

\fi

> **Task 4.**  
> Think about why, in Tasks 2.3 and 3.2, the percentage of people at a loss turned out to be almost the same. Was this merely a coincidence, or would we obtain a similar result for other numbers of pyramid levels?

\iffalse

*Solution.*  
Suppose the pyramid has $n$ (fully filled) levels and assume that $n \geq 3$. According to formula (1), the total number of participants is

$$
s_n = \frac{3^n - 1}{2}.
$$

The people at a loss are exactly those in the last two levels. Their number is

$$
z_n = 3^{n-2} + 3^{n-1},
$$

since there are $3^{k-1}$ people at the $k$th level. The proportion of people at a loss is therefore

$$
P_n = \frac{z_n}{s_n}
= \frac{3^{n-2} + 3^{n-1}}{\frac{3^n - 1}{2}}
= \frac{3^n \left(\frac{1}{9} + \frac{1}{3}\right)}{\frac{1}{2}(3^n - 1)}
= \frac{\frac{4}{9} \cdot 3^n}{\frac{1}{2}(3^n - 1)}
= \frac{8}{9} \cdot \frac{3^n}{3^n - 1}
= \frac{8}{9} \cdot \frac{1}{1 - 3^{-n}}.
$$

For large $n$, the expression $3^{-n}$ is negligibly small, and therefore the factor $\frac{1}{1 - 3^{-n}}$ is close to $1$. This means that

$$
P_n \doteq \frac{8}{9} = 0.\overline{8}.
$$

\fi

### Questions for Reflection (without calculations)

* Why does a pyramid scheme fail, even though it promises quick profit at the beginning? How is the growth in the number of investors related to real population limits?  

* How would the risk of loss change if you involved relatives or friends in the scheme? What impact could this have on personal relationships?  

* Why are pyramid schemes banned in most countries?  

* Imagine a pyramid scheme today (for example, online). How would you warn others, and what would you do if you were approached?  

* Is a pyramid scheme purely a fraud, or do legal forms of multi-level marketing (MLM) exist? Do you know the term MLM? In MLM, a distributor earns money from selling real products (e.g., Avon, Herbalife, Amway) and from commissions on sales within their network — how does this differ from a pyramid scheme, and why is it legal?

### References

* Yates K. (2021). *Mathematics for Life*. Prague: Kniha Zlín.

* Illinois Attorney General. *Pyramid schemes* [online]. Available at  
<https://ag.state.il.us/consumers/pyramid.html> [accessed June 1, 2023].
