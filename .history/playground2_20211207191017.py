import random 
A = True
while A:
    w,r,g,b =random.randint(0,401),random.randint(0,401),random.randint(0,401),random.randint(0,401)
    if w+2*r+3*g+4*b ==400:
        print(w,r,g,b)
        
    
