from django.shortcuts import render,redirect
from django.http import HttpResponse
from application.models import Register1,Register4,Contact3,Registerpg,Feed2,Applypg,Sendreq1
from django.conf.urls.static import static
def first(request):
	return render(request, "template/projectcopy.html")
def adpg(request):
	if request.session.has_key('admin'):
		email=request.session['admin']
		return render(request, "template/adpg.html",{"email":email})
	else:
		return redirect("/form/")
def wel(request):
	if request.session.has_key('user'):
		email=request.session['user']
		return render(request,"template/userwelcome.html",{"username":email})
	else:
		return redirect("/form/")
def wel2(request):
	if request.session.has_key('admin'):
		email=request.session['admin']
		return render(request, "template/adminwelcome.html",{"username":email})	
	else:
		return redirect("/form/")	
def second(request):
	return render(request, "template/projectcopy.html")
def third(request):
	return render(request, "template/form.html")
def regform(request):
	return render(request, "template/regform.html")
def contact(request):
    return render(request, "template/contact.html")	
def about(request):
    return render(request, "template/about.html")
def add(request):
    return render(request, "template/add.html")
def services(request):
    return render(request, "template/services.html")
def feed(request):
	if request.session.has_key('user'):
		return render(request, "template/feed.html")
	else:
		return redirect("/form/")
def sendreq(request):
	if request.session.has_key('user'):
		return render(request, "template/sendreq.html")	
	else:
		return redirect("/form/")
def showreq(request):
	if request.session.has_key('admin'):
		email=request.session['admin']
		data=Sendreq1.objects.filter(p_email=email).all()
		return render(request, "template/showreq.html",{"alldata":data})
	else:
		return redirect("/form/")	
		
def showpg(request):
	if request.session.has_key('user'):
		data=Registerpg.objects.all()
		return render(request, "template/showpg.html",{"alldata":data})
	else:
		return redirect("/form/")	
def showadpg(request):
	if request.session.has_key('admin'):
		if request.method=="POST":
			a=request.POST['t1']
			Registerpg.objects.filter(id=a).delete()
		data=Registerpg.objects.all()
		return render(request, "template/showadpg.html",{"alldata":data})
	else:
		return redirect("/form/")	
def showmypg(request):
	if request.session.has_key('user'):
		if request.method=="POST":
			a=request.POST['t1']
			Applypg.objects.filter(pid=a).delete()
			email=request.session['user']
			data=Applypg.objects.filter(email=email).all()
			return render(request, "template/mypg.html",{"alldata":data})
		else:
			email=request.session['user']
			data=Applypg.objects.filter(email=email).all()
			return render(request, "template/mypg.html",{"alldata":data})
	else:
		return redirect("/form/")
def showfeed(request):
	if request.session.has_key('admin'):
		data=Feed2.objects.all()
		return render(request, "template/showfeed.html",{"alldata":data})
	else:
		return redirect("/form/")
def reply(request):
	if request.session.has_key('user'):
		email=request.session['user']
		data=Sendreq1.objects.filter(p_email=email).count()
		if data==0:
			msg="No data"
			return render(request,"template/msg.html",{"msg1":msg})
		else:
			data=Sendreq1.objects.filter(p_email=email).all()
			return render(request, "template/reply.html",{"alldata":data})	
	else:
		return redirect("/form/")
def registercode(request):
	if request.method == "POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.POST['t8']
		i=request.POST['t9']
		j=request.POST['t10']
		data=Register1(fname=a,lname=b,address=c,qualification=d,gender=e,lookingfor=f,no=g,email=h,pwd=i,cpwd=j)
		data.save()
		msg="user register successfully"
		return render(request,"template/msg.html",{"msg1":msg})
	else:
		redirect('/register/')		  
def mobile(request):
    if request.method == "POST":
       a=request.POST['t1'] 
       b=request.POST['t2']
       c=request.POST['t3']
       d=request.POST['t4']
       e=request.POST['t5']
       f=request.POST['t6']
       g=request.POST['t7']
       h=request.POST['t8']
       data=Register4(fname=a,lname=b,address=c,gender=d,no=e,email=f,pwd=g,cpwd=h)
       data.save()
       msg="add pg successfully" 	   
       return render(request,"template/msg.html",{"msg1":msg})
    else:
        redirect('/add/')
def contact1(request):
    if request.method == "POST":
       a=request.POST['t1'] 
       b=request.POST['t2']
       c=request.POST['t3']
       data=Contact3(name=a,email=b,msg=c)
       data.save() 
       msg="message sent"	   
       return render(request,"template/msg.html",{"msg1":msg})
    else:
        redirect('/contact/')
def feed1(request):
    if request.method == "POST":
       a=request.POST['t1'] 
       b=request.POST['t2']
       c=request.POST['t3']
       data=Feed2(name=a,email=b,msg=c)
       data.save() 
       msg="feedback sent"	   
       return render(request,"template/msg.html",{"msg1":msg})
    else:
        redirect('/feed/')
