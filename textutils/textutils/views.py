from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyse(request):
    texty = request.POST.get('text', 'Default')
    removepunc = request.POST.get('removepunc','off')
    capall = request.POST.get('capall','off')
    newremove = request.POST.get('newremove', 'off')
    spacerem = request.POST.get('spacerem','off')
    charcount = request.POST.get('charcount','off')
    if removepunc == 'on':
        analysed=""
        punctuations ='''[][!"#$%&'()*+,./:;<=>?@^_`|{}~-'''
        for char in texty:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose':"Removed Punctuations",'analyzed_text': analysed}
        texty = analysed
        # return render(request, 'analysed.html', params)
    if capall == "on" :
        analysed=''
        for word in texty:
            woo = word.capitalize()
            analysed = analysed + woo
        params = {'purpose':"Capitalize First",'analyzed_text': analysed}
        texty = analysed
        # return render(request,'analysed.html',params)
    if (newremove == 'on'):
        analysed = ""
        for char in texty:
            if char != '\n' and char !='\r':
                analysed = analysed + char
        params = {'purpose':"Remove Newline",'analyzed_text': analysed}
        texty = analysed
        # return render(request,'analysed.html',params)
    if spacerem == 'on':
        analysed = ''
        for i in texty:
            if " " not in i:
                analysed = analysed + i
        params = {'purpose':"Space Remove",'analyzed_text':analysed}
        texty = analysed
        # return render(request,'analysed.html',params)
    if charcount=='on':
        analysed = ''
        count = 0
        for i in texty:
            if (i != None) and (i!=' '):
                count = count +1
        analysed = texty + str( count)
        params = {'purpose':"Charachter Count",'analyzed_text':analysed}
        

        
        
    if ((charcount!='on')and (spacerem != 'on') and (newremove != 'on') and (capall != "on") and (removepunc != 'on')):
        return render(request,'nonepage.html')
        # return render(request,'analysed.html',params)
    # else:
    #     return render(request,'nonepage.html')
    return render(request,'analysed.html',params)