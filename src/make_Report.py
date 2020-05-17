# -*- coding: utf-8 -*-

##########################################
#Name: Guilherme Mene Ale Primo
#Date: 16/05/2020
# QAQC geochemical data control and report
##########################################

#imports 

from fpdf import FPDF
from datetime import date


class makeReport ():

    def makePdf():

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
        pdf.cell(70, 10, txt='__name of batch__', ln= 1, align='C')
        pdf.set_font(family = 'arial', size = 10)
        pdf.cell(50, 10, txt= f'Technical Manager: __Manager__', ln= 0, align='L')
        pdf.cell(130, 10, txt= f'Date: __date__', ln= 1, align='R')


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
        pdf.cell(40, 10, ln = 2)
        pdf.cell(40, 10, ln = 2)
        pdf.cell(40, 10, ln = 2)
        pdf.cell(40, 10, ln = 2)

        #set the number of samples
        pdf.set_font(family = 'arial', size = 10)
        pdf.cell(190, 10, txt= f'Number of samples : __number of samples__', ln= 2, align='R')

        #image of chart 
        blank_path = r'/mnt/Arquivos/Database/Bases/Chart_blank.png'
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
        pdf.cell(40, 10, ln = 2)
        pdf.cell(40, 10, ln = 2)
        pdf.cell(40, 10, ln = 2)
        pdf.cell(40, 10, ln = 2)

        #set the number of samples
        pdf.set_font(family = 'arial', size = 10)
        pdf.cell(190, 10, txt= f'Number of samples : __number of samples__', ln= 2, align='R')

        #image of chart 
        blank_path = r'/mnt/Arquivos/Database/Bases/Chart_blank.png'
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.image(blank_path, x= None, y = None, w = 170)



        #save the final file 
        pdf.output('test.pdf', 'F')




makeReport.makePdf()









