n = int(input())
starList = []

if n == 1 :
    print("*")

else :
    realN = n + n + 2 * (n - 2) + 1
    for i in range(1, realN + 1) :
        star = ""
        
        if i == 1 or i == realN :    
            star = "*" * realN
        
        elif i <= realN // 2 + 1:
            if i % 2 != 0: # 홀수
                star += "* " * (i // 2)
                star += "*" * (realN - 2 * ((i // 2) * 2))
                star += " *" * (i // 2)
        
            else : # 짝수
                star += "* " * (i // 2)
                star += " " * (realN - 2 * ((i // 2) * 2))
                star += " *" * (i // 2)
                
        else :
            if i % 2 != 0: # 홀수
                star += "* " * ((realN - i) // 2)
                star += "*" * (realN - 2 * (((realN - i) // 2) * 2))
                star += " *" * ((realN - i) // 2)
        
            else : # 짝수
                star += "* " * ((realN - i + 1) // 2)
                star += " " * (realN - 2 * (((realN - i + 1) // 2) * 2))
                star += " *" * ((realN - i + 1) // 2)
        
        starList.append(star)  

for star in starList:
    print(star)