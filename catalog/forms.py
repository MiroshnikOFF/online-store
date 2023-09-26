from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError("Это запрещенный продукт!")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_current_version(self):
        is_current_version = self.cleaned_data.get('is_current_version')

        if is_current_version:
            existing_true_objects = Version.objects.filter(is_current_version=True)

            if self.instance.pk:
                existing_true_objects = existing_true_objects.exclude(pk=self.instance.pk)

            if existing_true_objects.exists():
                raise forms.ValidationError('Активная версия продукта уже существует!')

        return is_current_version


