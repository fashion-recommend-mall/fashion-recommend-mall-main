from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "검색창",
                "class": "search-input"
            }
        ))

class UploadFileForm(forms.Form):
    '''
    Title : UploadFileForm
    This form is used in index templates to upload barcode image
    Attributes:
        file (file) : this is file field
    '''
    file = forms.FileField()