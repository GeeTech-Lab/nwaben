from cloudinary.forms import CloudinaryFileField
from django.forms import forms
from burial_memories.models import BurialMemory, FamilyTree, MemoryGallery, MemoryTribute, Donation


class BurialMemoryForm(forms.ModelForm):

    class Meta:
        model = BurialMemory
        fields = (
            "title",
            "first_name",
            "last_name",
            "other_names",
            "image",
            "gender",
            "date_of_birth",
            "date_of_death",
            "place_of_birth",
            "place_of_death",
            "burial_ceremony_address",
            "cause_of_death",
            "brief_biography",
            "education",
            "work_life",
            "family_biography",
        )
        # widgets = {
        #     'content': SummernoteWidget(),
        # }


class MemoryGalleryForm(forms.ModelForm):

    class Meta:
        model = MemoryGallery
        fields = (
            "description",
            "image",
        )
        # image = CloudinaryFileField(options={'folder': 'media/photos/', 'tags': 'landscapes'})


class FamilyTreeForm(forms.ModelForm):

    class Meta:
        model = FamilyTree
        fields = (
            "title",
            "full_name",
            "image",
            "relationship",
        )


class MemoryTributeForm(forms.ModelForm):

    class Meta:
        model = MemoryTribute
        fields = (
            "tribute_text",
            "category",
        )


class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = (
            "donor_fullname",
            "amount",
        )
