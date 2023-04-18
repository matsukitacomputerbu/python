a = input('好きな文字列:')
c = list(a)
b = int(input('左から何番目:'))
d = b-1
print(c[d])

print('a番目からb番目')
e = int(input('a番目'))
f = int(input('b番目'))
print(c[e-1:f-1])