import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.base import View

from burial_memories.flutterwave import FLUTTERWAVE_PUBLIC_KEY
from burial_memories.models import BurialMemory, MemoryGallery, FamilyTree, MemoryTribute, Donation


class BurialMemoryList(ListView):
    model = BurialMemory
    context_object_name = "burial_memories"
    template_name = "burial_memories/list.html"


class BurialMemoryDetail(DetailView):
    model = BurialMemory
    context_object_name = "burial_memory"
    template_name = "burial_memories/detail.html"

    def get_context_data(self, **kwargs):
        context = super(BurialMemoryDetail, self).get_context_data(**kwargs)
        context["pub_key"] = FLUTTERWAVE_PUBLIC_KEY
        context["galleries"] = MemoryGallery.objects.filter(burial_memory=self.get_object())
        context["donations"] = self.get_object().donations.all()
        context["tributes"] = self.get_object().memory_tributes.all()
        return context


class BurialMemoryCreate(LoginRequiredMixin, CreateView):
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
    # success_url = reverse_lazy("burial_memories:list")
    template_name = "burial_memories/form.html"

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse("burial_memories:list")


class BurialMemoryUpdate(LoginRequiredMixin, UpdateView):
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
    template_name = "burial_memories/form.html"

    def get_success_url(self, **kwargs):
        memorial = BurialMemory.objects.get(by=self.request.user)
        return reverse("burial_memories:update", memorial.slug)


class BurialMemoryDelete(LoginRequiredMixin, DeleteView):
    model = BurialMemory
    success_url = reverse_lazy("burial_memories:list")


class GalleryView(View):
    def get(self, request, slug):
        get_memory = get_object_or_404(BurialMemory, slug=slug)
        context = {
            'memory': get_memory,
        }
        return render(request, 'burial_memories/gallery_list.html', context)

    def post(self, request):
        return render(request, 'burial_memories/gallery_list.html')


def list_gallery(request, slug):
    get_memory = get_object_or_404(BurialMemory, slug=slug)
    print(get_memory.get_name)
    galleries = get_memory.galleries.all()
    description = request.POST.get("description")
    image = request.FILES.get("memory_image")  # if True else None
    video = request.FILES.get("memory_video")  # if True else None
    audio = request.FILES.get("memory_audio")  # if True else None
    gallery = MemoryGallery.objects.create(
        by=request.user,
        burial_memory=get_memory,
        description=description,
        image=image,
        video=video,
        audio=audio,
    )
    get_memory.galleries.add(gallery)
    context = {
        'get_memory': get_memory,
        'galleries': galleries,
    }
    return render(request, 'burial_memories/gallery_list.html', context)


def add_tribute(request, slug):
    get_memory = get_object_or_404(BurialMemory, slug=slug)
    tribute_text = request.POST.get("tribute")
    get_category = request.POST.get("category")
    category = None
    if get_category == "candle":
        category = "candle"
    elif get_category == "flower":
        category = "flower"
    elif get_category == "note":
        category = "note"
    print(category)
    tribute = MemoryTribute.objects.create(
        burial_memory=get_memory,
        tribute_text=tribute_text,
        by=request.user,
        category=category,
        on=datetime.datetime.now(),
    )
    get_memory.memory_tributes.add(tribute)
    tributes = get_memory.memory_tributes.all()
    context = {
        "tributes": tributes,
    }
    return render(request, "burial_memories/tribute_list.html", context)


def add_donation(request, slug):
    get_memory = get_object_or_404(BurialMemory, slug=slug)
    get_name = request.POST.get('name')
    get_tx_ref = request.POST.get('tx_ref')
    get_amount = request.POST.get('amount')
    get_status = request.POST.get('status')
    donation = Donation.objects.create(
        burial_memory=get_memory,
        donor_fullname=get_name,
        status=get_status,
        trans_ref=get_tx_ref,
        amount=get_amount,
    )
    get_memory.donations.add(donation)
    messages.success(request, "Donation added successfully")
    return render(request, "burial_memories/donation_list.html")


def list_donations(request, slug):
    get_memory = get_object_or_404(BurialMemory, slug=slug)
    donations = get_memory.donations.all()
    return render(request, "burial_memories/donation_list.html", {'donations': donations})
