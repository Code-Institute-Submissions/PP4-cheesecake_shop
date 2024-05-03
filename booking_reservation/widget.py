from django import forms


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TextInput):
    input_type = 'time'