#!/usr/bin/env python3

"""
Court_Entry.py: a class used in Court_calendar to store attributes and
functions associated with a Wautaga county court entry.

CIS3680-101 
Programming Assignment
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonald"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Complete"

class Court_Entry:
    """
    Class to represent a court entry. You must provide a FILE NUMBER, 
    DEFENDANT NAME, COMPLAINANT, and ATTORNEY 
    """

    def __init__(self, file_id, num, defendent, complainant):
        self.file_id = file_id
        self.num = num
        self.def_name = defendent
        self.com_name = complainant
        self.attorney = ""
        self.police_abbrev = ""
        self.appointed = "No"
        self.cont = ""
        self.bond = ""
        self.need_fingerprinting = "No"
        self.need_check_digit = "No"
        self._offenses = []

    def add_attorney(self, attorney, apt):
        self.attorney = attorney
        if apt == 1:
            self.appointed = "Yes"
        else:
            self.appointed = "No"
    
    def add_police_group(self, police_abbrev):
        self.police_abbrev = police_abbrev
    
    def add_cont(self, cont):
        self.cont = cont

    def add_bond(self, bond):
        self.bond = bond

    def need_fingerprint(self):
        self.need_fingerprinting = "Yes"
    
    def missing_check_digit(self):
        self.need_check_digit = "Yes"

    def add_offense(self, offense):
        self._offenses.append(offense)
    
    def get_offenses(self):
        return self._offenses

    #for testing
    def __str__(self):
        return "file id:{0}\nfile number:{1}\ndefendent:{2}\ncomplainant:{3}\nattorney:{4}\n \
                attorney_appointed:{5}\npolice dept:{6}\ncont:{7}\nbond:{8}\nneed fingerprint:{9}\n \
                need check digit:{10}\noffenses:{11}".format(self.file_id, self.num, self.def_name, self.com_name, \
                self.attorney, self.appointed, self.police_abbrev, self.cont, self.bond, self. need_fingerprinting, \
                self.need_check_digit, self._offenses)

    
#End class student