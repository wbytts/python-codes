
s = 'hello world'
result = []

for i in range(len(s)):
    s = s[1:] + s[:1]
    result.append(s)

print(result)
