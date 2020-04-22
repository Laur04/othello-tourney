from django import forms

from ..models import Game, Submission


class GameForm(forms.Form):
    choices = Submission.objects.usable()
    black = forms.ModelChoiceField(label="Black:", queryset=choices, initial="Yourself")
    white = forms.ModelChoiceField(label="White:", queryset=choices, initial="Yourself")
    time_limit = forms.IntegerField(label="Time Limit (secs):", initial=5, min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['black'].label_from_instance = lambda obj: obj.get_user_name()
        self.fields['white'].label_from_instance = lambda obj: obj.get_user_name()


class WatchForm(forms.Form):
    games = forms.ModelChoiceField(label="Running Games:", queryset=Game.objects.running())