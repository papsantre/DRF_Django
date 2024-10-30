from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import NULLABLE, Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.PositiveIntegerField(verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)
    last_login = models.DateTimeField(default=datetime.now, verbose_name="Время последнего посещения", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Кто произвел оплату")
    payment_date = models.DateField(verbose_name='Дата платежа', **NULLABLE)
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE)
    cost = models.PositiveIntegerField(default=0, verbose_name="Стоимость покупки")
    CASH = "cash"
    NON_CASH = "non_cash"
    PAYMENT_METHOD = [(CASH, "cash"), (NON_CASH, "non_cash")]
    payment_method = models.CharField(choices=PAYMENT_METHOD, default=CASH, verbose_name='Способ оплаты')
    session_id = models.CharField(max_length=255, verbose_name='Id сессии', help_text='Укажите id сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', help_text='Укажите ссылку на оплату', **NULLABLE)

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return self.payment_method
