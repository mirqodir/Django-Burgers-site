from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Product,Comment
from django.core.paginator import Paginator
import requests
from django.urls import reverse_lazy
# Create your views here.




class HomePageView(TemplateView):
	template_name = 'index.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

class BookPageView(TemplateView):
	template_name = 'book.html'

class MenuPageView(ListView):
	model = Product
	template_name = 'menu.html'


######## pagelar saxifalaga otish
def menupageview(request):
	obj = Product.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,11)
	try:
		page = p.page(page_n)
	except Exception:
		page = p.page(1)
	context = {

		"page":page
	}

	return render(request,"menu.html",context)


########### telegram
def telegram_bot_sendtext(bot_message):
	bot_token = '5103339974:AAHI2WTgRRWldbEOr1zfPiWCkAgvRJi8WXw'
	bot_chatID = '708006401'
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message
	response = requests.get(send_text)

	return response.json()


def BookPageView(request):
	if request.method == 'POST':
		name = request.POST.get('name',None)
		phone = request.POST.get('phone',None)
		email = request.POST.get('email',None)
		message = request.POST.get('message',None)
		user = Comment.objects.create(
			userName = name,
			phone = phone,
			email = email,
			message = message
		)
		user.save()
		telegram_bot_sendtext(f"Ismi:{name}\nTelefon raqami:{phone}\nEmail:{email}\nXabar:{message}")
	return render(
	request=request,
	template_name = 'book.html'
	)

################# maxsulot qoshish yaratish qismi
class ProductCreateView(CreateView):
	model = Product
	template_name = 'product_create.html'
	# fields = ('name_card','description','price')
	fields = '__all__'
	success_url = reverse_lazy('index')