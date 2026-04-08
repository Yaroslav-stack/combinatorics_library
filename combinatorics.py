import math

class Combinatorics:
    
    @staticmethod
    def permutations(n: int, k: int) -> int:
        """Number of permutations: P(n,k) = n!/(n-k)!"""
        if not (isinstance(n, int) and isinstance(k, int)):
            raise TypeError("n and k must be integers")
        if k < 0 or k > n:
            raise ValueError("k must be between 0 and n")
        return math.factorial(n) // math.factorial(n - k)
    
    @staticmethod
    def combinations(n: int, k: int) -> int:
        """Number of combinations: C(n,k) = n!/(k!(n-k)!)"""
        if not (isinstance(n, int) and isinstance(k, int)):
            raise TypeError("n and k must be integers")
        if k < 0 or k > n:
            raise ValueError("k must be between 0 and n")
        return math.comb(n, k)  # или math.factorial(n) // math.factorial(k) // math.factorial(n-k)
    
    @staticmethod
    def binomial_expansion(a, b, n: int):
        """Expand (a + b)^n"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        terms = []
        for k in range(n + 1):
            coeff = math.comb(n, k)
            term = coeff * (a ** (n - k)) * (b ** k)
            terms.append(term)
        return sum(terms)
    
print(Combinatorics.binomial_expansion(7, 4, 5))