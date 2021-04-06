"""Provides different types of tool to help the other modules"""

import time
import datetime

class Tools:
    """Provides tools that will help to operate with data
    """

    def get_time(self):
        """Returns mktime of current time"""
        return time.mktime(time.localtime())

    def get_iso_time(self, mktime):
        """Returns isoformat from mktime

        Args:
            mktime (int): mktime to be converted

        Returns:
            str: mktime in isoformat
        """
        return datetime.datetime.fromtimestamp(mktime).isoformat()
