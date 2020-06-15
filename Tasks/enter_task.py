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

# Реализация каталога через словарь словарей
book_list = {'id1': {'style': 'Фантастика', 'auotor': "Желязны", 'work': "Девять принцев Амбера", 'Year': "1970"},
             'id2': {'style': 'Фантастика', 'auotor': "Желязны", 'work': "Ружья Авалона", 'Year': "1972"},
             'id3': {'style': 'Фантастика', 'auotor': "Желязны", 'work': "Знак Единорога", 'Year': "1975"},
             'id4': {'style': 'Фантастика', 'auotor': "Желязны", 'work': "Рука Оберона", 'Year': "1976"},
             'id5': {'style': 'Детектив', 'auotor': "Дойл", 'work': "Скандал в Богемии", 'Year': "1982"},
             'id6': {'style': 'Детектив', 'auotor': "Дойл", 'work': "Союз рыжих", 'Year': "1982"}}

name1 = input("Введите имя: ")
flag = True

for search_book_list in book_list:
    if book_list[search_book_list]['work'] == name1:
        print(f"Автор: {book_list[search_book_list]['auotor']} / "
              f"Произведение: {book_list[search_book_list]['work']} / "
              f"Год издания: {book_list[search_book_list]['Year']}")
        flag = False
if flag:
    print('нет такого значения')