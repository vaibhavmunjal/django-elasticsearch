from django.db import models

# Create your models here.


class Search(models.Model):

	name = models.CharField(max_length=100)

	description = models.TextField()

	timstamp = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Search"
		verbose_name_plural = "Searchs"

	def __str__(self):
		return self.name
