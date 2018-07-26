strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for word in strings:
    if (word != 'together'):
        sentence = sentence + word + ' '
    else:
        sentence = sentence + word

print(sentence)
print(' '.join(strings))
