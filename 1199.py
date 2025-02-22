N = input().strip()

while N != '-1':
    if N[:2].lower() == '0x':  
        res = int(N, 16)
        print(res)
    else:  
        res = hex(int(N))[2:].upper()  
        print(f"0x{res}")  
    
    N = input().strip()
