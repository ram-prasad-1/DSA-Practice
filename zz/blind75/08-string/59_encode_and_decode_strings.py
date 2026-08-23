# 59. Encode and Decode Strings (premium)
# Run: python 59_encode_and_decode_strings.py
# Time: O(N) total characters each way. Space: O(N).



# length-prefix framing survives any delimiter appearing in the payload
class Codec:
    def encode(self, strs):
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res



codec = Codec()
wire = codec.encode(["lint", "co#de", "love#4#you"])
print(wire)
print(codec.decode(wire))
