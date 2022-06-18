from django.shortcuts import render
from django.http import HttpResponse

from .forms import TextSubmission

import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# connect text similarity to program 
def calculate_similarity(text1, text2):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    text1_embed = model.encode(text1)
    text2_embed = model.encode(text2)
    sim_value = cosine_similarity([text1_embed], [text2_embed]).flatten()[0]
    return sim_value

# changes raw score to boolean value 
def determine_class(similarity_score):
    if similarity_score >= 0.91:
        return True 
    else: 
        return False 

def get_submission(request):
    if request.method == "POST":
        # creates a form instance and populates it with data from the request 
        form = TextSubmission(request.POST)
        # checking to see whether the form is valid 
        if form.is_valid():
            cleaned = form.cleaned_data 
            text1 = cleaned.get('text1')
            text2 = cleaned.get('text2')

            similarity = calculate_similarity(text1, text2)
            print(similarity)
            pred_class = determine_class(similarity)
            
    # if the request is GET or something else, a blank form is created 
    else: 
        form = TextSubmission()
        pred_class = ""
    
    return render(request, 'base.html', {'form': form, 'result': pred_class})