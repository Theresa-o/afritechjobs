from django.urls import path
from .views import RegisterView, VerifyEmail, RecruiterRegisterView, CandidateRegisterView, LoginAPIView


app_name = 'users'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_user"),
    path("verify-email/", VerifyEmail.as_view(), name="verify-email"),
    path("login/", LoginAPIView.as_view(), name="login_user"),
    path("register/recruiter/", RecruiterRegisterView.as_view(), name="recruiter_register"),
    path("register/candidate/", CandidateRegisterView.as_view(), name="candidate_register"),




]