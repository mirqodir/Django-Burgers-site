from django.urls import path
from .views import HomePageView,AboutPageView,BookPageView,menupageview,ProductCreateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [


		path('',HomePageView.as_view(),name='index'),
		path('about/',AboutPageView.as_view(),name='about'),
		path('book/',BookPageView,name='book'),
		path('menu',menupageview,name='menu'),
		path('product_create/',ProductCreateView.as_view(),name='product_create')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)