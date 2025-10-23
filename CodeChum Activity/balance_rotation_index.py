n = int(input("Enter array size: "))
print("Enter the elements:")
arr = list(map(int, input().split()))

min_sum = None
min_index = 0

for r in range(n):
    rotated = arr[r:] + arr[:r]

    weighted_sum = sum(i * rotated[i] for i in range(n))

    if min_sum is None or weighted_sum < min_sum:
        min_sum = weighted_sum
        min_index = r

print(f"Balanced Rotation Index: {min_index}")
