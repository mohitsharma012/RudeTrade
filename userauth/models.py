from django.db import models

          
class rudeusers(models.Model):
    id = models.AutoField(primary_key=True)
    user_pass =  models.CharField(max_length=50)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    user_email = models.CharField(max_length=50)
    currency = models.CharField(max_length=25)
    country = models.CharField(max_length=25, default="USD")

    def __str__(self):
        return self.user_email

