from django.db import models

# Create your models here.
class Product(models.Model):
	name_card = models.CharField(max_length=250,blank=True,null=True)
	description = models.TextField()
	price = models.CharField(max_length=25)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name_card


class Comment(models.Model):
	userName = models.CharField(max_length=250)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.userName


