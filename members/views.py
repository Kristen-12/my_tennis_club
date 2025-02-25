from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
#members page
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
 #detail page 
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
#main page
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

#def footer(request):
  #template = loader.get_template('footer.html')
  #return HttpResponse(template.render())

def testing(request):
  #mymembers = Member.objects.all().values()
  #mydata = Member.objects.all()
  #mydata = Member.objects.all().values() #value as dictonary
  #mydata = Member.objects.values_list('firstname')
  #mydata = Member.objects.filter(firstname='Kris').values()
  #mydata = Member.objects.filter(lastname='Nor', id=1).values()
  #mydata = Member.objects.filter(firstname='Kris').values() | Member.objects.filter(firstname='Tobias').values()
  #mydata = Member.objects.filter(firstname__startswith='L').values()
  #mydata = Member.objects.all().order_by('firstname').values()  #ascending order
  #mydata = Member.objects.all().order_by('-firstname').values() #descending order
  mydata = Member.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('template.html')

  context = {
    'mymembers': mydata,
    #'mymembers': mymembers,
    #'greeting' :1,
    #'day' : 'Friday',
    #'fruits': ['Apple', 'Banana', 'Cherry','Orange', 'Kiwi'],
    #'x': ['Apple', 'Banana', 'Cherry'], 
    #'y': ['Apple', 'Banana', 'Cherry'],

    #'emptytestobject': [],

    #'cars': [
      #{
        #'brand': 'Ford',
        #'model': 'Mustang',
        #'year': '1964',
      #},
      #{
        #'brand': 'Ford',
        #'model': 'Bronco',
        #'year': '1970',
      #},
      #{
        #'brand': 'Volvo',
        #'model': 'P1800',
        #'year': '1964',
      #}]
  }
  return HttpResponse(template.render(context, request))    

def tech(request):
  template = loader.get_template('tech.html')
  return HttpResponse(template.render( ))    