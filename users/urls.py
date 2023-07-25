from django.urls import path
from .views import RegisterView, VerifyEmail, RecruiterRegisterView, CandidateRegisterView, LoginAPIView, LogOutView, PasswordTokenConfirmView, RequestPasswordResetEmailView, SetNewPasswordView, VerifyRecruiterEmail, RecruiterLoginAPIView, RecruiterRequestPasswordResetEmailView, RecruiterPasswordTokenConfirmView, RecruiterSetNewPasswordView, RecruiterLogOutView


app_name = 'users'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_user"),
    path("verify-email/", VerifyEmail.as_view(), name="verify-email"),
    path("login/", LoginAPIView.as_view(), name="login_user"),
    path("register/candidate/", CandidateRegisterView.as_view(), name="candidate_register"),
    path("request-password-reset-email/", RequestPasswordResetEmailView.as_view(), name="request_password_reset_email"),
    path("password-reset/<uidb64>/<token>/", PasswordTokenConfirmView.as_view(), name="password_reset"),
    path("password-reset-completed/", SetNewPasswordView.as_view(), name="password_reset_completed"),
    path("logout/", LogOutView.as_view(), name="logout_user"),
    # -----------------Recruiter Url----------------
    path("register/recruiter/", RecruiterRegisterView.as_view(), name="recruiter_register"),
    path("verify-recruiter-email/", VerifyRecruiterEmail.as_view(), name="verify_recruiter_email"),
    path("login-recruiter/", RecruiterLoginAPIView.as_view(), name="login_recruiter"),
    path("recruiter-request-password-reset-email/", RecruiterRequestPasswordResetEmailView.as_view(), name="recruiter_request_password_reset_email"),
    path("recruiter-password-reset/<uidb64>/<token>/", RecruiterPasswordTokenConfirmView.as_view(), name="recruiter-password_reset"),
    path("recruiter-password-reset-completed/", RecruiterSetNewPasswordView.as_view(), name="recruiter_password_reset_completed"),
    path("logout-recruiter/", RecruiterLogOutView.as_view(), name="logout_recruiter"),

]