from django.urls import path

from . import views

# we use path function from django to specify url and view for this url

# below we did the urlconf -> url configuration
urlpatterns = [
    path("", views.index, name="index"),  # /challenges/
    # path("january", views.january),
    # path("february", views.february),
    # dynamic part
    path("<int:month>", views.monthly_challenge_by_number),
    # by giving name to urls we can create path from it using reverse in views
    # below month refer to argument which will appended to month-challenge = /challenges/
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
