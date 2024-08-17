from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.00)
    image = models.ImageField(default='default.jpg',upload_to='img')
    phone_number = models.CharField(max_length=11,blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.user.username}'s Balance"
    
@receiver(post_save, sender=User)
def createprofile(sender, instance, created, **kwarys):
    if created:
        user = profile(user=instance)
        user.save()

class Transactions(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciver")
    amount = models.FloatField(blank=True, null=False)
    def __str__(self) -> str:
        return f"Sender {self.sender.username} -- reciver {self.reciver.username} -- amount {self.amount} -- date {self.date}"
    
