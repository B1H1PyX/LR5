N = int(input("Enter the size of the array: "))
arr = []
for i in range(N):
    elem = int(input(f"Enter an item {i + 1}: "))
    arr.append(elem)
product = 1
for i in range(0, N, 2):
    product *= arr[i]
print("Product of elements with odd indices:", product)