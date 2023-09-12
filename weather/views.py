from django.shortcuts import render
import json
import urllib.request
from datetime import date
import calendar
from .models import City
# Create your views here.
def index(request):
    citylst = City.objects.all()
    if request.method == 'POST':
        
        city = request.POST['city']
        city=city.capitalize()
        err= city+ " is not available in our database. Please enter another city"
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f06ef8b87c4f16103f965ca9e4b9aea6').read()
        except:
            return render(request, 'index.html', {'city': city, 'error':err})

        json_data = json.loads(res)
        date1=date.today()
        day=calendar.day_name[date1.weekday()]  
     
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + 'Lon  ' +str(json_data['coord']['lat'])+'Lat',
            "temp": str(round(json_data['main']['temp']-273,5)),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "icon":"images/icons/"+str(json_data['weather'][0]['icon'])+".svg",
            "icondesc":str(json_data['weather'][0]['main']),
            "wind": str(json_data['wind']['speed']),
            "winddeg": str(json_data['wind']['deg']),
            "visibility": str(round(json_data['visibility']/10000,5)),
            "day":day,
            "date1":date1,
            'citylst':citylst,

        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})

def contact(request):
    return render(request,'contact.html')

def photos(request):
    return render(request,'photos.html')


