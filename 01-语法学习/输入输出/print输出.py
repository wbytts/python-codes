'''
print(value..., sep=' ', end='\n', file=sys.stdout, flush=False)
    value：可以向print传入一堆值，它会挨个打印
    sep：不同的值之间，用sep分隔
    end：所有值打印完之后，最后打印一个 end
    file：打印的目标，默认是控制台
    flush：刷新缓冲区
'''
print('hello world')

print('hello', 'world')

print('hello', 'world', sep='~')

print('hello', end='%')
print('world')

f = open('out.txt', 'w')
print('hello world', file=f)
f.close()
