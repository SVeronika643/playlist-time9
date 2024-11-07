## project_5

# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * многострочная строка
#   * кортеж из двух словарей
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""


playlist_f = (
	{
        "Free Bird": 9.08, 
        "Enter Sandman": 5.31, "One" : 7.45, "Sliver" : 2.10, "Come as You Are": 3.45},
	{"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong" : 4.51, "My Hero" : 4.02},
)

#решение
# from random import sample

# def get_random_pairs(playlist,n):
#     music = {**playlist[0],**playlist[1]}
#     return sample(music.items(),n) 

#Разобьем списки
playlist_e = [
    ("Sunday","Why Does My Heart Feel so Bad?","Everlong","To Let Myself Go Golden","Daisuke","Miami","Chill Bill Lofi","The Perfect Girl","Resonance"),
    (5.09,4.23, 3.25,2.56,2.41,3.31,2.05,1.48,3.32),
]

playlist_f = {
    "Free Bird": 9.08,
    "Enter Sandman": 5.31,
    "One" : 7.45,
    "Sliver" : 2.10,
    "Come as You Are": 3.45,
	"Thunderstruck": 4.53,
    "You Shook Me All Night Long": 3.29,
    "Everlong" : 4.51,
    "My Hero" : 4.02
}




#print(get_random_pairs(playlist_f,3))

