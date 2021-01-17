class C2vec:

    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return (f"{self.icap}i + {self.jcap}j")

class C3vec(C2vec):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return (f"{self.icap}i + {self.jcap}j + {self.kcap}k")


v2d = C2vec(1,3)
v3d = C3vec(5,6,7)
print(v2d)
print(v3d)

