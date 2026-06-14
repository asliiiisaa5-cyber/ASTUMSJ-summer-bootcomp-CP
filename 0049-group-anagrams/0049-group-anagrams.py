class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            s = sorted(list(i))
            m = "".join(s)
            ans[m].append(i)
        return list(ans.values())

        