
class father:
    name = ''
    def __init__(self):
        self.name = 'ali'
        self.chap()

    def chap(self):
        print(self.name)

class son(father):
    nam = ""
    def __init__(self):
        super().__init__()
        #self.chap()        #farakhanie tabey class ers borde shode

s = son()