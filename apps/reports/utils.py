from datetime import datetime
import pytz

from zundapp.settings.base import TIME_ZONE


def parse_datetime(s):
    """ Returns timezone aware datetime object (tz=utc).

    :param s: String representation of datetime object including a timezone (e.g. Fri May 17 13:49:45 CEST 2013)
    :type s: string
    :returns: datetime
    """
    naive = datetime.strptime("{} {}".format(" ".join(s.split()[:-2]), "".join(s.split()[-1:])), '%a %b %d %H:%M:%S %Y')
    local = pytz.timezone(TIME_ZONE)
    local_dt = local.localize(naive, is_dst=None)

    return local_dt.astimezone(pytz.utc)


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    import os
    from django.core.exceptions import ImproperlyConfigured

    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
    raise ImproperlyConfigured(error_msg)