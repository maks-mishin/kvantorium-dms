from django import forms


class DocumentForm(forms.Form):
    file = forms.FileField(label='')
    file.widget.attrs.update(
        {
            'class': 'form-control',
            'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;'
        }
    )
