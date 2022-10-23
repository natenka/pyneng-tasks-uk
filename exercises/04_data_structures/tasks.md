# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.2a

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
выводить на экран строки из конфига, исключая некоторые.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_2a.py config_sw1.txt

Вывести на стандартный поток вывода команды из переданного конфигурационного
файла, исключая строки, которые начинаются с '!' и строки в которых содержатся
слова из списка ignore.
Вывод не должен содержать пустые строки.

Пример вывода:
$ python task_7_2a.py config_sw1.txt
version 15.0
hostname sw1
interface Ethernet0/0
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet0/2
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet1/0
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

"""

ignore = ["duplex", "alias", "configuration", "end", "service"]
# -*- coding: utf-8 -*-
"""
Завдання 7.2b

Скопировать код из задания 7.2a и переделать его: вместо вывода на стандартный
поток вывода, скрипт должен записать полученные строки в файл.

Имена файлов нужно передавать как аргументы скрипту:
1 аргумент имя исходного файла конфигурации
2 аргумент имя итогового файла конфигурации, в который будут записаны строки

Пример вызова:
$ python task_7_2b.py config_sw1.txt new_config.txt

При этом, должны быть отфильтрованы строки со словами, которые содержатся в списке ignore
и строки, которые начинаются на '!'.
"""

ignore = ["duplex", "alias", "configuration", "end", "service"]
# -*- coding: utf-8 -*-
"""
Завдання 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
выводить на экран строки из конфига, исключая некоторые.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_2.py config_sw1.txt

Вывести на стандартный поток вывода команды из переданного конфигурационного
файла, исключая строки, которые начинаются с '!'.

Вывод должен быть без пустых строк.

Пример вывода:
$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт: Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Подсказка: Для сортировки удобно сначала создать список списков такого типа,
а потом сортировать.

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

Сортировка должна быть по первому элементу (vlan), а если первый элемент одинаковый,
то по второму. Так работает по умолчанию функция sorted и метод sort, если сортировать
список списков выше.

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Приклад роботи скрипта:
$ python task_7_3b.py
Введите номер влана: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.4

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
получать из него информацию о портах в режиме trunk и вланах, которые настроены
на этих портах.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_4.py config_trunk_sw2.txt
$ python task_7_4.py config_trunk_sw3.txt

Передавать имя файла как аргумент скрипту. Указанный конфиг надо обработать и
получить словарь портов в режиме trunk, где ключи номера портов,
а значения список разрешенных VLAN (список строк).

Записать итоговый словарь в переменную trunk_dict (именно эта переменная будет
проверяться в тесте). По желанию можно выводить словарь на экран, тест
проверяет только содержимое переменной. Тут удобно выводить словарь с помощью pprint.

Например, для файла config_trunk_sw2.txt должен получиться такой словарь:

$ python task_7_4.py config_trunk_sw2.txt
{'FastEthernet0/1': ['100', '200'],
 'FastEthernet0/3': ['100', '300', '400', '500', '600'],
 'FastEthernet0/4': ['400', '500', '600']}

Для файла config_trunk_sw3.txt должен получиться такой словарь:
$ python task_7_4.py config_trunk_sw3.txt
{'FastEthernet0/1': ['10', '20', '21', '22'],
 'FastEthernet0/2': ['10', '13', '1450', '1451', '1452'],
 'FastEthernet0/6': ['40', '50', '60']}


Проверить работу функции на примере файлов config_trunk_sw2.txt и config_trunk_sw3.txt.
Убедиться, что для этих файлов получаются правильные словари.

Подсказка по синтаксису cisco: в этом задании считаем, что интерфейс находится
в режиме trunk, если у него настроена команда switchport trunk allowed vlan.
"""
from pprint import pprint
# -*- coding: utf-8 -*-
"""
Завдання 7.5

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
получать из него информацию о конфигурации интерфейсов.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_5.py config_trunk_sw2.txt
$ python task_7_5.py config_trunk_sw3.txt

Передавать имя файла как аргумент скрипту. Указанный конфиг надо обработать и
получить словарь где ключи имя интерфейса, а значение список команд, которые
начинаются на switchport. Команды в списке должны быть без пробела в начале
строки и перевода строки в конце.

Записать итоговый словарь в переменную interface_dict (именно эта переменная будет
проверяться в тесте). По желанию можно выводить словарь на экран, тест
проверяет только содержимое переменной. Тут удобно выводить словарь с помощью pprint.

Например, для файла config_trunk_sw2.txt должен получиться такой словарь:

$ python task_7_5.py config_trunk_sw2.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,200',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,300,400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/4': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport mode access',
                     'switchport access vlan 20']}

Для файла config_trunk_sw3.txt должен получиться такой словарь:
$ python task_7_5.py config_trunk_sw3.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,20,21,22',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,13,1450,1451,1452',
                     'switchport mode trunk'],
 'FastEthernet0/3': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/4': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 40,50,60',
                     'switchport mode trunk'],
 'FastEthernet0/7': ['switchport mode access'],
 'FastEthernet0/8': ['switchport mode access']}

Проверить работу функции на примере файлов config_trunk_sw2.txt и config_trunk_sw3.txt.
Убедиться, что для этих файлов получаются правильные словари.

"""
from pprint import pprint
# -*- coding: utf-8 -*-
"""
Завдання 9.0

Пройти всі питання в pquiz по розділу 09.
Перед проходженням питань оновити pyneng-quiz:
$ pip install -U pyneng-quiz

Запуск:
$ pquiz
"""

# -*- coding: utf-8 -*-
"""
Завдання 9.1

Создать функцию convert_mac, которая конвертирует MAC-адрес из формата
1a1b.2c2d.3e3f в 1a:1b:2c:2d:3e:3f.

У функции должен быть один параметр: mac_address, который ожидает строку с
MAC-адресом в формате 1a1b.2c2d.3e3f.  Функция должна возвращать строку с
MAC-адресом в формате 1a:1b:2c:2d:3e:3f.

Проверить работу функции на разных MAC-адресах в списке mac_list.

В этом задании можно не проверять, что MAC-адрес, который передается функции
как аргумент записан в формате "aaaa.bbbb.cccc". Это будет сделано в задании 11го
раздела.

Пример работы функции:

In [4]: convert_mac("1a1b.2c2d.3e3f")
Out[4]: '1a:1b:2c:2d:3e:3f'

In [5]: convert_mac("1111.2222.3333")
Out[5]: '11:11:22:22:33:33'

In [6]: mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

In [7]: for m in mac_list:
   ...:     print(convert_mac(m))
   ...:
1a:1b:2c:2d:3e:3f
aa:aa:bb:bb:cc:cc
11:11:22:22:33:33

В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

# -*- coding: utf-8 -*-
"""
Завдання 9.2

Создать функцию check_ip, которая проверяет, что строка, которая была передана функции,
содержит правильный IP-адрес.

Адрес считается правильным, если он:
- состоит из 4 чисел (а не букв или других символов)
- числа разделены точкой
- каждое число в диапазоне от 0 до 255

У функции должен быть один параметр ip_addr, который ожидает строку с IP-адресом.
Функция должна возвращать True если адрес правильный, False иначе.

Проверить работу функции на строках в списке ip_list.
Пример работы функции:
In [3]: check_ip("10.1.1.1")
Out[3]: True

In [4]: check_ip("10.500.1.1")
Out[4]: False

In [5]: check_ip("10.a.b.1")
Out[5]: False

In [6]: check_ip("10.1.1.1.")
Out[6]: False

In [7]: check_ip("10.1.1.1.1")
Out[7]: False

In [8]: check_ip("10.1.1.")
Out[8]: False

In [9]: check_ip("10.1.1")
Out[9]: False

In [10]: for ip in ip_list:
    ...:     print(check_ip(ip))
    ...:
True
False
False
True
False

В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

ip_list = ["10.1.1.1", "10.3.a.a", "500.1.1.1", "150.168.100.1", "62.150.240.300"]
# -*- coding: utf-8 -*-
"""
Завдання 9.3a

Создать функцию clean_config.  Функция clean_config обрабатывает
конфигурационный файл и возвращает список команд из указанного
конфигурационного файла.

У функции clean_config должны быть такие параметры:
* config_filename - ожидает как аргумент имя конфигурационного файла
* ignore_lines - ожидает как аргумент список строк, которые надо игнорировать.
  Значение по умолчанию None. То есть по умолчанию никакие строки не игноруются
* ignore_exclamation - контролирует то игнорируются ли строки, которые
  начинаются с восклицательного знака. Возможные значения True/False.
  Значение по умолчанию True
* strip_lines - контролирует удаление пробела в начале строки и перевода строки в конце.
  True - удалить пробелы в начале строки и перевод в конце, False - не удалять.
  Возможные значения True/False. Значение по умолчанию False
* delete_empty_lines - контролирует удаление пустых строк. True - удалять, False - нет.
  Возможные значения True/False. Значение по умолчанию True

Для удобства все значения по умолчанию для необязательных параметров:
* ignore_lines - None
* ignore_exclamation - True
* delete_empty_lines - True
* strip_lines - False

Функция clean_config обрабатывает конфигурационный файл и возвращает список
команд из указанного конфигурационного файла:
* если в параметр ignore_lines передан список строк - исключая строки конфигурации,
  в которых содержатся строки из списка ignore_lines.
* если ignore_exclamation равно True - исключая строки которые начинаются с '!'
* если delete_empty_lines равно True - исключая пустые строки
* если strip_lines равно True - строки в списке должны быть без пробелов в начале
  и перевода строки в конце строки


