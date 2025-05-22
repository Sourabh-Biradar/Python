# method overriding
# child.method() changes behaviour of parent.method()

class P :
    def fn(self):
        return 'Father : im head of family'

class C(P):
    def fn(self):
        return 'Son : im head of family'

c = C()
p=P()
print(p.fn())