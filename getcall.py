from django.template import HttpResponse
from django.template import loader
from .modules import student_data
def home(request):
     students=student_data.objects.all().value()
     template=loader.get_template('first.html')
     context={
		'students':students
	     }
     return HttpResponse(template.render(context,request))
