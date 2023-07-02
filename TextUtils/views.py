from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    maintext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    analyzedtxt = maintext
    analysis_steps = []
    length1 = ''
    length2 = ''

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzedtxt = ""
        for char in maintext:
            if char not in punctuations:
                analyzedtxt += char
        analysis_steps.append("Punctuation removed")

    if uppercase == "on":
        analyzedtxt = analyzedtxt.upper()
        analysis_steps.append("Converted to uppercase")

    if newlineremove == "on":
        analyzedtxt = analyzedtxt.replace("\n", "").replace("\r","")
        print(analyzedtxt)
        analysis_steps.append("New lines removed")

    if spaceremove == "on":
        atxt=""
        atxt = " ".join(analyzedtxt.split())
        analyzedtxt = atxt
        
    if charcount == "on":
        length1 = len(maintext)
        length2 = len(analyzedtxt)
        analysis_steps.append("Character count calculated")

    params = {
        'purpose': 'Text Analysis',
        'analyzedtxt': analyzedtxt,
        'analysis_steps': analysis_steps,
        'length1': length1,
        'length2': length2
    }
    # print(analyzedtxt)
    return render(request, 'analyze.html', params)
