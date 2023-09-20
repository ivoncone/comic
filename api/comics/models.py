from django.db import models
from users.models import User

class Character(models.Model):
	name = models.CharField(max_length=250)
	image = models.URLField(max_length=250, null=True, blank=True)
	appearances = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'characters'

class Comic(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comic_id = models.IntegerField(null=True, blank=True)
	title = models.CharField(max_length=250)
	personaje = models.ForeignKey(Character, on_delete=models.CASCADE)
	image = models.URLField(max_length=250, null=True, blank=True)
	onSaleDate = models.DateField()

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'comics'


