# Little-tool
# u can find some short useful code
def cal (n1,n2,d):
    if d == "*":
        return int(n1) * int(n2)
    elif d == "/":
        return int(n1) / int(n2)
    elif d == "+":
        return int(n1) + int(n2)
    elif d == "-":
        return int(n1) - int(n2)

def solve_for_x(equation):
    # 42 = nhân
    # 43 = cộng
    # 45 = trừ
    # 47 = chia
    # 61 = bằng
    maxium = 1
    new = []
    i = 0
    while i != len(equation):
        #print(equation[i])
        if ord(equation[i]) == 42 or ord(equation[i]) == 43 or ord(equation[i]) == 45 or ord(equation[i]) == 47 or ord(equation[i]) == 61 or equation[i] == "x" or equation[i] == " ":            
            if equation[i] != " ":
                new.append(equation[i])
            i = i + 1
            continue
        elif i+1 !=len(equation) and ord(equation[i]) != 42 and ord(equation[i]) != 43 and ord(equation[i]) != 45 and ord(equation[i]) != 47 and ord(equation[i]) != 61 and equation[i] != "x" and equation[i] != " " and equation[i+1] != " ":
            s = ""
            while equation[i] != " ":
                s = s + equation[i]
                i = i + 1
                if i == len(equation):
                    break
            new.append(s)
        else:
            new.append(equation[i])
            i = i + 1    
# bên trên là công đoạn phân tách chuỗi thành các phần tử riêng lẻ
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```
    
    equal = 0
    for i in range(0,len(new)):
        if new[i] == "=":
            equal = i+1
            break

    for i in range(0, len(new)):
        if new[i] == ")" or new[i] == ")":
            continue
        if "(" in new[i]:
            new.insert(i,"(")
            s = new[i+1]
            b = ""
            for l in s:
                if l != "(":
                    b = b + l
            if len(b) != 0:         
                new[i+1] = str(b)
        elif ")" in new[i]:
            new.insert(i+1,")")
            s = new[i]
            b = ""
            for l in s:
                if l != ")":
                    b = b + l
            if len(b) != 0:         
                new[i] = str(b)


# VE 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Phần 2: phá ngoặc ()

    for i in range(0,equal):
        
        so_nhan = 0
        dau  = ""
        if new[i] == "(":
            for j in range(i,equal):
                if new[j] == ")":
                    break
            if i - 1 != 0 and new[i-1] == "*" or new[i-1] == "/":
                dau = new[i-1]
                so_nhan = new[i-2]
                new[i-1] = " "
                new[i-2] = " "
            elif new[j+1] == "*" or new[j+1] == "/":
                dau = new[j+1]
                so_nhan = new[j+2]
                new[j+1] = " "
                new[j+2] = " "
            #index = i + 1

            
            for u in range(i+1, j):
                if "x" in new[u]:
                    new[u] = new[u] + dau + so_nhan
                elif new[u] != "+" and new[u] != "-" and new[u] != "*" and new[u] != "/" and so_nhan != "x":
                    new[u] = str(cal(new[u],so_nhan,dau))
                elif new[u] != "+" and new[u] != "-" and new[u] != "*" and new[u] != "/" and so_nhan == "x":
                    if dau == "*":
                        new[u] = new[u] + so_nhan
                    elif dau == "/":
                        new[u] = new[u] + "/" + so_nhan
                

            new[i] = " "
            new[j] = " "
        elif new[i] == ")" or new[i] == " ":
            continue
# VE 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
    for i in range(equal, len(new)):
        
        so_nhan = 0
        dau  = ""
        if new[i] == "(":
            for j in range(i,len(new)):
                if new[j] == ")":
                    break
            if i - 1 != 0 and new[i-1] == "*" or new[i-1] == "/":
                dau = new[i-1]
                so_nhan = new[i-2]
                new[i-1] = " "
                new[i-2] = " "
            elif new[j+1] == "*" or new[j+1] == "/":
                dau = new[j+1]
                so_nhan = new[j+2]
                new[j+1] = " "
                new[j+2] = " "
            #index = i + 1

            
            for u in range(i+1, j):
                if new[u] != "+" and new[u] != "-" and new[u] != "*" and new[u] != "/" and so_nhan != "x":
                    new[u] = cal(new[u],so_nhan,dau)
                elif new[u] != "+" and new[u] != "-" and new[u] != "*" and new[u] != "/" and so_nhan == "x":
                    if dau == "*":
                        new[u] = new[u] + so_nhan
                    elif dau == "/":
                        new[u] = new[u] + "/" + so_nhan

            new[i] = " "
            new[j] = " "
        elif new[i] == ")" or new[i] == " ":
            continue

    for i in range(0,len(new)):
        for j in new:
            if j == " ":
                new.remove(j)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```

