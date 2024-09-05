from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Основная страница, на которой будет список всех статей")


def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Cтраница, на которой будут только статьи по темам, на которые подписан пользователь")


def article_id(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("Cтраница, на которой будет отображаться статья по id.")


def article_id_comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("Адрес, который мы будем использовать для написания комментариев к статье.")


def article_id_update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("Страница, которую мы будем использовать для изменения существующей статьи.")


def article_id_delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("Адрес, который мы будем использовать для удаления статьи")


def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, на которой мы будем создавать новые статьи.")


def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, с перечнем всех тем на сайте")


def topics_topic_id(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("Страница, со всеми статьями по определенной теме")


def topics_topic_id_subscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("Адрес для подписки на конкретную тему")


def topics_topic_id_unsubscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("Адрес для отписки от конкретной темы")


def profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, с данными пользователя и перечнем его подписок")


def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, регистрацией нового пользователя")


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, с изменением пароля")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, для входа на сайт")


def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Адрес для выхода с сайта")


def year_month(request: HttpRequest, year: int, month: int) -> HttpResponse:
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    year = int(year)
    month = int(month)

    if month < 1 or month > 12:
        return HttpResponse("Ошибка: нет такого месяца")
    if year > current_year or (year == current_year and month > current_month):
        return HttpResponse("Статей пока нет")

    return HttpResponse("Cтраница, на которой будут статьи созданные в конкретный месяц. В случае запроса не настоящей даты, должна быть ошибка.")
