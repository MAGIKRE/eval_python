class Exo:
    def puissance(self, x, n):
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.puissance(x, -n)
        
        if n % 2 == 0:
            half = self.puissance(x, n // 2)
            return half * half
        else:
            return x * self.puissance(x, n - 1)

exo = Exo()
print(exo.puissance(2, 3))  # Retourne 8


