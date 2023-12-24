from django.db import models

# Create your models here.

class UploadMagazine(models.Model):
    title_name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='magazine_pdf')
    

    def __str__(self):
        return self.title_name
    
class UploadComic(models.Model):
    title_name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='comic_pdf')

    def __str__(self):
        return self.title_name

class Newspaper(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, 
                              default='xyz'
                              )
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(
                                    max_length=500,
                                    default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Placeholder_book.svg/1200px-Placeholder_book.svg.png"
                                    )

    def __str__(self):
        return self.item_name

class Comic(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, 
                              default='xyz'
                              )
    model_name = models.CharField(default='comic', max_length=100)
    comic_name = models.CharField(max_length=50)
    comic_desc = models.CharField(max_length=500)
    comic_price = models.IntegerField()
    comic_image = models.CharField(
                                    max_length=500,
                                    default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Placeholder_book.svg/1200px-Placeholder_book.svg.png"
                                    )
    
    pdf_file = models.ForeignKey(UploadComic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.comic_name)

class Magazine(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, 
                              default='xyz'
                              )
    model_name = models.CharField(max_length=100, default='magazine')
    magazine_name = models.CharField(max_length=50)
    magazine_desc = models.CharField(max_length=500)
    magazine_price = models.IntegerField()
    magazine_image = models.CharField(
                                    max_length=500,
                                    default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Placeholder_book.svg/1200px-Placeholder_book.svg.png"
                                    )
    
    pdf_file = models.ForeignKey(UploadMagazine, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.magazine_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.email

        
class TimesofIndia(models.Model):
    TIMES_OF_INDIA = 'Times of India'
    HINDUSTAN_TIMES = 'Hindustan Times'
    THE_INDIAN_EXPRESS = 'The Indian Express'
    INDIA_TODAYS = 'India Todays'

    NEWSPAPER_CHOICE = [
        ('Times of India', 'Times of India'),
        ('Hindustan Times', 'Hindustan Times'),
        ('The Indian Express', 'The Indian Express'),
        ('India Todays', 'India Todays')
    ] 

    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER ='October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTH = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    ]
    title = models.CharField(max_length=100, choices=NEWSPAPER_CHOICE, verbose_name='Newspaper')
    day = models.CharField(max_length=100, default='01-01-2023')
    month = models.CharField(max_length=100, choices=MONTH, verbose_name='Month')
    pdf = models.FileField(upload_to='toi_pdf', default='test.pdf')
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


    
class HindustanTime(models.Model):
    TIMES_OF_INDIA = 'Times of India'
    HINDUSTAN_TIMES = 'Hindustan Times'
    THE_INDIAN_EXPRESS = 'The Indian Express'
    INDIA_TODAYS = 'India Todays'

    NEWSPAPER_CHOICE = [
        ('Times of India', 'Times of India'),
        ('Hindustan Times', 'Hindustan Times'),
        ('The Indian Express', 'The Indian Express'),
        ('India Todays', 'India Todays')
    ] 

    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER ='October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTH = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    ]
    title = models.CharField(max_length=100, choices=NEWSPAPER_CHOICE, verbose_name='Newspaper')
    day = models.CharField(max_length=100, default='01-01-2023')
    month = models.CharField(max_length=100, choices=MONTH, verbose_name='Month')
    pdf = models.FileField(upload_to='hinduatan_pdf', default='test.pdf')
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
class IndianExpress(models.Model):
    TIMES_OF_INDIA = 'Times of India'
    HINDUSTAN_TIMES = 'Hindustan Times'
    THE_INDIAN_EXPRESS = 'The Indian Express'
    INDIA_TODAYS = 'India Todays'

    NEWSPAPER_CHOICE = [
        ('Times of India', 'Times of India'),
        ('Hindustan Times', 'Hindustan Times'),
        ('The Indian Express', 'The Indian Express'),
        ('India Todays', 'India Todays')
    ] 

    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER ='October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTH = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    ]
    title = models.CharField(max_length=100, choices=NEWSPAPER_CHOICE, verbose_name='Newspaper')
    day = models.CharField(max_length=100, default='01-01-2023')
    month = models.CharField(max_length=100, choices=MONTH, verbose_name='Month')
    pdf = models.FileField(upload_to='indianexpress_pdf', default='test.pdf')
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
class IndiaToday(models.Model):
    TIMES_OF_INDIA = 'Times of India'
    HINDUSTAN_TIMES = 'Hindustan Times'
    THE_INDIAN_EXPRESS = 'The Indian Express'
    INDIA_TODAYS = 'India Todays'

    NEWSPAPER_CHOICE = [
        ('Times of India', 'Times of India'),
        ('Hindustan Times', 'Hindustan Times'),
        ('The Indian Express', 'The Indian Express'),
        ('India Todays', 'India Todays')
    ] 

    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER ='October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTH = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    ]
    title = models.CharField(max_length=100, choices=NEWSPAPER_CHOICE, verbose_name='Newspaper')
    day = models.CharField(max_length=100, default='01-01-2023')
    month = models.CharField(max_length=100, choices=MONTH, verbose_name='Month')
    pdf = models.FileField(upload_to='indiatoday_pdf', default='test.pdf')
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
        



