import json  # Нужна для сохранения переменных (словарей и списков)
import pathlib  # Нужна для создания папки
import shutil  # Нужна для удаления папки

from json.decoder import JSONDecodeError


# ---- Ш П А Р Г А Л К А ----
# r — открывает файл только для чтения.
# w — открывает файл только для записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для записи)
# w+ — открывает файл для чтения и записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для чтения и записи)
# a+ - открывает файл для чтения и записи.
#      (Информация добавляется в конец файла)
# b - открытие в двоичном режиме.

# Абсолютный путь (path) - показывает точное местонахождение файла
# Относительный путь (path) - показывает путь к файлу относительно какой-либо "отправной точки"

# JSON — текстовый формат обмена данными, основанный на JavaScript (похож на словарь Python)


# Класс для работы с файлами
class File:

    # Записать текст из "text" в файл по пути "path"
    @staticmethod
    def write_text(text: str, path: str, overwriting=True):
        # Файл перезаписывается
        if overwriting:
            # Открыть файл как объект и временно поместить его в переменную "file"
            with open(path, mode="w") as file:
                # Объект файл будет жить только в этом теле и по окончанию закроется и сохранится
                file.write(text)
        # Файл дополняется
        else:
            # Открыть файл как объект и временно поместить его в переменную "file"
            with open(path, mode="a+") as file:
                # Объект файл будет жить только в этом теле и по окончанию закроется и сохранится
                file.write(text)

    # Прочитать текст из файла по пути "path"
    @staticmethod
    def read_text(path: str):
        # Открыть файл как объект и временно поместить его в переменную "file"
        with open(path, mode="r") as file:
            # Объект файл будет жить только в этом теле и по окончанию закроется и сохранится
            return file.read()

    # Записать словарь/список из "data" в файл по пути "path"
    @staticmethod
    def write_json(data: dict or list, path: str, overwriting=True):
        # Файл перезаписывается
        if overwriting:
            with open(path, mode="w") as f:
                json.dump(data, f)
        # Файл дополняется
        else:
            try:
                # Чтение старого словаря.
                with open(path, mode="r") as f:
                    result = json.load(f)
            except JSONDecodeError:
                result = []
            except FileNotFoundError:
                result = []

            result.append(data)
            # Запись нового словаря.
            with open(path, mode="w") as f:
                json.dump(result, f, indent=4)

    # Прочитать словарь/список из файла по пути "path"
    @staticmethod
    def read_json(path: str):
        with open(path, mode="r") as file:
            return json.load(file)

    # Создание папки или всех папок в переданном пути. Указываем полный путь в "path"
    @staticmethod
    def create_folder(path: str):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    # Удаление папки и всех данных в ней (будь это файлы или папки)
    @staticmethod
    def delete_folder(path: str):
        shutil.rmtree(path, ignore_errors=True)
