from django.db import models
from django.core import validators


class Genre(models.Model):
    name = models.TextField(verbose_name='Название жанра')


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название книги')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    publishing_house = models.CharField(max_length=100, verbose_name="Издательство")
    year = models.DateField(verbose_name='Год выпуска')
    cover = models.ImageField(verbose_name='Обложка', null=True)
    description = models.TextField(verbose_name='Описание')
    book = models.FileField(verbose_name='Книга', null=True)
    uploaded_user = models.ForeignKey('User', on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    nickname = models.CharField(max_length=50, verbose_name='Никнейм')
    birthday = models.DateField()
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(max_length=11, verbose_name='Номер телефона',
                             null=True, blank=True,
                             validators=[validators.RegexValidator(
                                 regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                                 message='Неправильно введен номер телефона')])


class UsersCart(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя автора")
    surname = models.CharField(max_length=50, verbose_name="Фамилия автора")
    birthday = models.DateField()
    description = models.TextField(verbose_name="Биография")
