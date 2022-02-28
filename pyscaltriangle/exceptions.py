class TriangleException(Exception):
    def __init__(self, excep, msg):
        self.excep = excep
        self.msg = msg
        
        
class InexistenceTerm(TriangleException):
    def __init__(self, excep):
        self.msg = "Position not exists in Triangle"
        super().__init__(excep, self.msg)
        print(f"{self.msg}. Lanched {self.excep.name}")
