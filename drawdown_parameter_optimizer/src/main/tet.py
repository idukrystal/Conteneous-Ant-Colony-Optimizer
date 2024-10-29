class A():
    a = "a"
    def __init__(self):
        print(self.a)

class B(A):
    a = "b"
    def __init__(self):
        super().__init__()


b = B()
b.a = "c"
print(b.a)
c = B()
