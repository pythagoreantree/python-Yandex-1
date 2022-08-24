n = int(input())

words = {}
for _ in range(n):
    s1, s2 = map(str, input().split())
    words[s1] = s2
    words[s2] = s1

word = str(input())
if word in words:
    print(words[word])