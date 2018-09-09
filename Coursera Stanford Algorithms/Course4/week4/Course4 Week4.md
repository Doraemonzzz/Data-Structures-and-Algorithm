## Course4 Week4 

这一周的内容主要介绍了Local Search，讲解了Maximum Cut Problem以及2-SAT Problem，下面回顾下。



### Part 1: Local Search

在介绍Local Search之前，老师先介绍了Maximum Cut Problem，这个问题是一个NP完全问题，暂时还无法在多项式时间内解出。



#### Maximum Cut Problem

输入：无向图$G =（V,E）$。
目标：一种分割方法 $(A,B)$，将所有顶点分割成两群，同时使交叉边数量最大。

直接看定义还是有点抽象的，这里来看一个例子。



##### Quiz

下图的最大割是多少？

![](https://github.com/Doraemonzzz/md-photo/blob/master/Coursera%20Stanford%20Algorithms/Part4%20np-completeness/week4/2018062601.png?raw=true)

A) 4 

B) 6 

C) 8 

D) 10    

答案为C，按照图中的分法即可。



在介绍算法之前，定义两个符号。

##### 符号定义    

对于分割方法方法$(A,B)$和顶点$v$，定义

$c_v(A,B)= v$的边中穿越$(A,B)$的数量
$d_v(A,B)=v$的边中不穿越$(A,B)$的数量



有了定义就可以介绍算法了

##### Local search algorithm

（1）令$(A, B) $为$G$的任意切割。
（2）当有一个顶点$v$ 满足$d_v(A,B)> c_v(A,B)$：

- 将$v$移到切割的另一侧
  [关键点：通过$d_v(A,B)-c_v(A,B)>0$]增加交叉边的数量

（3）返回最终切割$(A, B) $



##### 分析

先看下这个算法的时间。这里假设没有平行边，所以最多有$C_n^2$条边，由(2)我们知道每次至少增加一条交叉边，所以最多迭代$C_n^2$次，因为交叉边数量每次至少增加$1$，而最多的交叉边数量为$C_n^2$。



再来看下算法的性能，这里给出一个定理。

定理：这个本地搜索算法总是输出一个切割，其中交叉边的数量至少为$50\%$的最大值（实际上至少为$|E|$的$50\%$）

证明：设$(A,B)$为局部最优割，那么对每个点$v$，$d_v(A,B)\le c_v(A,B)$，将这个式子关于每个点求和可得
$$
\sum_{v\in V}d_v(A,B)\le\sum_{v\in V} c_v(A,B)
$$
$\sum_{v\in V}d_v(A,B)$非交叉边数量的两倍，$\sum_{v\in V} c_v(A,B)$为交叉边数量的两倍，所以
$$
2|E|=\sum_{v\in V}d_v(A,B)+\sum_{v\in V} c_v(A,B) \\
2|E|\le \sum_{v\in V}c_v(A,B)+\sum_{v\in V} c_v(A,B)\\
\frac 1 2 \sum_{v\in V}c_v(A,B)\ge  \frac 1 2 |E|
$$
$\frac 1 2 \sum_{v\in V}c_v(A,B)$为交叉边数量，所以结论成立。



通过这个例子初步了解了Local search algorithm，下面更具体地介绍一下。

#### Principles of Local Search    

##### Neighborhoods

令$X=$一组候选的解决方案，Local Search算法的核心点是定义**Neighborhoods**，不同的**Neighborhoods**会有完全不同的结果，在上一个问题中，$x,y$是邻居等价于可以通过移动一个顶点将$x$变为$y$。



再来看一下算法的一般形式。

#####  A Generic Local Search Algorithm    

（1）令$x =$某个初始解。
（2）当前的解决方案$x$有一个更优的邻居解决方案$y$，令$x= y$
（3）返回最终（局部最优）解$x$



在介绍2-SAT Problem之前，需要做一些准备工作，先介绍随机游走。

#### Random Walks    

在时间$0$时位于位置$0$，在每个时间点，你的位置增加或减少$1$，各有$50\%$的可能性。

