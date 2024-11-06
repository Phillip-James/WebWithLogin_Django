import datetime
from datetime import timezone


from django.db import models

# Create your models here.

class Item(models.Model):
    name_text = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    num_of_users = models.IntegerField(default=1)
    last_time = models.IntegerField(default = 30)
    pub_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name_text

    # 30天内是否更新过信息
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=30)