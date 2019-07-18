from django.shortcuts import render_to_response

# Create your views here.
def hello(request):
    
    list = ['한은섭', '김원오' , '조근형', '이승일', '김수지'] 
    
    return render_to_response('hello.html',{'list':list}) #java로 치면 forwarding