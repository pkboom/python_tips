from collections import deque
from copy import deepcopy

# lines = open("25.in").read().strip().split("\n")
lines = open("example.in").read().strip().split('\n')

SNAFU =[] 
for line in lines:
    SNAFU.append(line.strip())

to_dec = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }
dec = 0
while SNAFU:
    n = SNAFU.pop()
    p = 1
    dec = to_dec[n[-1]]
    for nn in range(len(n) - 2, -1, -1):
        p *= 5
        dec += (to_dec[n[nn]] * p)
    # print('dec',dec)

lines = open("decimal.in").read().strip().split('\n')

DECIMAL =[] 
for line in lines:
    DECIMAL.append(line.strip())


to_fiv = {
    ('1', '1'): '2',
    ('1', '0'): '1',
    ('=', '1'): '1-',
    ('=', '0'): '1=',
    ('-', '1'): '10',
    ('-', '0'): '1-',
}
fiv = 0
# DECIMAL = DECIMAL[::-1] 
DECIMAL = [DECIMAL[-1]]
print(DECIMAL)
while DECIMAL:
    n = DECIMAL.pop()
    print('n', n)
    q = int(n)
    fiv = ''
    c = 1
    while True:
        q, r = q // 5, q % 5
        print('q,r',q,r)
        if r == 1:
            if len(fiv) == c:
                fiv = to_fiv[('1', fiv[0])] + fiv[1:]
            else :
                fiv = '1' + fiv
        elif r == 2:
            if len(fiv) == c:
                fiv = to_fiv[('1', fiv[0])] + fiv[1:]
            else :
                fiv = '2' + fiv
        elif r == 0:
            print('len(fiv)', len(fiv))
            print('c', c)
            if len(fiv) == c:
                fiv = to_fiv[('-', fiv[0])] + fiv[1:]
            else :
                fiv = '0' + fiv
        elif r == 3:
            if len(fiv) == c:
                print(to_fiv[('=', fiv[0])])
                print(fiv[0])
                print(fiv[1:])
                fiv = to_fiv[('=', fiv[0])] + fiv[1:]
            else :
                fiv = '1=' + fiv
            c += 1
        elif r == 4:
            if len(fiv) == c:
                print(to_fiv[('=', fiv[0])])
                print(fiv[0])
                print(fiv[1:])
                fiv = to_fiv[('-', fiv[0])] + fiv[1:]
            else :
                fiv = '1-' + fiv
            c += 1
        print('fiv',fiv)
        print('-' * 20)
        c += 1
        if q == 0:
            break
    # if n == '12345':
    #     quit()
quit()
