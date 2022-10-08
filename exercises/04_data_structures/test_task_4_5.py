

def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_4_5

    out, err = capsys.readouterr()
    correct_stdout = "['1', '3', '8']"
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний рядок"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_4_5

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_4_5) if not var.startswith("_")]

    correct_result = ["1", "3", "8"]
    assert (
        "result" in task_vars
    ), "Итоговый список должен быть записан в переменную result"
    assert (
        type(task_4_5.result) == list
    ), f"По заданию в переменной result должен быть список, а в ней {type(task_4_5.result).__name__}"
    assert (
        correct_result == task_4_5.result
    ), f"В переменной result должен быть список {correct_result}"