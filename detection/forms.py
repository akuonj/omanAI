from django import forms

from .models import ImageDetection


class ImageDetectionForm(forms.ModelForm):

    class Meta:

        model = ImageDetection

        fields = ['uploaded_image']


    def clean_uploaded_image(self):

        uploaded_image = self.cleaned_data.get('uploaded_image')


        if not uploaded_image:

            raise forms.ValidationError('This field is required.')


        return uploaded_image

