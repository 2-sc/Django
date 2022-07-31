# example > urls.py
from django.urls import path, include
from .views import BooksAPIMixins, helloAPI, bookAPI, booksAPI, BookAPI, BooksAPI, BookAPIMixins

urlpatterns = [
    path("hello/", helloAPI),
    path("fbv/books/", booksAPI),          # 함수형 뷰의 booksAPI 연결
    path("fbv/book/<int:bid>/", bookAPI),  # 함수형 뷰의 bookAPI 연결
    path("cbv/book/<int:bid>/", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
]