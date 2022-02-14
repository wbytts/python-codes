
def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res

print(intersect('hello world', 'how are you'))
