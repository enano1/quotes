from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

# Global quotes and images lists
quotes_list = [
    "I don't think people are going to talk in the future. I think they're going to communicate through eye contact, body language, emojis, and GIFs.",
    "I am a proud non-reader of books. I like to get information from bootlegs, and then I can interpret it my way.",
    "I'm not a businessman, I'm a business, man.",
    "I'm a giver. I like to give. I'm a giver.",
    "I'm not even gonna give you the energy to respond to that.",
    "I'm a trailblazer. I do everything different. I'm not afraid to take risks.",
    "If I was more complacent and I let things slide, my time would be wasted. I have no time for wasted time.",
    "I'm not a normal person, which is why I have a normal life.",
    "I'm a creative genius and there's no other way to word it.",
    "We're not afraid to take risks. We're not afraid to go against the grain.",
    "I'm not a celebrity. I don't fit into any of those categories. I'm a creative genius.",
    "I'm not a rapper. I'm a messenger. I'm a prophet. I'm a visionary."
]

images_list = [
    '/static/quotes/images/KW1.jpg',
    '/static/quotes/images/KW2.jpg',

    '/static/quotes/images/KW3.jpg',
    '/static/quotes/images/KW4.jpg',

    '/static/quotes/images/KW5.jpg',
    '/static/quotes/images/KW6.jpg',

    '/static/quotes/images/KW7.jpg',
  
]

def base(request):
    '''
    Function to handle the URL request for the main page.
    Get a random quote and image from the quote/image list.
    '''

    template_name = 'quotes/base.html'

    my_quote = "I'm not a businessman, I'm a business, man."

    my_image = '/static/quotes/images/KW7.jpg'


    return render(request, template_name, {'quote': my_quote, 'image': my_image})
def quote(request):
    '''
    Function to handle the URL request for the quote page.
    Get a random quote and image from the quote/image list
    '''

    template_name = 'quotes/quote.html'
    
    random_quote = random.choice(quotes_list)
    random_image = random.choice(images_list)

    return render(request, template_name, {'quote': random_quote, 'image': random_image})

def show_all(request):
    '''
    Function to handle the URL request for the show_all page.
    Display all of the images and quotes
    '''

    template_name = 'quotes/show_all.html'
    
    return render(request, template_name, {'quotes': quotes_list, 'images': images_list})

def about(request):
    '''
    Function to handle the URL request for the about page.
    '''

    template_name = 'quotes/about.html'
    
    return render(request, template_name)