def showuser(request):
	if request.method == "POST":
		a=request.POST['t1']
		b=request.POST['t2']
		data=Register1.objects.filter(email=a,pwd=b).count()
		if data!=0:
			request.session['user']=a
			return redirect("/welcome/")
		else:
			data=Register4.objects.filter(email=a,pwd=b).count()
			if data==0:
				msg="not match1"
				return render(request,"template/form.html",{"msg":msg})
			else:
				request.session['admin']=a
				return redirect("/adminwelcome/")
	else:
		msg="not match2"
		return render(request,"template/form.html",{"msg":msg})
		
def welcome(request):
	if request.session.has_key('user'):
		email=request.session['user']
		return render(request,"template/userwelcome.html",{"username":email})
	else:
		return redirect("/form/")
def logout(request):
	if request.session.has_key('user'):
		del request.session['user'] 
	if request.session.has_key('admin'):
		del request.session['admin'] 
	return redirect("/form/")
def account(request):
	if request.session.has_key('user'):
		email= request.session['user']
		data=Register1.objects.filter(email=email).all()
		return render(request,"template/editreg.html",{"alldata":data})
	else:
		return redirect("/userwelcome/")
def account2(request):
	if request.session.has_key('user'):
		email= request.session['user']
		data=Register4.objects.filter(email=email).all()
		return render(request,"template/editadd.html",{"alldata":data})
	else:
		return redirect("/adminwelcome/")
def final(request):
    if request.method == "POST":
       a=request.POST['t1'] 
       b=request.POST['t2']
       c=request.POST['t3']
       d=request.POST['t4']
       e=request.POST['t5']
       f=request.POST['t6']
       g=request.POST['t7']
       Register1.objects.filter(email=e).update(fname=a,lname=b,address=c,no=d,pwd=f,cpwd=g)
       msg="update" 
       return render(request,"template/msg.html",{"msg1":msg})
    else:
        redirect('/register/')
def editreg(request):
	if request.session.has_key('user'):
		username= request.session['user']
		data=Register1.objects.filter(email=username).all()
		return render(request,"template/editreg.html",{"alldata":data})
	else:
		return redirect("/form/")
def final2(request):
    if request.method == "POST":
       a=request.POST['t1'] 
       b=request.POST['t2']
       c=request.POST['t3']
       d=request.POST['t4']
       e=request.POST['t5']
       f=request.POST['t6']
       g=request.POST['t7']
       Register4.objects.filter(email=e).update(fname=a,lname=b,address=c,no=d,pwd=f,cpwd=g)
       msg="update pg successfully" 
       return render(request,"template/msg.html",{"msg1":msg})
    else:
        redirect('/register/')
def editadd(request):
	if request.session.has_key('admin'):
		username= request.session['admin']
		data=Register4.objects.filter(email=username).all()
		return render(request,"template/editadd.html",{"alldata":data})
	else:
		return redirect("/form/")
def adpgg(request):
	if request.method == "POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.POST['t8']
		i=request.POST['t9']
		j=request.FILES['t10']
		data=Registerpg(name=a,hno=b,address=c,sector=d,land=e,seats=f,room=g,food=h,email=i,photo=j)
		data.save()
		msg="add pg successfully"
		return render(request,"template/msg.html",{"msg1":msg})
	else:
		redirect('/adpg/')
def apply1(request):
	email=request.POST['t1']
	data=Applypg.objects.filter(pid=email).count()
	if data ==0:
		msg="No Booking"
		return render(request,"template/msg.html",{"msg1":msg})
	else:		
		data=Applypg.objects.filter(pid=email).all()
		return render(request, "template/apply1.html",{"alldata":data})	
def apply(request):
	id=request.POST['t1']
	email=request.session['user']
	all=Applypg.objects.filter(email=email).count()
	if all==0:
		data=Registerpg.objects.filter(id=id).all()
		for single in data:
			hno=single.hno
			address=single	.address
			sector=single.sector
			seats=single.seats
			photo=single.photo
		email=request.session['user']
		data2=Register1.objects.filter(email=email).all()
		for single2 in data2:
			fname=single2.fname
			no=single2.no
			print(email)
		data3=Applypg(pid=id,hno=hno,address=address,sector=sector,seats=seats,photo=photo,fname=fname,email=email,no=no)
		data3.save()
		msg="Apply pg successfully"
		return render(request,"template/msg.html",{"msg1":msg})
	else:
		msg="Already Apply pg"
		return render(request,"template/msg.html",{"msg1":msg})
		
def send(request):
	if request.method == "POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.POST['t8']
		data=Sendreq1(pid=a,name=b,no=c,email=d,type=e,msg=f,p_name=g,p_email=h)
		data.save()
		msg="Send request successfully"
		return render(request,"template/msg.html",{"msg1":msg})	
	else:
		if request.session.has_key('user'):
			username= request.session['user']
			data=Register1.objects.filter(email=username).all()
			data2=Applypg.objects.filter(email=username).count()
			if data2==0:
				msg="Plz Select PG FIRST"
				return render(request,"template/msg.html",{"msg1":msg})	
			else:
				data2=Applypg.objects.filter(email=username).all()
				for abc in data2:
					pgid=abc.pid
				data3=Registerpg.objects.filter(id=pgid).all()
				for abc2 in data3:
					pg_name=abc2.name
					pg_email=abc2.email
				return render(request,"template/sendreq.html",{"alldata":data,"pid":pgid,"p_name":pg_name,"p_email":pg_email})
		else:
			return redirect("/form/")