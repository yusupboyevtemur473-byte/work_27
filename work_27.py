#33-misol
#    n = int(input("n = "))
#    a = 1
#    b = 1
#    if n >= 1:
#        print(a)
#    if n >= 2:
#        print(b)
#    for i in range(3, n + 1):
#        c = a + b
#        print(c)
#        a = b
#        b = c


#34-misol
#    n = int(input("n = "))
#    a1 = 1
#    a2 = 2
#    if n >= 1:
#        print(a1)
#    if n >= 2:
#        print(a2)
#    for k in range(3, n + 1):
#        ak = (a2 + 2*a1) / 3
#        print(ak)
#        a1 = a2
#        a2 = ak


#35-misol
#    print("\n=== For35: Ketma-ketlik (n > 2) ===")
#    n = int(input("n ni kiriting (n > 2): "))
#    if n <= 2:
#        print("n > 2 bo'lishi kerak!")
#        return
#    
#    a = [0] * (n + 1)
#    a[1] = 1
#    a[2] = 2
#    a[3] = 3
    
#    for k in range(4, n + 1):
#        a[k] = a[k-1] + a[k-2] - 2 * a[k-3]
#    
#    print("Ketma-ketlik:")
#   for i in range(1, n + 1):
#        print(f"A{i} = {a[i]}")
#
#36-misol
#    print("\n=== For36: 1^K + 2^K + ... + N^K ===")
#    n = int(input("N ni kiriting: "))
#    k = int(input("K ni kiriting: "))
 #   
#    yigindi = 0
#    for i in range(1, n + 1):
#        yigindi += i ** k
#    
#    print(f"1^{k} + 2^{k} + ... + {n}^{k} = {yigindi}")
#
##37-misol
#    print("\n=== For37: 1^1 + 2^2 + ... + N^N ===")
#    n = int(input("N ni kiriting: "))
#    
#    yigindi = 0
#    for i in range(1, n + 1):
#        yigindi += i ** i
#    
#    print(f"1¹ + 2² + ... + {n}ⁿ = {yigindi}")
#
##38-misol
#    print("\n=== For38: 1^N + 2^(N-1) + ... + N^1 ===")
#    n = int(input("N ni kiriting: "))
#    
#    yigindi = 0
#    for i in range(1, n + 1):
#        yigindi += i ** (n + 1 - i)
#    
#    print(f"1^{n} + 2^{n-1} + ... + {n}^1 = {yigindi}")
#
##39-misol
#    print("\n=== For39: Har bir son o‘z qiymaticha chiqariladi ===")
#    a = int(input("A ni kiriting: "))
#    b = int(input("B ni kiriting (A < B): "))
 #   
 #   if a >= b:
 #       print("A < B bo'lishi kerak!")
#        return
#    
#    print("Natija:")
#    for son in range(a, b + 1):
#        print(f"{son} " * son, end="")
#    print()
#
##40-misol
#    print("\n=== For40: A → 1 marta, A+1 → 2 marta, ... ===")
#    a = int(input("A ni kiriting: "))
#    b = int(input("B ni kiriting (A < B): "))
#    
#    if a >= b:
#        print("A < B bo'lishi kerak!")
#        return
#    
#    print("Natija:")
#    for son in range(a, b + 1):
##        marta = son - a + 1
#        print(f"{son} " * marta, end="")
#    print()
