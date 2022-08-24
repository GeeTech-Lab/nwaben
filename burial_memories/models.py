import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from burial_memories.util import RELATIONSHIP
from nwaben.utils import unique_slug_generator


def upload_dir(instance, filename):
    return "{}/{}".format(instance.username, filename)


class BurialMemory(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )
    by = models.ForeignKey("accounts.User", related_name="memories", on_delete=models.CASCADE) # user.memories.all()
    title = models.CharField(help_text="Mr, Mrs, Miss, Sir....", max_length=100)
    first_name = models.CharField(help_text="John", max_length=100)
    last_name = models.CharField(help_text="Ezeh", max_length=100)
    other_names = models.CharField(help_text="Other titled names...", default="", max_length=100, null=True, blank=True)
    gender = models.CharField(help_text="Male/Female", max_length=100, default="Others", choices=GENDER, null=True, blank=True)
    slug = models.SlugField(unique=True)
    image = CloudinaryField(
        folder='Nwaben_Burial_Images',
        blank=True,
        null=True,
        help_text="The deceased image",
        transformation={"quality": "auto:eco"},
        resource_type="image",
    )
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    place_of_birth = models.CharField(help_text="City, State, Country", max_length=220, null=True, blank=True)
    place_of_death = models.CharField(help_text="City, State, Country", max_length=220, null=True, blank=True)
    cause_of_death = models.CharField(help_text="Sickness, Accident...", max_length=200, null=True, blank=True)
    brief_biography = models.TextField(help_text="Brief biography...", null=True, blank=True)
    education = models.TextField(help_text="Education...", null=True, blank=True)
    work_life = models.TextField(help_text="Work life...", null=True, blank=True)
    family_biography = models.TextField(help_text="Family's origin/history...", null=True, blank=True)
    burial_ceremony_address = models.CharField(help_text="Street, Town, City, State, Country", max_length=220, null=True, blank=True)
    donation_bank = models.CharField(help_text="Bank name", max_length=200, null=True, blank=True)
    donation_bank_account_num = models.CharField(help_text="Bank account number", max_length=10, null=True, blank=True)
    donation_bank_account_name = models.CharField(help_text="Bank account name", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.by.username} -> {self.title} {self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "BurialMemories"
        ordering = ("-created",)

    @property
    def get_name(self):
        return f"{self.title}-{self.first_name} {self.last_name}"
        
    @property
    def name(self):
        return f"{self.title}-{self.first_name}{self.last_name}-{self.pk}"

    @property
    def calculated_age(self):
        return self.date_of_death.year - self.date_of_birth.year - ((self.date_of_death.month, self.date_of_death.day)<(self.date_of_birth.month, self.date_of_birth.day))

    @property
    def image_url(self):
        if self.image:
            return f"{self.image.url}"
        return "https://res.cloudinary.com/geetechlab-com/image/upload/v1659898818/nwaben.com/daddy_heaven_3_m0xhos.jpg"


@receiver(pre_save, sender=BurialMemory)
def blog_pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_delete, sender=BurialMemory)
def burial_memory_image_delete(sender, instance, **kwargs):
    if instance.image:
        cloudinary.uploader.destroy(instance.image.public_id)


class MemoryGallery(models.Model):
    by = models.ForeignKey("accounts.User", related_name="galleries", on_delete=models.CASCADE, blank=True) # user.galleries.all()
    burial_memory = models.ForeignKey(BurialMemory, related_name="galleries", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, help_text="What was the event and where was it taken?...")
    image = CloudinaryField(
        folder='Nwaben_Burial_Images_Gallery',
        blank=True,
        null=True,
        help_text="The deceased memory image",
        transformation={"quality": "auto:eco"},
        resource_type="image",
        format="jpg"
    )
    video = CloudinaryField(
        folder='Nwaben_Burial_Video_Gallery',
        blank=True,
        null=True,
        help_text="The deceased memory video",
        transformation={"quality": "auto:eco"},
        resource_type="video",
        format="mp4",
    )
    audio = CloudinaryField(
        folder='Nwaben_Burial_Audio_Gallery',
        blank=True,
        null=True,
        help_text="The deceased memory audio",
        transformation={"quality": "auto:eco"},
        resource_type="audio",
        format="mp3",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.burial_memory.slug

    class Meta:
        verbose_name_plural = "MemoryGalleries"
        ordering = ("-created",)

    @property
    def image_url(self):
        if self.image:
            return f"{self.image.url}"
        return "https://res.cloudinary.com/dptrfsirm/image/upload/v1658601579/bg_logos/logo_dygcg3.png"

    @property
    def video_url(self):
        if self.video:
            return f"{self.video.url}"
        return "https://img.icons8.com/color/480/000000/video.png"

    @property
    def audio_url(self):
        if self.audio:
            return f"{self.audio.url}"
        return "https://img.icons8.com/color/480/000000/high-volume--v1.png"


@receiver(pre_delete, sender=MemoryGallery)
def memory_gallery_image_delete(sender, instance, **kwargs):
    if instance.image:
        cloudinary.uploader.destroy(instance.image.public_id)


class FamilyTree(models.Model):
    burial_memory = models.OneToOneField(BurialMemory, related_name="family_trees", on_delete=models.CASCADE)
    title = models.CharField(help_text="Mr, Mrs, Miss, Sir....", max_length=100)
    guest_full_name = models.CharField(help_text="full name(John Ezeh)...", max_length=100)
    user_full_name = models.ForeignKey("accounts.User", related_name="family_trees", on_delete=models.CASCADE, blank=True)
    image = CloudinaryField(
        folder='Nwaben_Family_Tree_Images',
        blank=True,
        null=True,
        help_text="The deceased memory image",
        transformation={"quality": "auto:eco"},
        resource_type="image",
    )
    relationship = models.CharField(help_text="Relationship with the deceased...", max_length=200, choices=RELATIONSHIP)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.full_name}"

    class Meta:
        verbose_name_plural = "FamilyTrees"
        ordering = ("-created",)

    def image_url(self):
        if self.image:
            return f"{self.image.url}"
        return "https://res.cloudinary.com/dptrfsirm/image/upload/v1658601579/bg_logos/logo_dygcg3.png"


@receiver(pre_delete, sender=FamilyTree)
def family_tree_image_delete(sender, instance, **kwargs):
    if instance.image:
        cloudinary.uploader.destroy(instance.image.public_id)


class MemoryTribute(models.Model):
    CATEGORY = (
        ("candle", "candle"),
        ("flower", "flower"),
        ("note", "note"),
    )
    burial_memory = models.ForeignKey(BurialMemory, related_name="memory_tributes", on_delete=models.CASCADE)
    tribute_text = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORY, default="candle")
    by = models.ForeignKey("accounts.User", related_name="tributes", on_delete=models.CASCADE)
    on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.by.username} {self.tribute_text[:10]}"


class Donation(models.Model):
    burial_memory = models.ForeignKey(BurialMemory, related_name="donations", on_delete=models.CASCADE)
    donor_fullname = models.CharField(help_text="Your fullname", max_length=200, blank=True, null=True)
    donor_email = models.CharField(help_text="Your email", max_length=200, blank=True, null=True)
    currency = models.CharField(help_text="curency type", max_length=200, default="NGN", blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    trans_ref = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=0.00, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.burial_memory_id} -> {self.donor_fullname} {self.amount}"
