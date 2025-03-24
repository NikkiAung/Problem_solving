res = []
solu = [1,2,3]
# res.append(solu)
res.append(solu[:])
solu[0] = 99
print(res)