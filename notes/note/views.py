from django.shortcuts import render, redirect

from .models import Note

def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = Note.objects.all()
    
    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if docid > 0:
            document = Note.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()
            
            return redirect('/?docid=%i' % docid)
        
        else:
            document = Note.objects.create(title=title, content=content)
            
            return redirect('/?docid=%i' % document.docid)
    
    if docid > 0:
        document = Note.objects.get(pk=docid)
    else:
        document = ''
    
    content = {
        'docid': docid,
        'documents': documents,
        'document': document,
    }
    
    return render(request, 'editor.html', content)