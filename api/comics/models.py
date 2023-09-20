from django.db import models


class Filtro(models.Model):
	personaje = models.CharField(max_length=200)
	comic = models.CharField(max_length=200)

	class Meta:
		db_table = 'filtross'

class Personaje(models.Model):
	name = models.CharField(max_length=250)
	image = models.URLField(max_length=250)
	appearances = models.CharField(max_length=250)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'personajes'

class Comic(models.Model):
	title = models.CharField(max_length=250)
	image = models.URLField(max_length=250)
	onSaleDate = models.DateField()

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'comics'

class Busqueda(models.Model):
	personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
	comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

	class Meta:
		db_table = 'busqueda'