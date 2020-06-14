from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return "{}, {}".format(self.full_name, self.birth_year)
        # return self.full_name




class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE, default=None,
                                  blank=True, null=True)
    price = models.DecimalField(default=None, max_digits=10, decimal_places=2)
    copy_count = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title



class Publisher(models.Model):
    name = models.TextField()
    country = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name


class Friend(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField("Book")
    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return self.name

