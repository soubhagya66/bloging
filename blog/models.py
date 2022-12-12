from pickle import TRUE
from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
   first_name=models.CharField(max_length=50)
   last_name=models.CharField(max_length=50)
   email_adress=models.EmailField(max_length=50)

   def full_name(self):
       return f"{self.first_name} {self.last_name}"

   def __str__(self) :
       return self.full_name()



class Tag(models.Model):   
    caption=models.CharField(max_length=20)    
    def __str__(self) :
        return f"{self.caption}"



class Post(models.Model):   
    title=models.CharField(max_length=50)
    excerpt=models.CharField(max_length=150)
    image=models.ImageField(upload_to="posts",null=True)
    date=models.DateField( auto_now=True)
    slug=models.SlugField(unique=True,db_index=True,null=True)
    content=models.TextField(MinLengthValidator(20))
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="posts")
    tags=models.ManyToManyField(Tag,blank=True)
    
    def __str__(self) :
        return f"{self.title}"



class Comment(models.Model):
    user_name=models.CharField(max_length=25)
    user_email=models.EmailField(null=True)
    text=models.TextField()
    post=models.ForeignKey(
        Post,on_delete=models.CASCADE,related_name="comments")




