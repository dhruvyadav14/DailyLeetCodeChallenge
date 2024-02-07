class Solution:
    def frequencySort(self, s: str) -> str:
        mmap = collections.Counter(s)
        x = sorted(mmap, key=mmap.get, reverse=True)
        return ''.join([c*mmap[c] for c in x])
##testin
