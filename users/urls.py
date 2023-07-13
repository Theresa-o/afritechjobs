from django.urls import path
from .views import RegisterView, RecruiterRegisterView, CandidateRegisterView

app_name = 'users'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_user"),
    path("register/recruiter/", RecruiterRegisterView.as_view(), name="recruiter_register"),
    path("register/candidate/", CandidateRegisterView.as_view(), name="candidate_register"),
]