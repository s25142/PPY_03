nums = input("Podaj liczby oddzielone przecinkiem: ").split(",")
print(nums)

num_list = []
for x in nums:
    num_list.append(int(x))

print("maksymalna:",max(num_list))
print("minimalna: ", min(num_list))