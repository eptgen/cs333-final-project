from math import factorial

K = 3

def choose(n, k):
	return factorial(n) / (factorial(n - k) * factorial(k))

def calc(n, p):
	global K
	result = 0
	for i in range(K, n + 1):
		to_add = choose(n, i) * (p ** i) * ((1 - p) ** (n - i))
		result += to_add
	return result

for j in range(3, 8):
	for i in range(4, 14):
		print(str(i) + ", " + str(j/10.0) + ": " + str(calc(i, j/10.0)));
