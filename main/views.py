from django.shortcuts import render, redirect
from .forms import ProjectForm

def home(request):
    return render(request, 'base.html')

def about(request):
    sections = [
        {
            "title": "Who We Are",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "image": "../static/church1.jpg",
        },
        {
            "title": "What We Do",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "image": "../static/church2.jpg",
        },
        {
            "title": "Where We Are",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "image": "../static/church2.jpg",
        },
        {
            "title": "Our Journey",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "image": "../static/church2.jpg",
        },
        {
            "title": "Our Vision",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "image": "../static/church2.jpg",
        },
        {
            "title": "Our Social Media Presence",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "image": "../static/church2.jpg",
        },
    ]

    context = {
        'sections': sections,
    }

    return render(request, 'about.html', context)

def programs(request):
    # Define the context for course items
    courses = [
        {
            "title": "Digging Deep / Mid-week Service",
            "date": "Every Wednesday",
            "time": "7:30pm-8:30pm",
            "link": "#",  # Add the appropriate URL for the link
        },
        {
            "title": "Another Program",
            "date": "Every Thursday",
            "time": "6:00pm-7:00pm",
            "link": "#",  # Add the appropriate URL for the link
        },
        {
            "title": "Another Program",
            "date": "Every Thursday",
            "time": "6:00pm-7:00pm",
            "link": "#",  # Add the appropriate URL for the link
        },
        {
            "title": "Another Program",
            "date": "Every Thursday",
            "time": "6:00pm-7:00pm",
            "link": "#",  # Add the appropriate URL for the link
        },
        {
            "title": "Another Program",
            "date": "Every Thursday",
            "time": "6:00pm-7:00pm",
            "link": "#",  # Add the appropriate URL for the link
        },
        {
            "title": "Another Program",
            "date": "Every Thursday",
            "time": "6:00pm-7:00pm",
            "link": "#",  # Add the appropriate URL for the link
        },
        {
            "title": "Another Program",
            "date": "Every Thursday",
            "time": "6:00pm-7:00pm",
            "link": "#",  # Add the appropriate URL for the link
        },
    ]

    context = {
        "courses": courses,
    }

    return render(request, 'programs.html', context)

def projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, save to the database or send an email
            return redirect('success')  # Redirect to a success page or similar
    else:
        form = ProjectForm()

    return render(request, 'projects.html', {'form': form})