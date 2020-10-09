def create_dict(name_tuple, read_books_tuple):
    name_and_read_books = dict(zip(name_tuple, read_books_tuple))
    return name_and_read_books


"""
Словарь создал с той целью, чтобы мои ссылки на имена были на голословны.
То есть чтобы к каждому имени присвоилось книга.
"""


def search_name(name_and_read_books, read_books, must_read_book):
    difference_of_books = read_books-must_read_book
    name_who_unread = []
    for (n, b) in name_and_read_books.items():
        if b in difference_of_books:
            name_who_unread.append(n)
    return name_who_unread


name = {'Vasya', 'Vanya', 'Kesha', 'Gosha', 'Klava'}
read_books = {'book1', 'book2', 'book3', 'book4', 'book5'}
must_read_book = {'book1', 'book2', 'book6', 'book7', 'book8'}
all_books = read_books | must_read_book
# преобразовал в кортеж для ключей в словарь
name_tuple = tuple(sorted(name))
# преобразовал в кортеж для выведения значений в словарь
read_books_tuple = tuple(sorted(read_books))

result = create_dict(name_tuple, read_books_tuple)
result1 = search_name(result, read_books, must_read_book)
print(f'{result1} have not read the required literature.')
