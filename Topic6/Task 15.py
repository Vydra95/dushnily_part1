"""
Создайте класс `TextFile`, который будет выступать контекстным менеджеров по работе с файлом sample_file.txt
Попробуйте с помощью объекта этого класса сделать новые записи в файле
"""


class TextFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__text = None

    def __enter__(self):
        try:
            self.__text = open(self.file_path, "a+")
            return self
        except Exception as e:
            print(f"{e}: Text source is unreachable")
            return None

    def write_info(self, info):
        if self.__text is not None:
            self.__text.write(info)
        else:
            print("File is not open. Cannot write information.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__text is not None:
            self.__text.close()
        return False


with TextFile("C:\\Users\\Lenovo\\PycharmProjects\\PythonProject\\Topic6\\sample_file.txt") as text:
    if text is not None:
        text.write_info("Hello")
