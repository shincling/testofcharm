class ttt():
    def __init__(self,a,b=2,c=3):
        self.fi=a
        self.se=b
        self.th=c
    def dd(self):
        print self.th*2

bb=ttt(1)

print bb.fi,bb.se,bb.th
bb.dd()

try:
    print cc
except Exception,e:
    print e