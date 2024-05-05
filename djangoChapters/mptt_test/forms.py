# forms.py
from django import forms
from .models import Chapter
from multiupload.fields import MultiFileField

class ChapterForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        required=False,
        queryset=Chapter.objects.filter(parent__isnull=True),
        empty_label="Create a new root chapter",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    context = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,
        help_text="Enter the context for the chapter (optional)"
    )

    # Use MultiFileField with MultiFileInput for multiple file uploads
    files = MultiFileField(max_file_size=1024 * 1024 * 5, required=False)

    class Meta:
        model = Chapter
        fields = ['name', 'parent', 'context', 'files']
