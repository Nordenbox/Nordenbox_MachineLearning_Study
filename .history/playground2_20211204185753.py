class Foo:
    def outprint(self,name):
        print('hello',name)

def outprint(name):
    print('hello',name)


a = Foo()
a.outprint('nordenbox')

outprint('nordenbox')