# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы.

def print_operation_table(operation, num_rows = 9, num_colomns = 9):
    for i in range(1, num_rows + 1):
        arr = []
        for j in range(1, num_colomns + 1):
            arr.append(str(operation(i,j)))
        print('\t'.join(arr))

print_operation_table(lambda x, y: x*y)