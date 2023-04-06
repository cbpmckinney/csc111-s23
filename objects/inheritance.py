
class Enemy:

    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity
    

class KoopaTroopa(Enemy):
    
    def __init__(self, initx, inity, initcolor):
        super().__init__(initx, inity)
        self.color = initcolor



enemy1 = KoopaTroopa(5,3,'red')

