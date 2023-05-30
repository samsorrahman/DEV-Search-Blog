from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = 'Welcome to DevSearch'
        message = f"Dear {profile.name},\n\nWe are delighted to welcome you to DevSearch! It's a pleasure to have you on board.\n\n"

        message += "You can connect with us on various social media platforms:\n>"
        message += "- LinkedIn: <a href='https://www.linkedin.com/in/samsor-rahman18/'>CEO LinkedIn</a>\n>"
        message += "- GitHub: <a href='https://github.com/samsorrahman'>CEO GitHub</a>\n"
        message += "- Instagram: <a href='https://www.instagram.com/samsor_rahman'>CEO Instagram</a>\n"
        message += "- Twitter: <a href='https://twitter.com/samsor_rahman'>CEO Twitter</a>\n\n"

        message += "If you have any questions or need assistance, feel free to reach out to us.<br><br>"
        message += "Once again, welcome to DevSearch, and we wish you all the best in your journey!\n\n"
        message += "Best regards,\nDevSearch Team"
        send_mail(
            subject,
            '',
            settings.EMAIL_HOST_USER,
            [profile.email],
            html_message=message,
            fail_silently=False
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):

    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
