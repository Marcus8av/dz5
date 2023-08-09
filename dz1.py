# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os

file_path = "C:/admin/mark/images/фотодома.png"
def parse_file_path(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

print(f'Путь: {file_path} \nКортеж из пути: {parse_file_path(file_path)}')