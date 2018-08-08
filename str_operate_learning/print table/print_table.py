def print_table(table):
    col_width = [0] * len(table)
    for n in range(len(table)):
        col_width[n] = len(table[n][0])
        for m in range(1, len(table[n])):
            if col_width[n] < len(table[n][m]):
                col_width[n] = len(table[n][m])
    print(col_width)

    for i in range(len(table[0])):
        single_line = ''
        for j in range(len(table)):
            if j == 0:
                single_line += table[j][i].rjust(col_width[j]) + ' '
            else:
                single_line += table[j][i].ljust(col_width[j]) + ' '
        print(single_line)


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)
