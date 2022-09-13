from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.first),
	path('project/', views.second),
	path('form/',views.third),
	path('regcode/', views.registercode),
	path('regform/', views.regform),
	path('contact/', views.contact),
	path('about/', views.about),
	path('add/', views.add),
	path('registercode/', views.registercode),
	path('contact1/', views.contact1),
	path('welcome/', views.welcome),
	path('logout/', views.logout),
	path('showuser/', views.showuser),
	path('mobile/', views.mobile),
	path('userwelcome/', views.wel),
	path('adminwelcome/', views.wel2),
	path('account/', views.account),
	path('account2/', views.account2),
	path('final/', views.final),
	path('final2/', views.final2),
	path('editreg/', views.editreg),
	path('editadd/', views.editadd),
	path('adpgg/', views.adpgg),
	path('adpg/', views.adpg),
	path('showpg/', views.showpg),
	path('showadpg/', views.showadpg),
	path('feed/', views.feed),
	path('feed1/', views.feed1),
	path('showfeed/', views.showfeed),
	path('apply/', views.apply),
	path('apply1/', views.apply1),
	path('sendreq/', views.send),
	path('reply/', views.reply),
	path('showreq/', views.showreq),
	path('showmypg/', views.showmypg),
	path('services/', views.services),
	
	
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


