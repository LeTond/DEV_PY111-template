"""
Дан каталог книг. Реализуйте библиотеку для хранения данных книг и поиску по каталогу. Каталог должен поддерживать
возможность добавления и удаления книг, редактирования информации о книге, а также обладать персистентностью
(т.е. сохранять библиотеку в внешнем файле и подгружать обратно). Также необходимо оформить точку входа,
поддерживать поиск по различным параметрам и обеспечить интерфейс взаимодействия пользователя с библиотекой.

Пример запуска кода:
python3 Tasks/enter_task.py show
python3 Tasks/enter_task.py -key Дойл show
python3 Tasks/enter_task.py -bk 8 -st Фантастика -au Ефремов -wo 'Туманность Андромеды' -ye 1957 save
python3 Tasks/enter_task.py -bk 8 delete
"""
import argparse
import json

json_file = 'Tasks/library'
list_book = ""


def search_in_library(json_file: str, list_book: str) -> None:
    parser = create_parser()
    namespace = parser.parse_args()
    search_key_name = namespace.key_word

    flag = True
    if namespace.command == 'show':
        with open(json_file, 'r') as file:
            template = json.load(file)
            for search_book_list in template:
                print_ = f"№: {search_book_list} / " \
                         f"Жанр: {template[search_book_list]['style']} / " \
                         f"Автор: {template[search_book_list]['author']} / " \
                         f"Произведение: {template[search_book_list]['work']} / " \
                         f"Год издания: {template[search_book_list]['year']}"
                if template[search_book_list]['style'] == search_key_name \
                        or template[search_book_list]['work'] == search_key_name \
                        or template[search_book_list]['author'] == search_key_name \
                        or template[search_book_list]['year'] == search_key_name:
                    list_book += print_ + '\n'
                    flag = False
                if search_key_name == None:
                    print(print_)
                    flag = False
            if flag:
                print_ = 'Данная книга отсутствует в библиотеке'
                print(print_)
        print(list_book)
    elif namespace.command == 'save':
        with open(json_file, 'r') as file:
            template = json.load(file)
            with open(json_file, "w", encoding="utf-8") as file:
                template[namespace.book] = {'style': namespace.style,
                                            'author': namespace.author,
                                            'work': namespace.work,
                                            'year': namespace.year}
                json.dump(template, file)

    elif namespace.command == 'delete':
        with open(json_file, 'r') as file:
            template = json.load(file)
            with open(json_file, "w", encoding="utf-8") as file:
                template.pop(namespace.book, None)
                json.dump(template, file)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-key",
                        "--key_word",
                        type=str,
                        help="Ключевое слово для поиска произведения")

    parser.add_argument("-bk", "--book",
                        type=str,
                        help="Номер нового произведения")

    parser.add_argument("-st", "--style",
                        type=str,
                        help="Жанр нового произведения")

    parser.add_argument("-au", "--author",
                        type=str,
                        help="Автор нового произведения")

    parser.add_argument("-wo", "--work",
                        type=str,
                        help="Название нового произведения")

    parser.add_argument("-ye", "--year",
                        type=str,
                        help="Год нового произведения")

    subparsers = parser.add_subparsers(dest="command")

    create_show_subparser(subparsers)
    create_save_subparser(subparsers)
    create_delete_subparser(subparsers)

    return parser


def create_show_subparser(subparsers):
    show_parser = subparsers.add_parser('show', help="Режим вывода в консоль")


def create_save_subparser(subparsers):
    save_parser = subparsers.add_parser('save', help="Режим добавления в файл")


def create_delete_subparser(subparsers):
    delete_parser = subparsers.add_parser('delete', help="Режим удаления книги из библиотеки")

if __name__ == '__main__':
    search_in_library(json_file, list_book)


