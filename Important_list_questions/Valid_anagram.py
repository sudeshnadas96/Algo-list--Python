# Given two strings (s) and (t) , return True if (s) is an anagram of (t), and return False otherwise
def anagram(s , t):
    n = len(s)
    m = len(t)
    s_char_freq = {}
    t_char_freq = {}
    for i in range(n):
        if s[i] in s_char_freq:
            s_char_freq[s[i]] += 1
            break
        #else:
        s_char_freq[s[i]] = 1
    for j in range(m):
        if t[j] in t_char_freq:
            t_char_freq[t[j]] += 1
            break
        #else:
        t_char_freq[t[j]] = 1
    return s_char_freq == t_char_freq
print(anagram('silent' , 'listennnnnnnnnn')) #False
print(anagram('race' , 'care')) #True
print(anagram('mat' , 'cat')) #False