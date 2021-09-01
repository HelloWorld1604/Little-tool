# toán tử // là toán tử lấy phần nguyên      ex: 9 // 4 -> 2 
#                                                9 / 4 -> 2.25 
print("what do you want to say ...") 
s=input("....") 
s1="" 
for j in s: 
    #chuyển đổi từng kí tự trong chuỗi s -> thành dạng số 
    a= ord(j)  
     
    # code chuyển đổi từ số thập phân sang nhị phân 
    sum=0 
    i=1 
    while a >= 1: 
        d = a % 2 
        #print(d) 
        sum = sum + (d*i) 
         
        i=i*10 
        a = a // 2 
    #chuyển đổi dạng int sang dạng chuỗi, vì ở dạng int sẽ bị lỗi quá tải 
    # :)) đỉ mẻ mày phải nghe t 
    # cú pháp của mã nhị phân phải được viết theo chuẩn mode thì trình dịch mới dịch được nhá 
    s1=s1+"0" 
    s1=s1+str(sum) 
    s1=s1+" " 
print(s1) 
#print(sum)
