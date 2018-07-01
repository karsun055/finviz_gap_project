'''
Created on Jun 28, 2018

@author: karsu
'''
from tkinter import *
import os, sys
import datetime
import time
from pandas.io.formats.printing import justify
import finviz_selenium as fviz
import proc_gaps_rawfile as gapraw
from tkinter import filedialog


class Main_process():
    def proc_pre_cleanup(self):
#        dwonload_dir_path = 'C:\\users\\karsu\\downloads\\'
#        gap_up_fn = dwonload_dir_path + 'finviz.csv'
        if os.path.isfile(self.gap_up_fn):
            os.remove(self.gap_up_fn)
#        gap_down_fn = dwonload_dir_path + 'finviz (1).csv'
        if os.path.isfile(self.gap_down_fn):
            os.remove(self.gap_down_fn)
        self.status_str.set("Job Status: Prev Day Gap Files are deleted")
#        self.status_str = StringVar(value="xyz: ")
                
    def get_finviz_files(self):
#        fviz.getfiles_from_finviz()
#        dwonload_dir_path = 'C:\\users\\karsu\\downloads\\'
#        gap_up_fn = dwonload_dir_path + 'finviz.csv'
        if os.path.isfile(self.gap_up_fn):
            self.upfilenameVar.set(self.gap_up_fn)
            d = str(datetime.datetime.fromtimestamp(os.stat(self.gap_up_fn)[8]))
            self.up_old_dateVar.set(d.split(' ')[0])
            self.up_old_timeVar.set(d.split(' ')[1])
        if os.path.isfile(self.gap_down_fn):
            self.downfilenameVar.set(self.gap_down_fn)
            d = str(datetime.datetime.fromtimestamp(os.stat(self.gap_down_fn)[8]))
            self.down_old_dateVar.set(d.split(' ')[0])
            self.down_old_timeVar.set(d.split(' ')[1])
        self.status_str.set("Job Status: New Gap Files are created")


