from django.shortcuts import redirect, render, HttpResponse
import sweetify

def test_success(request):
    sweetify.sweetalert(request, icon='success', title='YOU DID IT', text="Good Job! You successfully sent a SweetAlert Message", persistent='HELL YEAH')
    return redirect('/')

def test_error(request):
    sweetify.sweetalert(request, icon='error', title='YOU DID IT', text="Good Job! You successfully sent a SweetAlert Message", persistent='HELL YEAH')
    return redirect('/')

def test_warning(request):
    sweetify.sweetalert(request, icon='warning', title='YOU DID IT', text="Good Job! You successfully sent a SweetAlert Message", persistent='HELL YEAH')
    return redirect('/')

def test_info(request):
    sweetify.sweetalert(request, icon='info', title='YOU DID IT', text="Good Job! You successfully sent a SweetAlert Message", persistent='HELL YEAH')
    return redirect('/')