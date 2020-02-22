from django.db import models

class modeltable(models.Model):
    name=models.CharField(max_length=264,default='pqr')
    ingredients=models.CharField(max_length=264,default='pqr')
    time=models.CharField(max_length=264,default='pqr')
    directions=models.CharField(max_length=264,default='pqr')
    description=models.CharField(max_length=264,default='pqr')
    image=models.FileField(upload_to='fileupload',default='firstpro/static/p_resume.pdf')

class profiletable(models.Model):
    extra=models.CharField(max_length=264,default='mno')
    na=models.CharField(max_length=264,default='pqr')
    ing=models.CharField(max_length=264,default='pqr')
    ti=models.CharField(max_length=264,default='pqr')
    di=models.CharField(max_length=264,default='pqr')
    de=models.CharField(max_length=264,default='pqr')
    im=models.FileField(upload_to='fileupload',default='firstpro/static/p_resume.pdf')
