#!/usr/bin/env python3

"""
Court_Calendar.py: application that is designed to process Watauga County 
Court Calendar documents to produce a csv representation of the data.

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

import Court_Entry as CE

#Constants
H_END = "*" * 85
PAGE_HEADER_INDICATOR = "no."

#Method that initializes process to dissect a Watauga county court calender 
#into a csv file.
def court_file_to_csv_data(raw_file, out_file, col_names):

    data_file = open(raw_file, "r")

    #process header and save relevant information
    header_info = read_report_header(data_file)

    #process all records and save in a list
    records = read_court_records(data_file)

    data_file.close

    #print records to csv
    print_as_csv(out_file, col_names, header_info, records)

    print("A csv file named " + out_file + " has been created.")


#Reads the main header  
def read_report_header(data_file):

    run_date = "run date:"
    location = "location:"
    county = "county of"
    court_date = "court date:"
    time = "time:"
    courtroom_num = "courtroom number:"

    while(True):
        line = data_file.readline()
        line = line.lower()

        if line.find(run_date) != -1:
            start = line.find(run_date) + len(run_date)
            end = start + 9
            run_date = line[start : end]
        if line.find(location) != -1:
            start = line.find(location) + len(location)
            end = start + 12
            location = line[start : end]
        if line.find(county) != -1:
            start = line.find(county) + len(county)
            end = start + 8
            county = line[start : end]
        if line.find(court_date) != -1:
            start = line.find(court_date) + len(court_date)
            end = start + 9
            court_date = line[start : end]
        if line.find(time) != -1:
            start = line.find(time) + len(time)
            end = start + 9
            time = line[start : end]
        if line.find(courtroom_num) != -1:
            start = line.find(courtroom_num) + len(courtroom_num)
            end = start + 5
            courtroom_num = line[start : end]
        if(line.find(H_END)) != -1:
            break

    return (run_date, location, county, court_date, time, courtroom_num)


#Handles all court records assuming that the header has been processed first.
def read_court_records(opened_file):
    records = []

    while(True):
        line = opened_file.readline().rstrip("\n")
        line = line.lower()

        if is_summary_start(line):
            break
        if(line == "\n" or line == ""):
            continue
        if is_page_header(line):
            continue

        if line[5].isdigit():
            court_record = new_court_record(opened_file, line)
            records.append(court_record)
        elif line.find("bond") != -1:
            add_bond(line, court_record)
        elif line.find("fingerprinted") != -1:
            court_record.need_fingerprint()
        elif line.find("check digit") != -1:
            court_record.missing_check_digit()
        elif line.find("(") != -1:
            offense_start_index = line.find(")") + 1
            offense_end_index = line.find("plea:")
            offense = line[offense_start_index : offense_end_index]
            offense = offense.rstrip()
            court_record.add_offense(offense)

    return records


#Checks for the start of summary assuming the header has been processed.
def is_summary_start(line):
    line = line.lower()

    if line.find("run date:") != -1:
        return True
    else:
        return False



#Tells if the line is a page header used after the main header is processed.
def is_page_header(line):
    line = line.lower()

    if line.find(PAGE_HEADER_INDICATOR) != -1:
        return True
    elif line.find(H_END) != -1:
        return True
    elif line.find("page:") != -1:
        return True
    elif line.find("court date:") != -1:
        return True
    else:
        return False


#Creates a new court records.
def new_court_record(file, line):
    line = line.lower()
    data = line.split(" ")
    empty_string_cnt = data.count("")

    for i in range(empty_string_cnt):
        data.remove("")

    entry = CE.Court_Entry(data[1], data[2], data[3], data[4])

    if len(data) > 5:

        for i in range(5, len(data)):
            if data[i].find(":") != -1:
                data_line = data[i]
                start_atty_name = data[i].find(":") + 1
                
                if data[i].find("apt") != -1:
                    entry.add_attorney(data_line[start_atty_name : len(data[i]) - 1], 1)
                else:
                    entry.add_attorney(data_line[i][start_atty_name : len(data[i]) - 1], 0)
        
            elif len(data[i]) == 3:
                    entry.add_police_group(data[i])
            elif i == len(data) - 1:
                    entry.add_cont(data[i])
    
    return entry


#adds bond information a watauga county calendar record.
def add_bond(line, record):
    line = line.lower()
    data = line.split(" ")
    empty_string_cnt = data.count("")
    out = ""

    for i in range(empty_string_cnt):
        data.remove("")

    for i in range(1, len(data)):
        out = out + data[i]
        
    record.add_bond(out)


#Takes a desired output file name along with column names, header information,
#and watauga data records and prints them in csv format.
def print_as_csv(out_file, col_names, header_info, records):

    out = open(out_file, "w+")
    d = "," #delimiter
    col_names_csv_str = ""

    #prepare and write column names
    for i in range(len(col_names) - 1):
        col_names_csv_str += "\"" + col_names[i] + "\"" + d

    col_names_csv_str += "\"" + col_names[len(col_names) - 1] + "\"" + "\n"
    out.write(col_names_csv_str)

    #prepare and write records for each offense
    for r in records:
        
        header_csv_str = ""

        for data in header_info:
            header_csv_str += "\"" + data + "\"" + d

        csv_str = header_csv_str + r.file_id + d +  r.num + d + "\"" + r.def_name + "\"" + d + "\"" + r.com_name + "\"" \
            + d + r.police_abbrev + d + "\"" + r.attorney + "\"" + d + r.appointed + d + r.cont + d + \
                "\"" + r.bond + "\"" + d + r.need_fingerprinting + d + r.need_check_digit

        #print a record for each offense.
        for offense in r.get_offenses():
            csv_str_off = csv_str + d + "\"" + offense + "\""
            out.write(csv_str_off + "\n")

    out.close




    
 

