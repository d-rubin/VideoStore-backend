from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        "current_user": reset_password_token.user,
        "username": reset_password_token.user.username,
        "email": reset_password_token.user.email,
        "reset_password_url": "{}?token={}".format(
            instance.request.build_absolute_uri(reverse("password_reset:reset-password-confirm")),
            reset_password_token.key)
    }

    reset_password_url = context.get("reset_password_url")

    send_mail(
        "Reset Password",
        f"""ou successfully requested a reset of your password.\n
        To do so click this link\n
        {reset_password_url}""",
        "videoflix@daniel-rubin.de",
        [reset_password_token.user.email],
    )
