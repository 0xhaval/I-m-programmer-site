from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
'''
The get_queryset() method of a manager returns the QuerySet that will
be executed. We override this method to include our custom filter in
the final QuerySet. We have defined our custom manager and
added it to the Post model;
'''
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                            .filter(status='published')
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts')
    body = models.TextField()
    img = models.ImageField(upload_to='',default='None',null=True,blank=True)
    #(_(""), auto_now=False, auto_now_add=False) it's for publish var
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    objects = models.Manager() #the default manager
    published = PublishedManager() #Our custom manager 

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                                self.publish.month,
                                self.publish.day,
                                self.slug])
                    

""" 
title: This is the field for the post title. This field is CharField,
which translates into a VARCHAR column in the SQL database.

slug: This is a field intended to be used in URLs. A slug is a
short label that contains only letters, numbers, underscores,
or hyphens. We will use the slug field to build beautiful, SEOfriendly
URLs for our blog posts. We have added the
unique_for_date parameter to this field so that we can build
URLs for posts using their publish date and slug. Django will
prevent multiple posts from having the same slug for a
given date.

author: This field is a foreign key. It defines a many-to-one
relationship. We are telling Django that each post is written
by a user, and a user can write any number of posts. For this
field, Django will create a foreign key in the database using
the primary key of the related model. In this case, we are
relying on the User model of the Django authentication
system. The on_delete parameter specifies the behavior to
adopt when the referenced object is deleted. This is not
specific to Django; it is an SQL standard. Using CASCADE, we
specify that when the referenced user is deleted, the
database will also delete its related blog posts. You can take
a look at all possible options at https://docs.djangoproject.com/en/2.
0/ref/models/fields/#django.db.models.ForeignKey.on_delete. We specify
the name of the reverse relationship, from User to Post, with
the related_name attribute. This will allow us to access related
objects easily. We will learn more about this later.
body: This is the body of the post. This field is a text field,
which translates into a TEXT column in the SQL database.
publish: This datetime indicates when the post was published.
We use Django's timezone now method as the default value.
This returns the current datetime in a timezone-aware
format. You can think of it as a timezone-aware version of
the standard Python datetime.now method.

created: This datetime indicates when the post was created.
Since we are using auto_now_add here, the date will be saved
automatically when creating an object.

updated: This datetime indicates the last time the post was
updated. Since we are using auto_now here, the date will be
updated automatically when saving an object.

status: This field shows the status of a post. We use a choices
parameter, so the value of this field can only be set to one of
the given choices.
Django comes with different types of fields that you can use to
define your models. You can find all field types
at https://docs.djangoproject.com/en/2.0/ref/models/fields/.

The Meta class inside the model contains metadata. We tell Django to
sort results in the publish field in descending order by default when
we query the database. We specify descending order using the
negative prefix. By doing so, posts published recently will appear
first.
The __str__() method is the default human-readable representation
of the object. Django will use it in many places, such as the
administration site.
"""