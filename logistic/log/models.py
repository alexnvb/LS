from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Type(models.Model):

    TYPE_CHOICES = (
        ('Export', 'export'),
        ('Import', 'import')
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
    tel = models.CharField(max_length=150, verbose_name='Телефон')

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

class Employer(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    post = models.CharField(max_length=150, verbose_name='Должность')
    tel = models.CharField(max_length=150, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Record(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, verbose_name='Тип')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    date_appointed = models.DateTimeField(verbose_name='Назначеная дата')
    responsible = models.ManyToManyField(Employer, symmetrical=False, related_name="responsible", verbose_name='Ответственный')
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, null=True, verbose_name='Контрагент')
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, verbose_name='Город')
    forwarder = models.ManyToManyField(Employer, symmetrical=False, related_name="forwarder", verbose_name='Экспедитор')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, null=True, verbose_name='Автомобиль')
    comment = models.CharField(max_length=150, verbose_name='Коментарий')
    done = models.BooleanField(default=True, verbose_name='Видимость')

    def get_absolute_url(self):
        return reverse_lazy('record_view', kwargs={"record_id": self.pk})

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'