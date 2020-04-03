N = int(input())

# 6*(n-2)+2 = 6*n-10 부터 12*n-17까지
try:
    n = int((N+10)/6)
    print(n)
except:
    n = float((N+10)/6)
    print(int(n))
