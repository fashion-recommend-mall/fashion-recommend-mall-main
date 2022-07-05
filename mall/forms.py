from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "검색창",
                "class": "search-input"
            }
        ))