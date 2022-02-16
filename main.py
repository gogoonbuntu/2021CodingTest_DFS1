N, M = list(map(int, input().split()))
field = []
#visited = [ False for i in range(N * M) ]
result = 0
for i in range(N):
	i = list(map(int, input()))
	field.append(i)

print(field)

def dfs(ix, iy):
	if ix<0 or iy<0 or ix>=N or iy>=M:
		return False
	if field[ix][iy]==0:
		field[ix][iy]=1
		dfs(ix-1, iy)
		dfs(ix, iy-1)
		dfs(ix+1, iy)
		dfs(ix, iy+1)
		return True
	return False

for i in range(N):
	for j in range(M):
		if dfs(i, j)==True:
			result+=1

print(result)