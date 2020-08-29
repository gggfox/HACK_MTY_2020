from django.db import models
from django.contrib.auth.models import User


class contract(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	contratista = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contratista')
	contratante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contratante')
	title = models.CharField(max_length=100, default='default title')

	def __str__(self):
		return self.title