#Phần 3: chuyển về cùng một dạng

    for i in range(0, len(new)):
        if new[i] == "*":
            new[i] = new[i-1] + "*" + new[i+1]
            new[i-1] = " "
            new[i+1] = " "
        elif new[i] == "/":
            new[i] = new[i-1] + "/" + new[i+1]
            new[i-1] = " "
            new[i+1] = " "

    for i in range(0,len(new)):
        for j in new:
            if j == " ":
                new.remove(j)

    print(new)


    equal = 0
    for i in range(0,len(new)):
        if new[i] == "=":
            equal = i+1
            break

    v1 = ["0"]
    v2 = ["0"]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Phần 4: chuyển vế chung loại

# VE 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    

    # 1 vế trái của biểu thức
    for i in range(0, equal):
        if "x" in new[i]:
            #print("new[",i,"]:",new[i])
            #print("new[",i-1,"]:",new[i-1])
            #print("new[",i+1,"]:",new[i+1])
            if i == 0:
                v1.append("+")
                v1.append(new[i])
            elif i+1 != equal:
                if new[i+1] == "+" :
                    v1.append("+")
                    v1.append(new[i])
                elif new[i+1] == "-":
                    v1.append("-")
                    v1.append(new[i])
                elif new[i-1] == "+" :
                    v1.append("+")
                    v1.append(new[i])
                elif new[i-1] == "-":
                    v1.append("-")
                    v1.append(new[i])


    # 2 vế phải của biểu thức
    for i in range(equal, len(new)):
        if "x" in new[i]:
            #print("new[",i,"]:",new[i])
            #print("new[i-1]:",new[i-1])     
            #print("new[i+1]:",new[i+1])
            

            if i != equal:     
                    
                if new[i-1] == "+" :
                    v1.append("-")
                    v1.append(new[i])
                elif new[i-1] == "-":
                    v1.append("+")
                    v1.append(new[i])
                

            elif i+1 != len(new):
                if new[i-1] == "=":
                    
                    v1.append("-")
                    v1.append(new[i])
                elif new[i+1] == "+" :
                    v1.append("-")
                    v1.append(new[i])
                elif new[i+1] == "-":
                    v1.append("+")
                    v1.append(new[i])
            elif i == equal and new[i-1] == "=":
                    v1.append("-")
                    v1.append(new[i])
            

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

# VE 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
    

    # 1 vế trái của biểu thức
    for i in range(0, equal):
        if new[i] != "+" and new[i] != "-" and new[i] != "*" and new[i] != "/" and "x" not in new[i]:
            
            #print("new[i-1]:",new[i-1])
            #print("new[i+1]:",new[i+1])
            if i == 0:
                v2.append("-")
                v2.append(new[i])
            elif i+1 != equal:
                if new[i-1] == "+" :
                    v2.append("-")
                    v2.append(new[i])
                elif new[i-1] == "-":
                    v2.append("+")
                    v2.append(new[i])
                elif new[i+1] == "+" :
                    v2.append("-")
                    v2.append(new[i])
                elif new[i+1] == "-":
                    v2.append("+")
                    v2.append(new[i])


    # 2 vế phải của biểu thức
    for i in range(equal, len(new)):
        if new[i] != "+" and new[i] != "-" and new[i] != "*" and new[i] != "/" and "x" not in new[i]:
            #print("new[",i,"]:",new[i])
            #print("new[",i-1,"]:",new[i-1])
            #print("new[",i+1,"]:",new[i+1])
            if i != equal:
                if new[i-1] == "+" :
                    v2.append("+")
                    v2.append(new[i])
                elif new[i-1] == "-":
                    v2.append("-")
                    v2.append(new[i])
            elif i+1 != len(new):
                if new[i+1] == "+" :
                    v2.append("+")
                    v2.append(new[i])
                elif new[i+1] == "-":
                    v2.append("-")
                    v2.append(new[i])
            elif new[i - 1] == "=":
                v2.append("+")
                v2.append(new[i])


    print(v1)
    print(v2)
    print()
