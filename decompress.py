'''
Decompress a compressed string, formatted as <number>[<string>].  The decompressed string
should be <string> written <number> times.

Example input: 3[abc]4[ab]c 
Example output: abcabcabcababababc

Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

Characters allowed as input include digits, small English letters and brackets [ ].

Digits are only to represent amount of repetitions.

Letters are just letters.

Brackets are only part of syntax of writing repeated substring.

Input is always valid, so no need to check its validity.

source:
https://techdevguide.withgoogle.com/resources/compress-decompression/
'''


import re

pattern = r'\d+\[[a-zA-Z]*\]'
pattern_with_group = r'(\d+)\[([a-zA-Z]*)\]' # same as above, but grouped

def repeatstr(strin):
    m = re.match(pattern_with_group, strin)
    return int(m.groups()[0]) * m.groups()[1]

def decompress(strin):
    matches = re.findall(pattern, strin)
    while len(matches) > 0:
        for m in matches:
            strin = re.sub(m.replace('[','\\[').replace(']','\\]'), repeatstr(m), strin, 1)
        matches = re.findall(pattern, strin)
    return strin

def run_tests():
    tests = [
        ('abc', 'abc'),
        ('3[a]', 'aaa'),
        ('a3[b]', 'abbb'),
        ('xyz3[]2[b]', 'xyzbb'),
        ('3[a]2[b]1[c]0[d]', 'aaabbc'),
        ('xyz3[a]2[b]1[c]', 'xyzaaabbc'),
        ('xyz3[a]2[b]zzz', 'xyzaaabbzzz'),
        ('3[2[a]c]', 'aacaacaac'),
        ('3[2[a]2[b]c]', 'aabbcaabbcaabbc'),
        ('z3[2[a]c]z', 'zaacaacaacz'),
        ('1[1[1[1[1[a]]]]]', 'a'),
        ('x1[1[1[1[1[a]]]]2[b]]x', 'xabbx'),
        ('a100[50[]]2[bxyz]10000[]c', 'abxyzbxyzc'),
        ('10[a]0[b]100[c]', 10*'a'+ 0*'b' + 100*'c')
    ]
    for t in tests:
        td = decompress(t[0])
        print(td == t[1], ',', t[0],'-->', td)



if __name__ == '__main__':
    run_tests()