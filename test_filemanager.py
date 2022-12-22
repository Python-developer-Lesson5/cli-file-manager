from filemanager_funcs import*

# тестируем функцию выводящую данные об авторе программы
def test_program_author():
    assert about() == 'Author Name'

#тестируем функцию создания файла
def test_create_a_folder():
    name_file = "file_for_testing"
    assert create_dir(name_file) == 1

#тестируем функцию удаления  файла
def test_delete_file():
    name_file = "file_for_testing"
    assert del_dir(name_file) == 1

# тестируем функцию смены директории
def test_delete_dir():
    name_dir = "dir_for_testing"
    assert change_dir(name_dir) == 0