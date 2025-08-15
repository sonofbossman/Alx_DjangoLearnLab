from django import forms

class FeedbackForm(forms.Form):
  name = forms.CharField(max_length=50)
  email = forms.EmailField()
  rating = forms.IntegerField(min_value=1, max_value=5)
  comments = forms.CharField(widget=forms.Textarea)

  def clean_rating(self):
    rating = self.cleaned_data.get('rating')
    if rating not in range(1, 6):
      raise forms.ValidationError("Rating should be between 1-5!")
    return rating