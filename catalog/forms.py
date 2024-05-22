from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        restricted_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        if cleaned_data.lower() in restricted_words:
            raise forms.ValidationError("Присутствуют запрещенные слова в названии")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        restricted_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        if cleaned_data.lower() in restricted_words:
            raise forms.ValidationError("Присутствуют запрещенные слова в описании")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
