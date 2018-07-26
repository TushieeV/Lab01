strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for word in strings:
    sentence = sentence + word + ' '

print(sentence)
print(' '.join(strings))