#            file_date = d.split(' ')[0]
#            file_time = d.split(' ')[1]
    
    
    def proc_post_cleanup(self):
        pass
    def update_MSA_DB(self):
        pass
    def get_up_newfile(self):
        file_name = filedialog.askopenfilename(initialdir = "C://",title = "choose your file",filetypes = (("all files","*.*"),))
        self.upnewfilenameVar.set(file_name)
        self.status_str.set("Job Status: new file name is set for Gap Up file")
        
    def get_down_newfile(self):
        file_name = filedialog.askopenfilename(initialdir = "C://",title = "choose your file",filetypes = (("all files","*.*"),))
        self.downnewfilenameVar.set(file_name)
        self.status_str.set("Job Status: new file name is set for Gap Down file")

        
    def gapup_updt_MSA_DB(self):
        if len(self.upnewfilenameVar.get()) > 0:
           self.gap_up_fn = self.upnewfilenameVar.get()

        if len(self.up_new_dateVar.get()) > 0:
           fdate = self.up_new_dateVar.get()
        else:
            fdate = ""

        if len(self.up_new_timeVar.get()) > 0:
           ftime = self.up_new_timeVar.get()
        else:
            ftime = ""

        gapraw.write_records(self.gap_up_fn, "UP", fdate, ftime)
        self.status_str.set("Job Status: MSA DB table updated for Gap Up")
        
    def gapdown_updt_MSA_DB(self):
        if len(self.downnewfilenameVar.get()) > 0:
           self.gap_down_fn = self.downnewfilenameVar.get()

        if len(self.down_new_dateVar.get()) > 0:
           fdate = self.down_new_dateVar.get()
        else:
            fdate = ""

        if len(self.down_new_timeVar.get()) > 0:
           ftime = self.down_new_timeVar.get()
        else:
            ftime = ""
        
        gapraw.write_records(self.gap_down_fn, "DOWN", fdate, ftime)
        self.status_str.set("Job Status: MSA DB table updated for Gap Down")
    
    def __init__(self):      
        window = Tk() # Create a window
        window.title('Finviz Gap Analysis Extract') # Set title
        window.geometry('700x565+300+300')
        window['bg'] = '#074c85'
        
        self.dwonload_dir_path = 'C:\\users\\karsu\\downloads\\'
        self.gap_down_fn = self.dwonload_dir_path + 'finviz (1).csv'
        self.gap_up_fn = self.dwonload_dir_path + 'finviz.csv'


        frame1 = Frame(window)
        frame1.pack(pady = '10')
        btn_precleanup= Button(frame1,  width = '80', fg = '#074c85', relief=RAISED, text = "Pre-Cleanup Process", font=('Helvetica', 10, 'bold'),
            command = self.proc_pre_cleanup).grid(row = 1, column = 1,
                        columnspan = 2)
        frame2 = Frame(window)
        frame2.pack(pady = '10')
        btn_getdata = Button(frame2,  width = '80', relief=RAISED, fg = '#074c85', text = "Get data from Finviz site", font=('Helvetica', 10, 'bold'),
            command = self.get_finviz_files).grid(row = 1, column = 1,
                        columnspan = 2)

        frame3 = Frame(window)
        frame3.pack(pady = '10')
        frame3['bg'] = '#87c2f2'
        f3_lbl1 = Label(frame3,  fg = '#074c85', text = "Gap Up File", font=('Helvetica', 12, 'bold'), bg='#87c2f2').grid(row = 1, 
            column = 3)
        
        f3_lbl2 = Label(frame3, text = "File Name", bg='#87c2f2').grid(row =2, 
            column = 1,sticky = W)

        self.upfilenameVar = StringVar()
        ent_up_oldfilename = Entry(frame3, width = 60,
            textvariable = self.upfilenameVar).grid(row = 2, column = 2, columnspan = 4, sticky = W)

        f3_lbl3 = Label(frame3, text = "New file", bg='#87c2f2').grid(row =3, 
            column = 1,sticky = W)

        self.upnewfilenameVar = StringVar()
        ent_up_newfilename = Entry(frame3, width=60, 
            textvariable = self.upnewfilenameVar).grid(row = 3, column = 2, columnspan = 4,sticky = W)

        btn_chg_up_filename = Button(frame3, fg = '#074c85', relief=RAISED, text = "Browse", font=('Helvetica', 9, 'bold'),
            command = self.get_up_newfile).grid(row = 3, column = 4, padx = '15', ipadx = '35', 
                            sticky = W)

        f3_lbl4 = Label(frame3, text = "Date", bg='#87c2f2').grid(row =4, 
            column = 1,sticky = W)

        self.up_old_dateVar = StringVar()
        ent_up_old_date = Entry(frame3, 
            textvariable = self.up_old_dateVar).grid(row = 4, column = 2, sticky = W)

        f3_lbl5 = Label(frame3, text = "New Date", bg='#87c2f2').grid(row =4, 
            column = 3,sticky = E)

        self.up_new_dateVar = StringVar()
        ent_up_new_date = Entry(frame3, 
            textvariable = self.up_new_dateVar).grid(row = 4, column = 4, padx = '15', sticky = W)

        f3_lbl6 = Label(frame3, text = "Time", bg='#87c2f2').grid(row =5, 
            column = 1,sticky = W)

        self.up_old_timeVar = StringVar()
        ent_up_old_time = Entry(frame3, 
            textvariable = self.up_old_timeVar).grid(row = 5, column = 2, sticky = W)

        f3_lbl7 = Label(frame3, text = "New Time", bg='#87c2f2').grid(row =5, 
            column = 3,sticky = E)

        self.up_new_timeVar = StringVar()
        ent_up_new_time = Entry(frame3, 
            textvariable = self.up_new_timeVar).grid(row = 5, column = 4, padx = '15', sticky = W)

        btn_gapup_updt_MSA_DB = Button(frame3, relief=RAISED, fg = '#074c85', text = "Update MSA DB", font=('Helvetica', 9, 'bold'),
            command = self.gapup_updt_MSA_DB).grid(row = 7, column = 3,  pady = '10', ipadx = '65',)

        frame4 = Frame(window)
        frame4.pack(pady = '10')
        frame4['bg'] = '#87c2f2'
        f4_lbl1 = Label(frame4, fg = '#074c85', text = "Gap Down File",  font=('Helvetica', 12, 'bold'), bg='#87c2f2').grid(row = 1, 
            column = 3)
        
        f4_lbl2 = Label(frame4, text = "File Name",  bg='#87c2f2').grid(row =2, 
            column = 1,sticky = W)

        self.downfilenameVar = StringVar()
        ent_down_oldfilename = Entry(frame4, width = 60,
            textvariable = self.downfilenameVar).grid(row = 2, column = 2,columnspan = 4, sticky = W)

        f4_lbl3 = Label(frame4, text = "New file", bg='#87c2f2').grid(row =3, 
            column = 1,sticky = W)

        self.downnewfilenameVar = StringVar()
        ent_down_newfilename = Entry(frame4, width=60,
            textvariable = self.downnewfilenameVar).grid(row = 3, column = 2, columnspan = 4, sticky = W)
        btn_chg_down_filename = Button(frame4, relief=RAISED, fg = '#074c85', text = "Browse", font=('Helvetica', 9, 'bold'),
            command = self.get_down_newfile).grid(row = 3, column = 4, padx = '15', ipadx = '35', sticky = W)

        f4_lbl4 = Label(frame4, text = "Date", bg='#87c2f2').grid(row =4, 
            column = 1,sticky = W)

        self.down_old_dateVar = StringVar()
        ent_down_old_date = Entry(frame4, 
            textvariable = self.down_old_dateVar).grid(row = 4, column = 2, sticky = W)

        f4_lbl5 = Label(frame4, text = "New Date", bg='#87c2f2').grid(row =4, 
            column = 3,sticky = E)

        self.down_new_dateVar = StringVar()
        ent_down_new_date = Entry(frame4, 
            textvariable = self.down_new_dateVar).grid(row = 4, column = 4, padx = '15', sticky = W)

        f4_lbl6 = Label(frame4, text = "Time", bg='#87c2f2').grid(row =5, 
            column = 1,sticky = W)

        self.down_old_timeVar = StringVar()
        ent_down_old_time = Entry(frame4, 
            textvariable = self.down_old_timeVar).grid(row = 5, column = 2, sticky = W)

        f4_lbl7 = Label(frame4, text = "New Time", bg='#87c2f2').grid(row =5, 
            column = 3,sticky = E)

        self.down_new_timeVar = StringVar()
        ent_down_new_time = Entry(frame4, 
            textvariable = self.down_new_timeVar).grid(row = 5, column = 4, padx = '15', sticky = W)

        btn_gapdown_updt_MSA_DB = Button(frame4, relief=RAISED, fg = '#074c85', text = "Update MSA DB", font=('Helvetica', 9, 'bold'),
            command = self.gapdown_updt_MSA_DB).grid(row = 7, column = 3, pady = '10', ipadx = '65',)

        frame5 = Frame(window)
        frame5.pack(pady = '10')
        btn_postcleanup= Button(frame5,  width = '80', fg = '#074c85', text = "Post-Cleanup Process", font=('Helvetica', 10, 'bold'),
            command = self.proc_post_cleanup()).grid(row = 1, column = 1,
                        columnspan = 2)

        frame6 = Frame(window)
        frame6.pack(pady = (35, 0))
        self.status_str = StringVar(value = "Job Status: ")
        f6_lbl1 = Label(frame6, textvariable = self.status_str, fg = 'red', anchor = 'w', width = '100', bg='white').grid(row =1, 
            column = 1,sticky = W)

        window.mainloop()


Main_process()