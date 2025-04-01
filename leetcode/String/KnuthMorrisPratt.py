def constructLPS(pattern):
    pattern_len = len(pattern)
    lps = [0] * pattern_len

    j = 0
    i = 1
    while i < pattern_len:
        if pattern[j] == pattern[i]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1

    return lps

def kmp_search(txt, pattern):
    lps = constructLPS(pattern=pattern)
    txt_len = len(txt)
    pattern_len = len(pattern)
    result = []

    i = 0
    j = 0
    
    while i < txt_len:
        if txt[i] == pattern[j]:
            i += 1
            j += 1
            if j == pattern_len:
                result.append(i-j)
                j = lps[j-1]
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1

    return result
    

print(kmp_search("abcabcabead", "abcabead"))
