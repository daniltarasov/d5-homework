from p_library.models import Book, Author, Publisher
from django.db.models import Min, Sum, Count

# разные методы
pushkin = Author.objects.get(full_name="Пушкин Александр Сергеевич")
pushkin_books = Book.objects.filter(author=pushkin)

for book in pushkin_books:
    print(book.title)

pushkin_books.exists()

pushkin_books.count()

no_horsman_pushkin_books = Book.objects.all() \
    .filter(author=pushkin) \
    .exclude(title__icontains="всадник")

"""
сколько копий самой дешевой книги
"""

collection_books = Book.objects.all()
min_cost = None
id_book = 0
for book in collection_books:
    if min_cost is None:
        min_cost = book.price
    if book.price < min_cost:
        min_cost = book.price
        id_book = book.id

chip_book_count = Book.objects.get(id=id_book).copy_count
print(chip_book_count)

# лучшее решение
chip_book_count = Book.objects.filter(price=Book.objects.aggregate(pr=Min('price'))['pr']) \
    .first().copy_count

"""
Сколько стоят все библиотечные книги авторов, у которых больше одной книги?
"""
dict_auth = {}
collection_books = Book.objects.all()
sum_cost = 0
for book in collection_books:
    print(book.author)
    if dict_auth.get(book.author) is None:
        dict_auth[book.author] = 1
    else:
        dict_auth[book.author] += 1

for book in collection_books:
    if dict_auth[book.author] > 1:
        sum_cost += book.price * book.copy_count

print(sum_cost)

# другое решение
authors = Author.objects.all()
sum_cost = 0
for author in authors:
    if author.book_set.all().count() > 1:
        filt_book = Book.objects.filter(author=author)
        for book in filt_book:
            sum_cost += book.price * book.copy_count
print(sum_cost)


"""
Сколько стоят все библиотечные книги иностранных писателей?
"""
sum_cost = 0
collection_books = Book.objects.all()
foreign = Author.objects.exclude(country="RU")

for book in collection_books:
    if book.author in foreign:
        sum_cost += book.price * book.copy_count

print(sum_cost)

# лучшее решение
sum_cost = 0
collection_books = Book.objects.exclude(author__country="RU")
for book in collection_books:
    sum_cost += book.price * book.copy_count
print(sum_cost)


# лучшее решение
sum_cost = 0
sum_cost = Book.objects.exclude(author__country="RU")
for book in collection_books:
    sum_cost += book.price * book.copy_count
print(sum_cost)


"""
Сколько стоят все экземпляры Пушкина в библиотеке?
"""
sum_cost = 0
collection_books = Book.objects.all()
pushkin = Author.objects \
    .filter(full_name="Пушкин Александр Сергеевич")

for book in collection_books:
    if book.author in pushkin:
        sum_cost += book.price * book.copy_count

print(sum_cost)

# лучшее решение
sum_cost = 0
collection_books = Book.objects.filter(author__full_name="Пушкин Александр Сергеевич")
for book in collection_books:
    sum_cost += book.price * book.copy_count
print(sum_cost)

"""
Сколько стоят все книги, автор которых Douglas Adams? Не учитывайте стоимость копий.
"""
sum_cost = 0
collection_books = Book.objects.all()
adams = Author.objects.filter(full_name="Douglas Adams")

for book in collection_books:
    if book.author in adams:
        sum_cost += book.price

print(sum_cost)

# лучшее решение
sum_cost = 0
collection_books = Book.objects.filter(author__full_name="Douglas Adams")
for book in collection_books:
    sum_cost += book.price
print(sum_cost)

authors = Author.objects.all().annotate(books=book_set.all())
