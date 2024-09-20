from django import forms
from .models import *

# 重新定义部件MultipleFileInput
class MultipleFileInput(forms.ClearableFileInput):
    # 设置允许多文件上传
    allow_multiple_selected = True

# 重新定义表单字段FileField
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
class PersonInfoForm(forms.ModelForm):
    certificate = MultipleFileField(label='证件', allow_empty_file=True)
    class Meta:
        model = PersonInfo
        fields = '__all__'
        labels = {
            'name': '名字',
            'age': '年龄',
        }