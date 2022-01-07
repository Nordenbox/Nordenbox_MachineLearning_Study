class Men:  # 一个颜色测试
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def kill(self):
        
        print('order to kill',self.name)
        
    def release(self):
        print('release',self.name)

prinsonAuthority = Men()
prinsonAuthority.kill