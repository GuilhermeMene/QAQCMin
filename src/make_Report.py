# -*- coding: utf-8 -*-

##########################################
#Name: Guilherme Mene Ale Primo
#Date: 16/05/2020
# QAQC geochemical data control and report
##########################################

#imports 

from fpdf import FPDF
from datetime import date
import os


class makeReport():

    def makePdf(blank_data, dup_data, std_data, batch_name, technical_manager):


        #set today date 
        today = date.today()
        DToday = today.strftime("%d/%m/%Y")

        #set the pdf creator 

        pdf = FPDF()

        #Add a page 
        # Blank page
        pdf.add_page()

        #set a title of pdf 
        pdf.set_font('arial', 'B', 16)
        pdf.cell(60)
        pdf.cell(70, 10, txt="QAQC Control Report", ln= 2, align='C' )
        pdf.set_font(family= 'arial', size= 12)
        pdf.cell(70, 10, txt='Batch Name: ', ln= 2, align='C')
        pdf.cell(70, 10, txt= f'{batch_name}', ln= 1, align='C')
        pdf.set_font(family = 'arial', size = 10)
        pdf.cell(50, 10, txt= f'Technical Manager: {technical_manager}', ln= 0, align='L')
        pdf.cell(130, 10, txt= f'Date: {DToday}', ln= 1, align='R')


        #Add a image of company 
        image_path = r'/mnt/Arquivos/Database/Arica-Database/logo_arica.jpeg' 
        pdf.image(image_path, x= 10, y = 10, w = 30)


        #Add line for separate the 
        pdf.line(0, 50, 210, 50)

        #################################

        #Add the blank table
        pdf.set_font(family = 'arial', style = 'B', size = 14)
        pdf.cell(10, 10, txt='Blank Samples', ln = 2, align='L')
        pdf.cell(40, 10, ln = 2)

        #Making the blank table
        pdf.set_font(family = 'arial', style = 'B', size = 12)
        pdf.cell(50, 10, txt='Sample ID', border= 'B' , ln = 0, align = 'C')
        pdf.cell(40, 10, txt='Result', border = 'B', ln = 0, align = 'C')
        pdf.cell(40, 10, txt='Status', border = 'B', ln = 1, align = 'C')

        pdf.set_font(family = 'arial', size = 10)


        if not len(blank_data): 

            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)

        else:
            for i in range (0, len(blank_data[0][0])):
                pdf.cell(50, 10, txt= '%s' % (blank_data[0][0][i]), border= 'B' , ln = 0, align = 'C')
                pdf.cell(40, 10, txt= '%.3f' % (blank_data[0][1][i]), border= 'B' , ln = 0, align = 'C')
                pdf.cell(40, 10, txt= '%s' % (blank_data[0][2][i]), border= 'B' , ln = 1, align = 'C')


        #set the number of samples
        pdf.set_font(family = 'arial', size = 10)
        pdf.cell(190, 10, txt= f'Number of samples : {len(blank_data[0][0])}', ln= 2, align='R')

        if not len(blank_data):
            #image of chart 
            blank_path = (os.path.normpath(os.getcwd()) + "/img/nochart.png")
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.image(blank_path, x= None, y = None, w = 170)

        else:
            #image of chart 
            blank_path = (os.path.normpath(os.getcwd()) + "/.temp/blankchart.png")
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.image(blank_path, x= None, y = None, w = 170)

        #################################

        #Making the second page (Duplicate samples)

        #add a page 
        #Duplicate page
        pdf.add_page()

        #Add the duplicate table
        pdf.set_font(family = 'arial', style = 'B', size = 14)
        pdf.cell(10, 10, txt='Duplicate Samples', ln = 2, align='L')
        pdf.cell(40, 10, ln = 2)

        #Making the duplicate table
        pdf.set_font(family = 'arial', style = 'B', size = 12)
        pdf.cell(35, 10, txt='Sample ID', border= 'B' , ln = 0, align = 'C')
        pdf.cell(35, 10, txt='Result Sample', border = 'B', ln = 0, align = 'C')
        pdf.cell(35, 10, txt='Duplicate', border = 'B', ln = 0, align = 'C')
        pdf.cell(35, 10, txt='Result Duplicate', border = 'B', ln = 0, align = 'C')
        pdf.cell(35, 10, txt='Difference', border = 'B', ln = 1, align = 'C')

        pdf.set_font(family = 'arial', size = 10)

        if not len(dup_data):
            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)

        else:
            for i in range(0, len(dup_data[0][0])):                
                pdf.cell(35, 10, txt= '%s' % (dup_data[0][0][i]), border= 'B' , ln = 0, align = 'C')
                pdf.cell(35, 10, txt= '%.3f' % (dup_data[0][1][i]), border = 'B', ln = 0, align = 'C')
                pdf.cell(35, 10, txt= '%s' % (dup_data[0][2][i]), border = 'B', ln = 0, align = 'C')
                pdf.cell(35, 10, txt= '%.3f' % (dup_data[0][3][i]), border = 'B', ln = 0, align = 'C')
                pdf.cell(35, 10, txt= '%.2f' % (dup_data[0][4][i]) + '%', border = 'B', ln = 1, align = 'C')

        #set the number of samples
        pdf.set_font(family = 'arial', size = 10)
        pdf.cell(190, 10, txt= f'Number of samples : {len(dup_data[0][0])}', ln= 2, align='R')

        if not len(dup_data):
            #image of chart 
            dup_path = (os.path.normpath(os.getcwd()) + "/img/nochart.png")
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.image(dup_path, x= None, y = None, w = 170)

        else:
            #image of chart 
            dup_path = (os.path.normpath(os.getcwd()) + "/.temp/dupchart.png")
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.image(dup_path, x= None, y = None, w = 170)


        #################################

        #Making the second page (Standard samples)

        #add a page 
        #Standard page
        pdf.add_page()

        #Add the Standard table
        pdf.set_font(family = 'arial', style = 'B', size = 14)
        pdf.cell(10, 10, txt='Standard Samples', ln = 2, align='L')
        pdf.cell(40, 10, ln = 2)

        #Making the Standard table
        pdf.set_font(family = 'arial', style = 'B', size = 12)
        pdf.cell(25, 10, txt='Sample ID', border= 'B' , ln = 0, align = 'C')
        pdf.cell(25, 10, txt='Result', border = 'B', ln = 0, align = 'C')
        pdf.cell(25, 10, txt='Std Name', border = 'B', ln = 0, align = 'C')
        pdf.cell(25, 10, txt='Std Mean', border = 'B', ln = 0, align = 'C')
        pdf.cell(35, 10, txt='Assay Deviation', border = 'B', ln = 0, align = 'C')
        pdf.cell(25, 10, txt='BIAS', border = 'B', ln = 0, align = 'C')
        pdf.cell(20, 10, txt='Status', border = 'B', ln = 1, align = 'C')

        pdf.set_font(family = 'arial', size = 10)

        cont = 0
        
        if not len(std_data) :

            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)
            pdf.cell(40, 10, ln = 2)        
        
        else:
            for i in range(0, len(std_data)):
                for j in range(0, len(std_data[i])):                    

                    pdf.cell(25, 10, txt= '%s'   % (std_data[i][j][1]),border= 'B' , ln = 0, align = 'C')
                    pdf.cell(25, 10, txt= '%s'   % (std_data[i][j][2]), border = 'B', ln = 0, align = 'C')
                    pdf.cell(25, 10, txt= '%s'   % (std_data[i][j][0]), border = 'B', ln = 0, align = 'C')
                    pdf.cell(25, 10, txt= '%.3f' % (std_data[i][j][3]), border = 'B', ln = 0, align = 'C')
                    pdf.cell(35, 10, txt= '%.3f' % (std_data[i][j][4]), border = 'B', ln = 0, align = 'C')
                    pdf.cell(25, 10, txt= '%.2f' % (std_data[i][j][5]) + '%', border = 'B', ln = 0, align = 'C')
                    pdf.cell(20, 10, txt= '%s' % (std_data[i][j][6]), border = 'B', ln = 1, align = 'C')

                    cont+1

        #set the number of samples
        pdf.set_font(family = 'arial', size = 10)
        pdf.cell(190, 10, txt= f'Number of samples : {cont}', ln= 2, align='R')

        if not len(std_data):
            #image of chart 
            std_path = (os.path.normpath(os.getcwd()) + "/img/nochart.png")
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.image(std_path, x= None, y = None, w = 170)

        else:
            #image of chart 
            std_path = (os.path.normpath(os.getcwd()) + "/.temp/stdchart.png")
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.image(std_path, x= None, y = None, w = 170)


        #save the final file 
        pdf.output('/home/gmene/Documents/test.pdf', 'F')













