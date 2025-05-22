# strings : sequence of chars

s = "**Py*10*"

print(s.strip('*'))
print(s.lstrip('*'))
print(s.rstrip('*'))

print(s.find('10'))

print(s.count('*'))

print(s.replace('10','thon'))

print(s.startswith('*'))
print(s.endswith(':'))

ss = 'one-two-three'
print(ss.split('-'))

sss = ['c','+','+']
print('~'.join(sss))

print(s.rjust(15))

print(s.zfill(15))

#format()
name="Zyx"
r="my name is {n}".format(n=name)
print(r)

print(name.encode())
print(b'abxyz'.decode())