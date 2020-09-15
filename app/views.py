from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from . import models
from django.http import JsonResponse

class ClubesView(APIView):
    def get(self,request):
        clubes = models.Clube.objects.order_by('-pontos', '-vitorias', '-saldo_gols', '-gols_pro')
        clubes_ret = serializers.ClubeSerializer(clubes, many = True).data
        
        return  JsonResponse(clubes_ret, safe=False )

class JogoView(APIView):
    def get(self,request):
        jogos = models.Jogo.objects.filter(processed=False).all()
        for jogo in jogos:
            if jogo.placar_1 > jogo.placar_2:
                jogo.time1.vitorias += 1
                jogo.time1.pontos += 3
                jogo.time1.saldo_gols += jogo.placar_1 - jogo.placar_2
                jogo.time1.gols_pro += jogo.placar_1
                jogo.time2.gols_pro += jogo.placar_2
            if jogo.placar_1 == jogo.placar_2:
                jogo.time1.pontos += 1,
                jogo.time2.pontos += 1,
                jogo.time1.gols_pro += jogo.placar_1
                jogo.time2.gols_pro += jogo.placar_2
            if jogo.placar_2 > jogo.placar_1:
                jogo.time2.vitorias += 1
                jogo.time2.pontos += 3
                jogo.time2.saldo_gols += jogo.placar_2 - jogo.placar_1
                jogo.time1.gols_pro += jogo.placar_1
                jogo.time2.gols_pro += jogo.placar_2


            jogo.processed = True
            jogo.save()
            jogo.time1.save()
            jogo.time2.save()

                
            

       


        return JsonResponse({'ok':True})


# Create your views here.
