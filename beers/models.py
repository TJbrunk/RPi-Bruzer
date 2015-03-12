from django.db import models
from django import views
#from TempProfile.models import TempProfile
#from TempControl.models import TempSensor

class Beer(models.Model):
    Name = models.CharField(max_length = 50)
    BrewDate = models.DateField(unique=True)
    OG = models.DecimalField(max_digits=4, decimal_places=3)
    Notes = models.TextField(blank=True)
    RackDate = models.DateField(null=True, blank=True)
    FinishDate = models.DateField(null=True, blank=True)
    FG = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    ABV = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    OnTap = models.BooleanField(default = False)
    FermentationTemp = models.PositiveSmallIntegerField(default = 18)
#    TempProfile = models.ForeignKey(TempProfile,)
    
    def __unicode__(self, ):
        return self.Name
    

class BeerTempData(models.Model):
    Brew = models.ForeignKey(Beer)
    Updated = models.DateTimeField(auto_now=True)
    Temperature = models.DecimalField(max_digits=5, decimal_places=2)
    
    def GetTemps(self,):
        #temps = self.objects.filter(Brew_id = 1)
        return "Please work"#temps.Temperature
    
    def __unicode__(self, ):
        return self.Brew