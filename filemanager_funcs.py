import os

"""
создание папки
"""
def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        return 1
    else:
        return 0

"""
удаление файла(папки)
"""
def del_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)

    if os.path.exists(path):
        if os.path.isfile(dir_name):
            os.remove(dir_name)
        else:
            os.rmdir(dir_name)
        return 1
    else:
        print('Файл или папка отсутсвует')
        return 0


# """
# копировать (файл/папку)
# """
# def copy_dir(dir_name, dir_new):
#     if os.path.exists(dir_name):
#         if os.path.isfile(dir_name):
#             shutil.copy(dir_name, dir_new)
#         else:
#             shutil.copytree(dir_name, dir_new, False, None)
#     else:
#         print('Файл или папка отсутсвует')
#
# """
# просмотр содержимого рабочей директории
# """
# def review_directory():
#     print(os.listdir())
#
# def review_a_folders_directory():
#     for root, dirs, files in os.walk(os.getcwd()):
#         return dirs
#
# def review_files_directory():
#     for root, dirs, files in os.walk(os.getcwd()):
#         return files

# """
# просмотр содержимого рабочей директории
# """
# def save_info_directory_in_listdirTxt():
#     with open('listdir.txt', 'w') as f:
#         f.write(f'files:{review_files_directory()}\n')
#         f.write(f'dirs:{review_a_folders_directory()}\n')
#
#
# def info_os():
#     return platform.platform()

def about():
    return 'Author Name'

"""
смена рабочей директории
"""
def change_dir(dir_name):
    if os.path.exists(dir_name):
        os.chdir(dir_name)
        return 1
    else:
        print('Папка отсутсвует')
        return 0