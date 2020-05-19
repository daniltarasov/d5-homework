from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        # return "{}, {}".format(self.full_name, self.birth_year)
        return self.full_name

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

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.TextField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.name