![](https://github.com/Doraemonzzz/md-photo/blob/master/Coursera%20Stanford%20Algorithms/Part4%20np-completeness/week4/2018062602.png?raw=true)

对于随机游走的问题，我们比较关注的是走到某一个位置需要走的步数，因此令$T_n =$随机游走到位置$n$的步数，我们来看一个Quiz。



##### Quiz

$E[T_n]$是多少?

A) Θ(n) 

B) $Θ(n^2) $

C) $Θ(n^3) $

D) $Θ(2^n) $  

这题答案是B，具体证明见后面一个部分。



##### Analysis of $T_n$    

为了计算$E[T_n]$，我们考虑另一个随机变量，令$Z_i =$从$i$随机游走到$n$的步数。(注意$Z_0 = T_n$）

考虑递推关系，而对于$i=0,n$，显然有
$$
E[Z_n]=0,E[z_1]=1+E[z_0]
$$


对于$i\in \{1,2,...,n-1\}$，考虑出发的第一步，第一步或者走到第$i-1$个位置，或者走到第$i+1$个位置，所以
$$
\begin{aligned}
E[Z_i] &= Pr[\text {go left}] E[Z_i |\text {go left}] + Pr[\text {go right}] E[Z_i |\text {go right}] \\
&=\frac 1 2 (1+E[Z_{i-1}])+\frac 1 2 (1+E[Z_{i+1}]) \\
&=1+\frac 1 2 E[Z_{i-1}]+\frac 1 2 E[Z_{i+1}]
\end{aligned}
$$
对这个式子重新整理可得
$$
E[Z_i] - E[Z_{i+1}] = E[Z_{i−1}] - E[Z_i] + 2
$$
这个数列利用累加法即可求解，解得
$$
E[Z_0] =E[T_n]= n^2
$$


##### 推论

$$
\text {Pr}[T_n > 2n^2]\le \frac 1 2
$$

证明：
$$
\begin{aligned}
n^2&=E[T_n] \\
&=\sum_{k=0}^{2n^2}k \text{Pr}[T_n=k]+\sum_{k=2n^2+1}^{+\infty}k \text{Pr}[T_n=k]\\
&\ge 0+2n^2  \sum_{k=2n^2+1}^{+\infty} \text{Pr}[T_n=k]\\
&=2n^2   \text{Pr}[T_n>2n^2]\\
\end{aligned}
$$
所以
$$
\text {Pr}[T_n > 2n^2]\le \frac 1 2
$$

下面将应用Local Search Algorithm处理2-SAT Problem



#### The 2-SAT Problem    

这里输入感觉不怎么好翻译，直接给英文了

输入：
（1）$n$ Boolean variables $x_1,x_2,...,x_n$(Can be set to TRUE or FALSE)
（2）$m$ clauses of 2 literals each("literal"$= x_i$ or $\neg x_i$）

例子:$(x_1\vee x_2)\wedge (x_1\vee\neg x_3) \wedge (x_3 \vee x_4) \wedge (\neg x_2 \vee \neg x_4) $

输出：如果可以使每个clauses都为真则输出yes，否则输出no。

例子：对之前那个例子，取$x_1=x_3=true,x_2=x_4=false$可以使得每个clauses都为真，所以这个例子输出yes

后面把每种组合称为一种安排(assignment)



这里介绍算法：

##### Papadimitriou’s Algorithm

$n =$变量数
重复$log_2 n$次：

- 选择随机初始分配
- 重复$2n^2$次：
- 如果当前赋值满足所有clauses，则暂停+报告结果
- 否则，选择任意不满足的clauses并翻转其中一个变量的值[在两个变量之间随机选取]

报告”无法满足“



我们来简单分析下这个算法，显然这个算法是多项式时间内运行的，并且原例不满足的情形下一定正确（即原例无法每个clauses都为真时这个算法一定能返回”无法满足“），但是如果原例能满足每个clauses都为真时，这个算法有可能返回“无法满足”，来分析下这种情形的概率。

##### Theorem

对于具有$n$个变量的可满足的2-SAT实例，Papadimitriou的算法可以产生正确结果的概率$\ge1-\frac 1 n$

证明：首先关注外层每次循环。任取一个满足每个clauses都为真的安排$a^*$，令$a_t$为在内层循环$t$次之后的安排$(t=0,...,2n^2)$，$X_t$为$a_t$和$a^*$一致的变量数$(X_t \in\{1,...,n \})$

注意：如果$X_t=n$，那么算法停止。

现在假设$a_t$是不满足条件的安排，假设在$x_i,x_j$处不满足，注意$a^*$为满足条件的分配，那么$a^*$和$a_t$至少在$x_i,x_j$中一处不同，现在考虑$X_{t+1}$和$X_{t}$的关系：

（1）如果$a^*$和$a_t$在$x_i,x_j$两处都不同，那么
$$
X_{t+1}=X_{t}+1(100\%)
$$
（2）如果$a^*$和$a_t$在$x_i,x_j$ 中一处不同，那么
$$
X_{t+1}=\begin{cases}
X_t+1, &50\%\\
X_t-1, &50\%
\end{cases}
$$
看到这里，应该能把这个算法联系到之前所讲的随机游走，为证实这点，来看一个习题。



###### Quiz

随机变量$X_0,X_1,...,X_{2n^2}$的就像非负整数随机游走，除了：

A）有时以100％的概率向右移动（而不是50％）
B）可能有$X_0> 0$而不是$X_0 = 0$
C）可能会在$X_t = n$之前提前停止
D）以上全部

首先(A)是我们之前列的两种情况，正确；(B)也是对的，因为一开始可能有一些clauses为真；(C)可能在和$a^*$不完全相同的情形下停止，只要每个clauses都为真即可，所以这题选(D)。我们可以理解这题对应的随机游走比之前讨论的随机游走终止得更快一些。



回到定理证明，记我们这种随机游走达到$n$的步数为$S_n$，$T_n$为随机游走到位置$n$的步数，由上述性质，我们知道$Pr[S_n≤2n^2]\ge Pr[T_n≤2n^2]\ge \frac 1 2$

外层每次循环找到满足条件的安排相当于在$2n^2$步之内使得$X_t=n$，即$Pr[S_n≤2n^2]$，从而：
$$
外层每次循环找到满足条件的安排的概率≥Pr[T_n≤2n^2]≥\frac 12
$$
所以
$$
\begin{aligned}
Pr[\text{algorithm fails}] &≤ Pr[\text{all}\ log_2n\ \text{independent trials fail}]\\
&≤  (\frac 1 2)^{log_2 n}\\
&=\frac 1 n
\end{aligned}
$$
从而算法成功的概率$\ge 1- \frac 1 n$



### Part 2:习题

#### 思考题

##### Maximum Cut Problem推广

证明在具有正整数边权重的图中，最大切割问题的局部搜索算法不能保证在多项式时间内收敛。

这个问题是老师课件里留下的，现在每条边都有权重，用局部搜索算法求cross edge的权重最大，这里要说明这个算法不一定能在多项式时间内收敛，下面说明下。

现在有$n$个点，那么最多有$C_n^2$条边，设每条边的权重为$w_i$，cross edge的集合为$S$，cross edge的权重和为$\sum_{i\in S}w_i$，注意现在每一轮迭代并不一定增加$|S|$，所以可能把边的每种子集都列出来，即可能迭代$2^{C_n^2}$次，所以算法不一定在多项式时间内收敛。



#### 选择题

##### 选择题1

以下哪种说法对于通用局部搜索算法是不正确的？


A）局部搜索算法保证最终收敛到最优解。


B）局部搜索算法的输出通常取决于起始点的选择。


C）通用局部搜索算法的输出通常取决于如何选择邻居（存在多个邻居时）。

D）在某些情况下，通用局部搜索算法可能需要在终止之前进行指数次迭代。

显然这题选A



##### 选择题2

假设我们将局部搜索应用于最小割问题。给定一个无向图，我们从任意切割(A,B)开始。我们检查是否存在一个顶点$v$，以便将$v$从一个组切换到另一个将严格减少穿过切割的边的数量。 （此外，我们不允许切换顶点导致A或B变空）。如果有这样一个顶点，我们将它从一个组切换到另一个;如果有很多这样的顶点，我们随便挑一个来切换。如果没有这样的顶点，那么我们返回当前局部最优切割（A，B）。关于这个局部搜索算法，下列哪个陈述是正确的？


A）该局部搜索算法保证以迭代的多项式数终止。


B）这个本地搜索算法保证计算最小割。


C）这种局部搜索算法可以保证计算一个交叉边的数量至多是可能最小值的两倍。

D）如果这个局部搜索算法保证以多项式迭代次数终止，它将立即暗示P = NP。

假设有$n$个点，所以一共最多$C_n^2$条边，该算法每次至少一条边，所以最多迭代$C_n^2$次，因此这题选A



##### 选择题3

maximum k-cut problem，输入是一个无向图$G =(V，E)$，每个边都有非负重量$w_{\epsilon}$。目标是将$V$拆分成$k$个非子集$A_1,...,A_K$以最大化切割边缘的总重量（例如，边的两点属于不同的$A_i$）。最大切割问题的特殊情况$k = 2$对应于讲座中所研究的。

考虑应用局部搜索来最大化k -cut问题:

(i)从任意k -cut开始; 

(ii)重复：如果可能，移动一组顶点$A_i$至另一个$A_j$使得严格增加切割边缘的总重量; 

(iii)如果(ii)无法操作就停下来。

考虑以下陈述：对于每个maximum k-cut problem，每个局部最大值至少有目标函数值的$f (k )$乘以全局的最大值。以下哪一项是$f(k)$的最大值？

A) $\frac {k−1}{k}$

B)  $\frac 1 2$

