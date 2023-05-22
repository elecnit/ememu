from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import FoodItems,Category,order



def HomefrstView(request):
      tab_no = 1
      return render(request,'home.html',context={"tab_no":tab_no})


def HomesecView(request):
      tab_no = 2
      return render(request,'home1.html',context={"tab_no":tab_no})




def HomePageView(request,tab_no):
      food_list = FoodItems.objects.all()
      category_list = Category.objects.all()
      return render(request,'emenu.html',{'category_list':category_list,"food_list":food_list,"tab_no":tab_no})

order_list = []
total = 0
def GetOrderView(request,name,price,tab_no):
      global total
      order_list.append([name,price])
      total+=price
      food_list = FoodItems.objects.all()
      category_list = Category.objects.all()
      return render(request,'emenu.html',{'category_list':category_list,"food_list":food_list,"tab_no":tab_no})


def PlaceOrderView(request,tab_no):
      print(order_list)
      return render(request,'cart.html',{"order_list":order_list,"tab_no":tab_no})

def fetch_value():   
      order_str = ''

      for i in order_list:
            order_str += i[0]+'  '
      return order_str

def PlacedOrderView(request , tab_no , customer_id=1):
      data =  {
            'order_items':fetch_value(),
            'table_no':tab_no,
            'customer_id':customer_id
      }
      print(data)
      order_instance = order(order_items=data['order_items'],table_no=data['table_no'],customer_id=data['customer_id'])
      order_instance.save()
      return render(request,'finish.html',context={"tab_no":tab_no})

def ChiefOrderView(request):
      table1 = order.objects.filter(table_no='1',served=False).values()
      table2 = order.objects.filter(table_no='2',served=False).values()
      print(table2)
      print(table1)
      tab1 = table1[len(table1)-1]['order_items'].split('  ')
      tab2 = table2[len(table2)-1]['order_items'].split('  ')

      return render(request,'chieforder.html',{'table1':tab1,'table2':tab2})


class DetailFoodView(DetailView):
      model = FoodItems
      template_name = 'detailfood.html'


class AddFoodView(CreateView):
     model = FoodItems
     template_name = 'addfood.html'
     fields = '__all__'

class EditFoodView(UpdateView):
      model = FoodItems
      template_name = 'editfood.html'
      fields = '__all__'

class DeleteFoodView(DeleteView):
      model = FoodItems 
      template_name = 'deletefood.html'
      success_url = reverse_lazy('home')

