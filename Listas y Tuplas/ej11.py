n, m, p_escalar = [1,2,3], [-1,0,2], 0
for i in range(len(n)): p_escalar += n[i] * m[i]
print(p_escalar)