
from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import CustomerForm
from .models import *
from datetime import date
import winsound
from playsound import playsound

def index(request):
	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			winsound.PlaySound('static/audio/tone.wav', winsound.SND_ASYNC)
			print('play save sound')
			return HttpResponseRedirect('success/')

	context = {'form':form}
	return render(request, 'app/index.html', context)

    
def success(request):
    data = request.POST.get('textbox1')
    context= {'data':data}
    return render(request, 'app/success.html', context)

def monitor(request):
	data = request.POST.get('textbox1')
	today_year = date.today().year
	today_month = date.today().month
	today_day = date.today().day
	msg_view = Msg.objects.filter(msg_date__year=today_year, msg_date__month=today_month, msg_date__day=today_day).order_by('-msg_date')
	total_msgs = msg_view.count()
	test = Msg.objects.values_list('msg_count', flat=True)[1]

	if test < msg_view.count() & total_msgs != 0:
		winsound.PlaySound('static/audio/new_entry.wav', winsound.SND_ASYNC)
		print('new entry sound !!!!!!')
		Msg.objects.all().update(msg_count=total_msgs)

	if request.method == 'DELETE':
			Msg.objects.get(pk=request.DELETE['delete-id']).delete()

	context = {'data':data, 'msg_view':msg_view, 'total_msgs':total_msgs}
	return render(request, 'app/monitor.html', context)

def delete_event(request, event_id):
	event = Msg.objects.get(pk=event_id)
	event.delete()

	total = Msg.objects.all().count()-2
	Msg.objects.all().update(msg_count=total)
	winsound.PlaySound('static/audio/delete.wav', winsound.SND_ASYNC)
	print('play delete sound')
	return redirect('monitor')

def delete_all_event(request):
	Msg.objects.all().exclude(msg_room="xxx").delete() 
	Msg.objects.filter(msg_room="xxx").update(msg_count=0)
	winsound.PlaySound('static/audio/delete.wav', winsound.SND_ASYNC)
	print('play delete all sound')
	return redirect('monitor')

def mark_event(request, event_id):
	event = Msg.objects.get(pk=event_id)
	Msg.objects.filter(pk=event_id).update(msg_mark=True)
	winsound.PlaySound('static/audio/tone.wav', winsound.SND_ASYNC)
	print('play mark sound')
	return redirect('monitor')

def mark_all_event(request):
	Msg.objects.all().update(msg_mark=True)
	winsound.PlaySound('static/audio/tone.wav', winsound.SND_ASYNC)
	print('play mark all sound')
	return redirect('monitor')

def mark_event_x(request, event_id):
	event = Msg.objects.get(pk=event_id)
	Msg.objects.filter(pk=event_id).update(msg_mark=False)
	winsound.PlaySound('static/audio/out.wav', winsound.SND_ASYNC)
	print('play unmark sound')
	return redirect('monitor')