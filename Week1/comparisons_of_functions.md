# Comparisons of Functions

### Related Properties
- Transitivity (전이성, 이행관계(추이관계)):
  *aRb and bRc => aRc*
  > **f(n) = Θ(g(n))** and **g(n) = Θ(h(n))** => **f(n) = Θ(h(n))**.
  > Same for O, Ω, o, and ω.
- Reflexivity (반사관계):
  *aRa*
  > **f(n) = Θ(f(n))**
  > Same for O and Ω.
- Symmetry (대칭관계):
  *aRb => bRa*
  > **f(n) = Θ(g(n))** if and only if **g(n) = Θ(f(n))**.
- Transpose Symmetry:
  > **f(n) = O(g(n))** if and only if **g(n) = Ω(f(n))**.
  > **f(n) = o(g(n))** if and only if **g(n) = ω(f(n))**.

### Comparisons
- *f(n)* is **asymptotically smaller** than *g(n)* if **f(n) = o(g(n))**.
- *f(n)* is **asymptotically larger** than *g(n)* if **f(n) = ω(g(n))**.