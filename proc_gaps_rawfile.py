'''
Created on Jun 27, 2018

@author: karsu
'''

'''
    1. rename the gap files as:
        finviz_gapup and finviz_gapdown
    2. Open finviz_gapup, move all the fields to MS Access Table fields
    3. set GapType = "Up" in the MSA table
    4. Get today's date, display on the console and ask user to change if needed
    5. move the date to TrDate field on MSA table
    6. Get time from the 'file created' time
    7. move the date to TrDate field on MSA table
    8. insert the record into MSA table for all CSV records
    9. do the same for GapDown
    
'''

import os
import pyodbc
import csv
import db_utils as dbu
import datetime

def write_records(gap_file, gaptype, fdate, ftime):
    
    def init_outrec():
        outrec = {
            'Ticker': None,
            'TrDate':None,
            'ExtractTime':None,
            'GapType':None,
            'Price':None,
            'CurDayChg':None,
            'ChgFrmOpen':None,
            'Gap':None,    
            'Volume': None,
            'Beta':None,
            'AvgTrueRange':None,
            'SMV20D':None,
            'SMV50D':None,
            'SMV200D':None,
            'Hi52Wks':None,
            'Lo52Wks':None,
            'RelStr':None
        }
        return outrec
    
#    gap_file = "C:\\Users\\karsu\\Downloads\\finviz_gapup.csv"
    d = str(datetime.datetime.fromtimestamp(os.stat(gap_file)[8]))
    if (fdate):
        file_date = fdate
    else:
        file_date = d.split(' ')[0]
        
    if(ftime):
        file_time = ftime
    else:       
        file_time = d.split(' ')[1]
    
    
    gaps = csv.reader(open(gap_file, 'r'), delimiter=',')
    
    inrec = []
    lineNo = 1
    outrec = init_outrec()
    
    db_file = 'FinvizGapAnalysis.accdb'  #raw string, escape sequences are ignored
    db_file = os.path.abspath(db_file)    
    conn = dbu.createDBConnection(db_file)
    table_name = "tblRawFromFinviz"
    #print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    
    
    for gap in gaps:
        if (lineNo == 1):
            lineNo = lineNo + 1
            continue
        for i in range(len(gap)):
            if gap[i]:
                pass
            else:
                gap[i] = None
                
        outrec['Ticker'] = gap[1]
        outrec['TrDate'] = file_date
        outrec['ExtractTime'] = file_time
        outrec['GapType'] = gaptype
        outrec['Price'] = gap[10]
        outrec['CurDayChg'] = gap[11][:-1]
        outrec['ChgFrmOpen'] = gap[12][:-1]
        outrec['Gap'] = gap[13][:-1]
        outrec['Volume'] = gap[14]
        outrec['Beta'] = gap[2]
        outrec['AvgTrueRange'] = gap[3]
        outrec['SMV20D'] = gap[4][:-1]
        outrec['SMV50D'] = gap[5][:-1]
        outrec['SMV200D'] = gap[6][:-1]
        outrec['Hi52Wks'] = gap[7][:-1]
        outrec['Lo52Wks'] = gap[8][:-1]
        outrec['RelStr'] = gap[9]
        dbu.insert_recs(conn, table_name, outrec)
        
    
#        print(gap)
    

