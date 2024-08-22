# Домашняя работа по уроку "Модули и пакеты"

# обращение в модуле fake_math к функции divide и переименование её в данном модуле в divf
from fake_math import divide as divf
# обращение в модуле true_math к функции divide и переименование её в данном модуле в divt
from true_math import divide as divt

# Исходный код
result1 = divf(69, 3)
result2 = divf(3, 0)
result3 = divt(49, 7)
result4 = divt(15, 0)

# вывод результатов работы на консоль
print(result1)
print(result2)
print(result3)
print(result4)
