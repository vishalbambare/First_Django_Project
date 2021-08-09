from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", "Off")
    uppercase = request.POST.get("uppercase", "Off")
    newlineremover = request.POST.get("newlineremover", "Off")
    extraspaceremover = request.POST.get("extraspaceremover", "Off")
    charcount = request.POST.get("charcount" , "Off")

    if removepunc == "on":
        punctuations = """!@#$%^&*(){}[]|._-`/?:;"'\,~"""
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        punc = {"purpose": " Remove punctuation", "Analyzed_text": analyze}
        djtext = analyze
        # return render(request, "anayzer.html", punc)

    if(uppercase =="on"):
        analyze=""
        for char in djtext:
            analyze = analyze + char.upper()
        punc = {"purpose": " Uppercase", "Analyzed_text": analyze}
        djtext = analyze
        # return render(request, "anayzer.html", punc)
        
    
    if(newlineremover=="on"):
        analyze=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyze = analyze + char
        punc = {"purpose": " New line Remover", "Analyzed_text": analyze}
        djtext = analyze
        # return render(request, "anayzer.html", punc)

    if(extraspaceremover =="on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1]==" "):
                analyze = analyze + char
        punc = {"purpose": " Extraspace Remover", "Analyzed_text": analyze}
        djtext = analyze
        # return render(request, "anayzer.html", punc)

    if(charcount =="on"):
        # analyze= len(djtext)
        count = 0
        for char in djtext:
            if char != " ":
                count = count+1
        analyze = count
        punc = {"purpose": " Charcount", "Analyzed_text": analyze}
        
    if (charcount !="on" and extraspaceremover !="on" and newlineremover !="on" and uppercase !="on" and removepunc !="on"):
      return HttpResponse ("<H1> kindly check the checkbox </h1>")
      
        # return render(request, "anayzer.html", punc)
    # else:
    #     return HttpResponse("Kindly check the Checkbox")
    # punc = {"purpose": " Remove punctuation", "Analyzed_text": analyze}
    # return render(request, "anayzer.html", punc)
    return render (request, "anayzer.html", punc)