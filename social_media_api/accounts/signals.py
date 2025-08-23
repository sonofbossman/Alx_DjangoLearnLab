from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# creates a token when a user is first created.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_fullname_auth_token(sender, instance, created, **kwargs):
  if created:
    instance.fullname = f"{instance.first_name} {instance.last_name}".strip()
    instance.save()
    Token.objects.create(user=instance)

# ensures fullname is automatically computed for every user 
# and is updated whenever user instance is updated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_fullname(sender, instance, **kwargs):
  instance.fullname = f"{instance.first_name} {instance.last_name}".strip()
  instance.save()