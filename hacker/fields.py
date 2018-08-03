from django import forms

from django.db import models
from django_countries.fields import CountryField as OriginalCountryField
from django_countries.fields import Country

from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class CountryField(OriginalCountryField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    def from_db_value(self, value, expression, connection, context):
        return self.get_clean_value(value)

    def to_python(self, value):
        return self.get_clean_value(value)


class ShirtSizeField(models.CharField):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"

    SHIRT_CHOICES = (
        (XS, "EXtra Small (XS)"),
        (S, "Small (S)"),
        (M, "Medium (M)"),
        (L, "Large (L)"),
        (XL, "Extra Large (XL)"),
    )

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 4
        kwargs['choices'] = ShirtSizeField.SHIRT_CHOICES
        kwargs['default'] = ShirtSizeField.M
        super(ShirtSizeField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ShirtSizeField, self).deconstruct()
        del kwargs["max_length"]
        del kwargs['choices']
        del kwargs['default']
        return name, path, args, kwargs

class PhoneField(PhoneNumberField):
    def formfield(self, **kwargs):
        defaults = {'widget': PhoneNumberInternationalFallbackWidget()}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'

        return (text_html + data_list)

class FuzzyChoiceField(models.CharField):
    def __init__(self, data=None, *args, **kwargs):
        self.data = data
        super().__init__(*args, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'widget': ListTextWidget(self.data, self.name)}
        defaults.update(kwargs)
        return super().formfield(**defaults)
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.data is not None:
            kwargs['data'] = self.data
        return name, path, args, kwargs

class DegreeField(models.CharField):
    BACHELOR_ARTS = 'ba'
    BACHELOR_SCIENCE = 'bsc'
    MASTER_ARTS = 'ma'
    MASTER_SCIENCE = 'msc'
    PHD = 'phd'
    MBA = 'mba'

    DEGREE_CHOICES = (
        (BACHELOR_SCIENCE, 'Bachelor of Science'),
        (BACHELOR_ARTS, 'Bachelor of Arts'),
        (MASTER_SCIENCE, 'Master of Science'),
        (MASTER_ARTS, 'Master of Arts'),
        (PHD, 'PhD'),
        (MBA, 'MBA'),
    )

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 3
        kwargs['choices'] = DegreeField.DEGREE_CHOICES
        kwargs['default'] = DegreeField.BACHELOR_SCIENCE
        super(DegreeField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(DegreeField, self).deconstruct()
        del kwargs["max_length"]
        del kwargs["default"]
        del kwargs['choices']
        return name, path, args, kwargs


class YearField(models.IntegerField):
    C_2016 = 2016
    C_2017 = 2017
    C_2018 = 2018
    C_2019 = 2019
    C_2020 = 2020
    C_2021 = 2021
    C_2022 = 2022
    C_2023 = 2023
    CLASS_CHOICES = (
        (C_2016, '2016 (or before)'),
        (C_2017, '2017'),
        (C_2018, '2018'),
        (C_2019, '2019'),
        (C_2020, '2020'),
        (C_2021, '2021'),
        (C_2022, '2022'),
        (C_2023, '2023 (or later)'),
    )

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = YearField.CLASS_CHOICES
        kwargs['default'] = YearField.C_2018
        super(YearField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(YearField, self).deconstruct()
        del kwargs['choices']
        del kwargs['default']
        return name, path, args, kwargs


class UniField(models.CharField):
    # TODO: Update this list
    JACOBS = "JACOBS"
    OTHER = "OTHER"

    UNI_CHOICES = (
        (JACOBS, "Jacobs University"),
        (OTHER, "Other")
    )

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 25
        kwargs['choices'] = UniField.UNI_CHOICES
        kwargs['default'] = UniField.OTHER
        super(UniField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(UniField, self).deconstruct()
        del kwargs["max_length"]
        del kwargs['choices']
        del kwargs['default']
        return name, path, args, kwargs