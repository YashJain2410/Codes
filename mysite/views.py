# Manually generated file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyse(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    #Check checkbox values
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analysed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyse.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analysed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyse.html', params)

    if(extraspaceremover == "on"):
        analysed = ""
        for i, char in enumerate(djtext):
            if djtext[i] == " " and djtext[i+1] == " ":
                pass
            else:
                analysed = analysed + char
        params = {'purpose': 'Extra Space Remover', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)
    #
    # else:
    #     return HttpResponse('Error')

    return render(request, 'analyse.html', params)