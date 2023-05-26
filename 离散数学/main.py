#定义边类，其中包含边的起始点及权值
class Edge():
    def __init__(self,start:str,end:str,W:int):
        self.start=start
        self.end=end
        self.w=W
#定义判断边存在函数，用于判断两点间是否存在边
def isEdge(start:str,end:str):
    c = 0
    for e in edge:
        if e.start == start and e.end == end:
            c = 0
            break
        else:
            c = 1
    return c
#定义获取边长度函数，用于获取两点之间边的权值
def lenth(start:str,end:str):
    for e in edge:
        if e.start == start and e.end == end:
            return e.w
    return 0
#定义寻找对应节点函数，用于查找边权值对应的终点
def find_num(matrix:list[list], num:int,end_point:int):
    for i in range(len(matrix)):
        if matrix[i][end_point]==num:
            return i
#定义所要研究的图 包含两个列表 分别为节点和边
vertiex=['a','b','c','d','e']
e1=Edge('a','b',2)
e2=Edge('a','d',10)
e3=Edge('b','c',3)
e4=Edge('b','d',7)
e5=Edge('c','d',6)
e6=Edge('c','e',4)
e7=Edge('e','d',5)
edge=[e1,e2,e3,e4,e5,e6,e7]
#利用狄杰斯特拉算法得出图的最短路矩阵
T=['a']
V=vertiex[:]
result=[]
rcount=0
L=0
for i in vertiex:
    if isEdge(T[-1],i)==0:
        T.append(i)
    V.remove(i)
    if len(T)==1:
        L=0
    else:
        L+=lenth(T[-2],T[-1])
    result.append([])
    for j in V:
        if isEdge(i,j)!=0:
            result[rcount].append(float('inf'))
        else:
            result[rcount].append(L+lenth(i,j))
    rcount+=1
#将获得的矩阵进行变换，便于寻找最短路
long=len(result)-1
res=[]
for i in range(long):
    res.append([])
    for j in reversed(range(long)):
        if j-i>-1:
            res[i].append(result[i][j-i])
        else:
            res[i].append(float('inf'))
    res[i].reverse()
temp=list(map(list,zip(*res)))
#寻找a与各点间的距离和最短路
for i in range(long):
    temp[i].sort()
    print('a与%s的距离为%d'%(vertiex[i+1],temp[i][0]))
    loc=find_num(res,temp[i][0],i)
    way=vertiex[0:loc+1]
    way.append(vertiex[i+1])
    print('路径为')
    print(way)