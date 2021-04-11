В данном каталоге содержится директория data, в которой хранятся данные по исследованиям. 
Вам нужно пройтись рекурсивно по директориям и считать все файлы, у которых выполнены условия (для этого нужно создать 
итератор как класс, который принимает на вход путь к директории и будет возвращать подходящие файлы). 

Пример:
```
for file_name in DirReader("dir"):
```
Условие для чтения файла - файл оканчивается на .txt. 
Нам интересно знать, какие именно файлы нам подходят. Создайте декоратор print_iter, который будет выводить на экран имена файлов 
вовремя работы DirReader.
```
@print_iter
class DirReader:
```
Для чтения записей внутри файла нужно создать менеджер контекста, который открывает файл, 
пропускает первую строку и возвращает ваш собственный генератор, который читает только те записи, 
у которых выполнено условие - все символы в последовательности повторяющиеся.

Пример:
```
with FileReader(file_name) as record_reader:
    for record in record_reader:
``` 

С помощью данных из файла вам нужно создать экземпляры класса Research, с полями из файла (кроме id). 
По считанным исследованиям нужно посчитать и записать в файл result.txt: В какой час было сделано больше всего исследований по каждому прибору.
Создайте рядом директорию, в которой нужно будет создать файл для каждого учёного и записать соответствующие
исследования.
Задание нужно оформить в гит репозитории, с настроенным CI и тестированием.
