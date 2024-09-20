from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random
# Create your views here.
# def home(request):
#     '''Handle the main URL for the hw app'''

#     response_text = f'''
#     <html>
#     <ht>Hello world!</h1>
#     <p>This is our first django web application!</p>
#     <hr>
#     This page was generated at {time.ctime()}.
#     </html>
#     '''

#     # create and return a response to the client
#     return HttpResponse(response_text)

def home(request):
    '''
    Function to handle the URL request for /hw (main page).
    Delegate rendering to the template hw/home.html.
    '''

    #se this template to render the resopnse

    template_name = 'hw/home.html'
    
    #create a dictionary of context variables for the template:
    context = {
        'current_time': time.ctime(),
        'letter1': chr(random.randint(65,90)),
        'letter2': chr(random.randint(65,90)),
        'number': random.randint(0,100),
                      
    }
    
    return render(request, template_name, context)


