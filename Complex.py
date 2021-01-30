import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        # print("real: %0.2f imaginary: %0.2f" % (self.real, self.imaginary))

    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
        # C = Complex(self, no)
        # C.real = self.real + no.real
        # C.imaginary = self.imaginary + no.imaginary
        # return C
        # # return print("%.2f+%.2fi"%(self.real, self.imaginary))
        
    def __sub__(self, no):
        # self.real -= no.real
        # self.imaginary -= no.imaginary
        return Complex(self.real-no.real, self.imaginary-no.imaginary)
    
    def __mul__(self, no):
        # self.real = ((self.real*no.real)-(self.imaginary*no.imaginary))
        # self.imaginary = ((self.real*no.imaginary)+(self.imaginary*no.real))
        return Complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+self.imaginary*no.real)
        
    def __truediv__(self, no):
        # self.real = ((self.real*no.real)+(self.imaginary*no.imaginary))/((no.real*no.real)+(no.imaginary*no.imaginary)) 
        # self.imaginary = (-(self.real*no.imaginary)+(self.imaginary*no.real))/((no.real*no.real)+(no.imaginary*no.imaginary))
        # return Complex(((self.real*no.real)+(self.imaginary*no.imaginary))/((no.real*no.real)+(no.imaginary*no.imaginary)), (-(self.real*no.imaginary)+(self.imaginary*no.real))/((no.real*no.real)+(no.imaginary*no.imaginary)))
        x=no.real**2+no.imaginary**2
        a=(self.real*no.real+self.imaginary*no.imaginary)/x
        b=(-no.imaginary*self.real+self.imaginary*no.real)/x
        return Complex(a, b)

    def mod(self):
        a=pow(self.real**2+self.imaginary**2, 0.5)
        b=0
        return Complex(a,b)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))