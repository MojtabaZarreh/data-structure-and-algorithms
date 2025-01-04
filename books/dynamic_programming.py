word = 'fosh'
words = ['fish', 'vista']

table = [[0 for _ in range(len(words[0]))] for _ in range(len(word))]

for i in range(1, len(word)):
    for j in range(1, len(words[0])):
        if word[i] == words[0][j]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = 0

# for i in range(1, len(word)):
#     for j in range(1, len(words[0])):
#         if word[i] == words[0][j]:
#             table[i][j] = table[i-1][j-1] + 1
#         else :
#             table[i][j] = max(table[i-1][j], table[i][j-1])

for row in table:
    print(row)