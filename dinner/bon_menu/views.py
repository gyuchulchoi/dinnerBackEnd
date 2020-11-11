from ..models import BonMenu
from .serializers import BonSerializer
from django.http import JsonResponse, HttpResponse
import urllib.request, json
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
import requests
from bs4 import BeautifulSoup
import re

class BonList(viewsets.ModelViewSet):
    queryset = BonMenu.objects.all()
    serializer_class = BonSerializer
    req = requests.get('https://www.bonif.co.kr/menu/list?brdCd=BF104')
    html = req.content.decode('utf-8').strip()
    soup = BeautifulSoup(html, 'lxml') # pip install lxml
    dataCrwl = soup.find('ul', id = "menuList")
    subject2 = dataCrwl.findAll('li')


    
   # @action(detail=False, methods=['get'])
    #def details(self, request):
    
    menu_price = []
    menu_name = []
    menu_new = []
    menu_best = []
    menu_type = []
    
    for index in range(0, len(subject2)):
        price_data = subject2[index].find('p', attrs={'class': 'price'}).text
        name_data = subject2[index].find('p', attrs={'class': 'nm'}).text

        if subject2[index].find('em', attrs={'class': 'new'}) != None:
            new_data = subject2[index].find('em', attrs={'class': 'new'}).text
        else:
            new_data = "false"

        if subject2[index].find('em', attrs={'class': 'best'}) != None:
            best_data = subject2[index].find('em', attrs={'class': 'best'}).text
        else:
            best_data = "false"

        if name_data.find('짬뽕순두부') > -1:
            menu_type.insert(index, 'winter')
        elif name_data.find('여수꼬막덮밥') > -1:
            menu_type.insert(index, 'winter')
        elif name_data.find('반상') > -1:
            menu_type.insert(index, 'half')
        elif name_data.find('한상') > -1:
            menu_type.insert(index, 'one')
        elif name_data.find('한정식') > -1:
            menu_type.insert(index, 'korean')
        elif name_data.find('(반찬)') > -1:
            menu_type.insert(index, 'banchan')
        elif name_data.find('(국)') > -1:
            menu_type.insert(index, 'banchan')            
        elif name_data.find('핫윙콤보') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('아이스홍시') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('단호박') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('스팸') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('후라이') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('참고소한') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('흑미밥') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('곤드레 나물밥') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('단호박영양밥') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('생일 복') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('정관장') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('콜라') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('사이다') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('미소된장') > -1:
            menu_type.insert(index, 'other')
        elif name_data.find('미역국') > -1:
            menu_type.insert(index, 'other')               
        else:
            menu_type.insert(index, 'small')
        
        print(int(price_data.replace("원","").replace(",", "")), name_data, new_data , best_data, menu_type[index])
        menu_price.insert(index,int(price_data.replace("원","").replace(",", "")))
        menu_name.insert(index,name_data)
        if new_data != 'false' :
            menu_new.insert(index, True)
        else:
            menu_new.insert(index, False)
        if best_data != 'false' :
            menu_best.insert(index, True)
        else:
            menu_best.insert(index, False)
        
        data = [ {'menu_price' : menu_price[index], 'id' : index, 'menu_name' : menu_name[index], 'menu_new' : menu_new[index], 'menu_best' : menu_best[index], 'menu_type' : menu_type[index]}]
        
        serializer = BonSerializer(data=data, many = True)
        serializer.is_valid()
        serializer.save()
class BonData():
    queryset = BonMenu.objects.all()
    serializer_class = BonSerializer
    
    
        #serializer.data['id'] = index
        #serializer.data['menu_price'] = menu_price[index]
        #serializer.data['menu_name'] = menu_name[index]
        #serializer.data['menu_new'] = menu_new[index]
        #serializer.data['menu_best'] = menu_best[index]
        #serializer.data['menu_type'] = menu_type[index]
class BonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BonMenu.objects.all()
    serializer_class = BonSerializer
