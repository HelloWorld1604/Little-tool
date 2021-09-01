def checkEqualFrequency(arr): 
    only = [] 
    value = [] 
    only.append(arr[0]) 
    # phân các giá trị vào mảng only[] mỗi giá trị lấy 1 cái 
    for i in range(0, len(arr)): 
        ticket = True 
        for j in only: 
            if arr[i] == j: 
                ticket = False 
                 
        if ticket == True: 
            only.append(arr[i]) 
    # đếm xem trong mảng gốc arr[] có bao nhiêu phần tử bằng mới giá trị trong mảng only[] 
    for i in only: 
        dem = 0 
        for j in arr: 
            if i == j: 
                dem = dem + 1 
        value.append(dem) 
