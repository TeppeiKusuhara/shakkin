from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "money", "memo")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "記入例:楠原　鉄平"}),
            "money": forms.NumberInput(attrs={"min": 0}),
            "memo": forms.Textarea(attrs={"rows": 4}),
        }
