# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChapterForm
from .models import Chapter
import markdown2

def show_chapter(request):
    chapters = Chapter.objects.all()

    for chapter in chapters:
        if chapter.context:
            # Consider doing Markdown conversion in the template
            # chapter.context = markdown2.markdown(chapter.context)
            pass
        else:
            chapter.context = ""

    return render(request, "index.html", {'chapters': chapters})

def create_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)

        if form.is_valid():
            chapter = form.save(commit=False)

            # Consider doing Markdown conversion in the template
            # chapter.context = markdown2.markdown(chapter.context)

            chapter.save()

            # Handle multiple files
            for file in request.FILES.getlist('files'):
                try:
                    chapter.files.create(file=file)
                except Exception as e:
                    # Handle file creation error (e.g., file size exceeded, etc.)
                    print(f"Error creating file: {e}")

            form.save_m2m()  # Save many-to-many fields, if any
            return redirect('create_chapters')
    else:
        form = ChapterForm()

    return render(request, 'create_genre.html', {'form': form})

def chapter_detail(request, chapter_name):
    chapter = get_object_or_404(Chapter, name=chapter_name)
    return render(request, 'chapter_detail.html', {'chapter': chapter})
