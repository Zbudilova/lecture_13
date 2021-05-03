def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo = recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)
        return fibo

# def recursive_nth_fibo(n):
#     first = 0
#     second = 1
#     list = [0, 1, ]
#     for i in range(0, n-1):
#         fibo = first + second
#         first = second
#         second = fibo
#         list.append(fibo)
#     return list

def main():
    n = int(input("Zadej číslo: "))
    if n <= 0:
        print("Zadal jsi 0 nebo záporné číslo.")
    else:
        for i in range(n+1):
            print(recursive_nth_fibo(i))




if __name__ == '__main__':
    main()
