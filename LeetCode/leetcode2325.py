class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key1 = sorted(list(set(key)), key=key.index)
        for i in range(key1.count(' ')):
            key1.remove(' ')
        key0 = list('abcdefghijklmnopqrstuvwxyz')
        dic = dict(zip(key1, key0))
        d={' ':' '}
        dic.update(d)
        decode = []
        message=list(message)
        for i in range(len(message)):
            message[i]=dic[message[i]]
        ans=''.join(message)
        return ans
pass
solu = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(solu.decodeMessage(key, message))
