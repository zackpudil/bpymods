
class GLSLType:

    def add(self, v):
        pass

    def sub(self, v):
        pass

    def mul(self, v):
        pass

    def rmul(self, v):
        pass

    def truediv(self, v):
        pass

    def neg(self):
        pass

    def abs(self):
        pass

    def __add__(self, v):
        return self.add(v)

    def __radd__(self, v):
        return self.add(v)

    def __sub__(self, v):
        return self.sub(v)

    def __rsub__(self, v):
        return self.neg().add(v)

    def __mul__(self, v):
        return self.mul(v)

    def __rmul__(self, v):
        return self.rmul(v)

    def __truediv__(self, v):
        return self.truediv(v)

    def __neg__(self):
        return self.neg()

    def __abs__(self):
        return self.abs()
