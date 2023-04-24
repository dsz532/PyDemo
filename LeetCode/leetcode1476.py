class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rec=rectangle
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row2+1)[row1:]:
            for j in range(col2+1)[col1:]:
                self.rec[i][j]=newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]
pass

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

sub=SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(sub.getValue(0, 2))
print(sub.updateSubrectangle(0, 0, 3, 2, 5))
print(sub.getValue(0, 2))

