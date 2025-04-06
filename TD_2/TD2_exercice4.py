class Polynomial_modulo:
    
    def __init__(self,L,q,n):
        self.q = q
        self.n = n
        self.coefficients = L
        self.coeff_modulo = self.reduce()
        
    
    def reduce(self):
        L = self.coefficients
        l = len(L)
        L = L[::-1]
        if l >= self.n:
            for k in range(self.n,l):
                L[k-self.n] -= L[k]
                L.pop(k)
        L = L[::-1]
        modulo_q = [k%self.q for k in L]
        return modulo_q


    def __str__(self):
        polynome = ""
        n = len(self.coeff_modulo)
        for k in range(n):
            if self.coeff_modulo[k] != 0 and self.coeff_modulo[k] != 1:
                if k == n-1:
                    polynome += f"+{self.coeff_modulo[k]}"
                elif k == n-2:
                    polynome += f"+{self.coeff_modulo[k]}*X"
                elif k == 0:
                    polynome += f"{self.coeff_modulo[k]}*X^{n-1}"
                else:
                    polynome += f"+{self.coeff_modulo[k]}*X^{n-k-1}"
            elif self.coeff_modulo[k] == 1:
                if k == n-1:
                    polynome += f"+{self.coeff_modulo[k]}"
                elif k == n-2:
                    polynome += "+X"
                elif k == 0:
                    polynome += f"X^{n-1}"
                else:
                    polynome += f"+X^{n-k-1}"
        return polynome
    
    
    def scalar(self,c):
        L = [c*k for k in self.coeff_modulo]
        return Polynomial_modulo(L,self.q,self.n)
    
    def rescale(self,r):
        return Polynomial_modulo(self.coeff_modulo,r,self.n)
    
    
    def __add__(self, other):
        n = len(self.coefficients)
        m = len(other.coefficients)
        new_coeff = []
        if n==m:
            for k in range(n):
                new_coeff.append(self.coefficients[k] + other.coefficients[k])
        if n > m:
            for k in range(1,m+1):
                new_coeff.append(self.coefficients[-k] + other.coefficients[-k])
            for k in range(m+1, n+1):
                new_coeff.append(self.coefficients[-k])
        if n < m:
            for k in range(1,n+1):
                new_coeff.append(self.coefficients[-k] + other.coefficients[-k])
            for k in range(n+1,m+1):
                new_coeff.append(other.coefficients[-k])
        return Polynomial_modulo(new_coeff[::-1],self.q,self.n)
       

if __name__  == '__main__':
    p = Polynomial_modulo([4,2,0,1],5,3)
    q = Polynomial_modulo([2,1,3],5,3)
    somme = p+q
    print(somme)
    assert(somme.__str__()=="4*X^2+X")
    
    