def isPermutation(s1, s2):
    alphabet = [0] * 26
    
    if len(s1) != len(s2): 
        return False
    for ch1, ch2 in zip(s1.lower(), s2.lower()):
        alphabet[ord(ch1)-97] += 1
        alphabet[ord(ch2)-97] -= 1
    
    return sum(alphabet) == 0