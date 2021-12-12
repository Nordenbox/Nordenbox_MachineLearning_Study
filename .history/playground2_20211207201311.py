
result = 0
for w in range(1,401):
    for r in range(1,201):
        for g in range(1,151):
            for b in range(1,101):
   
                if w+9*r+11*g+7*b ==400:
                    result += 1
                    
print(result)      
    
