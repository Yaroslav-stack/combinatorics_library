# Combinatorics library

So, I try to create my first library on python and I think it turned out well.

## What formulas does the program use

- $$(n)_k = \frac{n!}{(n-k)!} = n \cdot (n-1) \cdot \ldots \cdot (n-k+1)$$

- $$C_n^k = \frac{n!}{k!(n-k)!}$$

- $$(a + b)^n = \sum_{k=0}^{n} C_n^k a^{n-k} b^k$$

## Usage Examples

### Basic Examples

```python
from combinatorics import Combinatorics

# Calculate permutations (arrangements)
# How many ways to arrange 3 books on a shelf from 5 books?
result = Combinatorics.permutations(5, 3)
print(result)  # 60

# Calculate combinations
# How many ways to choose 3 fruits from 5?
result = Combinatorics.combinations(5, 3)
print(result)  # 10

# Binomial expansion
# Calculate (2 + 3)⁴
result = Combinatorics.binomial_expansion(2, 3, 4)
print(result)  # 625 (because (2+3)⁴ = 5⁴ = 625)
```

## My comments

As you may have noticed, the code looks more thoughtful and contains only what is necessary.I tried to make it that way, because the previous programmes works in one way or another, but there were many things that could have been made smarter.

I made a library out of the functionality of the previous programs. Personally, I recommend using this library instead of the previous programs, as it is simply more convenient and contains more concise code, if you decide to use it.
