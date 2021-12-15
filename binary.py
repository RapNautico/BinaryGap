def binary_gap(N):
    try: 
        b= bin(N)
        c = b.replace('0b','')
        d   = c.split('1')
        n = 0
        for i in range(0,len(d)-1):
            if(len(d[i])>n):
                n=len(d[i])
        return n
    except:
        return 0

N=binary_gap(int(input('Enter a number: ')))
print(f'The length of its longest binary space is: {N}')