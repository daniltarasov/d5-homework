from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from p_library.models import Book, Author, Publisher
from p_library.models import Book, Author, Publisher, Friend

# Для создания админа выполнить команду python manage.py createsuperuser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    @staticmethod
    def borrowed(obj):
        friends = obj.friend_set.all()
        lst=[]
        for friend in friends:
            lst.append(friend.name)
            
        return lst

    list_display = ('title', 'author_full_name', 'borrowed')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publisher', 'price', 'copy_count')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    
    @staticmethod
    def list_book(obj):
        books=obj.book_set.all()
        lst=[]
        for book in books:
            lst.append(book.title)
            
        return lst
    
    list_display = ('full_name', 'list_book')
    fields = ('full_name', 'birth_year', 'country')

    # pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
        
    @staticmethod
    def list_book(obj):
        books=obj.book_set.all()
        lst=[]
        for book in books:
            lst.append(book.title)
            
        return lst
    
    list_display = ('name', 'list_book')
    fields = ('name', 'country')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):

    @staticmethod
    def book_list(obj):
        books = obj.books.all()
        lst=[]
        for book in books:
            lst.append(book.title)
            
        return lst
    
    @staticmethod
    def friend_name(obj):
        return obj.name

    list_display = ('friend_name', 'book_list')



