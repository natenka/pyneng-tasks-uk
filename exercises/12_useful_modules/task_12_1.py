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
