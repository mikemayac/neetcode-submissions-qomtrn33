import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length:int, width:int = None):
        if width is None: # Circle Area
            circle_area = math.pi * (length**2)
            return round(circle_area, 2)
        else:   # Rectangle area
            return length * width

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
