def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1,num_rows+1):
        res = []
        for j in range(1,num_columns+1):
            res.append(operation(i,j))
        print(*res, sep ='\t')

print_operation_table(lambda x, y: x*y)
