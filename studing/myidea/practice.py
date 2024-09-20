# primes.else.py
primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)

# primes.py
primes = [] # 这个列表将包含最终的质数
upto = 100 # 上限，包含此数
for n in range(2, upto + 1):
    is_prime = True # 标志，外层for循环每次迭代时都会更新
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime: # 检查标志
        primes.append(n)
print(primes)