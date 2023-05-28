#定义边类，其中包含边的起始点及权值
class Edge():
    def __init__(self,start:str,end:str,W:int):
        self.start=start
        self.end=end
        self.w=W
#定义获取边长度函数，用于获取两点之间边的权值
def lenth(start:str,end:str):
    for e in edge:
        if (e.start == start and e.end == end) or (e.start == end and e.end == start):
            return e.w
    return float('inf')
#定义所要研究的图 包含两个列表 分别为节点和边
vertiex=['a','b','c','d','e','f']
e1=Edge('a','b',2)
e2=Edge('a','d',5)
e3=Edge('b','c',3)
e4=Edge('b','d',1)
e5=Edge('b','e',7)
e6=Edge('c','d',1)
e7=Edge('c','e',3)
e8=Edge('c','f',5)
e9=Edge('d','e',2)
e10=Edge('e','f',1)
edge=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
#利用狄杰斯特拉算法得出图的最短路
T=['a']
V=vertiex[1:]
result=[0]
edgeLen=[]
L=0
for rcount in range(len(vertiex)-1):
    if len(T)==1:
        L=0
        T.append(vertiex[1])
        for i in V:
            if lenth(T[0],i)<lenth(T[0],T[1]):
                T[-1]=i
        V.remove(T[-1])
    else:
        T.append(vertiex[rcount+1])
        for i in V:
            if lenth(T[-2],i)<lenth(T[-2],T[-1]):
                T[-1]=i
        V.remove(T[-1])
    result.append(L+lenth(T[-2],T[-1]))
    L+=lenth(T[-2],T[-1])
for i in T:
    print('a到'+i+'的距离为'+str(result[T.index(i)]))
    print('路径为'+str(T[0:T.index(i)+1]))