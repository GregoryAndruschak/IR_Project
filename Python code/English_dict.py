d = open('words(dirty).txt', 'r').read()
temp = ''
for char in d:
    if char.isalpha() or char == '\n':
        temp += char
dictionary = temp.split('\n')
dictionary.sort()
res = []
isFirst = True
for word in dictionary:
    same = False
    if len(word) > 1:
        t = ''
        for ch in word:
            if ch == t:
                same = True
            else:
                same = False
            t = ch
    if isFirst:
        res.append(word)
        isFirst = False
    else:
        if word == res[-1] or same:
            continue
        else:
            res.append(word)
del res[0]
out = open('words.txt', 'w')
for w in res:
    out.write(w + '\n')
out.close()
