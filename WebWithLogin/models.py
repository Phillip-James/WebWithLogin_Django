import datetime
from datetime import timezone,timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Item(models.Model):
    name_text = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    num_of_users = models.IntegerField(default=1)
    last_time = models.IntegerField(default = 30)
    pub_date = models.DateField(default=datetime.date.today)
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name_text

    # 30天内是否更新过信息
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=30)

class subscribed_items(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    overtime = models.BooleanField(default=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.item)} - {self.user} - {self.subscribed_at} - {self.overtime}"

    def overtime_judge(self):
        if datetime.date.today() - self.subscribed_at.date() > timedelta(days=self.item.last_time):
            self.overtime = True
        else:
            self.overtime = False
        self.save()
        return self

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    introduction = models.TextField(max_length=500, blank=True)
    last_money = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user}'s profile"



from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()