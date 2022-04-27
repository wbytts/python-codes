# 双端队列，可以快速的从另外一侧追加和推出对象

lst = deque([1,2,3,4,5,6,7])
lst.append(8)   # 末尾增加
lst.appendleft(0) # 首加
lst.pop()		# 末尾删除
lst.popleft()	# 首删
