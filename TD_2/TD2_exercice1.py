class Polynomial:
    
    def __init__(self,L):
        self.coefficients = L
    
    def __str__(self):
        polynome = ""
        n = len(self.coefficients)
        for k in range(n):
            if self.coefficients[k] != 0 and self.coefficients[k] != 1:
                if k == n-1:
                    polynome += f"+{self.coefficients[k]}"
                elif k == n-2:
                    polynome += f"+{self.coefficients[k]}*X"
                elif k == 0:
                    polynome += f"{self.coefficients[k]}*X^{n-1}"
                else:
                    polynome += f"+{self.coefficients[k]}*X^{n-k-1}"
            elif self.coefficients[k] == 1:
                if k == n-1:
                    polynome += f"+{self.coefficients[k]}"
                elif k == n-2:
                    polynome += "+X"
                elif k == 0:
                    polynome += f"X^{n-1}"
                else:
                    polynome += f"+X^{n-k-1}"
        return polynome
    
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
        return Polynomial(new_coeff[::-1])
    
                
            
            
    
if __name__  == '__main__':
    a = Polynomial([1,2,3,7])
    b = Polynomial([4,5,6])
    somme = a+b
    print(a)
    print(somme)
    assert(a.__str__() == "X^3+2*X^2+3*X+7") 
    assert(somme.__str__() == "X^3+6*X^2+8*X+13")
    
    
    

    
        
            
                
                
                
        
        
        
        

