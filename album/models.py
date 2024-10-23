from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Team(models.Model):
    """ equipo  """
    name = models.CharField(max_length=50)
    shield = models.ImageField(upload_to='shields/')
    team = models.ImageField(upload_to='teams/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("team-list")

class Player(models.Model):
    """ futbolista """
    team = models.ForeignKey('team', on_delete=models.PROTECT,related_name='get_players' )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='players/')
    pub_date = models.DateField(auto_now_add=True)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_absolute_url(self):
        return reverse("player-list")
    
@receiver(post_delete, sender=Team)
def team_delete(sender, instance, **kwargs):
     """ Borra los ficheros de las fotos que se eliminan. """
     instance.shield.delete(False)
     instance.team.delete(False)
     
@receiver(post_delete, sender=Player)
def player_delete(sender, instance, **kwargs):
     """ Borra los ficheros de las fotos que se eliminan. """
     instance.photo.delete(False)