L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[3:7])
# start:stop:step 这种写法其实是一种语法糖（给你点甜头，让你写起来简单）
# start:stop      相当于 slice(start, stop)
# start:stop:step 相当于 slice(start, stop, step)
切片 = slice(3, 7)
print(type(切片))
print(L[切片])
切片 = slice(3, 7, 2)
print(L[切片])




