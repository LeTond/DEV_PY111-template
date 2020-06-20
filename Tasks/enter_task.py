"""
Данное задание необходимо выполнить до конца курса. Все неоднозначные или не упомянутые моменты могут
трактоваться вами в любую сторону по вашему желанию. Решение должно представлять собой модуль с готовой реализацией,
прикрепленный в качестве ответа. По любым вопросам можно обращаться к преподавателю или задавать в форуме
"Вопросы и ответы", но запрещено делиться реализацией с другими людьми.

Использовать готовые решение запрещается, при сдаче работы будьте готовы к тому, что у преподавателя будут вопросы по
нюансам реализации или работе той или иной подсистемы. Сдача задания после указанного срока может привести к появлению
дополнительных заданий для вас.

Сдача задания является одним из обязательных условий получения зачета по курсу PY111.

Задание:

Дан каталог книг. Реализуйте библиотеку для хранения данных книг и поиску по каталогу. Каталог должен поддерживать
возможность добавления и удаления книг, редактирования информации о книге, а также обладать персистентностью
(т.е. сохранять библиотеку в внешнем файле и подгружать обратно). Также необходимо оформить точку входа,
поддерживать поиск по различным параметрам и обеспечить интерфейс взаимодействия пользователя с библиотекой.
"""
from Tasks.GUI import *
import json

# Реализация каталога через словарь словарей
book_list = {
    1: {'style': 'Фантастика', 'author': "Желязны", 'work': "Девять принцев Амбера", 'year': "1970"},
    2: {'style': 'Фантастика', 'author': "Желязны", 'work': "Ружья Авалона", 'year': "1972"},
    3: {'style': 'Фантастика', 'author': "Желязны", 'work': "Знак Единорога", 'year': "1975"},
    4: {'style': 'Фантастика', 'author': "Желязны", 'work': "Рука Оберона", 'year': "1976"},
    5: {'style': 'Детектив', 'author': "Дойл", 'work': "Скандал в Богемии", 'year': "1982"},
    6: {'style': 'Детектив', 'author': "Дойл", 'work': "Союз рыжих", 'year': "1982"}
}

book_add = {
    7: {'style': 'Детектив', 'author': "Дойл", 'work': "Собака Баскервилей", 'year': "1901"}
}

json_file = 'library'


def library_from_json(json_file):
    # with open(json_file, "w", encoding="utf-8") as file:
    #     json.dump(book_list, file)
    #     print(json.dumps(book_list, indent=4, ensure_ascii=False))
    with open(json_file, 'r') as file:
        template = json.load(file)

        with open(json_file, "w", encoding="utf-8") as file:
            # Добавляем новую книгу с новым ключем
            template['7'] = {'style': 'Детектив', 'author': "Не Дойл", 'work': "Собака Баскервилей", 'year': "1901"}
            # Удаляем книгу по ключю
            # template.pop('7', None)
            json.dump(template, file)
            print(json.dumps(template, indent=4, ensure_ascii=False))
            # print(template)
            # print(template.keys())


def search_in_library(json_file):

    list_book = ""
    # gui_interface(list_book)
    search_key_name = input("Введите ключевое слово: ")
    # search_key_name = text
    flag = True

    with open(json_file, 'r') as file:
        template = json.load(file)

        for search_book_list in template:
            if template[search_book_list]['style'] == search_key_name \
                    or template[search_book_list]['work'] == search_key_name \
                    or template[search_book_list]['author'] == search_key_name \
                    or template[search_book_list]['year'] == search_key_name:
                print_ = f"№: {search_book_list} / " \
                         f"Жанр: {template[search_book_list]['style']} / " \
                         f"Автор: {template[search_book_list]['author']} / " \
                         f"Произведение: {template[search_book_list]['work']} / " \
                         f"Год издания: {template[search_book_list]['year']}"
                list_book += print_ + '\n'
                flag = False
        if flag:
            print_ = 'Данная книга отсутствует в библиотеке'
            gui_interface(print_)
    gui_interface(list_book)

if __name__ == '__main__':
    library_from_json(json_file)
    search_in_library(json_file)

