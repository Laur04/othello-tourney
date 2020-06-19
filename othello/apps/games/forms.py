from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

from ...sandboxing import import_strategy_sandboxed
from .models import Submission


class SubmissionForm(forms.ModelForm):
    name = forms.CharField(required=False)

    class Meta:
        model = Submission
        fields = (
            "name",
            "code",
        )

    def clean(self):
        cd = self.cleaned_data
        if "code" not in cd:
            raise ValidationError("Please upload a non-empty Python file!")
        if not cd["name"]:
            cd["name"] = cd["code"].name
        if (errs := import_strategy_sandboxed(cd["code"].temporary_file_path())) != 0:
            raise ValidationError(errs["message"])

        return cd


def _get_submission_name(obj):
    return obj.get_submission_name()


def _get_game_name(obj):
    return obj.get_game_name()


class DownloadSubmissionForm(forms.Form):
    script = forms.ModelChoiceField(label="Previous Submissions:", queryset=None,)

    def __init__(self, user, *args, **kwargs):
        super(DownloadSubmissionForm, self).__init__(*args, **kwargs)
        choices = Submission.objects.filter(user=user).order_by("-created_at")
        self.fields["script"].queryset = choices
        self.fields["script"].initial = choices.first()
        self.fields["script"].label_from_instance = _get_submission_name


class GameForm(forms.Form):
    choices = Submission.objects.latest()
    black = forms.ModelChoiceField(label="Black:", queryset=choices, initial="Yourself")
    white = forms.ModelChoiceField(label="White:", queryset=choices, initial="Yourself")
    time_limit = forms.IntegerField(
        label="Time Limit (secs):", initial=5, min_value=1, max_value=settings.MAX_TIME_LIMIT
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["black"].label_from_instance = _get_game_name
        self.fields["white"].label_from_instance = _get_game_name
