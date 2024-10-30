from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

monthly_challenges = {
    "januar": "Become Backend Developer!",
    "februar": "Become Frontend Developer!",
    "märz": "May Allah Guide and Succeed you Ameen!",
    "april": "Learn Devops!",
    "mai": "Master Version Management",
    "juni": "Learn Data Engineering",
    "juli": None,
    "august": "Apply for jobs with effort",
    "september": "Start new job",
    "oktober": "Make effort to succeed in your job",
    "november": "Please stay consistent to job",
    "dezember": "Successful in job",
}


# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


# 302 -> redirect response
def monthly_challenge_by_number(request, month):
    # list of months from keys
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenges/januar -> nonth-challenge refers to /challenges args refer to month will appended to this
    return HttpResponseRedirect(redirect_path)


# second parameter need to same as in urls.
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month},
        )
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # we can't use render method because it is used for success response
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        # Http404 used like to raise an error and automatically looks 404.html in root templates folder we don't need to pass it

        raise Http404()
