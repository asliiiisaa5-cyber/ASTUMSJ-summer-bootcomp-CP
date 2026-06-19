class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        rows = len(score)
        cols = len(score[0])
        for i in range(rows):
            for j in range(0,rows-i-1):
                if score[j][k] < score[j + 1][k]:
                    score[j], score[j + 1] = score[j + 1], score[j]
                
        return score
        