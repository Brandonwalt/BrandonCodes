class LogicGate(object):
    def __init__(self, a=False,b=False):
        self._a = a
        self._b = b
        self._ = self.evaluate()
        
    def set_a(self, a):
        self._a = a
        self.evaluate()

    def set_b(self, b):
        self._b = b
        self.evaluate()

    def evaluate(self):
        self._x = None

    def output(self) :
        return self._x

class ANDGate(LogicGate):
    def evaluate (self):
        self._x = self._a and self._b
    
u1 = ANDGate()
print(u1.output())
u1.set_a(True)
u1._b=True
print(u1.output())
