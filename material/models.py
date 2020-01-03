from django.db import models

class FirstSatage(models.Model):
    subject_name = models.CharField(max_length=100)
    down_link = models.CharField(max_length=300)
    attempt = models.IntegerField(default=1)
    course_name = models.CharField(max_length=100)
    course_author = models.CharField(max_length=100)
    course_link = models.CharField(max_length=300)
    img_course = models.ImageField(upload_to='',default='None',null=True,blank=True)
    book_name = models.CharField(max_length=100)
    book_isbn = models.IntegerField()
    book_link = models.CharField(max_length=300)


    def __str__(self):
        return self.subject_name

class SecondStage(models.Model):
    subject_name = models.CharField(max_length=100)
    down_link = models.CharField(max_length=300)
    attempt = models.IntegerField(default=1)
    course_name = models.CharField(max_length=100)
    course_author = models.CharField(max_length=100)
    course_link = models.CharField(max_length=300)
    img_course = models.ImageField(upload_to='',default='None',null=True,blank=True)
    book_name = models.CharField(max_length=100)
    book_isbn = models.IntegerField()
    book_link = models.CharField(max_length=300)

    def __str__(self):
        return self.subject_name

class ThirdStage(models.Model):
    subject_name = models.CharField(max_length=100)
    down_link = models.CharField(max_length=300)
    attempt = models.IntegerField(default=1)
    course_name = models.CharField(max_length=100)
    course_author = models.CharField(max_length=100)
    course_link = models.CharField(max_length=300)
    img_course = models.ImageField(upload_to='',default='None',null=True,blank=True)
    book_name = models.CharField(max_length=100)
    book_isbn = models.IntegerField()
    book_link = models.CharField(max_length=300)

    def __str__(self):
        return self.subject_name

class ForthStage(models.Model):
    subject_name = models.CharField(max_length=100)
    down_link = models.CharField(max_length=300)
    attempt = models.IntegerField(default=1)
    course_name = models.CharField(max_length=100)
    course_author = models.CharField(max_length=100)
    course_link = models.CharField(max_length=300)
    img_course = models.ImageField(upload_to='',default='None',null=True,blank=True)
    book_name = models.CharField(max_length=100)
    book_isbn = models.IntegerField()
    book_link = models.CharField(max_length=300)

    def __str__(self):
        return self.subject_name
    
