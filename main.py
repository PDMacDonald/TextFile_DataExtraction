#!/usr/bin/env python3

"""
main.py: Create an application capable of dissecting Watauga County Criminal 
Court Calendar text files and converting the data into a CSV record set for 
analysis. The application should extract all possible data from the calendar 
including the date and time of the hearing, as well as the courtroom in which
it is scheduled. Each offense charged should appear as an individual complete
record in the final file.
When complete, you should be able to open the output file in Excel to answer 
questions such as:
What is the most charged offense in the county?
How many drug charges were brought during the period?
What is the average bond for drug possession?

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


import Court_Calendar as CC


raw_court_file_1 = "DISTRICT.DISTRICT_COURT_.04.03.19.txt"
raw_court_file_2 = "DISTRICT.DISTRICT_COURT_.04.04.19.txt"
out_file_name_1 = "Court_Data_04_03_19.csv"
out_file_name_2 = "Court_Data_04_04_19.csv"

#column names for the Watauga County Court Calendar specifically.
col_names = []
col_names.append("run_date")
col_names.append("location")
col_names.append("county")
col_names.append("court_date")
col_names.append("time")
col_names.append("courtroom_num")
col_names.append("file_id")
col_names.append("file_num")
col_names.append("defendent_name")
col_names.append("complaintant_name")
col_names.append("police_abbrev")
col_names.append("attorney")
col_names.append("attorney_appointed")
col_names.append("cont")
col_names.append("bond")
col_names.append("need_fingerprinting")
col_names.append("need_check_digit")
col_names.append("offense")

#Dissect Watauga Calendar records to produce a csv file.
CC.court_file_to_csv_data(raw_court_file_1, out_file_name_1, col_names)
CC.court_file_to_csv_data(raw_court_file_2, out_file_name_2, col_names)

