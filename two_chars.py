import sys


def check_str(s):
    if len(s) < 2 or s[0] == s[1]:
        return False
    ch1 = s[0]
    ch2 = s[1]

    for i, ch in enumerate(s):
        if i != 0:
            if ch != ch1 and ch != ch2:
                return False
            if ch == s[i-1]:
                return False
    return True

def remove_others(s, ch1, ch2):
    new_str = []
    for ch in s:
        if ch == ch1 or ch == ch2:
            new_str.append(ch)
    return ''.join(new_str)

def two_chars(s):
    distinct = []
    for ch in s:
        if ch not in distinct:
            distinct.append(ch)
    max_len = 0
    if len(distinct) <= 2:
        if check_str(s):
            return len(s)
        return 0
    
    for i in range(len(distinct)):
        ch1 = distinct[i]
        for n in range(i, len(distinct)):
            ch2 = distinct[n]
            removed = remove_others(s, ch1, ch2)
            if check_str(removed):
                max_len = max(len(removed), max_len)
    return max_len




if __name__ == '__main__':
    s_len = int(input().strip())
    s = input().strip()

    print(two_chars(s))

