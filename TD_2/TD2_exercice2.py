class Polynomial_modulo:
    
    def __init__(self,L,q,n):
        self.q = q
        self.n = n
        self.coeff = L
        self.coeff_modulo = self.reduce()
        
    
    def reduce(self):
        L = self.coeff
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
    

if __name__  == '__main__':
    p = Polynomial_modulo([4,2,0,1],5,3)
    print(p)
    assert(p.__str__()=="2*X^2+2")
    
    
                
        
        
        
