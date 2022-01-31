class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        for x in range(len(sentences)):
            sentences[x]=len(sentences[x].split(" "))
        return max(sentences)