import os
import platform
import random
import shutil
from pathlib import Path

# Текущая рабочая директория
WORKDIR = Path.cwd()


def create_folder():
    folder_name = input('Введите название папки: ')
    folder_path = WORKDIR / folder_name
    if folder_path.exists():
        print('Папка с таким именем уже существует!')
        return
    folder_path.mkdir()
    print('Папка создана')


def remove():
    fname = input('Введите название папки/файла: ')
    fpath = WORKDIR / fname
    if not fpath.exists():
        print('Папки/файла с таким именем не существует.')
        return
    if fpath.is_dir():
        shutil.rmtree(fpath)
    else:
        os.remove(fpath)
    print('Удаление выполнено')


def copy():
    fname = input('Введите название папки/файла: ')
    fpath = WORKDIR / fname
    new_fname = input('Введите название новой папки/файла: ')
    new_fpath = WORKDIR / new_fname
    if not fpath.exists():
        print('Папки/файла с таким именем не существует.')
        return
    if fpath.is_dir():
        shutil.copytree(fpath, new_fpath)
    else:
        shutil.copy(fpath, new_fpath)
    print('Копирование завершено')


def show_workdir():
    for f in WORKDIR.glob('*'):
        print(f'- {f.name}')


def show_workdir_folders():
    for f in WORKDIR.glob('*'):
        if f.is_dir():
            print(f'- {f.name}')


def show_workdir_files():
    for f in WORKDIR.glob('*'):
        if f.is_file():
            print(f'- {f.name}')


def show_os_info():
    print(platform.platform())


def creator_info():
    print('Александр Масс')


def play_quiz():
    ###   СПИСОК ИЗВЕСТНЫХ ЛЮДЕЙ   ###
    """
    1. 10 января - Алексей Николаевич Толстой, писатель, 1883 год
    2. 15 января - Александр Грибоедов Дата рождения:  1795 года
    3. 23 января - Стендаль (Анри Мари Бейль), писатель, 1783 год
    4. 27 января - Вольфанг Амадей Моцарт, композитор, 1756 год.
    5. 29 января - Антон Павлович Чехов, писатель, 1860 год.
    6. 1 февраля - Борис Ельцин Дата рождения:  1931 года
    7. 7 февраля - Чарльз Диккенс, писатель, 1812 год.
    8. 8 февраля - Дмитрий Менделеев, химик, 1834 год.
    9. 15 февраля - Галилео Галилей, астроном, 1564 год.
    10.19 февраля - Николай Коперник, астроном, 1473 год.
    """

    months = {'01': 'января', '02': 'февраля'}

    days = {'10': 'десятое', '15': 'пятнадцатое', '23': 'двадцать третье',
            '27': 'двадцать седьмое', '29': 'двадцать девятое', '01': 'первое',
            '07': 'седьмое', '08': 'восьмое', '19': 'февраля'
            }

    spisok = ['Алексей Николаевич Толстой', 'Александр Грибоедов',
              'Стендаль', 'Вольфанг Амадей Моцарт', 'Антон Павлович Чехов',
              'Борис Ельцин', 'Чарльз Диккенс', 'Дмитрий Менделеев',
              'Галилео Галилей', 'Николай Коперник']

    while True:
        right = 0
        incorrect = 0
        viktorina = random.sample(spisok, 5)

        for element in viktorina:
            if element == 'Алексей Николаевич Толстой':
                year_birth1 = input(
                    'Введите дату рождения А.Н.Толстого: ')  # 10.01.1883
                if year_birth1 == '10.01.1883':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth1 = '10.01.1883'
                    day, month, year = year_birth1.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Александр Грибоедов':
                year_birth2 = input(
                    'Введите дату рождения А. Грибоедова: ')  # 15.01.1795
                if year_birth2 == '15.01.1795':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth2 = '15.01.1795'
                    day, month, year = year_birth2.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Стендаль':
                year_birth3 = input(
                    'Введите дату рождения Стендаля: ')  # 23.01.1783
                if year_birth3 == '23.01.1783':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth3 = '23.01.1783'
                    day, month, year = year_birth3.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Вольфанг Амадей Моцарт':
                year_birth4 = input(
                    'Введите дату рождения В.А. Моцарта: ')  # 27.01.1756
                if year_birth4 == '27.01.1756':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth4 = '27.01.1756'
                    day, month, year = year_birth4.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Антон Павлович Чехов':
                year_birth5 = input(
                    'Введите дату рождения А.П. Чехова: ')  # 29.01.1860
                if year_birth5 == '29.01.1860':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth5 = '29.01.1860'
                    day, month, year = year_birth5.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Борис Ельцин':
                year_birth6 = input(
                    'Введите дату рождения Б. Ельцина: ')  # 01.02.1931
                if year_birth6 == '01.02.1931':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth6 = '01.02.1931'
                    day, month, year = year_birth6.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Чарльз Диккенс':
                year_birth7 = input(
                    'Введите дату рождения Чарльза Диккенса: ')  # 07.02.1812

                if year_birth7 == '07.02.1812':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth7 = '07.02.1812'
                    day, month, year = year_birth7.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Дмитрий Менделеев':
                year_birth8 = input(
                    'Введите дату рождения Д. Менделеева: ')  # 08.02.1834
                if year_birth8 == '08.02.1834':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth8 = '08.02.1834'
                    day, month, year = year_birth8.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Галилео Галилей':
                year_birth9 = input(
                    'Введите дату рождения Галилео Галилея: ')  # 15.02.1564
                if year_birth9 == '15.02.1564':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth9 = '15.02.1564'
                    day, month, year = year_birth9.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Николай Коперник':
                year_birth10 = input(
                    'Введите дату рождения Николая Коперника: ')  # 19.02.1473
                if year_birth10 == '19.02.1473':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth10 = '19.02.1473'
                    day, month, year = year_birth10.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

        print('Количество правильных ответов =', right)
        print('Количество ошибок =', incorrect)
        print('Процент правильных ответов =', right * 100 / 5)
        print('Процент неправильных ответов =', incorrect * 100 / 5)

        play_again = input(
            'Хотите начать игру сначала (введите "да" или "нет") ?: '
        )
        while play_again.lower() not in ['нет', 'да']:
            play_again = input(
                'Не могу вас понять. Введите "да" или "нет" ?: '
            )
        if play_again == 'нет':
            return


