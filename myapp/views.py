from django.shortcuts import render
from . import mymain
from . import textToSpeechModule
from django.template import loader

# Create your views here.
def main(request):
	template=loader.get_template('myapp/f.html')
	context={} 
	return render(request, 'myapp/f.html', context)


def index(request):
	template=loader.get_template('myapp/respVoice.html')
	path="C:\\Users\\dell\\Desktop\\website\\tweets\\static\\image\\twitter-wallpaper.png"
	tosay=mymain.foo()
	context={
						'mystring': tosay
	} 
	return render(request, 'myapp/respVoice.html', context)