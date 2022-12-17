class Solution:
    def findDuplicate(self, nums ) -> int:
        numsDict = {}
        for number in nums:
            if number in numsDict.keys():
                return number
            else:
                numsDict[number] = True

dummyList1 = [1,2,3,4,5,6,3]
dummyList2 = [1,2,3,4,2,4,5,6,7,8]

print(Solution().findDuplicate(dummyList1))
print(Solution().findDuplicate(dummyList2))
