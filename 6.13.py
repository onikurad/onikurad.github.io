from math import sqrt

class Triangle():       
    def __init__(self,a,b,c):   
        self.a=a
        self.b=b
        self.c=c
            
    def perimeter(self):
        return self.a + self.b +self.c
    
    def area(self):
      s=(self.a + self.b + self.c)/2
      return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    
    def scale(self, scale_factor):
        return Triangle (scale_factor*self.a, scale_factor*self.b,scale_factor*self.c )
    
    def is_valid(self):
        if (self.b+self.c)>self.a and (self.a+self.c)>self.b and (self.a+self.b)>self.c:
            return 'True'
        else:
            return 'False'
        
    def is_right(self):
        if pow(self.a,2) == pow(self.b,2) + pow(self.c,2) or pow(self.b,2) == pow(self.c,2) + pow(self.a,2) or pow(self.c,2) == pow(self.b,2) + pow(self.a,2):
            return 'True'
        else:
            return 'False'
        
        
t = Triangle(3,4,5)


print ("Perimeter=%d" % t.perimeter())  
print ("Area = %d" %t.area())

q = t.scale(3)
print (q.a, q.b,q.c)

print(t.is_valid())

print (t.is_right())
