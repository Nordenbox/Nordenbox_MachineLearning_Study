class Men:  # 一个颜色测试
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def kill(self):
        
        print('order to kill',self.name)
        
    def release(self):
        print('release under ',self.age)

prinsonAuthority = Men('bob', 29)
prinsonAuthority.kill()
prinsonAuthority.release()