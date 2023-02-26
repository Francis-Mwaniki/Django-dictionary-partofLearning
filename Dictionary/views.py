from django.shortcuts import render
# importing the PyDictionary library
from PyDictionary import PyDictionary
# Create your views here.

def homeView(request):
    return render(request, template_name='index.html',)

""" searchVies is the view for the search page """
def searchView(request):
    # capturing the word from the form via the name search
      word = request.GET.get('search')
    # creating a dictionary object
      dictionary=PyDictionary()
    # passing a word to the dictionary object
      meanings = dictionary.meaning(word)
    # getting a synonym and antonym  
      synonyms = dictionary.synonym(word)
      antonyms = dictionary.antonym(word)
    # bundling all the variables in the context  
      context = { 
                 'word':word,
                 'meanings':meanings,
                 'synonyms':synonyms,
                 'antonyms':antonyms
      }
      print(context)
      return render(request, 'search.html', context)