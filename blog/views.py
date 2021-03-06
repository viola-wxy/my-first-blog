
# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment, info, work, skills, hobby, education 
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm, educationForm, InfoForm, workForm, skillsForm, hobbyForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import markdown


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def publish(self):
    self.published_date = timezone.now()
    self.save()

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)




def cv(request):
    infos = info.objects.all()
    length = len(infos)
    for a in range(1,length+1):
        infos[a-1].text = markdown.markdown(infos[a-1].text,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
                                  
    educations = education.objects.all()
    length = len(educations)
    for a in range(1,length+1):
        educations[a-1].text = markdown.markdown(educations[a-1].text,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    works = work.objects.all()
    length = len(works)
    for a in range(1,length+1):
        works[a-1].text = markdown.markdown(works[a-1].text,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    skillss = skills.objects.all()
    length = len(skillss)
    for a in range(1,length+1):
        skillss[a-1].text = markdown.markdown(skillss[a-1].text,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    hobbys = hobby.objects.all()
    length = len(hobbys)
    for a in range(1,length+1):
        hobbys[a-1].text = markdown.markdown(hobbys[a-1].text,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    return render(request, 'cv/cv.html', {'infos': infos, 'educations':educations, 'works':works, 'skillss':skillss, 'hobbys':hobbys})

@login_required
def cv_new(request):
    if 'info' in request.POST:
        form = InfoForm(request.POST)
        newinfo = form.save()
        return redirect('cv')
    elif 'education' in request.POST:
        form = educationForm(request.POST)
        neweducation = form.save()
        return redirect('cv')
    elif 'work' in request.POST:
        form = workForm(request.POST)
        newwork = form.save()
        return redirect('cv')
    elif 'skills' in request.POST:
        form = skillsForm(request.POST)
        newskill = form.save()
        return redirect('cv')
    elif 'hobby' in request.POST:
        form = hobbyForm(request.POST)
        newhobby = form.save()
        return redirect('cv')
    else:
        form = InfoForm(request.POST)
    return render(request, 'cv/cv_new.html', {'form': form})  