def my_bank_account():
    bill_sum = 0
    history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет: {bill_sum}')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            cost = int(input('Введите сумму пополнения в копейках: '))
            bill_sum += cost
        elif choice == '2':
            cost = int(input('Введите сумму покупки в копейках: '))
            if cost > bill_sum:
                print('Недостаточно средств')
            else:
                bill_sum -= cost
                name = input('Введите название покупки: ')
                history.append((name, cost))
        elif choice == '3':
            if history == []:
                print('У вас нет покупок.')
            else:
                print(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


def change_workdir():
    global WORKDIR
    new_wd = input('Введите путь к новой рабочей директории:')
    # Есть путь - полный
    if new_wd.startswith('/'):
        new_wd_path = Path(new_wd)
    else:
        new_wd_path = WORKDIR / new_wd
    if not new_wd_path.exists():
        print('Ошибка. Директории не существует.')
        return
    WORKDIR = new_wd_path
    print('Новая рабочая директория:', WORKDIR)


def main():
    print('Вас приветствует консольный файловый менеджер.')
    while True:
        print(
            '\nВыберите команду:\n',
            '1 - создать папку\n',
            '2 - удалить (файл/папку)\n',
            '3 - копировать (файл/папку)\n',
            '4 - просмотр содержимого рабочей директории\n',
            '5 - посмотреть только папки\n',
            '6 - посмотреть только файлы\n',
            '7 - просмотр информации об операционной системе\n',
            '8 - создатель программы\n',
            '9 - играть в викторину\n',
            '10 - мой банковский счет\n',
            '11 - *смена рабочей директории\n',
            '0 - выход\n',
        )
        cmd = input('>: ')
        if cmd == '0':
            print('Завершение работы.')
            break
        elif cmd == '1':
            create_folder()
        elif cmd == '2':
            remove()
        elif cmd == '3':
            copy()
        elif cmd == '4':
            show_workdir()
        elif cmd == '5':
            show_workdir_folders()
        elif cmd == '6':
            show_workdir_files()
        elif cmd == '7':
            show_os_info()
        elif cmd == '8':
            creator_info()
        elif cmd == '9':
            play_quiz()
        elif cmd == '10':
            my_bank_account()
        elif cmd == '11':
            change_workdir()


if __name__ == '__main__':
    main()