n = [x for x in range(1, 11)]
n.sort(reverse=True)

print(", ".join(str(num) for num in n))