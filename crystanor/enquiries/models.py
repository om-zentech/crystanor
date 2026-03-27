from django.db import models

class Enquiry(models.Model):
    full_name = models.TextField()
    company_name = models.TextField()
    country = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    industry = models.TextField()
    application = models.TextField()
    purity = models.TextField()
    volume = models.TextField()
    packaging = models.TextField()
    delivery_terms = models.TextField()
    destination_port = models.TextField()
    additional_specs = models.TextField()
    
    def __str__(self):
        return self.full_name