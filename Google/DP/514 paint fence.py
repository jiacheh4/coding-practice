# https://www.lintcode.com/problem/514/?fromId=18&_from=collection

"""
@param n: non-negative integer, n posts
@param k: non-negative integer, k colors
@return: an integer, the total number of ways

(k−1)×(num_ways(n−1)+num_ways(n−2))

"""
def num_ways(self, n, k):
    # write your code here
    def num_ways(self, n, k):
        # write your code here
        return self.f(n, k)
    def f(self, n, k):
        if k == 1 and n > 2:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k**2
        return (k-1) * (self.f(n-1,k) + self.f(n-2,k)) 

if __name__ == "__main__":
    num_ways()
