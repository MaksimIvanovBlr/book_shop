from django.db import models
from django.urls import reverse_lazy


class Book(models.Model):
    """модель книги"""
    ZERO = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'

    CHOISE_GROUP = {
        (ZERO, '0'),
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
        (SIX, '6'),
        (SEVEN, '7'),
        (EIGHT, '8'),
        (NINE, '9'),
        (TEN, '10')
    }

    cover = models.ImageField(
        verbose_name='Обложка книги',
        upload_to='uploads/%Y/%m/%d'
        
    )


    name = models.CharField(
        verbose_name='Название',
        max_length=40
    )

    author_book = models.ManyToManyField(
        'guide.Author',
        verbose_name='Автор',
        related_name= 'authorbook', 
    )
    
    series_book = models.ForeignKey(
        'guide.Series',
        verbose_name='Серия',
        on_delete=models.PROTECT,
        related_name= 'seriesbook' 
    )

    genre_book = models.ForeignKey(
        'guide.Genre',
        verbose_name='Жанр',
        on_delete=models.PROTECT,
        related_name= 'genrebook' 
    )
    publishing_book = models.ForeignKey(
        'guide.Publishing',
        verbose_name='Издательство',
        on_delete=models.PROTECT,
        related_name= 'publishingbook' 
    )

    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=5, 
        decimal_places=2
    )
    last_change = models.DateField(
        verbose_name='Дата последнего изменение карточки',
        auto_now=True
    )
    add_to_catalog = models.DateField(
        verbose_name='Дата добавления в каталог',
        auto_now_add=True
    )

    quantity_available = models.PositiveSmallIntegerField(
        verbose_name='Количество в наличии'
    )

    weight = models.PositiveSmallIntegerField(
        verbose_name='Вес(гр.)',
        blank=True,
        null=True
    )
    quantity_of_pages = models.PositiveSmallIntegerField(
        verbose_name='Количество страниц',
        blank=True,
        null=True
    )

    binding = models.TextField(
        verbose_name = 'Переплет',
        max_length=100,
        blank=True,
        null=True
    )

    book_format = models.TextField(
        verbose_name = 'Формат',
        max_length=100,
        blank=True,
        null=True
    )

    year_of_publication = models.DecimalField(
        verbose_name='Год издания',
        max_digits=4, 
        decimal_places=0,
        blank=True,
        null=True
    )

    isbn =  models.TextField(
        verbose_name = 'ISBN',
        max_length=100,
        blank=True,
        null=True
        )

    age_restrictions =  models.TextField(
        verbose_name = 'Возрастные ограничения',
        max_length=10,
        blank=True,
        null=True
        )

    rating = models.CharField(
        verbose_name='Рейтинг',
        max_length=50,
        choices = CHOISE_GROUP,
        default = ZERO

        )
    
    availability = models.BooleanField(
        verbose_name = 'Доступен для заказа'
    )


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse_lazy('book:detail-book', kwargs ={'pk':self.pk}) 
# Create your models here.
