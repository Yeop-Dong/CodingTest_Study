import collections

s = input()
s = s.upper()
k = collections.Counter(s).most_common()

if len(k) > 1:
    if k[0][1] == k[1][1]:
        print('?')
    else:
        print(k[0][0])
else:
    print(k[0][0])