C) $\frac  1 k$

D) $1-\frac{1}{k(k-1)}$

这题和我们之前讨论的maximum cut problem类似，这里采用类似的方法。

对于分割方法方法$A_1,...,A_K$和顶点$v$，定义

$c_v(A_i,A_j)= v$的边中穿越$(A_i,A_j)$的边的权重
$d_v(A_i)=v$的边中在$A_i$内的数量的边的权重

由算法的规则我们知道
$$
c_v(A_i,A_j)\ge d_v(A_i)
$$
对于次式两边关于$j\neq i$累加求和可得
$$
\sum_{i\neq j}c_v(A_i,A_j)\ge (k-1)d_v(A_i)
$$
最后再关于$i$求和可得
$$
\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)\ge (k-1)\sum_{i=1}^{k}d_v(A_i)
$$
$\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)$为该算法求出的cross edge的权重的两倍，$\sum_{i=1}^{k}d_v(A_i)$为非cross edge权重的两倍，记所有边的权重和为$W$，显然$2W=\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)+\sum_{i=1}^{k}d_v(A_i)$

现在对不等式两边同时加上$(k-1)\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)$
$$
\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)+(k-1)\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)\ge (k-1)\sum_{i=1}^{k}d_v(A_i)+(k-1)\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)\\
k\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)\ge 2(k-1)W\\
\frac{\sum_{i=1}^{k}\sum_{i\neq j}c_v(A_i,A_j)}{2}\ge \frac {k-1}{k}W\ge \frac {k-1}{k} \text{最优解}
$$
所以这题为选A



##### 选择题4

Suppose $X$ is a random variable that has expected value 1. What is the probability that $X$ is 2 or larger? (Choose the strongest statement that is guaranteed to be true.) 

A) At most 100%

B) 0

C) At most 25%

D) At most 50%

构造这样一个分布
$$
P(x=4)=0.75,P(x=-8)=0.25\\
P(x\ge2)=0.75
$$
所以这题选A





##### 选择题5

Suppose $X$ is a random variable that is always nonnegative and has expected value 1. What is the probability that $X$ is 2 or larger? (Choose the strongest statement that is guaranteed to be true.) 

A) At most 100%

B) 0

C) At most 25%

D) At most 50%

这题和上一题挺像的，不同之处在于非负
$$
1=E[X]=E_{0\le x< 2}[X]+E_{x\ge 2}[X]\ge E_{x\ge 2}[X]\ge2Pr(X\ge 2)\\
Pr(X\ge 2)\le \frac 1 2
$$
所以选D