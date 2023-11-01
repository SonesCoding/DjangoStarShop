from django.db import models

from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.')
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Quote(models.Model):
    name = models.CharField(max_length=50)
    Qtext = models.TextField()
    Author = models.ManyToManyField(Author)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.')
    
    def __str__(self):
        return self.name + ", " + str(list(self.Author.all())[0]) #since the relationship is many to many i access manager and make it a list then just grab the first element. 
    #----thank you - eve----


        
class Star(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.TextField(max_length=100)
    Quote = models.ManyToManyField(Quote)
    createdBy= models.TextField(max_length=50)
       
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('star_detail',
                       kwargs={'name': self.name,
                               'createdBy': self.createdBy})

    
class cartDetails(models.Model):
    shippingName = models.CharField(max_length= 50)
    shippingAddress = models.CharField(max_length=500)
    debitcardNumber = models.CharField(max_length=16)
    debitcardCVC = models.CharField(max_length=3)
    debitcardExp = models.CharField(max_length=4)
    
    
    
#class Tag(models.Model):
    #name = 
    
    
# Will display stars, pick 1 star and hit a done button. use star data to fill in a statement and assign a random
#quote that will come with your star

#timestamp model for the checkout star + quote page.

"""
        Sirius, 50.00, Blue
        Regulus, 50.00, Orange
        Aldebaram, 65.00, Gold
        Maia, 100.00, Purple
        Electra, 150.00, ???
        Alcyone, 100.00, Red
        Celaeno, 75.00, Pink
        
        Beyonce,
        Emma Xu,
        Vincent Van Gogh
        Maya Angelou
        Socrates
        Oscar Wilde
        
        A, "Shine Bright Like a diamond.", Beyonce
        B, "You can be the brightest star in someones darkest nights.", Emma Xu
        C, "For my part I know nothing with any certainty, but the sight of the stars makes me dream." , Vincent Van Gogh
        D, "Nohting can dim the light which shines from within.", Maya Angelou
        E, "Be as you wish to seem.", Socrates
        F, "Wisdom begins in wonder.", Socrates
        G, "You can never be overdressed or overeducated.", Oscar Wilde
        
        """