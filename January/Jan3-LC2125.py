class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        firstRow=bank[0]
        lasers=0
        for i in range(1,len(bank)):
            currentrow=bank[i]
            mysum = currentrow.count('1')
            if mysum==0:
                continue
            firstRowSum=firstRow.count('1')
            if firstRowSum > 0:
                lasers+=mysum*firstRowSum
            firstRow=currentrow
        return lasers