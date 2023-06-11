from django.contrib.auth.models import AbstractUser
from django.db.models import CharField{% if cookiecutter.username_type == "email" %}, EmailField{% endif %}
from django.utils.translation import gettext_lazy as _
{%- if cookiecutter.username_type == "email" %}

from {{ cookiecutter.project_slug }}.users.managers import UserManager
{%- endif %}


class User(AbstractUser):
    """
    Default custom user model for {{cookiecutter.{{ cookiecutter.project_slug }}}}.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    {%- if cookiecutter.username_type == "email" %}
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    {%- endif %}
