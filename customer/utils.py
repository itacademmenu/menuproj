import datetime

from authentication.models import User


def time_checker(start_hour, end_hour):
    current_time = datetime.datetime.now()
    start_hour = current_time.replace(hour=start_hour, minute=0, second=0)
    end_hour = current_time.replace(hour=end_hour, minute=0, second=0)
    if start_hour < current_time < end_hour:
        return True
    else:
        return False


def get_email(request):
    superusers_email = User.objects.filter(is_superuser=True).values_list('email')
    email = superusers_email[0]
    mail = email[0]
    return mail

superusers_emails = User.objects.filter(is_superuser=True).values_list('email')
dic_mail = superusers_emails[0]
email = dic_mail[0]