'''k=[[23,"Kochi"],['OneTeam',19]]
n=k
n[0][1]="Python"
print(k)
print(n)'''

import copy
k=[[23,"Kochi"],['OneTeam',19]]
n=copy.copy(k)

n[0][1]="Python"
print(n)
print(k)