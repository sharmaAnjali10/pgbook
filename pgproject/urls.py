from django.contrib import admin
from django.urls import path, include
from application import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
	path('project/', include('application.urls')),
	path('form/', include('application.urls')),
	path('regcode/', include('application.urls')),
	path('regform/', include('application.urls')),
	path('showuser/', include('application.urls')),
	path('contact/', include('application.urls')),
	path('about/', include('application.urls')),
	path('registercode/', include('application.urls')),
	path('contact1/', include('application.urls')),
	path('welcome/', include('application.urls')),
	path('logout/', include('application.urls')),
	path('mobile/', include('application.urls')),
	path('userwelcome/', include('application.urls')),
	path('adminwelcome/', include('application.urls')),
	path('account/', include('application.urls')),
	path('account2/', include('application.urls')),
	path('final/', include('application.urls')),
	path('final2/', include('application.urls')),
	path('editreg/', include('application.urls')),
	path('editadd/', include('application.urls')),
	path('adpgg/', include('application.urls')),
	path('adpg/', include('application.urls')),
	path('showpg/', include('application.urls')),
	path('showadpg/', include('application.urls')),
	path('feed/', include('application.urls')),
	path('feed1/', include('application.urls')),
	path('showfeed/', include('application.urls')),
	path('apply/', include('application.urls')),
	path('apply1/', include('application.urls')),
	path('sendreq/', include('application.urls')),
	path('reply/', include('application.urls')),
	path('showreq/', include('application.urls')),
	path('showmypg/', include('application.urls')),
	path('services/', include('application.urls')),
]

