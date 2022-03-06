from django.db import models


class Quote(models.Model):
    quote          = models.TextField("Цитата")
    num_letters    = models.IntegerField("Общее количество букв")
    num_vowels     = models.IntegerField("Количество гласных букв")
    num_consonants = models.IntegerField("Количество согласных букв")
    num_repetition = models.TextField("Общее количество повторений каждой буквы")
    average        = models.IntegerField("Средняя длина всех слов в цитате")
    long_word_1    = models.CharField("Длинное слово 1", max_length=255)
    long_word_2    = models.CharField("Длинное слово 2", max_length=255)
    long_word_3    = models.CharField("Длинное слово 3", max_length=255)

    def __str__(self):
        return self.quote
    
    verbose_name = "Цитата знаменитого реппера и предпринимателя Kanye West"
    verbose_name_plural = "Цитаты знаменитого реппера и предпринимателя Kanye West"