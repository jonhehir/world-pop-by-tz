from datetime import datetime
from typing import List

import pytz


class Timezone:
    """
    This is really a wrapper around `tzinfo`.
    """
    def __init__(self, name):
        self.tzinfo = pytz.timezone(name)
    
    @staticmethod
    def all():
        return [Timezone(i) for i in pytz.all_timezones]
    
    def _offset_at_date(self, month, day) -> int:
        dt = datetime(datetime.today().year, month, day)
        return int(self.tzinfo.utcoffset(dt).total_seconds() // 60)

    @property
    def winter_offset(self) -> int:
        """
        Minutes from UTC at January 1
        """
        return self._offset_at_date(1, 1)

    @property
    def summer_offset(self) -> int:
        """
        Minutes from UTC at July 1
        """
        return self._offset_at_date(7, 1)
    
    @property
    def iana_name(self) -> str:
        return str(self.tzinfo)
