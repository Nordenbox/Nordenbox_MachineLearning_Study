class Men:  # 一个颜色测试
    
    def __init__(self):
        #self.name = name
        #self.age = age
        
    def kill(self,name):
        
        print('order to kill',self.name)
        
    def release(self):
        print('release',self.name)

prinsonAuthority = Men()
prinsonAuthority.kill('bob')