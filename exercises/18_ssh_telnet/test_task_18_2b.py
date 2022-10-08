
import pytest
import task_18_2b
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


correct_return_value = (
    {
        "ip http server": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#ip http server\n"
        "R1(config)#",
        "logging buffered 20010": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging buffered 20010\n"
        "R1(config)#",
    },
    {
        "a": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#a\n"
        '% Ambiguous command:  "a"\n'
        "R1(config)#",
        "logging": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging\n"
        "% Incomplete command.\n"
        "\n"
        "R1(config)#",
        "logging 0255.255.1": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging 0255.255.1\n"
        "                   ^\n"
        "% Invalid input detected at '^' marker.\n"
        "\n"
        "R1(config)#",
    },
)


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_2b, "send_config_commands")


def test_function_return_value(capsys, first_router_from_devices_yaml):
    """
    Перевірка роботи функції
    """
    commands_with_errors = ["logging 0255.255.1", "logging", "a"]
    correct_commands = ["logging buffered 20010", "ip http server"]
    test_commands = commands_with_errors + correct_commands

    return_value = task_18_2b.send_config_commands(
        first_router_from_devices_yaml, test_commands, log=False
    )

    # проверяем возвращаемое значение
    assert return_value != None, "Функція нічого не повертає"
    assert type(return_value) == tuple, "Функция должна возвращать кортеж"
    assert 2 == len(return_value) and all(
        type(item) == dict for item in return_value
    ), "Функція має повертати кортеж із двома словниками"
    correct_good, correct_bad = correct_return_value
    return_good, return_bad = return_value
    assert (
        correct_good.keys() == return_good.keys()
    ), "Функція повертає неправильне значення для словаря с командами без ошибок"
    assert (
        correct_bad.keys() == return_bad.keys()
    ), "Функція повертає неправильне значення для словаря с командами с ошибками"


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_function_stdout(error, command, capsys, first_router_from_devices_yaml):
    return_value = task_18_2b.send_config_commands(
        first_router_from_devices_yaml, [command], log=False
    )

    # Проверяем вывод информации об ошибках в stdout
    # во входящих данных три команды с ошибками
    # при каждой ошибке, должна выводиться информация:
    # ошибка, IP устройства, команда
    # в тесте проверяется наличие этих полей
    stdout, err = capsys.readouterr()
    ip = first_router_from_devices_yaml["host"]
    assert error in stdout, "В сообщении об ошибке нет самой ошибки"
    assert command in stdout, "В сообщении об ошибке нет выполняемой команды"
    assert ip in stdout, "В сообщении об ошибке нет IP-адреса устройства"
