import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()
from library.models import Author, Book, category
from library.models.users import User

## Задача 1: Создание нового члена библиотеки

# new_user = User.objects.create_user(username='Serg', email='serg@gmail.com', password='qwertyuiop',
#                                     role='lib_member',
#                                     first_name='John',
#                                     last_name='Doe',
#                                     gender='male',
#                                     age=25,
#                                     birth_date='2000-01-22')
#

# Задача 2: Получение конкретного автора и обновление рейтинга


# author = Author.objects.filter(id=1).update(rating=9.5)

# author = Author.objects.filter(id=1).first()
# author.rating = 8.5
# author.save()

# author = Author.objects.get(id=1)
# author.rating = 7.5
# author.save()

# Задача 3: Фильтрация книг по категории и количеству страниц с подсчетом

# books = Book.objects.filter(
#     category__name__contains='Fiction',
#     pages__gt=200
# )
# print(books)
# print(books.query)
# print(books.count())
#


# Задача 4: Поиск членов

# from django.db.models import Q
#
# users_staff_members = User.objects.filter(
#     Q(role='admin') | Q(role='moderator')
# ).exclude(is_active=False).order_by('last_name', 'first_name')
#
# for staff_members in users_staff_members:
#     print(staff_members)


# Задача 5: Поиск авторов с использованием field lookups

# author = Author.objects.filter(name__startswith='A')
#
# author_rating = Author.objects.filter(rating__gt=8.5)
#
# author_year = Author.objects.filter(date_for_birth__year__gt=1950)
#
# first_author = author.first()
#
# print(author)
# print(author_rating)
# print(author_year)
# print(first_author.name)

## Задача 10: Сложные фильтры с Q-объектами


# from django.db.models import Q
#
# autors = Author.objects.filter(
#     Q(rating__gt=9.0)|Q(date_for_birth__year__lt=1980),
#     deleted=False
# ).exclude(date_for_birth__isnull=True)
#
# print(autors)
# print(autors.query)
# print(autors.count())
# print(autors.exists())
#
# if autors:
#     print(autors)



# Задача 11: Создание связи члена библиотеки с библиотекой через M2M
# member= User.objects.get(id=15)
# lib= Library.objects.get(id=2)
# membership= Membership.objects.create(member=member,library=lib)
# print(member, membership.library)

# Задача 12: Поиск просроченных займов с использованием Q объектов

# from django.utils import timezone
#
# date = str(timezone.now().date())
# # print(date)
# # print(type(date))
# borrows = Borrow.objects.filter(
#     Q(is_returned=False) & Q(return_plane_date__lt=date)
# ).exclude(return_actual_date__isnull=True).order_by("issue_date")
#
# print(borrows)
#
# for borrow in borrows:
#     print(borrow)