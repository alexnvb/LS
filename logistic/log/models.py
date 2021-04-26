from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Type(models.Model):

    TYPE_CHOICES = (
        ('Export', 'export'),
        ('Import', 'import'),
        ('Touch', 'touch'),
    )

    name = models.CharField(max_length=150, choices=TYPE_CHOICES, verbose_name='Тип записи')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Contractor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Электронная почта')
    tel = models.CharField(max_length=150, verbose_name='Телефон')
    comment = models.CharField(max_length=150, verbose_name='Комментарий')

    def get_absolute_url(self):
        return reverse_lazy('contractor_view', kwargs={"contractor_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

class Vehicle(models.Model):
    name = models.CharField(max_length=150, verbose_name='Марка/Модель')
    plate_number = models.CharField(max_length=150, verbose_name='Госномер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Manager(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    tel = models.CharField(max_length=150, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

class Forwarder(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    tel = models.CharField(max_length=150, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экспедитор'
        verbose_name_plural = 'Экспедиторы'

class Record(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, verbose_name='Тип')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='Дата обновления')
    date_appointed = models.DateField(verbose_name='Назначеная дата')
    responsible = models.ForeignKey(Manager, on_delete=models.PROTECT, null=True, verbose_name='Ответственный')
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, null=True, verbose_name='Контрагент')
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, verbose_name='Город')
    forwarder = models.ForeignKey(Forwarder, on_delete=models.PROTECT, null=True, verbose_name='Экспедитор')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, null=True, verbose_name='Автомобиль')
    comment = models.CharField(max_length=150, verbose_name='Коментарий', blank=True)
    done = models.BooleanField(default=False, verbose_name='Статус')

    def get_absolute_url(self):
        return reverse_lazy('record_view', kwargs={"record_id": self.pk})

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'