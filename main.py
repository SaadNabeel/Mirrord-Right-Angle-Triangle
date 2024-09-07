n = int(input("Enter a number of rows: "))

for c in range(1, n + 1):
    
    for d in range(c):
        print("*", end=" ")

    
    for space in range(2 * (n - c)):
        print(" ", end=" ")

    
    for d in range(c):
        print("*", end=" ")

    
    print()
