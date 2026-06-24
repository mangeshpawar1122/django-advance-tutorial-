from django.db.models.signals import pre_save,post_save
from . models import Blog
from django.dispatch import receiver

# Triggred befor saving a blog
@receiver(pre_save, sender=Blog)
def before_blog_save(sender,instance,**kwargs):
  print(f"About to save Blog[pre-save]:{instance.title}")



# Triggred after saving a blog
@receiver(post_save,sender=Blog)
def after_blog_save(sender,instance,created, **kwargs):
  if created:
    print(f"New blog created [post-save]:{instance.title}")
  else:
    print(f"Updated blog[post-save]:{instance.title}")  
