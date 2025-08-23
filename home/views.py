from django.shortcuts import render,redirect
fro.form import feedbackform

def feedback_view(request):
    if request.method =='post':
        form = feedbackform(request.post)
        if form.is_valid():
            form.save()
            return redirect('feedback')
        else:
            form = feedbackform()
        return render(request, 'feedback.html',{'fomr':form})
        