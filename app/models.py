from django.db import models

class Clube(models.Model):
    nome = models.CharField(
        max_length=100,
        )
    vitorias = models.IntegerField(default=0, editable=False)

    pontos = models.IntegerField(default=0, editable=False)

    saldo_gols = models.IntegerField(default=0, editable=False)

    gols_pro = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    time1= models.ForeignKey(Clube, on_delete=models.CASCADE, related_name='time2',blank=True,null=True)
    time2= models.ForeignKey(Clube, on_delete=models.CASCADE, related_name='time1',blank=True,null=True)
    placar_1 = models.IntegerField(default=0)
    placar_2 = models.IntegerField(default=0)
    processed = models.BooleanField(default=False) 
    



# Create your models here.
