"""
PYTHON SOLUTION - Count Primes
08/11/2026
TIME COMPLEXITY: O(N log log N)
SPACE COMPLEXITY: O(N)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## COUNT PRIMES   ##
    ####################
    def countPrimes(self, n: int) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # No primes exist below 2 (0, 1, and negative n are all trivial)
        if n < 3:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Sieve of Eratosthenes
        # KEY INSIGHT: Instead of checking each number individually for
        # primality (which is slow), mark off MULTIPLES of each prime
        # as "not prime" in one sweep. Whatever's left unmarked IS prime.
        #
        # is_prime[i] starts as True for all i, then we "cross out"
        # composites by marking multiples of each found prime as False.
        
        # Assume all numbers from 0 to n-1 are prime initially
        is_prime = [True] * n
        is_prime[0] = False  # 0 is not prime
        if n > 1:
            is_prime[1] = False  # 1 is not prime
        
        # Only need to check potential primes up to sqrt(n)
        # (any composite number has a factor <= sqrt(n))
        p = 2
        while p * p < n:
            if is_prime[p]:
                # Mark all multiples of p (starting from p*p) as NOT prime
                # We start at p*p because smaller multiples of p
                # (like 2p, 3p, ...) were already marked by smaller primes
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1
        
        # Count how many numbers remain marked as prime
        return sum(is_prime)

#########
## EOF ##
#########