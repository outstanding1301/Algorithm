# Asymptotic Analysis

> Ignore machine-dependent constants.
> Look at **growth** of **T(n) as n->Inf**

## Θ (Big-Theta) Notation =="점근적 한계"==
![Big Theta](https://cdn.kastatic.org/ka-perseus-images/2bdc25c7eda8486d05b8031c5a63535684ecb5a1.png)

### Mathematical Definition
> **Θ(g(n))** = **{f(n)**: there exist positive constants **c~1~**, **c~2~**, and **n~0~** 
> such that **0 <= c~1~g(n) <= f(n) <= c~2~g(n) for all n >= n~0~}**


### Engineering Definition
> Drop low-order terms and ignore leading constants.
> Ex) ~~4~~**n^3^** ~~+ 90n^2^ - 7n + 6036~~ = **Θ(n^3^)**

## O (Big-O) Notaion =="점근적 상한선"==
![Big O](https://cdn.kastatic.org/ka-perseus-images/501211c02f4c6765f60f23842450e1151cfd9c89.png)

> **O(g(n))** = **{f(n)**: there exist positive constants **c**, and **n~0~** 
> such that **0 <= f(n) <= cg(n) for all n >= n~0~}**
> 
> - **g(n)** is an **asymptotic upper bound** for **f(n)**.
> 
> Ex)　　2n^2^ = O(n^3^), with c=1 and n~0~=2.
>  also,　 2n^2^ = O(n^2^), with c=2 and n~0~=1.
> 
> Examples of functions in *O(n^2^)*:
> - n^2^, n^2^ + n, n^2^ + 1000n, 1000n^2^ + 1000n
> - n, n/1000, n^1.9999^, n^2^/*lg* n
> 
> TIP : Leading Term이 *g(n)* 보다 작거나 같은 *f(n)* 들이 해당됨


## Ω (Big-Omega) Notaion : =="점근적 하한선"==
![Big Omega](https://cdn.kastatic.org/ka-perseus-images/c02e6916d15bacae7a936381af8c6e5a0068f4fd.png)

> **Ω(g(n))** = **{f(n)**: there exist positive constants **c**, and **n~0~** 
> such that **0 <= cg(n) <= f(n) for all n >= n~0~}**
> 
> - **g(n)** is an **asymptotic lower bound** for **f(n)**.
> 
> Ex)　　√n = Ω(*lg* n), with c=1 and n~0~=16.
> 
> Examples of functions in *Ω(n^2^)*:
> - n^2^, n^2^ + n, n^2^ - n, 1000n^2^ + 1000n, 1000n^2^ - 1000n
> - n^3^, n^2.0000^, n^2^*lg* n, 2^n^
> 
> TIP : Leading Term이 *g(n)* 보다 크거나 같은 *f(n)* 들이 해당됨

## o (Small-O) Notaion
> **o(g(n))** = **{f(n)**: for all constants **c > 0**, there exist a constant **n~0~ > 0** 
> such that **0 <= f(n) ==<== cg(n) for all n >= n~0~}** 
>  
> - **g(n)** is an **asymptotic ==strict== upper bound** for **f(n)**.
> 
> Examples of functions in *o(n^2^)*:
> - ~~n^2^, n^2^ + n, n^2^ + 1000n, 1000n^2^ + 1000n~~ (Leading Term이 같은 level임)
> - n, n/1000, n^1.9999^, n^2^/*lg* n
> 
> TIP : Leading Term이 *g(n)* 보다 작은 *f(n)* 들이 해당됨

## ω (Small-Omega) Notaion
> **ω(g(n))** = **{f(n)**: for all constants **c > 0**, there exist a constant **n~0~ > 0** 
> such that **0 <= cg(n) ==<== f(n) for all n >= n~0~}** 
>  
> - **g(n)** is an **asymptotic ==strict== lower bound** for **f(n)**.
> 
> Examples of functions in *ω(n^2^)*:
> - ~~n^2^, n^2^ + n, n^2^ - n, 1000n^2^ + 1000n, 1000n^2^ - 1000n~~ (Leading Term이 같은 level임)
> - n^3^, n^2.0000^, n^2^*lg* n, 2^n^
> 
> TIP : Leading Term이 *g(n)* 보다 큰 *f(n)* 들이 해당됨


*Image Source: [Khan Academy](https://ko.khanacademy.org/computing/computer-science/algorithms#asymptotic-notation)*