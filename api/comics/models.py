from django.db import models
from users.models import User

class Personaje(models.Model):
	name = models.CharField(max_length=250)
	image = models.URLField(max_length=250, null=True, blank=True)
	appearances = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'personajes'

class Comic(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
	image = models.URLField(max_length=250)
	onSaleDate = models.DateField()

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'comics'

class Busqueda(models.Model):
	criterios = models.CharField(max_length=200)

	class Meta:
		db_table = 'busqueda'
