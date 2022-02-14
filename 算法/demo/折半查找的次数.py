
lis = [1, 3, 9, 12, 32, 41, 45, 62, 75, 77, 82, 95, 100]
x = 82
count = 0
low = 0
high = len(lis) - 1

while True:
    mid = None
    if low + high % 2 == 1:
        mid = (low + high) // 2 + 1
    else:
        mid = (low + high) // 2

    count += 1
    if x == lis[mid]:
        print(f"找到了, {count} 次")
        break
    if x < lis[mid]:
        high = mid
    if x > lis[mid]:
        low = mid





# while True:
#     mid = lis[len(lis) // 2]
#     print(f"中间的数是{mid}")
#     count += 1
#     if mid == x:
#         print(f"找到了, 次数为{count}")
#         break
#     if mid > x:
#         print("x比中间大，去左边找")
#         lis = lis[:len(lis) // 2]
#     if mid < x:
#         print("x比中间小，去右边找")
#         lis = lis[len(lis) // 2:]
#
#     print(f"下面在 {lis} 中查找")
#     print("------")
