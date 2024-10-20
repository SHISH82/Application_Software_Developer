# TODO Найдите количество книг, которое можно разместить на дискете

pages = 100
line = 50
symbol = 25
bytes_for_symbol = 4

total_sum = 1.44 * 1024 * 1024

size = pages * line * symbol * bytes_for_symbol

cnt = int(total_sum / size)

print("Количество книг, помещающихся на дискету:", cnt)
