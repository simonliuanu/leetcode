# hashset solution(O(n), O(n)):
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        s = set()
        for i in range(len(documents)):
            if documents[i] in s:
                return documents[i]
            else:
                s.add(documents[i])
        return -1

# space optimisation(O(nlogn), O(1)):
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        documents.sort()
        tmp = documents[0]
        for i in range(1, len(documents)):
            if documents[i] == tmp:
                return tmp
            else:
                tmp = documents[i]
