# Составные сообщения об ошибках
def test_input_text(expected_result, actual_result):
    # Проверяем равенство ожидаемого результата и фактического результата
    assert expected_result == actual_result, \
           f"expected {expected_result}, got {actual_result}"


# Составные сообщения об ошибках и поиск подстроки
def test_substring(full_string, substring):
    # Проверка наличия подстроки в строке
    assert substring in full_string, \
           f"expected '{substring}' to be substring of '{full_string}'"