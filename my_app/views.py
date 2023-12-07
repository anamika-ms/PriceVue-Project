from django.shortcuts import render
from . models import reg
import pandas as pd
from sklearn import linear_model

# Create your views here.

data=pd.read_csv(r'C:\Users\grapes\Downloads\homeprices2.csv')
values = {"bedrooms":1.0}
data = data.fillna(value=values)
x=data.drop('price',axis=1)
y=data.price
model=linear_model.LinearRegression()
model.fit(x,y)

def index(request):
    return render(request,'index.html')

def register(request):
   if request.method =='POST':
      fname = request.POST.get('rfname')
      age1 = request.POST.get('rage')
      address1 = request.POST.get('raddress')
      email1 = request.POST.get('remail')
      phone = request.POST.get('rcontact')
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      reg(fullname=fname,age=age1,address=address1,email=email1,contact=phone,username=uname,password=passw).save()
      return render(request,'login.html')
   else:
      return render(request,'register.html')
   
def login(request):
   if request.method=='POST':
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      cr = reg.objects.filter(username=uname,password=passw)
      if cr:
         # details = reg.objects.get(username= uname , password = passw)
         # username = details.username
         # request.session['cs']=username

         return render(request,'price.html')
      else:
         message="Invalid Username Or Password"
         return render(request,'login.html',{'me':message})
   else: 
      return render(request,'login.html')
   
def price(request):
   if request.method=='POST':
      Area=float(request.POST.get('area',0.0))
      Num=float(request.POST.get('room',0.0))
      Time=float(request.POST.get('limit',0.0))
      res=model.predict([[Area,Num,Time]])[0]
      return render(request,'price.html',{'res':res})
   else:
      return render(request,'price.html')
    

