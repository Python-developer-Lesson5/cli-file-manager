import os
import shutil
from pathlib import Path
import platform

"""
создание папки
"""
def create_dir(path: Path):
    if not path.exists():
        path.mkdir()
        return True
    else:
        return False

"""
удаление файла/папки
"""
def del_file_or_dir(path: Path):
    if path.exists():
        if path.is_file():
            os.remove(path)
        else:
            os.rmdir(path)
        return True
    else:
        return False

"""
копирование файла/папки
"""
def copy_file_or_dir(path: Path, new_path: Path):
    if path.exists():
        if path.is_dir():
            shutil.copytree(path, new_path)
        else:
            shutil.copy(path, new_path)
        return True
    else:
        return False

"""
получение списка файлов/папок
"""
def get_files_and_dirs(path: Path):
    items = []
    for f in path.glob('*'):
        items.append(f.name)
    return items

"""
получение списка файлов
"""
def get_files(path: Path):
    files = []
    for f in path.glob('*'):
        if f.is_file():
            files.append(f.name)
    return files

"""
получение списка папок
"""
def get_dirs(path: Path):
    dirs = []
    for f in path.glob('*'):
        if f.is_dir():
            dirs.append(f.name)
    return dirs

"""
сохранение содержимого рабочей директории
"""
def save_workdir_contents(path: Path):
    files = get_files(path)
    dirs = get_dirs(path)

    with open(path / 'listdir.txt', 'w') as f:
        if len(files) > 0:
            files_str = ', '.join(files)
            f.write(f'files: {files_str}\n')
        if len(dirs) > 0:
            dirs_str = ', '.join(dirs)
            f.write(f'dirs: {dirs_str}')

"""
получение новой рабочей директории
"""
def get_new_workdir_path(current_path: Path, new_work_dir: str):
    if Path(new_work_dir).is_absolute():
        new_work_dir_path = Path(new_work_dir)
    else:
        new_work_dir_path = current_path / new_work_dir

    if new_work_dir_path.exists():
        return new_work_dir_path
        
    return None

"""
получение информации об OS
"""
def get_os_info():
    return platform.platform()

"""
получение информации об авторе
"""
def get_creator_info():
    return 'Александр Масс'