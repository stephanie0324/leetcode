class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        columns = []
        cnt = 0
        
        for i in range(len(grid[0])):
            tmp = []
            for j in range(len(grid[0])):
                tmp.append(grid[j][i])
            columns.append(tmp)

        for row in grid:
            if row in columns:
                cnt+=columns.count(row)
        return cnt
                