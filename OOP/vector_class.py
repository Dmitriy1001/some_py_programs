import math


class Vector:
    '''The class that supports addition, subtraction, dot products, and norms.
    Of tries to add, subtract, or dot two vectors with different lengths, you throw an error.
    Also have an equals method, to check that two vectors that have the same components are equal.'''

    def __init__(self, lst):
        self.coord = lst

    def equals(self, vect_obj):
        return all(self.coord[i] == vect_obj.coord[i] for i in range(len(self.coord)))    

    def equal_length(self, vect_obj):
        if isinstance(vect_obj, Vector):
            return len(self.coord) == len(vect_obj.coord)
        else:
            return False        

    def add(self, vect_obj):
        if self.equal_length(vect_obj):
            return Vector([self.coord[i] + vect_obj.coord[i] for i in range(len(self.coord))])
        else:
            raise Exception

    def subtract(self, vect_obj):
        if self.equal_length(vect_obj):
            return Vector([self.coord[i] - vect_obj.coord[i] for i in range(len(self.coord))])
        else:
            raise Exception

    def dot(self, vect_obj):
        if self.equal_length(vect_obj):
            return sum([self.coord[i] * vect_obj.coord[i] for i in range(len(self.coord))])
        else:
            raise Exception
            
    def norm(self):
        return math.sqrt(sum([i**2 for i in self.coord]))

    def __str__(self):
        return '(' + ','.join([str(i) for i in self.coord]) + ')'


# Example
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])

# a.add(b)        returns a new Vector([4, 6, 8])
# a.subtract(b)   returns a new Vector([-2, -2, -2])
# a.dot(b)        returns 1*3 + 2*4 + 3*5 = 26
# a.norm()        returns sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)        raises an exception