class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for str in strs:
            previous_char = ''
            count = 1
            for ch in str:
                if ch == previous_char:
                    count += 1
                else:
                    if previous_char != '':
                        encoded_str = encoded_str + previous_char + str(count)

                previous_char = ch

            encoded_str = encoded_str + previous_char + str(count)
            encoded_str = encoded_str + '|'

        return encoded_str
            
# Read up the editorial in leetcode, not sure if this is a useful problem. editorial link : https://leetcode.com/problems/encode-and-decode-strings/editorial/.

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        for ch in s:
            
