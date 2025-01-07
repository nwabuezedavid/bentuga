from django.db import models

# Create your models here.
class siteedit(models.Model):
    name = models.CharField( max_length=50 ,blank=True, null=True,)
    email = models.CharField( max_length=50 ,blank=True, null=True,)
    owneremail = models.CharField( max_length=50 ,blank=True, null=True,)
    domain = models.CharField( max_length=50 ,default=name, blank=True, null=True,)
    Address = models.CharField( max_length=50 ,blank=True, null=True,)
    country = models.CharField( max_length=50 ,blank=True, null=True,)
    dis = models.TextField( blank=True, null=True,)
    phone = models.CharField( max_length=50 ,blank=True, null=True,)
    logo = models.ImageField( blank=True, null=True,)
    image1 = models.ImageField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    
    facebooklink = models.CharField( max_length=500 ,blank=True, null=True,)
    twiiterlink = models.CharField( max_length=500 ,blank=True, null=True,)
    instergram = models.CharField( max_length=500 ,blank=True, null=True,)
    youtubelink = models.CharField( max_length=500 ,blank=True, null=True,)
    whatsapplonk = models.CharField( max_length=500 ,blank=True, null=True,)
   
    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=18)
    email = models.EmailField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
  
    subject = models.CharField(max_length=50, choices=[
        ('Support', 'Support'),
        ('Offer', 'Special offer'),
        ('Other', 'Other'),
    ])
    message = models.TextField()
    files = models.FileField(upload_to='contact_files/', blank=True, null=True)
    consent = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"    