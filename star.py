

star=("*")

for star in range(1, 10):
    print("*"*star)

cnt=1

while cnt <= 20:
    if cnt <= 10:
        print('*' * cnt )
    else:
        print('*' * (20 - cnt))
    cnt = cnt + 1 #same as cnt+=1



