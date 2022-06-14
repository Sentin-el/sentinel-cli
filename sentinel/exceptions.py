import traceback

import psutil


class PsUtilError(Exception):
    def __init__(self, e: Exception, message=None):
        self.message = message or "psutil configuration/installation error"
        super(PsUtilError, self).__init__(self.message)
