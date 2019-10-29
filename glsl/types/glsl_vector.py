
class GLSLVector:
    coords = []

    names = {
        'x': 0,
        'y': 1,
        'z': 2,
        'w': 3,
        'r': 0,
        'g': 1,
        'b': 2,
        'a': 3
    }

    def __init__(self, coords):
        self.coords = coords

    def __str__(self):
        return "vec{0}({1})".format(str(len(self.coords)), ','.join(str(c) for c in self.coords))

    def __getattr__(self, attr):
        nv = []
        for c in list(attr):
            nv.append(self.coords[self.names.get(c)])

        return nv.pop() if len(nv) == 1 else GLSLVector(nv)

    def __setattr__(self, attr, value):
        if attr == "coords":
            super().__setattr__(attr, value)
            return

        s = list(attr)
        if len(s) == 1:
            self.coords[self.names.get(s[0])] = value
            return

        for i in range(0, len(s)):
            self.coords[self.names.get(s[i])] = value.coords[i]


    def componentOps(self, v, op):
        nv = []
        if isinstance(v, GLSLVector):
            for i in range(0, len(self.coords)):
                nv.append(op(self.coords[i], v.coords[i]))
        else:
            for x in self.coords:
                nv.append(op(x, v))

        return GLSLVector(nv)

    def add(self, v):
        return self.componentOps(v, lambda a, b: a + b)

    def sub(self, v):
        return self.componentOps(v, lambda a, b: a - b)

    def mul(self, v):
        return self.componentOps(v, lambda a, b: a * b)

    def truediv(self, v):
        return self.componentOps(v, lambda a, b: a / b)

    def neg(self):
        return GLSLVector(list(map(lambda c: -c, self.coords)))

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
        return self.mul(v)
    def __truediv__(self, v):
        return self.truediv(v)

    def __neg__(self):
        return self.neg()

    def __abs__(self):
        return GLSLVector(list(map(lambda c: abs(c), self.coords)))