Пример работы функции:
In [3]: clean_config("config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list, ignore_exclamation=False)
Out[3]:
['hostname PE_r3',
 '!',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 '!',
 '!',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 '!',
 '!',
 '!',
 'alias configure sh do sh',
 '!',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']

In [4]: clean_config("config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list)
Out[4]:
['hostname PE_r3',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 'alias configure sh do sh',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']

In [5]: clean_config("config_r3_short.txt", strip_lines=True, delete_empty_lines=False)
Out[5]:
['hostname PE_r3',
 '',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 '',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 '',
 'alias configure sh do sh',
 'alias exec ospf sh run | s ^router ospf',
 'alias exec bri show ip int bri | exc unass',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

# -*- coding: utf-8 -*-
"""
Завдання 9.3

Создать функцию clean_config.

У функции clean_config должно быть два параметра:
* config_filename - ожидает как аргумент имя конфигурационного файла
* ignore_lines - ожидает как аргумент список строк, которые надо игнорировать

Функция clean_config обрабатывает конфигурационный файл и возвращает список
команд из указанного конфигурационного файла, исключая строки конфигурации,
которые начинаются с '!' и строки конфигурации в которых содержатся строки из
списка ignore_lines.
Команды в списке должны быть без перевода строки в конце строки.

Проверить работу функции на примере файла config_sw1.txt, config_sw2.txt,
config_r1.txt и списка ignore_list.

Пример работы функции:
In [2]: clean_config("config_r2_short.txt", ignore_list)
Out[2]:
['version 15.2',
 'hostname PE_r2',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 'ip access-list standard LDP',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'line con 0',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 'line aux 0',
 'line vty 0 4',
 ' login',
 ' transport input all']

In [7]: clean_config("config_r2_short.txt", ["ip", "service", "line"])
Out[7]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'alias exec ospf sh run | s ^router ospf',
 'alias exec id show int desc',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']

In [8]: clean_config("config_r2_short.txt", ["ip", "service", "line", "alias"])
Out[8]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

# -*- coding: utf-8 -*-
"""
Завдання 9.4

Создать функцию generate_access_dict, которая генерирует конфигурацию
для access-портов.

У функции должно быть два параметра:
* intf_vlan_dict - ожидает как аргумент словарь с соответствием интерфейс-VLAN
  (пример access_dict)
* access_template - ожидает как аргумент список строк, которые надо добавить
  для каждого интерфейсы (пример cmd_list)

Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_cmd_list. В конце строк в списке не должно быть
символа перевода строки.
Если в шаблоне access_template есть команда switchport access vlan, добавить к
ней номер влана указанный в словаре intf_vlan_dict

Проверить работу функции на примере словаря access_dict и списка команд
access_cmd_list.  Если предыдущая проверка прошла успешно, проверить работу
функции еще раз на словаре access_dict_2 и списке команд cmd_list и убедиться,
что в итоговом списке правильные номера интерфейсов и вланов.

Пример работы функции

In [4]: generate_access_dict(access_dict, cmd_list)
Out[4]:
['interface FastEthernet0/12',
 'switchport mode access',
 'switchport access vlan 10',
 'interface FastEthernet0/14',
 'switchport mode access',
 'switchport access vlan 11']

In [6]: generate_access_config(access_dict_2, access_cmd_list)
Out[6]:
['interface FastEthernet0/3',
 'switchport mode access',
 'switchport access vlan 100',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/7',
 'switchport mode access',
 'switchport access vlan 101',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/9',
 'switchport mode access',
 'switchport access vlan 107',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/10',
 'switchport mode access',
 'switchport access vlan 111',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable']


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
access_dict = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}
access_dict_2 = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/9": 107,
    "FastEthernet0/10": 111,
}

access_cmd_list = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
cmd_list = ["switchport mode access", "switchport access vlan"]
# -*- coding: utf-8 -*-
"""
Завдання 9.5a

Сделать копию функции generate_trunk_config из задания 9.5

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict и шаблона trunk_cmd_list.

Пример работы функции
In [2]: pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
{'FastEthernet0/1': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 10,20,30'],
 'FastEthernet0/2': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 11,30'],
 'FastEthernet0/4': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 17']}

В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""


trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
# -*- coding: utf-8 -*-
"""
Завдання 9.5

Создать функцию generate_trunk_config, которая генерирует
конфигурацию для trunk-портов.

У функции должны быть такие параметры:

- intf_vlan_dict: ожидает как аргумент словарь с соответствием интерфейс-VLANы
  (пример trunk_dict)
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
  списка команд (пример trunk_cmd_list)

Функция должна возвращать список команд с конфигурацией на основе указанных портов
и шаблона trunk_cmd_list. В конце строк в списке не должно быть символа
перевода строки.
Если в шаблоне trunk_template есть команда switchport trunk allowed vlan, добавить к
ней вланы указанные в словаре intf_vlan_dict.

Проверить работу функции на примере словаря trunk_dict и списка команд trunk_cmd_list.
Если предыдущая проверка прошла успешно, проверить работу функции еще раз
на словаре trunk_dict_2 и убедится, что в итоговом списке правильные номера
интерфейсов и вланов.


Пример работы функции
In [8]: generate_trunk_config(trunk_dict, trunk_cmd_list)
Out[8]:
['interface FastEthernet0/1',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 10,20,30',
 'interface FastEthernet0/2',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 11,30',
 'interface FastEthernet0/4',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 17']

In [9]: generate_trunk_config(trunk_dict_2, trunk_cmd_list)
Out[9]:
['interface FastEthernet0/11',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 120,131',
 'interface FastEthernet0/15',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 111,130',
 'interface FastEthernet0/14',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 117']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_dict_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}
# -*- coding: utf-8 -*-
"""
Завдання 9.6a

Сделать копию функции get_int_vlan_map из задания 9.6.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
Пример работы функции
In [2]: get_int_vlan_map("config_sw2.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30,
  'FastEthernet1/3': 1,
  'FastEthernet2/0': 1,
  'FastEthernet2/1': 1},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [4]: access, trunk = get_int_vlan_map("config_sw2.txt")

In [5]: access
Out[5]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30,
 'FastEthernet1/3': 1,
 'FastEthernet2/0': 1,
 'FastEthernet2/1': 1}

In [6]: trunk
Out[6]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""
# -*- coding: utf-8 -*-
"""
Завдання 9.6

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access
  VLAN (числа)
* словарь портов в режиме trunk, где ключи номера портов, а значения список
  разрешенных VLAN (список чисел)

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Пример работы функции
In [2]: get_int_vlan_map("config_sw1.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [3]: access, trunk = get_int_vlan_map("config_sw1.txt")

In [4]: access
Out[4]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30}

In [5]: trunk
Out[5]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""
# -*- coding: utf-8 -*-
"""
Завдання 9.7

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (команды которые НЕ начинаются с пробела), будут ключами.
* Если у команды верхнего уровня есть подкоманды (команды которые начинаются с
  пробела), они должны быть в значении у соответствующего ключа, в виде списка
  (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', пустые строки, а также строки в которых содержатся слова из списка ignore.

Пример работы функции:
In [3]: pprint(convert_config_to_dict("config_r2_short.txt"), sort_dicts=False)
{'version 15.2': [],
 'no service timestamps debug uptime': [],
 'no service timestamps log uptime': [],
 'hostname PE_r2': [],
 'no ip http server': [],
 'no ip http secure-server': [],
 'ip route 10.2.2.2 255.255.255.255 Tunnel0': [],
 'ip access-list standard LDP': ['deny   10.0.0.0 0.0.255.255',
                                 'permit 10.0.0.0 0.255.255.255'],
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32': [],
 'mpls ldp router-id Loopback0 force': [],
 'control-plane': [],
 'line con 0': ['exec-timeout 0 0',
                'privilege level 15',
                'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all']}

In [4]: pprint(convert_config_to_dict("config_sw1.txt"), sort_dicts=False)
{'version 15.0': [],
 'service timestamps debug datetime msec': [],
 'service timestamps log datetime msec': [],
 'no service password-encryption': [],
 'hostname sw1': [],
 'interface FastEthernet0/0': ['switchport mode access',
                               'switchport access vlan 10'],
 'interface FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 100,200',
                               'switchport mode trunk'],
 'interface FastEthernet0/2': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 100,300,400,500,600',
                               'switchport mode trunk'],
 'interface FastEthernet1/0': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet1/1': ['switchport mode access',
                               'switchport access vlan 30'],
 'interface FastEthernet1/2': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 400,500,600',
                               'switchport mode trunk'],
 'interface Vlan100': ['ip address 10.0.100.1 255.255.255.0'],
 'line con 0': ['exec-timeout 0 0',
                'privilege level 15',
                'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all'],
 'end': []}


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""
ignore = ["duplex", "alias", "configuration"]
# -*- coding: utf-8 -*-
"""
Завдання 11.0

Пройти всі питання в pquiz по розділу 11.
Перед проходженням питань оновити pyneng-quiz:
$ pip install -U pyneng-quiz

Запуск:
$ pquiz
"""

# -*- coding: utf-8 -*-
"""
Завдання 11.1a

Создать функцию convert_mac_list которая конвертирует список MAC-адресов из
разных форматов в 1a:1b:2c:2d:3e:3f.

Конвертация MAC-адресов должна выполняться с помощью функции convert_mac из
задания 11.1. При этом нельзя копировать код функции convert_mac.

У функции convert_mac_list должно быть два параметра:
* mac_list - ожидает как аргумент список с MAC-адресами
* strict - параметр, который контролирует, что делать с неправильными
  MAC-адресами. Возможные значения True/False. Значение по умолчанию False.

Если все MAC-адреса правильные, функция должна вернуть список этих же
MAC-адресов, но в формате 1a:1b:2c:2d:3e:3f. Если какие-то MAC-адреса
неправильные (функция convert_mac сгенерировала исключение ValueError), в
зависимости от параметра strict надо:
* если strict равен True - не перехватывать исключение ValueError из функции
  convert_mac
* если strict равен False - игнорировать неправильные MAC-адреса и добавить в
  список только те, которые прошли проверку

Пример работы функции:

In [9]: convert_mac_list(["1a1b.2c2d.3e3f", "111122223333", "11-11-22-22-33-33"], strict=False)
Out[9]: ['1a:1b:2c:2d:3e:3f', '11:11:22:22:33:33', '11:11:22:22:33:33']

In [10]: convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"], strict=False)
Out[10]: ['1a:1b:2c:2d:3e:3f', '11:11:22:22:33:33']

In [11]: convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"], strict=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [11], in <cell line: 1>()
----> 1 convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"], strict=True)
...
ValueError: '1111WWWW3333' does not appear to be a MAC address
"""
# -*- coding: utf-8 -*-
"""
Завдання 11.1

Создать функцию convert_mac которая конвертирует mac-адрес из разных форматов в
1a:1b:2c:2d:3e:3f.
У функции должен быть один параметр: mac_address, который ожидает строку с
MAC-адресом в одном из форматов ниже.  Функция должна возвращать строку с
MAC-адресом в формате 1a:1b:2c:2d:3e:3f.

Должна поддерживаться конвертация из таких форматов:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a-1b-2c-2d-3e-3f
* 1a.1b.2c.2d.3e.3f
* 1a1b-2c2d-3e3f
* 1a:1b:2c:2d:3e:3f (оставить без изменений)

Функция также должна проверять, что строка, которая была передана функции,
содержит правильный MAC-адрес. MAC-адрес считается правильным, если он:
- записан в одном из поддерживаемых форматов
- каждый символ, кроме разделителей ":,-.", это символ в диапазоне a-f или 0-9
- не считая разделители, в MAC-адресе должно быть 12 символов

Если как аргумент была передана строка, которая не содержит правильный
MAC-адрес, сгенерировать исключение ValueError (... должно быть заменено на
переданное значение, примеры ниже): ValueError: '...' does not appear to be a
MAC address

Проверить работу функции на разных MAC-адресах в списке mac_list.

Пример работы функции:

In [2]: convert_mac("1a1b.2c2d.3e3f")
Out[2]: '1a:1b:2c:2d:3e:3f'

In [3]: convert_mac("1111.2222.3333")
Out[3]: '11:11:22:22:33:33'

In [4]: convert_mac("111122223333")
Out[4]: '11:11:22:22:33:33'

In [5]: convert_mac("1111-2222-3333")
Out[5]: '11:11:22:22:33:33'

In [6]: convert_mac("1111-2222-33")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [6], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33")
...
ValueError: '1111-2222-33' does not appear to be a MAC address


In [7]: convert_mac("1111-2222-33WW")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33WW")
...
ValueError: '1111-2222-33WW' does not appear to be a MAC address

"""
"""
Завдання 11.2

Создать функцию prompt_user_ip которая запрашивает пользователя ввод IP-адреса,
проверяет правильность введенного адреса и, если он неправильный, запрашивает
адрес снова. Если пользователь ввел правильный IP-адрес, функция возвращает его.

У функции prompt_user_ip должны быть такие параметры:
* max_retry - максимальное количество попыток ввода IP-адреса. Значение по умолчанию 5.
* ensure_unicast - если параметру передано значение True, адрес должен быть не
  только правильным в целом, но и должен быть именно unicast адресом, то есть
  первый октет адреса должен быть в диапазоне 1-223.  Возможные значения
  True/False. Значение по умолчанию False.

IP-адрес считается правильным, если он:
- состоит из 4 чисел (а не букв или других символов)
- числа разделены точкой
- каждое число в диапазоне от 0 до 255


Пример работы функции:

In [7]: prompt_user_ip(max_retry=5, ensure_unicast=False)
Введите правильный IP-адрес: 10.1.1.1.1
Неправильный IP-адрес
Введите правильный IP-адрес: 10.1.1.1
Out[7]: '10.1.1.1'

In [8]: prompt_user_ip(max_retry=5, ensure_unicast=False)
Введите правильный IP-адрес: 110.1.500.1
Неправильный IP-адрес
Введите правильный IP-адрес: 4.4.4.4
Out[8]: '4.4.4.4'

In [9]: prompt_user_ip(max_retry=3, ensure_unicast=False)
Введите правильный IP-адрес: a
Неправильный IP-адрес
Введите правильный IP-адрес: a
Неправильный IP-адрес
Введите правильный IP-адрес: a
Неправильный IP-адрес
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: После 3 попыток не был введен правильный адрес

In [10]: prompt_user_ip(max_retry=5, ensure_unicast=True)
Введите правильный IP-адрес: 255.255.255.255
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 10.1.1.1
Out[10]: '10.1.1.1'

In [12]: prompt_user_ip(max_retry=3, ensure_unicast=True)
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: После 3 попыток не был введен правильный адрес

"""
# -*- coding: utf-8 -*-
"""
Завдання 11.3

Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show
cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как
аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все
содержимое файла в строку, а затем передать строку как аргумент функции (как
передать вывод команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция
должна работать и на других файлах (тест проверяет работу функции на выводе из
sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Пример работы функции
In [3]: with open("sh_cdp_n_sw1.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}

In [4]: with open("sh_cdp_n_r1.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1')}

In [5]: with open("sh_cdp_n_r2.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R2', 'Eth0/0'): ('SW1', 'Eth0/2'), ('R2', 'Eth0/1'): ('SW2', 'Eth0/11')}

In [6]: with open("sh_cdp_n_r3.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

"""

def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
# -*- coding: utf-8 -*-
"""
Завдання 11.4a

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

С помощью функции create_network_map из задания 11.4 создать словарь topology
с описанием топологии для файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему
для словаря topology, полученного с помощью create_network_map.  Как работать с
функцией draw_topology надо разобраться самостоятельно, почитав описание
функции в файле draw_network_graph.py.  Полученная схема будет записана в файл
svg - его можно открыть браузером.

С текущим словарем topology на схеме нарисованы лишние соединения. Они
возникают потому что в одном файле CDP (sh_cdp_n_r1.txt) описывается соединение
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
а в другом (sh_cdp_n_sw1.txt)
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

В этом задании надо создать новую функцию unique_network_map, которая из этих
двух соединений будет оставлять только одно, для корректного рисования схемы.
При этом все равно какое из соединений оставить.

У функции unique_network_map должен быть один параметр topology_dict, который
ожидает как аргумент словарь.  Это должен быть словарь полученный в результате
выполнения функции create_network_map из задания 11.4.

Пример словаря:
{
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
}


Функция должна возвращать словарь, который описывает соединения между
устройствами. В словаре надо избавиться от "дублирующих" соединений
и оставлять только одно из них.

Структура итогового словаря такая же, как в задании 11.4:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

После создания функции, попробовать еще раз нарисовать топологию,
теперь уже для словаря, который возвращает функция unique_network_map.

Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg

При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций create_network_map и draw_topology.

Пример работы функции
input_topology = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
}

In [7]: pprint(unique_network_map(input_topology))
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11')}

"""

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]
�PNG

   IHDR    �   ��G9   sBIT|d�   	pHYs  �  ��+   tEXtSoftware www.inkscape.org��<    IDATx���wxTe��{jz/��	=�H���AAł����(`[,�X@�4�"% !���I�>��3)@¤ܿ��^�y��g�33�9�-��={�@DDDDD����Q��䀈���� 09 """"�j�nP)�C��WC7KM�XY��,K�ADdB������aPd���)u��Zbk�0���ِ��-F����A��'nk�f��r(̈́õ]�����M�~�۸X:�A�՝�/˶tL�O/��{[:�AH�>8�09 ح���Z*���݆�#5L����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""�&�t �ֳ�;�����p��BA�7��p9��.$�tr.t:���L뇿R�f�E�v�L鋶n�X��)��������]���u��
 �����A� O�9@��d�����h<4Z�y�DDd9�;��ɨ���Z��er���3I�YTfv�o���DTc��m��sK<^j��{b���k��/�#��?�MBR��^��;��I�Hʓ��5V��HZur������Z���s�YGk)z�����X:�+�}�{.�![V�a|1 ��$9�����a�!	�/._�H0*��-���C�۾||:��"1W��7� Q�18�Q����6�? YT��#���29dr%�B!<�a#c��H,��4�?k�ߤ��!�+Ͷ�z��M,��������(,W��R���|�����x�sx}��Z�p��b��c�����s��47�69����'�ER����1ʆ``;/��ðM��Ꮻ���#am�q5��P�?�$"!�*�y�$�C}P�P�tr�a��)xd�A�e���[���<�;k]Ɵ7r�Q�b�_��h<��ߠ�����C�fjHHGlz��>���:Tj���"������Po|��P���_����Yf�����婑p��B��>�p����1�@  ��=��1�N����k��������3  �ü���A��;.�`P�q�����z���l�4�>(��8k� U���� �G����I""jvt:`_\:>?� �@��a���Z�#ײ���K �����D�o�'���Z����U�M�*���_5��J����`BUr0$�ǨޠPo���?�f���!�����^����}�"U�_RT���!"���\ �FMBAY�uIM���1�1�_(����J�{��Qk�݊&d@��a��4�����׺�����ap������J�ށ�|�:_�z�6(���4B�$�PBf���.�[[h�:���[we""j�j_���W��߃6�x3� GV���"�����(�����qz��'�7��r
�Χ<�Ȩ�����lj�o�oM������!�L��S��Wj.~9��7L�;��������W���?��G�e�jN12�+08�O\P���\���m�iѐ����ͧ��F~�f "���Z"������m�˹�o�8����˙��Y���!� ��"x;�bf�v��/�2�7�Q��!m����ٱ+x�w��������  V�]�R�h�v�.���Q�~X1�~>w�66�Zt �*9�+YE��Ҫ;6 ���LØ[���zbgl
������{��՜b<�݉�{�DD��|:3
�Ό2���4X��"^�i~���VM�QX���D�N�.X2�+��_�@��~A?;D5Z91+'F^�4Z�?�W��6:�B<�}�(���Eߝ�@��Zur  q�EX����W  �y8aH�^�S{�RF!��u�P����tUO��3�7�X_���>���`H��:��
��OO�@zQ9F|�%�槦#"��i_\:.�WMk=�8XK��B
�j�]�n��N��⯔<<�� �y:���;�����ረ>�\�©�slFd;x;����T�+�F��G��W��DB<l�dTG�ɱ�|����O�On��U�+��[�7p�Չ���(9ȑU�RF!�������zb�?��ٍ�z#��@����
�7s� 1������qDD��l��l��tWl�8;����l�w!��=�����l���پ+7S�n:u'_��OO�@Ԛ�&ݤ��"����l;A���Q�;5��A3�j�Gki��� @VI @,4���@B:���������%�ɐVX��a�vwDzQ�њ�{aX��p_�N�ń��f� "���xb6��t_��݋F���������@Ս,���Y��6��mGb�3U	���Ã�I흲���3�0��ݜq��i�S�~8�VM�k��/��Z>���T����UO^�y�r�eߝ9|-�;�!2����Na*
�����~��\2�����|s����:x9c����o�\�A����>�=0��R��5	Q}��e[� ����{+	���1E
�:��jQT���f,5=��ɁH(��Q]����8|-g��PR�DG����>�8�����l����YP��h�h���M}�q5�����H�.��3��J� �z�`�1�����iDD�z���¼�0�{6<���0t:`tg?�<�+���ğ7rP*W���+fD�� ,����R�[��"B<��C�Ó��nϳ��&�n;��ix�g0���`t����ZN	��r�=t��`�2�
�Ʀ�{�v_J3)��j�����'J��P^�J��]�-""jFd�*�ȗAV�2)��txl�pzF����x�0|y�*�^NG���v���. ��̝I�ū��ƾݭ2E��XTn�N���O����}]�hHgê��$�"����B�F$�ٳg��}E�A�2�!�ltb�n�V����_&G���K��s(�D�]����D\�4ȭ�-F��t����ye�(�h^]7®�}Y���x`��E�����aPB���Ĵ+yk�j��N��r�5;����-��5�V; �������19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19 """"" L�������"""""�䀈�����19����t DDf	t���IXi��i��8(,5��={6�٪۠���l���l��������v�����2s��h�X7��Ǎp8��6�q��J��K�AD ���@PPqS!�V$m����X�[�0$��@Vn�]�=j7�\���F��i�-σH��t�f�ĉ������� �nЈ�뽿H(�F��w��B(b�ѓ���j��	tPٔCZa_��46���I�UaҤI����?����\ ���ju***L������C�o߾P���
P*�b����ׯ�������c���u���?�C�N�0~�x��#F�K�.x������ɓ����?�ܤL+V�JQ Y��""�j���Gttt�u����۷ ���{{{��Ǜ��۷/���b���(��� �BL�>�ƍ���7*++q��|��g��ɩu�i��a�ҥ�1c�d��;w�ܹsѩS'�B�����o�ő#GuttlKep�m_��D��7�ZG&��g� xzz"""�����0��oٲe���ɁmE�7����'�|:t�H$Brr2���;l߾�֛�...����������[����aѢE4h ��p��!|���(..6n���?��ՙ�9�{����������T�C�����x���;8+++|���GRR���ѩS'<ݺu��իk�����7�|c61hӦ-Z�z%���x�g���o69�t���:�9���~~~>|8�r9�J�w���x�bDEE!22ڻ��Z�+V ::׮]þ}���cǢ���5k���9��Ѹr�
�]�f�֣G�_����8|�0�J%�����{�᭷�¶m�  Z� "����?�@��;������u��ԩ�y��\�[�n���8��>


�e�(�J:������_׸�1c �H�s�N�6[[[|������Ǿ}���������� <<�?�8
J�K!�
`_�z���z_�FGG����lYM���̙3��?��pA.�J��`ڴiػw/bcc��;n�8�B���F��q>���
�(--�5�^x���CPP�B!���?6�����wHDDz�W�6��y"""�cǎᥗ^2$C���ի�`����f�E���;��	,[�*�
�g�FZZ `ݺuشi��y8p ���Ј�n\	U�ה$&&b�ܹ��B�/��2���1k�,��� ���Klڴ	����Ν;QTTdv������"99ٰ�GA۶m�f�����퉉�x��1i�$|����˄U��2��7Rii)d2��?�V�D ���|}}R�i�O2�'OFdd$�b�<e	���ė_~iئT*�Bm�����q��y��^ff&N�>�M�6�����������ǏcӦMP(j�S�T��~]�����t����� �޽{#22���0�/�J1v�X<���x��bRg��� �����)ġC�����aÆA"���%&&
����	 ڷo���`;v���G&�aǎ������ ZI�����	E߾} ݻw��ɓ1y�dL�0�l��z���*^{�5L�2VV�7;t� ???;v̐ �B���]�`mm���(�m���#$$۷o7�>b���j���[�n�V��ȑ#��R�̥Ι�w�o@-W���	

-[  }����;es��5��?|�p<������0lKHH�O<a� wuu���?Μ9�Jet���8TVV�[�nfc���@``�QR�w�x�~����ۻ��u�����]p��vӭ����������6��[�n�a��M�������{��X�p!���۞}�Y���8y�ր���ph�Z\�t��X�Ν����d�m�J<F���=��ܹ3 �&�?�P��~�H-�W�$r��5]�ԩSTu�3f����_����b������4��С��@U% �x�ɱ��Rxx��'k111�����ۤR)BBB���`2���)))�СJ|K ҈���xW�Z�z'���f@rr2�����s�a�ڵ���ŧ�~j(�q�Q����駟p��aXYY��Cdd$~�al޼ _����&�S����χ��/�� �����������}{DDda�:u��w&))	O=�����w�ޘ4i��n���[�L���[�b�ҥ(..ƀ�ꫯ�^0J|||PVV��J�)E��H}}}M���������bM��\��� I���k�������g�6[&����?��o�Evv6�|�M����صk �\��o�gΜ��ٳ///�\�}��A�^�p��Y 0ܨ4�mH�����Lkkk�90��xyyA(��C�������
��S��Zvm�[�|��g5�͚5W�\1�䅅�8s�L��g̘a�/.))	�w�FϞ=Ɂ�}U߷�~(*++!�H`mmm��nkk�#F`�޽��9%Qs1u�T���;mܸ�ׯGNN��=##��ɫV��/��bx�}�v�=={������w��ή�~���;;;����h������6�nkkk�o}ۣ�����-2[VXX�~�J��p��r�d�*<�<�~�i����Ll޼��BCC�M666 j?o����{{{�.E���%���)j#���u���wr�����x����uW�y�����\�������V`�cj��T���α
Ç����Q�&""j�6o�ltW�vw�;cn����t�������!�@P����w��B㻪^^^���ħ�~jr�X_�\Ңߦ�S�X���)hw�$
v-j*��+��-��ٱ�;�?���nuC L�<�%&&���&��Է=�V�\v)"c�N~���:g�����F_��D�����!��ά8::������k�H���1ܸq�֧��K����p�~C�wY�T��\��S}Ws�0��u�S�X�
�
@`R�,H�T�]��!ۿ��Z��yS�y����ݻc�ڵ&����u�{�.dJƚL'�;�[}�L}��;988������B۶mѵk�>5O999����Hd:c�~V��B
��0a���O����:99�����'ww��Z ��J�9w;WWW�:z&L�F���ݻM���ɁV�����.C...P�T(�6ߥ�Z�M���%�[���P(7)��􄻻;�����GGGC�VcϞ=�}���s��Ŧ����a�v4�o����!�JѡC��.]�@�VM�ѫW/�����u��ի�}� ���]u�!���Hs�!�C�j��fa�ڵ+���NzB��ǏǱc��:V(���|z��舠� ħ�7�"���4hr�R�PRRR�����T*q��)����}��FeC� =z԰M$aܸq8r���@��6�)5�h������}PP�}�u��! �رc�����"$$�O�Fyy�a{tt4���p��1����Ƣ���2x,
1r�Hh4�o�P]=>A���H�K,�V\\���0h� Ó��ZJ�G�1l�ׯ<==k�)q��H$�?�h{tt4�!~9�K{RkW�tw���&��}�嗆6W�\A�~��d��;w���8v�����:��7b��x����'� ++���X�p!rss�F�0 ���uv)�ի�a�'''H$L�<@�#�;�=��CpwwP�!utt4�ONN6�[MDD�����aQ�;�ݻ���������o��ݻwC"� ##�d���8z�(bcc1m�4X[[~�y���j���0d�����5���j�_�+V�����?lݺJ��F�BDD�l�b�"�09h�ڵk�M�6�-��d��	nܸ���TL�0666��ͅ��7�.]z���j������;�૯�={�T*1l�0������?GA���111��˫q ? |���?~<^~�et�����		��1c�����[vB.�G��Դ�P5E�>9X�f�~�mL�>ӧOPu'�^����8���x��W��o�'$$���_7�����:u��6���M�-_� p��q��̙3ѳgO�k[[[C��[��������k�+������ʐ��+++� w���ѣG�~�z̜9.�J��'�| (//GFF��)!KJJ���a4VM����_��/��1c���~�:�/_�+W��=VVVuΆ�}�v�B̛7�0�L&����?lذ�PO���ª�f���t��=��V��d�,^�}���@ 0�����`�J��B�@||�ɘ��b�ҥ�?>�͛�j��5k���4�sqqATT6o�\�L[@�97�|����s���[On��#���Q�Ժ	z���(�۴iGGG����8�o}�D"���������&6WWW�ٳ_}����k����B2�fggg���~H�R�������l��M�6A�VcΜ9�jO(���B�����^��N,C$A�P��͘1/��"�L�b6�����ry���    IDATe�d�p>������ANN���C��ݽ�����!��N+GDD-WC%@�X���L�e�ڵCǎ��[oջ=�V�����
�Z�Z]�:O&L�����*1 �>+�n�P�*���^T�FK������_���KDDDu	

�������7h�yAy�)��}��i��n�����'O�ĉ����F�<GN�B�j�nE���ݺ2�
�s���c�P�� 4�EЈ��Z�\��銹DD��䠁8�;@"�X:""jF$r	T��E%jH)�S��6��aP3�䠁�;��y�������B����J�B�B��\׀��䀈��B$�(m٭�WA@Dj����L�����9�7��|�e�Ј5P���5���47ê�D��Y�@

 ��[:""jF����`g�Y�FS�Y���������Qs$�
aUae�0��̃c�#�˭-
5L���,Ha��F��m���C��9ۙ��v+"""���l��i�0���H��C���àf����ۡ¹:��ҡP�頰UX:j��Y�}�=�"-*+,
� E�E��Tc�P��ᘃ�{�#"��f]f�B�2�2��Y:j!r���9�"%>��ë�"R� �
,5C�E�(s-�t�BT:U�ܵ����!&�Խ*k.bCDDwϾ��5���y�.��@d�'LHbd"d2K�ADD͐K�B�
�t���j��#�O��p���I+��VJ-� ���j�pO��to�5:�e�ep�cW�w�ɞp�u�P��!tox�5e�e�����rK�B͜U���C�f��Q`_h�B�b�bK�B͑ H�H�܁�%�&DDDM�@'�s�3
}
-
5CE^E����6�'&���?�
�x�;�TwT:VrZS�k�����2kK�B����~����@ѽ�+��]���,
5#�^Ũp��w���C���Q���h�ZK�B�Dv�l8g;�Ffc�P�`r�@bGĲ�(�7�t>ԙSQR��x��ܹ�O��p����h�q��V���ՏD!��Uo��Z:j!�5A�A�h�H��t(Ԅٖ�¶��5ޚ ""j�TV*dvȄF��t(��:�<d��Z &DDDM�W�  r�s,
5A�H�L��Fi�P��ar@DD��T"�Ij�����Ԗ���P���,���CZ)�t8�|||��P����!005�@EEE�m�;��.������Y�1l�00 ���(//Gqq�K�����ׯ���ב��eR����nݺ���J�i�^�R�|GXUX�;V""����l���D�<GK������GG���Z-T*U�m�=�/FBB�����T*E�>}гgOx{{���
��������^{������#$$2���u�	Ɂ�C���!iD��ѝt@����hѢZ�_�7n ���

���?oR������������}���ʕ+��x�T��᫯�ºu�j�wʔ)����ŋ͖O�:�<��̙�K�.���;Ӯ�qՇP-��5/d�g�#�Ve-��c�=�9s��Zg������ �=����r�J�z>>>������C��߫W/�\�����m
��V��Ν;k���GA`` ���k,_�`�L�����z�t'�T��l�In�Br��դQf+ھ};�\�b�,..���:t@DDD�����V�Bee%,X�.���˖-Ü9sp��u�߿��}�������C����6   QQQ����$N""����Ie�ܹsg�б�����۷/\]]�&w�����.�J%�,Y���x{{�W^��+���bt��yxx����ꫯ���Z�����֭&N�x�1@fX&�:!�$�i�����(���3gj��WB�...(..6�8nҤI�����իq��Y �͛7��k�a�޽�9sf�1�3���@PP�M� (//���CZ�4�e�����^�"�	�N ����������>�cN�6���X�|9��� @VV�-[��~�	�g��K/�dv�q��A(�\GDFFzTh4�D��H#��7�"5�Q��:_~�%BCC!�H�c���~�[�l1��D�5k{�1���@�R�����������2C��}� N�:et���b\�r�;w���#d2�i�bbbk�(�ȑ#8r� ��g���?^��)(�]��""j�YaY�������������b1֯_o����?�СC��B�S�Nţ�>��m�"''�G}d�[�_�~�j�8y��q�������>}�@$�ܠ����ٳg���aT�m�6l۶ �|�rL�<���w����n��6�������d��t8}���/==ݨ�����aΜ98v��lق�7obȐ!X�p�Q���@�����X���
�4)GHH�Q�BDD��!�Sz�[���RÅ�L&3��9ițo��ŋ#--���X,�̙31o�<C�@��� ����x�KHH���5|}}Mʺu놀��:�$�/��:��Q�A4ғ��_˖-3[��_��o��ڵkѩS'899��W����X�j�a俵�5v�܉�c�b͚5�z���fg��Uc����
�����~DDD�H-��e$�L�[���?ж�Y�d���N_�58�+V`˖-puu�� �^��U�V!'�j�www�ܹ#G�ħ�~
 ������M��)귻��!--ͨ,::���FO+�V��������x���!5Jr���h�ީ����ٳ�hJ0�\���X<��MH"�@(B.��mC�����h���5F���kzU"""Kr�r�s�3R�����N)��.�|��5I~~>���ХK�Bh�ZXYU�UYYi���;gP������ñk׮zMwz�r��@%U�3�u�=!�h����k�ɷ+-- ÇY�VC��B"1?���ޝܡC����۷oo�X���R��@\y�
R"Rr6���4�5k�4�䒒��bH$(
�؃��#����4r�H���4j�"������Ӫf�"�i�+$�>MP��AYYY�k"��U.))1������&#""jjDJ��ī�m�^�L�yQ^^�FS�uĝ��DGG�ڵk���o�@�uI�U�<��Ԁ�'��A�III�����hz��ȷϙ���=z4X��{\3\�HDDt�
v2�9Ζ�������h4��̄�����F������&M	

BDDD�NhR�[���h�z��.MJKK!�H�j䚜={B��z�2�nkk�Ν;�ƍ(,,4l����F���ݻ���  R���%"�����u��9�Myy9lll$A8w���v�С����'FGGC�T��~��c�Di��g�'���Dwj��]�v���4����c�w��M �̙3aee{{{��}�v�T*,Z� ���꫰��2,�T�e?~<�?n�0�I"��������J� ����ە��Be���؉���Ur�d�v5��ps��;���}����4���`��� �~��� ��z�=��a�S�D��^z	"��h|�X,Ƹq�p��a��'5�$/�_�o����i��s���ܹs͖�_�7nP�P�رc�`�,X�  �a�|��gw}���L��?���+�u�V���b�{���֭[u���OOO���۵�9b����F�֭[���bdd�a{bd".���]�NDDt�\�]����$��t8b�ҥ5��^��p�o˖-=z4V�\�e˖������b��u��elذ���Ǟ={���OOO8::����F�������Zg��I�&VH�Ϙ��7�@��@&�a�ĉf��;�!�K Rq6*z�={�l�g����h׮]�u����V"vpp�СC�����b���HKK���:t耋/"//Ϩ�N�:���ǎ3�����Æ���JKKq��)����FuV�Z����?�d���y{{#<<�l�N�����Ϗ=�䀈�,"'8���WH������Z�\�p7n�0������ѣ�����B�߿7n�@XX���q���R���___�ر��:�G�6l<<< ��p��	>|:ݭ˥���ڵ�ĉM7�.88ݺu3[�P(�vm֊���B;^��߂�14hr�899��~÷�~kx
���%�E��зa'�`#���|d���+��ك/��6lh���;�#�m>:�i����'���g+z�ƍ�D�_��ҡ5����)�AR�$��jK��bM�0B��v�j�˝ˑ��+~L�bZݓ��b�Bj�O��Z6�Z����t��̬W[��.rrr�f͚���M�6���������`T������k>hnź|�r��j�^�ڰM("$$��ް��Czz:�]�֨+��~~~���Fbbb�����P<�
1B�mж��F�H��P����W�� uh��bk(�]K����/#��"�,p>R�tjHZ��(B%���"=P۶m3;��\.���T��7o�<�޽ǎ3�ۣG��w�"
�d�L�:�(A�x�"�.]j�S/V���k(�	th���&M�G}d�>i�$,\�������d2��������o�TRN��w#�@I�_G�K��V��PJ�[�Rey��B��Œ�S ��GX���4 ����2f�p�e����d�T��y�Z�K�A5���G�+[��Bȭ]p��K�Aw�	ȖU�}�+��I�Z}�+���+��˗/�M���ٳ����СC�ꫯPYY��Çc���X�r%�z�)�}2:f@i�Ģ���h������#??[�l��k�PVV��ݻc޼yx뭷���nX�W%�ť.���{�:؞ ʴ�uW��4*t��e#E��Œ��b��#hP:��FM�����&*�T�5��ED����f�BVV^{�5�TUk�lذ���?~<�v튋/��爔~)=q�ɺ>_�5��Ӎf�����B���/���c��z@��:BWKW7�{�䀈��4��� L�<���P�>γ�>kT���O?�4z�!H$\�~k׮5���ҥp��Cb�w��Q�?0I�0[0^�^x��W����I�899��;'����㈈�,    ?��z��ӧO�ڵk�ڵ+>���
�@�\� L߾-$$��1�z9�9�R�9!9u�Զm[ @zz�]�"j�䀈����y:���̀M�h�2�R�'�xG�Aee%֯_��[�b���fےH$������?�z��0k�,>۶m ��U͂W^n:贬�̨��\]]�͛7���7nv�	�R\�z"�ӧO�V�ž}���AD-�Y@RR~��G�v��� U�e�Y[[ *+Mg��o�׹�رc!��s�Nx��Dй�ZWO~�������fR"���O����)1W��oli��%%% ����ӏ3�H$&��Ҫ���J�IYtt4Ο?���4 �k�iK˝�aW|k��'�x�<�N�8��k�6�;!��O�����Fc�M�u���A���Ψ�^�.]�;v�죴U�ꀫ�^5(y޼yX�p!N�<��K�M�JD��""�FRۊ����Y���פL���ه���Q^^����#��"�|
�
�`�,X� ����K/��Ց��݊����~,����w��j��ի�I�~���m�fcc��#Gb߾}���f��.��'�>��~#�ɡO�ſ� Tf�Q+�'DDD�$��___�?C����t::���  GG�{:fQQ�9�nݺaԨQ��AAA�6m
�Va6l����v)�[�~=F���?n��>�b�m����x"j]�䀈�����8�ꪹ 暔��r8 PXX����cԨQ8x� ������~����q׬Y���0���[X�p!�r9����R��d���������������ӯ�0w�\�5�^ ��'�Ĺs��)^"j�����mA(@�U�+�I��y_�u�8q]�t�X,6�tÆ���n'����G�,x����3f`ҤI�T*���Ǳs�N�lD@��jݻw�|P�{�����~ :�� ��AD-�""�zX��" @�*��T�Z�{����={Lʾ��;������믿6[VVV�M�6�z���h��j���o��۲e���r;9��
�8�渚�CD-�� "��ƍÑ#GPTTtOmXUX�=��ݓ��
�@��QQS�'DDD-�H$��ŋ���s�mt���¦���R��Q�/�sFIDM�� J����(,,��\3]v"r9��$Y!5L���Ȅm�-:� �B
*�ށ�Z&DDDd�D.A�鮀2�ҡ��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈���� 09 """"�jL����� �"""""��䀈����  bK��=;$vR��uI����8���lY��}�m���D� w�ۣB�����+	��*tj��� 7;k��R��29N'��fQY��[�ExaXL���Լ��Z��i_g;��2�
ye��+%���u���)=����	�V�����l̐�ӟKz�J���H�.ƅ�f�	���>vw����%��w;/�B��=����&uX1��8ژlWk��|*��\�1*K��#����
H�B<����醹_����H���,����&۵:~9��'�9�R�������;�#�'��}[0�#�x�l�����0����/����H��d�@��
 ȖUT]�	���=��/"ښ-;����DFq���OfDa~T �L�DQ��;��ɨ�8u#�?܅r���c'jJ��CVI��� ���
��]���x�(
+�x�SF��2���p�ť��R	 ��-?��OgFa��4U(����A���g�f ������lt7<�3�
5�|}ب���>���\����SK�t3�*�%m���#0�s ��51����������h<���72�������["|ja����J*`o%A���)=����a�Z�Өn�J�U�.��	��/ x8X��y�1���w��Z�mY�ԃV�CQ�E
$���kl*&~R���h�v&���+~<{Ð ��)������o����Zn��)��w��R�����L�)��p&%�|���W(QT�@Za�g`�'�QT���� �[I��>�'c;�/c�����zu�#�KIe��x��G�ea���ZP���L��8�e[� �+�c�� ��6�Oj�Z:&�(��2�vV��"�W%*���¢V�T�BfI9��"HD����J<����|���P�Ԛ(�$�B(�Vj�����(S���ο,�6Z��sK �޿�m] �Ʊ
D-�ݣ W{8ZKq�Fn���C��jq9��������V
?;$�ʠT3�$˲�����29rK+�=��#��3`+cJ� �;�R��ٔ|HH���?����B�y9�B�FJA�彝l1*��&���kY�p�7T��arp���ŬA �w�X�}��p|{:��Y���g�X(Ě��;���T��3��F�W��6*���
 mㄔ�3`-�R������tr.&}�Y%����a%a��>�w�Ǫ}L&�]��h�f�N���>���9�'��*19�O�]>@�� W{T��xj�1�r.����xa���H+,�?�l�p����磃��nPk�X��)��x�������+��j��l�9@  ��}�$Yu��Pէ{���p�z�jx9���^��_���k�X�mP�g��4Z�J�h�f�X�^�k�k�����+�t�A_W���>.����Pr�"j]�ԃ~@2Pu1&	���+��Xݏ{z`��ѐɕ�v��i����|��� ���k�Q�,��\	���j    IDAT�N�P k�?����z֤��HX5Z~���v��a{���=���`d'?�8�T&�%�J(�hu:�J�8���>U���`��'�:�D�fQ�ץV��A=��1��� ���\:KGvå�B|{:�����`��#Q*Wa�� >����S�5���F"�/������Q����l��5��^T�Ԑ�����XL���������+*����ܠP�N���y��킶�L�=�����~~j&u�{S��Փ�M��c݌����Z�Vt��+���n/
���b� <���l��=����1ȑUb�����A���*UjL\�7�����~��h鐨Si����︖S��}��z��Q��؃;�����Ft?�:��Υ���a�����_ �"3sC�pL�AR��>� ضp��<�����si��Z�����O������R�ƖyC�u4�r�*��^U(Ln�d�*p�F.Fv�Ch'�����;��<���=��d��N �İ�Z�EdS*$Jk��ZQ����~h��Ժv�k�����-7�*
n����@V��u2If&���30d$�,��rI��s��Ùs�g�5�0sd<�-��*zL��I�3Q���_����|۔
Sb�w��4TJ�e%y1�Hrp��<R������0ﭾ�XC���2���h������\A&�\|��Ow�^q:���ڗ>#D��?���ۦתY��Ă�$�'�-��+�+l1H�n䊿�R��?��%���v�
���R�OIc�)��Y�|p�b"�Z���V�2���A����<�v����q>���'J��]�-㿿�!?�y��cAV�_1�������Ń�:�х|d��9x��<΋�䞋����.�'�C�V����S�Wei�����e�bx��"��Ϸ<�l��Cf>���VI�a|��K���2w4���ԇ�Îby;&z�g����Ɨ<��_��|������Y�§<�r�����׷���?6�����q	q�v㺗?g�Mx��K���۔54�ޞ�NbaV�_��c~��YMI�ɓ'�MC�����ݒc�げ��]��
�c�WR��_���.���w526����^���3M��2�;��J�2�V)(��|!��F(�nj�joC�R�e�~YC3vg�s���u�>�`��gZCc80�G��#�����Z:]�,5ƀJ����Fc뉱z��Y��$D�nj�Mk:hښ�����84a�M��8��p=z���:+Nw��	R�hTJ�[�~��Ij��F��*;K��vv��B�v2񻗂�D���4N���x(�������=�h���S�6�[�I�+�dF���-'�=P��!�!�Ltm���m�1�-�T!@�!�B!���@!�BHr �B!�8N�!�B! ɁB!��8I�B!��$B!�B��$9B!�B �!�B!���@!�BHr �B!�8N�!�B! ɁB!��8I�B!��$B!�B��$9B!�B �!�B!���@!�BHr �B!�8N�!�B! ɁB!��8I�B!��$B!�B��$9B!�B �!�B!���@!�BHr �B!�8N�!�B! ɁB!��8I�B!��$B!�B��$9B!�B �!�B!���@!�BHr �B!�8N�!�B! ɁB!��8I�B!��$B!�B��$9B!�B �!�B!�S; ���z�����ͻ<8�s5����@I������^�@� �D9d?���f��[쿆��Q���%!�u$�}{�z�1���"�+)��h������O0QXQMSsk�vVx���O"�N'�6�w�#:�%�!�)���ĲoI������O�iD��QRU��}[L�Xvc޳�"�_4m-��W���M}}=---h�-gt<[*��ds��-445w� 
7� ��|LV���O�\�^���%�0��"��,`�&�'(��K1P�Jr�h�"�L��e�w�}��{� ..�����n�ѭ\���\�����3:�J��+�`����L&���ٲeo��G�7��o��+V������z_����Y�r%iiix<8�k��FAA����J4 ���b���o$44��:�<�.��R��`�n�c��}۵+	�����7�t:�я~t�珈���k�����G��RZZ����ٵkW��)
��m=����Z�ʯ|ѢE,Z��ٌ�b᫯�⭷ޢ��D�|,���*�;�XE�9r$�f��ΡC�ضmО h4����x���͘1�G}��z����?��Z�������Y�t))))�����w���[o������Y�f�?=�w�����ˊ+x���;��D�1a�L&S�uv����]֙|�K.��y��a���R��:�'M�ĬY�0����駟r���Ӟ��;�dٲe\r�%~�3�L\r�%$''�����ݻٴi.׉�� �AOB���=���z%98���Y�lY�uv���޽{x��g�x<���L(�J{�1�̙CAA�"%%�իW3s�Ln�������j�,Y�_|�w3�7o�<�---|��h4.��b-Z�M7�����}u��h��o9���������.������r����k��Ƌ/������s>��l��_�l6s���5k_|1��X�~}��N�8����{�9��{ｗ�/����j�9BBBw�q]t��z���4'�y��m���e�u����������>|��e˖�f�l6������0{�l�,Y7���9������嫯��M�Pp�uױb�
�����HB�=�V�9qn���:�̙�e��n���}�~�z����ڵk{����sW^y%����F������ӟ��o���~Z��ŋ�i�&��tʔ)<�����QSS�^��ꫯfϞ=�^����P@Bn���_	!�^�v+��سgOo������3g��y�x���_��\{�\~��[�.�3g�$::�6��BBBX�f���\{�TWW����+��½���5�\㫯o�S�\�G�A1D�܃�رc\u�U�n?]�����/I\\k֬�O> **�_|�;͛7S[[pߜ����شi��lڴi\~��|���}�ݾD���o�'?�	W^y%���?0�0w��P��_|�w�y'����s�f3w�y'�������������˹��Y�j�����ٳy�7��Ʀ���z�j2220���u��N,$e_
�%�=���Y���{ihh��ȑ#�?'&&RYY�#�\�p!W^y%[�la�ڵX�V�f3O>�$��կرcyy�[��ΝKDD�߿���Pz�!�N'�_={��E�Vs�7p�M7q�-���㏃�*�~$�87Ay�P(���B�բ�������DFFv����7o?��OX�h�\z�@���M�/��"n�۷=��������o|e3f��%��  //��?����L��O�/�*�bܧ�$1�c������^��5��F���|?Je�
,Z����Ǝ�a{XX���#//ϗ ������¢E�����������7-]�ho�8������p������������?�6�ٌ^� !!�w�����������ӧ�a��ŋ�j����+�� �[*JKK���K�h4��x�b�ju����rQ]]͗_~��K�s��Ȫ�q������پ}{���m����gܸq�^�W^y%���z��
@uu5O>�$J��+����cgggS^^Ύ;|e���#&&��_�׫��t����SRRBNNn���i���u�"�J�k������??������۾ߧO��c�=FRR������믿���2_���㩮��+�Z�������S�$���2s�L^}�U�n��|ܸq |�]����v�bѢE�?��vF�T��[��\x�<��@���˗�m��U*��X��U�V�� ����r���~3f���;wv8�����������:l���			���6a����;�q��l�߿��'b4ijj��9�Yޢ O=���� ��h������~7�L<��̛7�Wf�Z������'N��/�ܹ���222��<z���{�n�����}��\�����wط!�c��=�݉nHNN�}�N�6��|���lݺ��{JJ
�V�b��龲�?��������l�r�j�L�0����-�{�졵���q����L�6��{���[��o�>{<�m�ƕW^I�%	|q�2��8��!���;��ѣ				��{S���kۛ
i��UQQ�W��լ_��>����6�.]���˹������ ���	���U]]MVV			�\z�(��k���@���ޖo/{���N���o�D�P��deeu��СCl߾�Gy�5kְq�F�}�]�v����sJJ
7�t���
;v� 66�U�V�h�"�}�]_˒�������e�^^������q��A��OQQ�ߗ���;@rr2�9���IL~��dDf���k������*��������?����7`�ԗ7�t���臨��)S�p��r�=��u_LNN��v����ˁ�����`�ر���q���w�s�UnM��H����w�{�ɚ��ill��+��z+eee~/�JJJ�����߿���z�7o��ر���� $%%�R�(**�p>��IYY#F�@�V�
/o����_�aÆ<�7Ƥ�$>L��oB�z598�a�T����x���9x� ������t�;/����{nn.,`	�2�[��f�hiio�4~�
����lv��Iii��6o�@���i>�x�I���e�'�:�<�gEGG��<��.������T^^����֭��eŊ~�5Z[[��_���ɓ}�AW׆����tb4;lKKKc�ر<��c~�z��Ry�ׯҩ�T��+?����pۺu�x��Gٶm��h��͝v�x��7y��'}���_MVVS�N%""���F��[��f�0���NuG��Φ��ůܙj�kģ�Y)]������A{¹k�.^}�UV�ZEEE���j��x���}���16l`�ܹ���{my��S����R�0~c!�J%K�.e�֭^�uuL�wm	�u��
!zV�&���:}����+'��p��=z�1c���T���S�Txy�y�yM�0���T^|���x�<p��������TdV��;жȌ}�b����Ow���k"��� �����<���t:;\k�ޭ��p�q�F�r�u���N��r�ۭvKrD�q��^���L���wh5:r�S�N%..Η���Ng]�z_
		��/����i�:�)�	C�A��Co��V������_��^^^N]]		'��k���k�M��G��5e���_��a�N����jڨk��M�2�}�W���~�m��V����7��۬�YW��Z���ijj��O?x�Ύ������P��Xb,ĶȌ}�f�u9mhO�޼_����R�N��pmh4/^������:�.`޵��T:�cq�;~����w��^�����ON4�v{�	�������	󛍭;���S+����_~��������7��{���^�'���);;���6o��a�͆Z�F�RuxgOm?��N�uB��V�����ikk��������䛨^�g��|��G~��xy�:f��(�
��be!���رc@�k�`0�P(|u�fϞ�a�\������O{�z��M\*Ys0�u����Vۡu N\�55��n���PPP��	�l��j0�zz�
�<a�����hkk��b����.��7n�T�c����K�¨k����bnB�s�/����K���n7����9��MK�T���űc�|M��>W�^���m�w�@SYz��i�1Jr�y��{�z�v=zt�m�k��n%�)��ꆒ��p��1c�������v��F��������Yw������>�y��xYJJ
'N<�V���4G�Κ�o�������q8~�x{�������ѣG��]r�%�t�N��D���H�P1S3ӯ��w��䠦�����o���͛Q�T\t�E~�ӧO�`0th�����0k�ɾ��K�n7,@�8�v�V���/�j���2�:���6Y-���N�wr�ٳUPP@ii)S�L�0�s�ܹ lٲ�Wf2����x��������J�ҷ�ט1c0�;�����L#�IV
��X:[`�;��3�z�DDDp���SPP�7�ҥKq:�ƹ�	��EiV)6c��p�����@tt�9��t�c��FJ���US�NE�����/F����(�ɼө^p�����6�j5ӦM�b�p���s�]qz��F�j�*���'[�n�v����N�4�?��|��'���s�����X�n?�яX�f1119r��Çs�7����?��_��Ç3~�x�T������a�.��ry�>���Z-W^y%�������Iߨ'kK���ͮ�g�F�5N��?���Emm-���̛7�n����"��믿~V�(?�����������_�b�0g�.��2v����B�d���~'����͊+��;�j���撔��-�܂����W^9Q�Ӿ��Y�fp۞={|/$����5�\Ýw��o������v�%�g���?����k�������ۉ��ছnB����K/��*�J�,Y�_|�a��ɢ���4i �F��׍iIh!#9��ϋp!�T���ŋij
�R�e�_����M��W\���ۉ��������+����̘1�x�|���r233�뮻p8~3(edd���左G�8KJJX�b���|��g4^��}���l6��s��D��z%9��lX,ߢ?�lڴ���^z���$�ϟ�\���a�ڵ@�l�%�M����à���zn��V~���q����y��|s�C���@�Ɯ����v�������}�~��g���SIb�wBCCY�lY���q\.���|�[n�h�j��o�Ur������7�̓O>�+��������J�P(X�t)۷o87���ba���<����}�ݾ������A���JW�h��M�ƴi�n[�n�/9شi����پE�֯_VɁ���W���<���v����p�?��?��W6c��f�i������#�����'?�'��E/.�����B��������|����>Kzz:k֬�m_�z�Y%۷o���3��vo����������ϯ�*;;���G}���N'w�uO=��o�J�>� �l�B�ޡ�<yr�Y>)44���h���;���;���������*��>���;wv���daaa����t:)..�bp2��Cc|#�z=Z�Liڟ�T*��t������JFFZ���G�v�>pҤI<��s��7���?>�c�����j�СC�"�~m���ݩ���>�Fsڮ���Ì-���$''c�X())��t�V�����l�I�N�C��a�Z^�F�"))���V�������Ge�ر,Y����l�/����v�>�ȝ#�0��h<)))�N`�U\\�w3�L�0���(���ؽ{7v����D"""����p�����P(N��]�822���j����Z���7��_���I��2�©h.�RB�'_�!zO�J�҅^�O<����ʶm�z���=��$����^9�~���3{�l/^|V-�)�X�K�"}{ǁ�BDDD�q�F^�u�y�n�_�QN���}<�Gq��8�����[��LN,�9��1��A��N��6d�"�1�M�6u:kLOPxDTEP� ӯej����D�x�M ��Z�={L1xL�<����Ng�9g����I�Y��Φ�������7G5S�TGҁ$I��!�r�W,&��f��ci
�8�g�&����2��E!�YEfMQMdl�8}e!D��-}%�&m��ڔ�`�"����*7m!B��&!7�Qߎ
vBi��6Ĕ�P�\�G!�4�g�Zt �ú/Dw��n^���    IDATr/ȕuZD�qj�x��gw��DB�$} �h.��ֈ�`�"M����XT�s_uW�ƄF�����4�E�)�X�0�Hr�'t�:�4}��{ z^�TBe�d�sjRj?.Ɂ�uIuXL̅�z���Ir�G�ͮb ��ٱ�Z0����tms�ؒXu]�� ������a5T�W������ȡ����$��W�m�^�P�P<��KE��`�"�8N��>�Ҹ�U�K�
v(bQ��4G7�*3�s�V��M��Tl��D�;6��q��~�*��B�#�����X����)�F=x�%\f��ƭt[K���`�"� ��EB^�Zc�CB�D��>�r�0��Q�[�v8b�P��жj%9�Lݦ&y2j�:ء�! �H<�y��Cq
I���ЌS�E�D�2��F[����tm�U��B����z�^+D?&�A��4�JLTdT�V����Z#��o!!��tt)G~p$�a�A�!���I4�5;!D'��8�P;� �q��k��Շ��9Ѵ����{�Z'���M	v(b��M,"�,��Ҙ`�#��$A�v�I�Kvb�5���&#�a��&��KAtyt�C��[�&J>���v8B�.H�� rj��%�;!�P�h_�%�h,J�|%��Q4��6]#w�D��L��L��Q�����D�,3�ܵ���wA.��g�!�{�S���,zGc\#	��LCۢv8B�Ӑ� ��ʣ0�(>�X��s��i�FYi47;1�K=Fde$:�.ء�A*�*��/�0��zB����c�ۨU�P� �r�0�iH�Y@ęKۑF�>�,z^�����+�14��!Δ$A�kёt0��Q�4G6;1�EVD�hn�ir�S9Uhm��C����rg�R�V�P��$�A?`.2c�1Pt~�t/g/�2
�҃�d	v(��k5�R�U*��g��9�#�����G�M���w'� �K�P� ���1��K�Y�Dתҫh�k��cD�r���a4v#�)�iB@��Oh[�Ė�;1��L�Zep��=�N]R	Gd��s�B�ȝ��B� }[:*�*�!	!΂$��S����`3؂���ʣH:��0D?V1�m�����`�"���J 2��@c��څ�$9�gT.N���i�8��`�#0�ʍG!cX�?��N]r	y	(<��C����d~���&���$��¥ ��t<x8�#2XP�����{����d�2�m����`�"���k1P��� G$�8W��Cj��������N,�����Tz���T�FP��#�`���sf���;#�Fs�̴'� "�A?ba���XL�&I� �-.?��BKdK�C�HlI,���Cp�ɵ�����``��Q2+���$����@���h[��Ot[xu8a�aT����l�0{���@yF9E�a*11�ۑ(��(!�`"���9c�����g���@tS��x�hov("�JƕP<�8�a��<����J��Nʾ�Fm!I���)S�0� YI�%����`�"����HSl������Ef2�fs4&ء!z�L+0�DVGRx~!n��a{��qF�v���i�F�S*�L�2��:N��]�v���֯_Ͼ}�X�v�ǠP(�8q"YYYh4


غu+�������������� ��zƎ��~۷o?��N�ʳʉ���Pg���b�k�n�f#�hj��]���_� U�ҩ�`J.�������B�!��W��j�y�.���׳p�B &M�į�k^~�e6m�ԡnbb"���g|���P�x�	�M��W^XX���NEE�c=&L���I�x��}e			��<�K��M����ʈ�#����)���/!�*\Z�"$9`"�"HߖΑ�G(�TȈ�F�pK� N�tt)�zà������W_}5�6��� \��HVV��=����_3m�4���ꫯ�p8X�x1��s=�7�pC��fggc�Z&)[�n�K΅K��2b�bm�(z�[��踣�$��O�!Yu]��B���Xc$}{:���YE���`�$ ����1G	?>�f���e���=~\���R��b鸐\xx8���<x����/�����3v�X���?~<{��鰯^�g��lܸ���a{ii)�|�I�|���6tV��2�@�9��F����v�U쐄}h�<!1�Z#_e`.0;1@$LƥrQ�1��6�я~Ľ���-��ذao��F���G��^��>cӦM���;̚5˯ΤI�P��l۶����|� ӧO����lذ�\?�i�4���u&�6y$�\�B�N%�7���@�!H��Loѣt��/�^�]/s��Ω�j�r��J��5bhMmZQQA^^�>&`۶ml۶��;w��3f���
.���^{��?����x|�A"""|�F�h��ȑ��y�*''�Çs����۵Z-���w���D���rR�ԑߎ$�L���o"!����A��tS;��ʌJҷ��o�;$�O��M�Ǖ��UƠ�>f̘�}�X�l_�5��3f�q��N�!�l6��n���o��o��9s������-��t\}�������o\�����y�':�<���dgg�p88p� �=�\�f*jHh r>c>CH��5]�mL* �@2���%)b���`P��d|�A��rg�2b�"�נS�C<��;���R�TGL���}�j������}P?S����
m߾�o������u:@�1�2o��egg�p8���:lkmm�>�������z=�G�fƌ<����s�=|��g��n�����S#��8��a5s}�^�! I�SE��tJƖ�?5��CI���ʢ�PK(�_g����b֬Y�kǷZ���þw���֐��:^j��K/��͛7����a����k,̙3�'�|�իW�QrP�Q�K�"��.#:��F��b,&q�q$J-�B�s'�� �p+HݓJhS(�cJ�(=$�%;,��Շ��E�,����ݡ�;��78Yhh(@�`�̙�����;�t��[�l������TBCCim�|,Akx+�#��o��[�C��d�`R�6_e`����'Hr0�̈́ZC	i�&bѵ��Eh[�$:S]*��>CII	xб����د<''���ʀ3�N[[�i�x�&VFlql��!�]��أ�$�&�&�B/�+R�cF4��7�u�u4�49"��ՅQ�^AS��>���?���c��n7?��:l�|�8���fΜɻ��%wQ6l)))v�j�ҸP;Ԥ�I��GCD}R=u�u �Zt$H��@����F��I<�(��S�	��B��"�6g�v�[��`�=����t�k�.��m���f���lܸ���j�N~~~��YWWǧ�~����Y�nn��ٳg���Caa!;v��տ��KQ(�َy���)--��w�����(�JF�͚5kP�T���k]Ƥv��mT�?�ܜ:'%cK�O�'>?ʃ���xO��F|7c����%X����~*�*�a�~"uw*��pb!���p����x�gn���g� �����o�r�J�C��je�ܹgu�G}�#Fp�w�z�j�N'����~�������c���;2s�\,_���˗��xP(��n^x�.�*4�����t��jRj(]�ҩ$c[�c�`�$� �'O`��lY��L*@�Q2b��A�bHk	o!wV.qqf��R�d޼y]�q8lٲůl�ԩ�3�RI~~>�7o`޼y444�Z�ӧO����Ç�m�j�̝;��cǢT*)((��?�ua�0a/��"���o�裏:�U�P0v�Xƌ��l&$$���
6o���HͰJƗ��9�Ц�.�>����;(�XHsT3�B������BHqf$9b�:'�q���l�L]'|j����Ĉ]�W�gg�ڵ\t�E\r�%��=��y[h�/܏��$S�
��E��"%���)��}G�1j��Q[G�q��ڍ�)ӆ�ؒXbKd������Y�`��^�' E���5$�ʔ�C]CB��B3�6#��vHB�J��!Jkk��9��#S�0l�0�ʣ���P�^A��XߌW����v�,Y��,Cg�X�1,&�_gʬ3C�]o�踣4�1����b��`�m%�"��ID�G1l߰9c��9.����:��:C�*����[0�'9��F����N��\jU�UT�U�kё�M&�Z���N��}���	Ÿ���V�
iE�z�fBߨg���<�
�t���o([p?AiY�n��x�<��{��늠ho���øn'`.2�p��1!Dϐ�@��4.JǔR�RCbn"	yҏy(k�l!wF.���4pN�̄3T������`�!N�V�Q��x�*�+1�P�IK��g�� D��t+���$�!C�A�q�}����2@��-#�!�>b:v ���0�q--N*�c%�2�G��ֈ�-cM�=O�,����B�! �'Փ{A.6�<(EU$H��p�����8B�/���C��nb��lbB��'-�Kn����z*3*A�z�����M�Ʋe�())�j�vk���hRRRP�T477��>�\�����n�����3�J]����W������)�T�S�d��a��OA۪vhB�!@���.�5���E�#�)�(�.���}�DTG;�>��_�������:O=���. ����t:�z��&L��u�]��Nee��?99��ɓ'�P�'h�桇b߾}]�����Y�f����=���˗s��ws�e�QZZڱ�Gf,��X���'֓�?	S�I!��$�qG�*��tt)G~p���)����O�t:���ٵkuuu�TUU���r�J���&ݥ��y�g0�L����:t���$���z�~�iV�\Iyyy�}����w���p��l63q�Dn���s�Qqv�Z'U#��*�Bߨ'�"���S �
I�ӶhIۑFSl!M�c<J�gH����/�}��>=�e�HLL��Geݺu��Ç���O�ӟ���~8ྋ-"$$�w�yǯ���.�;��ո��sj�T���zD5
����0�z I�A#Ɂ�6c�������T�W���@lI��G8��[o%&&�N�m���+߼y3{���;~�x�/_Njj*|��'������3w�\<�|�_����ihh`�ܹ�����83qNN���:tȯ��w�a��� �v�m,X���>���8�N�GTS�V�­ �p<�"�z�"��$9�$�4G���c�R�VM��$"+#�V�͟?���R��{�.((�KV�ZŔ)S����n����ɼy�p�\|�駾z�F�����Cw&��;}��5k���;v�o�ȑ#3f�>�h��V�o0��lB����D�w$s�YV!B�+��s�v����);���)��$H&�>,�����+Wv����?d׮],[��7�|���prrr:=��d���og�֭@�@���뮻Η���FIII�cxg��������p8�����9�=�5����z��w�FZ
���$�G�u��L�9��ҬR�mr0k֬N�:t�]�v�������{��~߽{7�f��ᾲ�����[[[�[�����5�/��>����B�s��D��J,&�M��ͨ���ZdZ`!D�%Ɂ�Qa�ad~��G���ݥqQt~q�q�A��g�r�-�: ������L4mmm��틏)���2�T�]�N�_��ٳ���bÆ��G�!����*�#�1�Iߞ>$�BL��^᝗۩u��8ɝ�KxM8	�	�&I�-mmm~���� ������q999����cǎ^�R��h�`r������Aۂ*��$9�J׬#��L��V�3�ɝ����@b^"�c��@`�٨���d2��-?y���̌3x���}-B����±ǈ�� �"�PK(�>��&�!&%����@��2��@�QP8��rp?�:t���[�w�^bbbHMM�+�j��3���B���|�K�,��,��9����zrg�rp�A�#��ۙ$B��L�ѧ�5F2�� kK�o����*��|����
"""���<�cmܸ�����('֒��k�j��� 
���K��m�6*++���B��FV�w�^
'�����&�џ�&�J�pBҭH�Ʀ���5����2J�J1��-�E�迗�3�<�鶇~�����a��ϟϳ�>����	�����_��W����g���_�t�R222���%%%��'���Ǜo��;i�$RRR����uy�y��q�W 0b� ��~�v;��5k�t;N!�]o'��}̏#�ALy�"�i!B>��	LÿNbn"�ë�L��bTѥ���b<7����{��LQQ���_�5w�y'��٘L&���((( �����_������غu+���~c�n7w�u+V�`޼yL�:���K/��+������زeK��Z�VJKK|���E��Pg�S�RCmJ-
��q�� eJ�#B�ޥ�<y����!4��M}b=�����s4&�!(aaa|��G�_��'�|�ǎ�{µ8ա=v<ѿ������`���<*qԤ�`����k�)�!�$]��M ���@�+J����b�b�О��6��c.2]��M�(���/�����{�`�"ĀS5����r"�#H�6���p��wB�AD��?y@A���ҭ�Po�tt)��K���$�$c�L�z���R֮]K^^^�C�_���&�R�XO�W������s4�]s�!� %Ɂ���-ZRw���?���:j�ՒwA^�
_e��Izs�f!:��I]Bu�u4G5��i�.���ۧn��D!��;�0TN�b�b��4�5���f�tmDTG�VgB/k���y(�J"+"I�M�Xc�nCBq
IĀj	%�rb�l�����
4�G��-�%����t$��;.����F��I8���AOXcÿNdU$J�,�#����@
�y�Ė�R�\C�Z�ҫ��SC\~\��B�2��EC\�	�XLP�/���@�R]�(�����@�-�y�$N�m�.������݌�U��U.b0iic］���pR��Y��!3�	!DwIr jj~ťY�X��D�EU�R������i�o�!��ؒXbJc��4�}����(S!�9��@�d`��P�TOyf9G��Xg�Tl"�,*��	!Q�O8�מ،6�mj"�"�&���b�B1xHr ��[ADu���n,��D�v��Q]R�aa k�.��҃ڮƭp���<4v�U��;C�AfB�^"Ɂ��n%���DV��m�L��5��]CDUU�ׄ�t��&B��D��hj�b���Lܑ8�%�t+��X4��P!��$B�d��Ѵ[i�k�!�����%�y�$NvxB*���	EXL�:'���c�̈́ׄ��Ib �}G�!N�JhS(�G�q�4��f8:�#h[�k�k����H��q��4�4�ۄ��@de$
��GA\~�"��.B�T#D�v51Gc|�{�z,�j�������p"+"	�b�B��k�������9�����D0����R!D��
���C�$��K�)�	K������K��ѴhkCᖁ�b�s��4G6��k�Yu��#ӎ�qh0�1��Gm��!����.-�YR���5{'�7*�(�n��t)�7�1���2�\j�h+�+�h+͑�x�%�p8�[��M�$B�F��B����V��X�;֨����*GU]͈]#����5v�Y�Y��e�u���ɞE{�(<�XC0��-��Xg���%1B��G��B��U�Ϊ�YpꜸUn����Ŵ����i	�CߠGߠ'�1LZDPy���ր�f�Q��mi#uO*�ű�jFnIXc�$ B1��]]�>r�C�y_�GKd��KƱ�p�80���* k��7Z唄A�u�.��ҍƮ!�>s�C�}��W-�:"�A
!��-�$J�C�C��W֦kåu�?MI    IDAT~?6�u�u�����zB-���W�:���e"��h��@ע��CO�:�ѣG���o���ح}�J%����f\.��w ��ә9s&7n�����v�ш�n��pt+!��$9���5h�'|�sI��h�li��h�X�1���O��׈�di�"�ҾF�P_�9R�e��8�LF�J%��������������MD�j�<����w�1���є�Yɫ�� ;=�L�F�g��ce� !Bϖ�=��z�GMDE<:[= ?��Ϙ;wn��<���l۶�ٳg����֭[;ԛ={6+W�d���g���f���̙�V�����/���'�|�����no���M��o��N�㪫�b޼y����׷�����������8��3�K!+I���6-�J�oV$�o�K�9�����j7x����XCHݝ�Ʈ��r�V�}�p��]<���p"�����X��'?��#~�/�d��1��|�_�W�������|��(����o�F��_-a_y�y��yTJ/]w!�q����G~¾OVV����l�����o~��b�ꫯ>�s��z�}�Y���y��),,$55��/����LV�\��j�oxx8s���_��mmm ���p��S[[�W_}Eaa!F�����s�m�1r�H֮]{�q!�@6������-�e�D�E`���J������`��rx�aT!�!�X��4�`�3����K��v�$�;Z��������r{H3Y����drQf�/9��`9?�ys3;$f$ 0+=�R�ײ0u��0��M��[d%1sd<?�´�f�5��az�X�v-��s._��aÆ�����o�������{���y��x�b�Z-6l𕵶������{��u%z饗x뭷��Kx��hjj�%����x"B �k֡k�Y�W�ƨoFa7رl�6�b�p�:�s$��x�.�C۪EעC۬Eתk�w�pwr��C�R���hhqp����z���h���y<��w,��+��P\������;�i�l-�fz��ɩ�l+<�gݛ8|z��/��	�\:n g��;�I���+W���Q�T\w�u�m_|�~���Ҹ��HLL�����>������ՙ7on����{ϯ|�ƍ�u�],X���� ''�}������+�����ۻ�������OWIPI�H�r�DQTr*��96SZYiͬ�rf*K�ԙ�\V�wLgp&3-��-QӔ�ㅼ�xDDADA�r����s�Ɣ�c-���?��sH��?{��&99�^ۢ�"�����^��"Ҵ)8i�+�q/p��r�}�2$�C�ŮT�QA�o1W�]�]�.-��'�ˣnw'�\ٗs�"0�ڕ�j���2�οx�����'����430u�V�� ��~�Al����f�/Ne��T ���ݚ�̟����ёq��мys�Ν;g<��S0���jjjprrb���=� ���ӡCN�8Qo���˗9z�(�;w��ɩ^Bq�N�fڴi{۶m�ر#{�졸��'}~�ۅ��� ::���p-Z����um�֭��򢨨��g�6�.]�п�,YB^�7��j�nݚ��"��SS�C�n�s%��;�Qc�Η�Sp���~�u�����׿H9�C�����]�|{����������Ns�t!}������K��D����e�q���$���w�����u�8v��Y��9���lڴ	�����y�7=z4'Nj�mެa0����ԩSu			����~�z�ch׮QQQ���Ozz:�������۞��z饗<x�5�L�>�6 0t�PjjjX�lY�v���5�u��588

�7� $$�\v��Q�~�m:t�k�|�IBBB�;w. �7���X�����JJJX�p!III��ԘwO����%�����>ѓ�ٕu�����S��* �l��NE&�s�׍����A��6l;~�*��o���dtGs�AD��4wv��op�8p�ͺ#G�p�ر�5n�8��>+V�`̘1t���\f�I����V�(++�hg����<@JJ
���6�p��2i�$ 222���8w�\�?������߽ȯ���3����ڵ��6�W��5���*��Ac�����G����ܹs9q��=�?��#FX��j���>��S���mڴaРA�۷�={�������7Æ��_�`0�`���ۇ��Wr�?>Jd`k"[��Ζ�1��ü�&�"`�3TT��c*i8��y�/SW�`�\���JX�;��m���ƌc3 �uo��s
���,��뱳�����۷/���\��ק���w�^<==͉�+W�d�ԩ����H��H#%&&�����{�1�֭[3e�V�Ze.���f�̙<���̜9��������[��r��9�~�i���k�vݺu,]����������w�u+X�'��{2h����{���o��&���=~�x������T��|z���hOw/�pv`���=��;����؎mؙ�Ol��+ٕմ�2���QRR��o�n���pqq���4c`jg2x�`������]f�vv�����			�\������D�����`0��/���NMM�Eb�ƍ�-���`���mۖ3gΰv�ZRRR,����b4ٴi�E��m�(++#66�fp0h� ���Kvv��,??��LCNN�N�"((gg��k�k�STJNQ)��� �Ӎ��iC��E��Y�خ2�p1|��.z�����J�����.,�¾���	n��)�����i��S�QPP@EEV�=<<0������ܹs�<x�>}���@D���}���/�`0G�f�puu%..�����g���W^!11�Ν;ӬY3bbb�1c111�6����u�]ddd�[C]]]Mzz:mڴ��0�֭AAA�]bq�ؽ��())��k��_4/���ânczm�@ߎ~�����g-n�7ɥW{_��k��4�%E�QYY�����^��h�ȑ#���nQ���Jpp0Ǐ�ةh����������!|}}tƁ�4y�9i�Q�F�L"^�j`����X����*~�a�}�����Ϛ�@DFF�����?η�~@�V�ptt���Ô����S��&!!����z3�4t���Q�Oz��e��#V����I����y�9#;��X^��]�$�N�Yc�$�#g�׍���&�7�d����ˣ[�nxxxPXXxC}mذ����f����cooo���``РAl߾���k��������*6oތ��/$$���x���عs��YD�V��@�����c�n�޽8p��}���I��v�";;���@sY�f�{��z�oJ5�����~��%����2i�$.]������~-�prd��>��ە�ݚN���/��`O�;=��C���׊��"������6���v�=�̔o`�����5��л8w������w8;�Tw����;;h��l~�KW*�^w+�9sf�� �w�}�m۶���_ƂHKK�y��^��-[�4�=���4h�=�;v$33���@���GFFK�.5�����M�66��A�_�G�&??��{�RRRB@@ @�nc�6i*�4�SO=��&$X,?2��bk��D�� ���k�f<<<���pww���8}��[6s����s��ُ�?��W_e42g������ק�a`� .]�d�I�d��+��T�Z��H.����ه�E�mQV�~�I�+�e1d��?��\����}�~u𙜜���+<� �z�����<�u��Iv��i5XMOO��\\^^�رcy����ӧ�������,_����D��������Xc�͋���{��xyyq��E�o�NRR�rDDPp �SUey�����3&�][~|�lBBם����䣏>��ߟɓ'��3�j�\(�9k�j�B\�;���W'��5�8Wº���)����g;O�[\FqY������_��@O7���c��|��i�.���j��ݢE�X�hQ���F.\���}��|��V�{�����_�p��ӧ3}�t�����F�>}��������Znn.���c޼y��""M���_�ϱkKqq1���x{{[�����h4Z��@hh(�gϾf����|��xyy�ꫯ^�뭢�R9�w��~�ɿx��{2l���:w��Kwd���M�/������b�_�i�[��/�ʕ+899�,}8p ???|||,ʛ7oNpp0G��ص%!!���*֬Yc�ϐ��ϟ���/���mH�T^^Μ9s�̴>k#""��@�r��Y|||

��L7��G��(5j��"���'>>�o����"�K`�����㏹x�"O<�����1��,+W����IDDOˊD��-l���������'�|��Çqsscɒ%?i�úu눏�g�Сt�҅���ڵ+���X�M�֭Y�|���"##qvv��ۛ��$�mRRR�6mZ��*"""�."�o�>��W�ԩS�?�^��˗/��C���M^^�y����INN��m�m�,N3��$�	&�裏˽��KQQs����O?���(??�;������ߓ��|��r���k֋�����.<<�qg̋ȯ���k֬!))���ğ��}�>N���ݒ�����R���ޕIDDn_�9��<��C���k��I��F222x����ɹ�C�[�rDn#���7{"""r�́����� 
DDDDD��������H"""""(8�:
DDDDDPp """""u�������@DDDDD�(8@��������Qp """""�����@DDDDD """""RG������� 
DDDDD��������H"""""(8�:
DDDDDPp """""u�������@DDDDD�(8@��������Qp """""�����@DDDDD """""RG������� 
DDDDD�����������M�C��=�o�{c������$
D��em��C��-+@��������Qp """""�����d��������gQ���KMM������8::Z�]�|����_l��v]�t�O�����e�HNN���ڴicQVRR�ŋt���͚��{VYYEEE?y<""�"r[sttdŊe�f�bѢEVۿ��{t��ŢlÆ7Ǎ��䄋����TT�zۄ�={���$��>�·�~{C��jժ��$--�g�}��׺���x�b<<<�e+V��/���IDDjiY����***��� ""��dz����{�Vۏ9���RSSY�x17 <��lڴ�#F�P?7Kaa!)))9r�g������߉i',,�����^;t�Ps`�p�B"""�����H�RZZ���ӦM�e˖7{8�9s���~��휜�9r��������H����H~~>>>>L�:�A��l��׿���&**��ݻ�l7t�PJJJnxY���ئ�iR
y���ILL$::�'�x�4���@BB$  ���233Y�jk֬1/�iݺ5���
��� <����S�L�����ۢ�ٳgs��Y "##y�ᇙ5k��� �mۖ_|��>77�9s�_���3r�H���iٲ%����޽���$N�>mnץKF�i~�j�*���x����޽;����9s����S\\l�����&!!��lǎ,_����gNN�֭#>>�ѣG[|6Ӭ��ٳm.	pww������Ю];Z�jŅHKK#))���l��ӦM3����$%%1f�z���N�bɒ%�Y����GD�V�Gf"�䤥�1w�\ ƎKDDD������o�������g̘1�7��G�2e��z�-s�+W����n��?w�������jN�8���;qqq������Ε+W�}:���8����e��大�D������4�EEE�h�"�v�ʴi�>|83f� 44��>����ps�K�.����w�A\\���̛7���*�/_Naa!]�t������QXXș3g�ׯ����ts`�����h4r�}�R�~���������r�~����k��FII	��y��Gy����֭����	�h��arss����G�|���F��}�}�]\\\�:u*�?�|�?��ȭH���4I.d�֭�y�<==tݨQ����eժU̙3���L�=ʬY�ؾ};���<��@���III�ٳ�����SQQ��+�3����$�...������5)((��O?��ˋy��j�*�v�3f���Ȅ	ؽ{7�ܹ�	&���3pww~xR��w�0|�p^�u�|�M������+�\��(**"&&��?��I�&���Ď;�]^-;;�����g�yƢ��ёQ�F�`��F�u�2jǎ#//��[����/����K/�d�v�,[��Ν;�e�fϞ͖-[X�ncƌ��ŋ<��t�֭џKD�V��@D�����z�-rss����X^b����=� �/�Wo��|�G5���4
����E�����h���(,,$$$�֭[��"##)//����!C����������˳x���\RSSiժ��:�={����f~���C�~��3?����Y�v-3gδyvDC�f���-�_4���
֯_�>֯_�/�Po,999�9s����z�X�TTT��_X�]�p����cggǰa�~§��(8�&˴�������pƎ{��������SQQAFFF���'Op�=������q�F����ӧ��<..�6�y�f}����۴i�œ���H��ɹ5�rS���UiII�է�]�t�O>a���̟?����233�ˆL;988��B2kPVVFII	���:��c�2n�8ƍ���+���Y��ܹs����+?t��5sDDn
D�I;t��g���'��gϞ6ۚ��;99�c�v��m�t�R�����˔LL7Ŧ�gggz���ƍٸq�E�������r/// ��9 �K�6��t�c���̙3ǜ�Ԡ��4{C�N�����h4�v��]߾}{���IHH���777��ܰ���9Cd�e����ߩ�ȭH��H��d�BCC0` S�N����v���@���^��K�.5j{�졸����H���	#??��ǏcooOQQ���xzzҡC***طo�EUUU 6�͘�M�~��]��ꫯҡC^~�e�y�F�����|��	������ǘ1c

b������Z��m۶eƌ�������-l]o��{k�DDnu�9�~�mN�<I�-�>}:������ ���JUU%%%6��j���|��78::һwo���o�0ՙ���űy��z�a��'ܦ�S�N5jl?�x�bv��ɢE�HMM�C�L�0����'�|BMM111���5x����Ӷm[***HNNn���f^l����6�O�[��jg&M�Dyy9!!!V�7=y�y��N�:Y�g֬Y�mRMLO�����eAAA���Y�3=��{��X6d����������p0[[��rn�1�̃)�����Gy�޽{�P�&G�e�֭ ���l�L�)X�����m�����6m��+�ѣ ���4�[���:Ǐ��+`}�IMM~�!P�ݦi��}��GLL_}��E�iͺiI����yM��v��EII	QQQ�?�"�x���\�p���0���ٻwo��[��cǎq�=�fQI�Ν9z��y�ПCaa!�'O����ɓ'��gh�ɓ'3x�`V�X��k���(--��Օ��X����8Z�ju��+++�m�کS'z����˗����<�[�����[7{""��M�F\\:t��ח=zP^^^�\�}j���Kǎ����IMM������ҥK2��={���H`` C�a���,[����$�kΟ?ϰa�����2���P�}�]�$X��H�v��ر#_~�%�v��cǎ�^��m۶���h$55����76ggg<<<0` ���*YYYL�8�����$�?���DDD��ၧ�'���x{{[l������ɓ�����ˋV�Z�����������ˋ�-,ա�  �IDAT[ңG���9|���}�y�w0` w�}7�����ٓ��,s2uee%/^��0��ܽ{wZ�hA˖-	�����Ǐc4��ϧw��������2d}�����
777�ر�y&�E��1�C�QPP�3�<C@@ qqqL�8;;;�x���DD�ve~cS�����R�|���?~��5���L�2���4�,Yb����?>� AAA�FN�>����m��СC�������X�����z�	#55��I��ڵ#<<�]�v]3o�����￟��HZ�h��عs'6l�H������jsv��i~ݼysP�ݖ-[0���ԫۼy�����L���l۶��
 ݺu�}���ʏ9���ͯ�������	��������������9���lڴ	��].[�����3z�h���K�^�pww';;��˗[$EDnG
DD�I�:8xꩧn�pDDn*�������sDD�	���2n׼ys������'++��LD�&Ѳ"i������:�v�Z>���4"��K������� �9�:
DDDDDPp """""u�������@DDDDD�(8@��������Qp """""�����@DDDDD """""RG������� ��-7l�"k�    IEND�B`�<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.38.0 (20140413.2041)
 -->
<!-- Title: %3 Pages: 1 -->
<svg width="581pt" height="355pt"
 viewBox="0.00 0.00 581.00 355.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 351)">
<title>%3</title>
<polygon fill="#333333" stroke="none" points="-4,4 -4,-351 577,-351 577,4 -4,4"/>
<text text-anchor="middle" x="286.5" y="-9.2" font-family="Times,serif" font-size="16.00" fill="white">Network Map</text>
<!-- SW1 -->
<g id="node1" class="node"><title>SW1</title>
<polygon fill="#006699" stroke="#006699" points="288,-99 196,-99 196,-26 288,-26 288,-99"/>
<text text-anchor="middle" x="242" y="-58.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">SW1</text>
</g>
<!-- R2 -->
<g id="node3" class="node"><title>R2</title>
<polygon fill="#006699" stroke="#006699" points="96.5,-223 19.5,-223 19.5,-150 96.5,-150 96.5,-223"/>
<text text-anchor="middle" x="58" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R2</text>
</g>
<!-- SW1&#45;&#45;R2 -->
<g id="edge2" class="edge"><title>SW1&#45;&#45;R2</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M195.85,-66.0313C157.833,-70.6235 105.266,-83.1667 74,-117 65.7944,-125.879 61.5425,-138.135 59.4135,-149.829"/>
<text text-anchor="middle" x="124" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="34.4135" y="-138.629" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="170.85" y="-54.8313" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/2</text>
</g>
<!-- R1 -->
<g id="node4" class="node"><title>R1</title>
<polygon fill="#006699" stroke="#006699" points="219.5,-223 142.5,-223 142.5,-150 219.5,-150 219.5,-223"/>
<text text-anchor="middle" x="181" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R1</text>
</g>
<!-- SW1&#45;&#45;R1 -->
<g id="edge1" class="edge"><title>SW1&#45;&#45;R1</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M195.881,-96.793C190.284,-102.865 185.364,-109.638 182,-117 177.403,-127.061 176.014,-138.852 176.109,-149.788"/>
<text text-anchor="middle" x="232" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="151.109" y="-138.588" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="170.881" y="-85.593" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
</g>
<!-- R6 -->
<g id="node7" class="node"><title>R6</title>
<polygon fill="#006699" stroke="#006699" points="342.5,-223 265.5,-223 265.5,-150 342.5,-150 342.5,-223"/>
<text text-anchor="middle" x="304" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R6</text>
</g>
<!-- SW1&#45;&#45;R6 -->
<g id="edge4" class="edge"><title>SW1&#45;&#45;R6</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M271.235,-99.2785C275.175,-105.007 278.915,-111.023 282,-117 287.27,-127.212 291.593,-138.931 294.97,-149.755"/>
<text text-anchor="middle" x="339" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="269.97" y="-138.555" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
<text text-anchor="middle" x="246.235" y="-103.079" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/5</text>
</g>
<!-- R3 -->
<g id="node8" class="node"><title>R3</title>
<polygon fill="#006699" stroke="#006699" points="465.5,-223 388.5,-223 388.5,-150 465.5,-150 465.5,-223"/>
<text text-anchor="middle" x="427" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R3</text>
</g>
<!-- SW1&#45;&#45;R3 -->
<g id="edge3" class="edge"><title>SW1&#45;&#45;R3</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M288.272,-70.4405C320.828,-77.3989 363.655,-90.9867 393,-117 402.836,-125.719 410.149,-137.939 415.42,-149.648"/>
<text text-anchor="middle" x="456" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="390.42" y="-138.448" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="313.272" y="-59.2405" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/3</text>
</g>
<!-- R5 -->
<g id="node2" class="node"><title>R5</title>
<polygon fill="#006699" stroke="#006699" points="403.5,-347 326.5,-347 326.5,-274 403.5,-274 403.5,-347"/>
<text text-anchor="middle" x="365" y="-306.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R5</text>
</g>
<!-- SW2 -->
<g id="node6" class="node"><title>SW2</title>
<polygon fill="#006699" stroke="#006699" points="104,-347 12,-347 12,-274 104,-274 104,-347"/>
<text text-anchor="middle" x="58" y="-306.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">SW2</text>
</g>
<!-- R2&#45;&#45;SW2 -->
<g id="edge5" class="edge"><title>R2&#45;&#45;SW2</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M58,-223.115C58,-239.01 58,-257.704 58,-273.629"/>
<text text-anchor="middle" x="108" y="-244.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="29" y="-262.429" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/11</text>
<text text-anchor="middle" x="33" y="-226.915" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
</g>
<!-- R4 -->
<g id="node5" class="node"><title>R4</title>
<polygon fill="#006699" stroke="#006699" points="526.5,-347 449.5,-347 449.5,-274 526.5,-274 526.5,-347"/>
<text text-anchor="middle" x="488" y="-306.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R4</text>
</g>
<!-- R3&#45;&#45;R5 -->
<g id="edge7" class="edge"><title>R3&#45;&#45;R5</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M388.218,-210.267C377.75,-218.511 367.74,-228.841 362,-241 357.274,-251.011 356.378,-262.789 357.152,-273.728"/>
<text text-anchor="middle" x="412" y="-244.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="332.152" y="-262.528" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="363.218" y="-214.067" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/2</text>
</g>
<!-- R3&#45;&#45;R4 -->
<g id="edge6" class="edge"><title>R3&#45;&#45;R4</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M455.28,-223.045C459.199,-228.854 462.927,-234.955 466,-241 471.208,-251.244 475.514,-262.971 478.893,-273.794"/>
<text text-anchor="middle" x="523" y="-244.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="453.893" y="-262.594" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="430.28" y="-226.845" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
</g>
</g>
</svg>
# -*- coding: utf-8 -*-
"""
Завдання 11.4

Создать функцию create_network_map, которая обрабатывает вывод команды show cdp
neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент
список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между
устройствами. Структура словаря такая же, как в задании 11.3:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

Не копировать код функции parse_cdp_neighbors.
Если функция parse_cdp_neighbors не может обработать вывод одного из файлов
с выводом команды, надо исправить код функции в задании 11.3.

Пример работы функции
In [3]: pprint(create_network_map(infiles), sort_dicts=False)
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1'),
 ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [4]: pprint(create_network_map(["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt"]), sort_dicts=False)
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1'),
 ('R1', 'Eth0/0'): ('SW1', 'Eth0/1')}

"""
infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]
# -*- coding: utf-8 -*-
"""
Завдання 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функція має повертати кортеж із двома списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через
subprocess).  IP-адрес считается доступным, если выполнение команды ping
отработало с кодом 0 (returncode).  Нюансы: на Windows returncode может быть
равен 0 не только, когда ping был успешен, но для задания нужно проверять
именно код. Это сделано для упрощения тестов.

"""
# -*- coding: utf-8 -*-
"""
Завдання 12.2

Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Пример вызова функции
In [3]: convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'])
Out[3]:
['8.8.4.4',
 '1.1.1.1',
 '1.1.1.2',
 '1.1.1.3',
 '172.21.41.128',
 '172.21.41.129',
 '172.21.41.130',
 '172.21.41.131',
 '172.21.41.132']

In [4]: convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.10-12', '10.1.1.1-10.1.1.4'])
Out[4]:
['8.8.4.4',
 '1.1.1.10',
 '1.1.1.11',
 '1.1.1.12',
 '10.1.1.1',
 '10.1.1.2',
 '10.1.1.3',
 '10.1.1.4']

"""
# -*- coding: utf-8 -*-
"""
Завдання 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функція нічого не повертає, только делает print.

Пример вызова функции
In [6]: reach_ip = ["10.1.1.1", "10.1.1.2"]
In [7]: unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]

In [8]: print_ip_table(reach_ip, unreach_ip)
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
