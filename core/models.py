# core/models.py
from django.db import models

class Major(models.Model):
    name = models.CharField("Направление", max_length=255)
    code = models.CharField("Код (шифр)", max_length=10)
    level = models.CharField("Уровень образования", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.code})"


class Profile(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="profiles", verbose_name="Направление")
    name = models.CharField("Наименование профиля", max_length=255)
    full_time = models.BooleanField("Очная форма обучения", default=True)
    part_time = models.BooleanField("Заочная форма обучения", default=False)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["major", "name"]

    def __str__(self):
        return f"{self.name} — {self.major.name}"


class ProfileDocument(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="documents", verbose_name="Профиль")
    title = models.CharField("Наименование документа", max_length=255)
    file = models.FileField("Документ (файл)", upload_to="profile_docs/")

    class Meta:
        verbose_name = "Документ профиля"
        verbose_name_plural = "Документы профиля"

    def __str__(self):
        return f"{self.title} — {self.profile.name}"


class CompetencePassport(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="passports", verbose_name="Профиль")
    title = models.CharField("Наименование документа", max_length=255)
    file = models.FileField("Файл паспорта/программы", upload_to="passports/", blank=True, null=True)

    class Meta:
        verbose_name = "Паспорт / Программа компетенций"
        verbose_name_plural = "Паспорта / Программы компетенций"

    def __str__(self):
        return f"{self.title} — {self.profile.name}"


class Module(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="modules", verbose_name="Профиль")
    name = models.CharField("Наименование дисциплины")
    annotation = models.FileField("Аннотация", upload_to="modules/annotation/")
    syllabus = models.FileField("Программа дисциплины (syllabus)", upload_to="modules/syllabus/")
    assessment_fund = models.FileField("Фонд оценочных средств", upload_to="modules/assessments/")

    class Meta:
        verbose_name = "Дисциплина / Модуль / Практика"
        verbose_name_plural = "Дисциплины / Модули / Практики"

    def __str__(self):
        return f"{self.name} — {self.profile.name}"