# Phần 5: Tính ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # tính v2[] trước
    for i in range(0,len(v2)):
        if "*" in v2[i]: # xử lí nhân chia trước
            si = v2[i]
            v2[i] = str(int(si[0]) * int(si[2]))
        elif "/" in v2[i]:
            si = v2[i]
            v2[i] = str(int(si[0]) / int(si[2]))


    for i in range(0, len(v2)):
        if v2[i] == "+":
            v2[i] = int(v2[i-1]) + int(v2[i+1])
            v2[i-1] = "0"
            v2[i+1] = "0"
        elif v2[i] == "-":
            v2[i] = int(v2[i-1]) - int(v2[i+1])
            v2[i-1] = "0"
            v2[i+1] = "0" 

    total = 0
    for i in v2:
        if type(i) == int:
            total = total + i # xử lí xong vế 2 v2[]

    v2 = []
    v2.append(total)

    dau = " "

    # tinh v1[] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    for i in range(0, len(v1)):
        if "/" in v1[i]:
            s = v1[i]
            v = ""
            for j in range(0,len(s)):
                if s[j] != "/" and s[j] != "x":
                    v = v + s[j]
            num = int(v)
            v2[0] = v2[0] * num
            for h in range(0, len(v1)):
                if v1[h] != v1[i] and "x" in v1[h]:
                    v1[h] = v1[h] + "*" + str(num)
            v1[i] = "x"


    for i in range(0, len(v1)):
        if v1[i] == "+":
            # s1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            s1 = 0
            s2 = 0
    
            if len(v1[i-1]) == 1 and "x" in v1[i-1]:
                s1 = 1
                dau = "*"
            elif len(v1[i-1]) >= 2 and "x" in v1[i-1]:
                s = v1[i-1] 
                t="" 
                for k in range(0, len(s)):
                    if s[k] != "*" and s[k] != "/" and s[k] != "x":
                        t = t + s[k]
                    if s[k] == "*" or s[k] == "/":
                        dau = s[k]
                s1 = int(t)                 
            elif v1[i-1] == "0":
                s1 = 0

            # s2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if len(v1[i+1]) == 1 and "x" in v1[i+1]:
                s2 = 1
                dau = "*"
            elif len(v1[i+1]) >= 2 and "x" in v1[i+1]:
                s = v1[i+1] 
                t=""
                for k in range(0, len(s)):
                    if s[k] != "*" and s[k] != "/" and s[k] != "x":
                        t = t + s[k]
                    if s[k] == "*" or s[k] == "/":
                        dau = s[k]
                s2 = int(t)
            elif v1[i+1] == "0":
                s2 = 0

            v1[i] = int(s1) + int(s2)
            v1[i-1] = "0"
            v1[i+1] = "0"

        elif v1[i] == "-":
            # s1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if len(v1[i-1]) == 1 and "x" in v1[i-1]:
                s1 = 1
                dau = "*"
            elif len(v1[i-1]) >= 2 and "x" in v1[i-1]:
                s = v1[i-1]  
                t="" 
                for k in range(0, len(s)):
                    if s[k] != "*" and s[k] != "/" and s[k] != "x":
                        t = t + s[k]
                    if s[k] == "*" or s[k] == "/":
                        dau = s[k]
                s1 = int(t)  
            elif v1[i-1] == "0":
                s1 = 0

            # s2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if len(v1[i+1]) == 1 and "x" in v1[i+1]:
                s2 = 1
                dau = "*"
            elif len(v1[i+1]) >= 2 and "x" in v1[i+1]:
                s = v1[i+1]   
                t=""  
                for k in range(0, len(s)):
                    if s[k] != "*" and s[k] != "/" and s[k] != "x":
                        t = t + s[k]
                    if s[k] == "*" or s[k] == "/":
                        dau = s[k]
                s2 = int(t)
            elif v1[i+1] == "0":
                s2 = 0

            v1[i] = s1 - s2
            v1[i-1] = "0"
            v1[i+1] = "0"

    total = 0
    for i in v1:
        if type(i) == int:
            total = total + i # xử lí xong vế 2 v2[]

    v1 = []
    v1.append(total)
    
    print("dau:",dau)
    print(v1)
    print(v2)

    if dau == " ":
        if v1[0] == 0:
            return v2[0] / -1
        elif v1[0] == 1:
            return v2[0]
    elif dau == "*" or dau == "/":
        if dau == "*":
            return v2[0] / v1[0]
        elif dau == "/":
            return v2[0] * v1[0]

print(solve_for_x('(x - 30) * 2 = x'))
