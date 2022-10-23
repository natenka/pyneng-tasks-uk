# -*- coding: utf-8 -*-
"""
Завдання 4.0

Пройти всі питання в pquiz по розділу 04.
Перед проходженням питань оновити pyneng-quiz:
$ pip install -U pyneng-quiz

Запуск:
$ pquiz
"""
# -*- coding: utf-8 -*-
"""
Завдання 4.1

Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX
в формат XXXX.XXXX.XXXX (заменить : на .)
Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"
# -*- coding: utf-8 -*-
"""
Завдання 4.2

Если запустить код задания, будет такой вывод:
$ python task_4_2.py
ip nat inside source list ACL interface FastEthernet0/1 overload

Надо преобразовать строку nat таким образом, чтобы на экран была выведена такая
строка (заменен тип интерфейса с FastEthernet на GigabitEthernet и строка
переведена в нижний регистр):

$ python task_4_2.py
ip nat inside source list acl interface gigabitethernet0/1 overload

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat)
# -*- coding: utf-8 -*-
"""
Завдання 4.3

Получить из строки config такой список VLANов:
['1', '3', '10', '20', '30', '100']

Записать итоговый список в переменную result.
(именно эта переменная будет проверяться в тесте)

Полученный список result вывести на стандартный поток вывода (stdout)
с помощью print.
Тут очень важный момент, что надо получить именно список (тип данных), а не,
например, строку, которая похожа на показанный список.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
# -*- coding: utf-8 -*-
"""
Завдання 4.4

Список vlans это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка vlans нужно получить новый список уникальных номеров VLANов,
отсортированный по возрастанию номеров. Для получения итогового
списка нельзя удалять конкретные vlanы вручную.
В данном случае итоговый список должен выглядеть так:
[1, 2, 3, 4, 10, 20, 30, 100]

Записать итоговый список уникальных номеров VLANов в переменную result.
(именно эта переменная будет проверяться в тесте)

Полученный список result вывести на стандартный поток вывода (stdout)
с помощью print.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
# -*- coding: utf-8 -*-
"""
Завдання 4.5

Из строк command1 и command2 получить список VLANов, которые есть
и в команде command1 и в команде command2 (пересечение). Элементы
списка должны быть отсортированы по возрастанию.

В данном случае, результатом должен быть такой список: ['1', '3', '8']

Записать итоговый список в переменную result (именно эта переменная будет
проверяться в тесте).
В списке result вланы должны быть отсортированы по возрастанию номеров.
Для получения итогового списка нельзя удалять конкретные vlanы вручную.

Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Это задание можно выполнить не используя циклы и условия.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
# -*- coding: utf-8 -*-
"""
Завдання 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
# -*- coding: utf-8 -*-
"""
Завдання 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Подсказка: MAC-адрес без : это шестнадцатеричное число AAAABBBBCCCC.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"
# -*- coding: utf-8 -*-
"""
Завдання 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ip = "192.168.3.1"
# -*- coding: utf-8 -*-
"""
Завдання 4.9a

В задании создан список words
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]

Надо вывести на экран такую строку, которая содержит каждое ВТОРОЕ слово из
списка words, слова должны быть разделены пробелом.

Пример работы задания:
$ python task_4_9a.py
Guido Rossum working Python the 1980s

Ограничение: нельзя изменять список words.
"""
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]
# -*- coding: utf-8 -*-
"""
Завдання 4.9b

В задании создан список words
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]

Надо вывести на экран каждое слово из списка words на отдельной строке вывода.

Пример работы скрипта:
$ python task_4_9b.py
Guido
van
Rossum
began
working
on
Python
in
the
late
1980s

Ограничение: нельзя изменять список words.
Будет плюсом решить задание без использования цикла for.
"""
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]
# -*- coding: utf-8 -*-
"""
Завдання 4.9

В задании создан список words
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]

Надо вывести на экран строку, которая содержит каждое слово из списка words,
слова должны быть разделены пробелом.

Пример работы задания:
$ python task_4_9.py
Guido van Rossum began working on Python in the late 1980s

Ограничение: нельзя изменять список words.
"""
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]