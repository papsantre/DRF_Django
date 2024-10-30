from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=50, help_text='Назавание курса')
    course_preview = models.ImageField(upload_to='materials/course_previews', verbose_name='Превью курса',  **NULLABLE)
    description = models.TextField(verbose_name='Содержание курса')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса", **NULLABLE)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=50, help_text='Назавание урока')
    description = models.TextField(verbose_name='Содержание урока')
    lesson_preview = models.ImageField(upload_to='materials/lesson_previews', verbose_name='Превью урока', **NULLABLE)
    url_video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец урока", **NULLABLE)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    sign_of_subscription = models.BooleanField(default=False, verbose_name='Признак подписки')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'{self.user}: {self.course}'
