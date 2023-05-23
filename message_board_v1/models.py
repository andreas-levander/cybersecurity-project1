from django.db import models

class SelfUser(models.Model):
	username = models.TextField()
	password = models.BinaryField()
	
class Message_v1(models.Model):
	user = models.ForeignKey(SelfUser, on_delete=models.CASCADE)
	content = models.TextField()