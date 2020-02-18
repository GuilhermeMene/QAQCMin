# -*- coding: utf-8 -*-

##########################################
#Name: Guilherme Mene Ale Primo
#Date: 18/01/2020
# QAQC geochemical data control and report
##########################################

#import libraries
import wx
import wx.xrc
import wx.lib.agw.ribbon as rb
import wx.grid
import numpy as np
import sys
import sqlite3 as sqlite
import matplotlib.pyplot as plt
import standard_dialog

# Set MainFrame
class MainFrame( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Geochemical QAQC Program", pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.DEFAULT_FRAME_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		box = wx.BoxSizer( wx.VERTICAL )

		open_Proj = wx.Window.NewControlId()
		save_Proj = wx.Window.NewControlId()
		exp_Rep = wx.Window.NewControlId()
		std_db = wx.Window.NewControlId()
		exit_bot = wx.Window.NewControlId()

		self.rb = rb.RibbonBar( self , wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_BAR_DEFAULT_STYLE )
		self.Page1 = rb.RibbonPage( self.rb, wx.ID_ANY, u"MyRibbonPage" , wx.NullBitmap , 0 )
		self.file_panel = rb.RibbonPanel( self.Page1, wx.ID_ANY, wx.EmptyString , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb1 = rb.RibbonButtonBar( self.file_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb1.AddSimpleButton( open_Proj, u"Open Project", wx.Bitmap( u"img/open_47.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rbb1.AddSimpleButton( save_Proj, u"Save Project", wx.Bitmap( u"img/save_47.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rbb1.AddSimpleButton( exp_Rep, u"Save Report", wx.Bitmap( u"img/report_47.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.db_panel = rb.RibbonPanel( self.Page1, wx.ID_ANY, wx.EmptyString , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb2 = rb.RibbonButtonBar( self.db_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb2.AddSimpleButton( std_db, u"Standard Database", wx.Bitmap( u"img/database_47.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.exit_panel = rb.RibbonPanel( self.Page1, wx.ID_ANY, wx.EmptyString , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb3 = rb.RibbonButtonBar( self.exit_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb3.AddSimpleButton( exit_bot, u" Exit", wx.Bitmap( u"img/exit_47.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rb.Realize()

		#Set buttom event in the Ribbon buttons
		self.rbb1.Bind(rb.EVT_RIBBONBUTTONBAR_CLICKED, self.openProject, id=open_Proj)
		self.rbb1.Bind(rb.EVT_RIBBONBUTTONBAR_CLICKED, self.SaveProject, id=save_Proj)
		self.rbb1.Bind(rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ExportReport, id=exp_Rep)
		self.rbb2.Bind(rb.EVT_RIBBONBUTTONBAR_CLICKED, self.StandardDB, id=std_db)
		self.rbb3.Bind(rb.EVT_RIBBONBUTTONBAR_CLICKED, self.Onclose,None, id=exit_bot)

		box.Add( self.rb, 0, wx.ALL|wx.EXPAND, 5 )

		self.note = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.data_panel = wx.Panel( self.note, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		box1 = wx.BoxSizer( wx.HORIZONTAL )

		self.Datagrid = wx.grid.Grid( self.data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Datagrid.CreateGrid( 100, 4 )
		self.Datagrid.EnableEditing( True )
		self.Datagrid.EnableGridLines( True )
		self.Datagrid.EnableDragGridSize( False )
		self.Datagrid.SetMargins( 50, 0 )

		# Columns
		self.Datagrid.SetColSize( 0, 100 )
		self.Datagrid.SetColSize( 1, 100 )
		self.Datagrid.SetColSize( 2, 100 )
		self.Datagrid.SetColSize( 3, 100 )
		self.Datagrid.EnableDragColMove( False )
		self.Datagrid.EnableDragColSize( True )
		self.Datagrid.SetColLabelSize( 30 )
		self.Datagrid.SetColLabelValue( 0, u"Sample ID" )
		self.Datagrid.SetColLabelValue( 1, u"Sample Type" )
		self.Datagrid.SetColLabelValue( 2, u"Duplicate" )
		self.Datagrid.SetColLabelValue( 3, u"Assay 01" )
		#self.Datagrid.SetColLabelValue( 4, u"Assay 02" )
		#self.Datagrid.SetColLabelValue( 5, u"Assay 03" )
		self.Datagrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Datagrid.EnableDragRowSize( True )
		self.Datagrid.SetRowLabelSize( 50 )
		self.Datagrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Datagrid.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		box1.Add( self.Datagrid, 0, wx.ALL, 5 )

		box2 = wx.BoxSizer( wx.VERTICAL )
		box2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self.data_panel, wx.ID_ANY, u"Open Data File ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		box2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.open_file = wx.BitmapButton( self.data_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.open_file.SetBitmap( wx.Bitmap( u"img/opendata_47.png", wx.BITMAP_TYPE_ANY ) )
		box2.Add( self.open_file, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        #Set open file data function
		self.open_file.Bind(wx.EVT_BUTTON, self.LoadData)

		box2.Add( ( 0, 0), 1, 0, 5 )

		self.m_staticText2 = wx.StaticText( self.data_panel, wx.ID_ANY, u"Clear Data ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		box2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.clear_datagrid = wx.BitmapButton( self.data_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.clear_datagrid.SetBitmap( wx.Bitmap( u"img/trash_47.png", wx.BITMAP_TYPE_ANY ) )
		box2.Add( self.clear_datagrid, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        #Set open file data function
		self.clear_datagrid.Bind(wx.EVT_BUTTON, self.clear_DataGrid)

		box2.Add( ( 0, 0), 1, 0, 5 )

		self.m_staticText3 = wx.StaticText( self.data_panel, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		box2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.run_bot = wx.BitmapButton( self.data_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.run_bot.SetBitmap( wx.Bitmap( u"img/run_47.png", wx.BITMAP_TYPE_ANY ) )
		box2.Add( self.run_bot, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#Set open file data function
		self.run_bot.Bind(wx.EVT_BUTTON, self.runProject)


		box2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		box1.Add( box2, 1, wx.EXPAND, 5 )

		self.data_panel.SetSizer( box1 )
		self.data_panel.Layout()
		box1.Fit( self.data_panel )
		self.note.AddPage( self.data_panel, u"DATA", True )

		self.report_panel = wx.Panel( self.note, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.note.AddPage( self.report_panel, u"Report", False )

		box.Add( self.note, 1, wx.EXPAND |wx.ALL, 5 )

		self.SetSizer( box )
		self.Layout()

		self.Centre( wx.BOTH )

		#set the types
		self.type = ["SMP", "BLANK", "DUP"]

		#Load std for list
		self.Load_STD()

		#set Datagrid cell Editor for fill with list
		self.type_editor = wx.grid.GridCellChoiceEditor(self.type, True)
		#set the editor cell
		for i in range(0,100):
			self.Datagrid.SetCellEditor(i, 1, self.type_editor)


	def clear_DataGrid(self, event):
		""" This fuction clear datagrid
		"""

		self.resp = wx.MessageBox(' Are you sure about that ?\n This will remove all data in the table...', 'Warning',
							wx.OK | wx.CANCEL | wx.ICON_WARNING)

		if self.resp == wx.OK:

			# Clear datagrid
			self.Datagrid.ClearGrid()
		else:
			pass


	def Load_STD(self):

		""" This fuction fill the std combobox in the datagrid choice editor
		"""

		#Connect to database
		self.conn = sqlite.connect('db/standard_db.db')
		self.cursor = self.conn.cursor()

		self.num_tables_db = self.cursor.execute("""SELECT count(*) FROM sqlite_master WHERE type = 'table'""").fetchone()


		if self.num_tables_db[0] == 0:
			self.cursor.execute("""create table if not exists Standards (Id INTEGER PRIMARY KEY,
								std_name text, certified_value real, std_deviation real);""")

		else:
			#Execute query for get std_names
			self.nstds = self.cursor.execute("""SELECT std_name FROM Standards""")

			#append names to type variable
			for line in self.nstds:
				self.type.append(line[0])

		self.conn.close()

	def __del__( self ):
		pass

	def LoadData(self, event):
		""" This fuction load the data from text file
		"""

		#Open File Dialog
		with wx.FileDialog(self, "Open Data File", wildcard="CSV Files (*.csv)|*.csv| TXT Files (*.txt)|*.txt",
							style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return #If the user cancel

			pathname = fileDialog.GetPath()

			#get data and fill datagrid
			try:

				c1, c2  = np.loadtxt(pathname, dtype=str, delimiter=',', skiprows=1, unpack=True)


				for i in range(0, len(c1)):
					self.Datagrid.SetCellValue(i, 0, str(c1[i]))
					self.Datagrid.SetCellValue(i, 1, "SMP")
					self.Datagrid.SetCellValue(i, 2, "")
					self.Datagrid.SetCellValue(i, 3, str(c2[i]))


			except IOError:
				wx.MessageBox("Cannot open data file '%s'.", pathname, "Cannot open data file")

			except ValueError:
				wx.MessageBox("Cannot open data file \n Are yout sure about file format?", "Incorrect File format")


	def openProject(self, event):
		""" This fuction open project file
		"""
		print("Hello World!")

	def SaveProject(self, event):
		""" This fuction save the project file
		"""
		print("Hello World!")

	def ExportReport(self, event):
		""" This fuction export the plots report into PDF
		"""
		print("Hello World!")

	def StandardDB(self, event):
		""" This fuction open the Standard managment dilaog.
		"""
		std_dialog = standard_dialog.STDDialog(self)
		std_dialog.Show()

	def runProject(self, event):
		""" This fuction get the data from datagrid and make plots of BLANK, DUP and STD.
		"""
		#set the lists

		self.s_Id = []
		self.s_type = []
		self.s_dup = []
		self.s_Assay1 = []

		#Get values of datagrid

		for row in range(0, 100):

			self.s_Id.append(self.Datagrid.GetCellValue(row, 0))
			self.s_type.append(self.Datagrid.GetCellValue(row, 1))
			self.s_dup.append(self.Datagrid.GetCellValue(row, 2))
			self.s_Assay1.append(self.Datagrid.GetCellValue(row, 3))

		if  self.s_Id[0] == '':

			wx.MessageBox("Cannot run the project. \n Datagrid is empty", "Datagrid is empty")

		else:

			#filter the None of data
			self.s_Id = list(filter(None, self.s_Id))
			self.s_type = list(filter(None, self.s_type))
			self.s_Assay1 = list(filter(None, self.s_Assay1))

			#convert the assay ppb to ppm
			for i in range(0, len(self.s_Assay1)):
				if self.s_Assay1[i] == '<5':
					self.s_Assay1[i] = 0.003
				else:
					self.s_Assay1[i] = int(self.s_Assay1[i])/1000


			##############################
			#getting data of blank samples
					#set the blank list
			self.s_blankId = []
			self.s_blankAssay = []
			self.s_blank_num =[]

			# Separate the types of QAQC items
			for i in range(0, len(self.s_Id)):
				if self.s_type[i] == "BLANK":
					self.s_blankId.append(self.s_Id[i])
					self.s_blankAssay.append(self.s_Assay1[i])
					self.s_blank_num.append(i)

			##############################
			#get std data from database
			#Connect to database
			self.conn = sqlite.connect('db/standard_db.db')
			self.cursor = self.conn.cursor()

			#Execute query for get std_names
			self.stdname = self.cursor.execute("""SELECT * FROM Standards""")

			self.std_name = []
			self.std_value = []
			self.std_deviation = []

			for line in self.stdname.fetchall():
				self.std_name.append(line[1])
				self.std_value.append(line[2])
				self.std_deviation.append(line[3])

			self.conn.close()

			#separete the types of qaqc items
			self.standard_project = []

			for std in range(0, len(self.std_name)):
				self.standard_project.append([])
				for item in range(0, len(self.s_type)):
					if self.s_type[item] == self.std_name[std]:
						self.standard_project[std].append([self.s_type[item], self.s_Id[item], self.s_Assay1[item]])

			self.standard_project = list(filter(None, self.standard_project))

			##############################
			#getting the duplicate data
			self.sample_assay = []

			# Get duplicates of datagrid
			for i in range(0, len(self.s_Id)):
				if self.s_type[i] == "DUP":							

					self.sample_assay.append(self.s_Assay1[i])


			##############################
			#check what the data exist or not for plot into graphics

			qaqc_items = ""

			#check if blank exist and plot then
			if len(self.s_blankAssay) > 0:
				#Plot blank into graphics
				self.plotBlank()
			else:
				qaqc_items += "Blank " 		

			if len(self.sample_assay) > 0:
				#plot DUP into graphics
				self.plotDUP()

			else:
				qaqc_items += "Duplicate "

			if len(self.standard_project) > 0:
				#plot STD into graphics
				self.plotSTD()

			else:
				qaqc_items += "Standard "

			#warning if data not exist
			if len(qaqc_items) > 0:	

				wx.MessageBox("Warning! . \n {} data is empty".format(qaqc_items), "0 {} found.".format(qaqc_items))
				plt.show()

			else:
				plt.show()	


	def plotBlank(self):
		"""This function plot the blank data in the chart"""
		
		#set the roundrobin of blank data
		blank_rr = []
		blank_x = []
		for i in range(0, 100):
			blank_x.append(i)
			blank_rr.append(0.01)

		#setting the plot setup
		fig , ax_blank = plt.subplots(num="Blank Plot - Quality Control Chart", figsize=(8, 6))
		ax_blank.scatter(self.s_blank_num, self.s_blankAssay, label='Samples', marker='s')
		ax_blank.plot(blank_x, blank_rr, label='Blank Limit', color='red')
		for i, lbl in enumerate(self.s_blankId):
			ax_blank.annotate(self.s_blankId[i], (self.s_blank_num[i], self.s_blankAssay[i] + 0.0005), rotation=90, verticalalignment='bottom')
		ax_blank.set_title("Blank Samples Plot - Quality Control Chart")
		ax_blank.set_xlabel("Samples")
		ax_blank.set_ylabel("Au (ppm) Fire Assay")
		ax_blank.set_xticklabels([])
		ax_blank.set_yticks((0.00250, 0.01250, 0.02250))
		ax_blank.grid(axis='y')
		plt.legend()

	def plotSTD(self):
		"""This function read the standards database and get the round robin of std"""

		#setting number of stds
		num_stds = len(self.standard_project)

		if num_stds <= 1:
			#set multiple plot of stds
			fig, ax_std = plt.subplots(num="Standard Plot - Quality Control Chat", figsize=(8, 6))
			fig.subplots_adjust(top= 0.90, bottom= 0.10, left= 0.10, right= 0.95, wspace = .15)

			standard_rr, standard_x = self.getRoundRobin()

			#plot the 1st round robin (approval)
			ax_std.plot(standard_x, standard_rr[0], label='Approved', color='green')
			ax_std.plot(standard_x, standard_rr[3], color='green')

			#plot the 2st round robin (revise)
			ax_std.plot(standard_x, standard_rr[1], label='Revise', color='yellow')
			ax_std.plot(standard_x, standard_rr[4], color='yellow')

			#plot the 2st round robin (revise)
			ax_std.plot(standard_x, standard_rr[2], label='Disapproved', color='red')
			ax_std.plot(standard_x, standard_rr[5], color='red')

			if len(self.standard_project[0]) > 1:
				for sample in range(0, len(self.standard_project[0])):
					#plot same standard in the figure
					ax_std.scatter(sample, self.standard_project[0][sample][2], label='Standard', color= 'b', marker='s')
					ax_std.annotate(self.standard_project[0][sample][1], (sample, self.standard_project[0][sample][2] + (self.standard_project[0][sample][2]* 0.05)),
									rotation=90, verticalalignment='bottom')

			else:
				#plot a standard in the figure
				ax_std.scatter(0, self.standard_project[0][0][2], label='Standard', color= 'b', marker='s')
				ax_std.annotate(self.standard_project[0][0][1], (0, self.standard_project[0][0][2] + (self.standard_project[0][0][2]* 0.05)),
								rotation=90, verticalalignment='bottom')

			#set the axis
			ax_std.set_title("Standard {} Plot - Quality Control Chart".format(self.standard_project[0][0][0]))
			ax_std.set_xticklabels([])
			ax_std.set_xlabel("Samples")
			ax_std.set_ylabel("Au (ppm) Fire Assay")
			ax_std.grid(axis='y')

		else:
			
			if num_stds > 2:
				#set a plot in the figure for more 2 plots
				fig, ax_std = plt.subplots(1, num_stds, num="Standard Plot - Quality Control Chat", figsize=(18, 6))

			else:
				#set a plot in the figure for until 2 plots
				fig, ax_std = plt.subplots(1, num_stds, num="Standard Plot - Quality Control Chat", figsize=(15, 6))

			fig.subplots_adjust(top= 0.90, bottom= 0.10, left= 0.05, right= 0.95, wspace = .15)
			ax_std = ax_std.ravel()


			#set list of standards and plot
			for i in range(0, len(self.standard_project)):
			
				standard_rr, standard_x = self.getRoundRobin(i)

				#plot the 1st round robin (approval)
				ax_std[i].plot(standard_x, standard_rr[0], label='Approved', color='green')
				ax_std[i].plot(standard_x, standard_rr[3], color='green')

				#plot the 2st round robin (revise)
				ax_std[i].plot(standard_x, standard_rr[1], label='Revise', color='yellow')
				ax_std[i].plot(standard_x, standard_rr[4], color='yellow')

				#plot the 2st round robin (revise)
				ax_std[i].plot(standard_x, standard_rr[2], label='Disapproved', color='red')
				ax_std[i].plot(standard_x, standard_rr[5], color='red')

				for sample in range(0, len(self.standard_project[i])):
					#plot the scatter with standards
					ax_std[i].scatter(sample, self.standard_project[i][sample][2], color= 'b', marker='s')
					ax_std[i].annotate(self.standard_project[i][sample][1], (sample, self.standard_project[i][sample][2] + (self.standard_project[i][sample][2]* 0.05)),
											rotation=90, verticalalignment='bottom')
	
				#set the axis
				ax_std[i].set_title("Standard {} Plot - Quality Control Chart".format(self.standard_project[i][0][0]))
				ax_std[i].set_xticklabels([])
				ax_std[i].set_xlabel("Samples")
				ax_std[i].set_ylabel("Au (ppm) Fire Assay")
				ax_std[i].grid(axis='y')
	
			plt.legend(loc='upper right')


	def getRoundRobin(self, standard_index = 0):

		"""This function get round robin for plot standards"""

		#get round robin of standard database
		standard_rr = []

		std_x = []
		for j in range(0, len(self.std_name)):
			if self.std_name[j] == self.standard_project[standard_index][0][0]:
				self.n_std = self.std_name[j]
				self.v_std = self.std_value[j]
				self.d_std = self.std_deviation[j]

		#set the range of plots
		for n in range(0, 20):
			standard_rr.append([])
		#set the round robin
		for num in range(0, 20):
			#append the num_x
			std_x.append(num)
			#append the std deviation
			standard_rr[0].append(self.v_std + self.d_std) #set the approved (+)
			standard_rr[1].append(self.v_std + (2*self.d_std))#set the revise (+)
			standard_rr[2].append(self.v_std + (3*self.d_std))#set the disapproved (+)
			standard_rr[3].append(self.v_std - self.d_std)#set the approved (-)
			standard_rr[4].append(self.v_std - (2*self.d_std))#set the revise (-)
			standard_rr[5].append(self.v_std - (3*self.d_std))#set the disapproved (-)

		return standard_rr, std_x

	def plotDUP(self):

		"""This function plot the duplicate samples on the graphics"""

		#get the assay of the duplicate
		dup_assay  = self.get_ID()
		#get the round robin of duplicate samples
		XUp10,YUp10,XDn10,YDn10,XUp5,YUp5,XDn5,YDn5,XBis,YBis = np.loadtxt('db/dup_rr.csv', delimiter=',', skiprows=1, unpack=True)
		#setting the plot setup
		fig , ax_dup = plt.subplots(num="Duplicates - Quality Control Chart", figsize= (8, 6))
		#set the UP 10% range
		ax_dup.plot(XUp10, YUp10, color='red')
		#set the UP 5% range
		ax_dup.plot(XUp5, YUp5, color='yellow')
		#set the Bissetriz of duplicates chart
		ax_dup.plot(XBis, YBis, color='blue')
		#set the Bottom 10% range
		ax_dup.plot(XDn10, YDn10, color='red')
		#set the Bottom 5% range
		ax_dup.plot(XDn5, YDn5, color='yellow')

		#plot the values of duplicate samples (x is the original sample and y is the dupicate of sample)
		ax_dup.scatter(self.sample_assay, dup_assay, label='Duplicate samples', marker='s', color='b')

		ax_dup.set_title("Duplicates Samples Plot - Quality Control Chart")
		ax_dup.set_xlabel("Au (ppm) Fire Assay")
		ax_dup.set_ylabel("Au (ppm) Fire Assay")
		ax_dup.set_xlim(-0.5, 7)
		ax_dup.set_ylim(-0.5, 7)
		ax_dup.grid(axis='y')
		plt.legend(loc='lower right')
		
	def get_ID(self):
		"""This get id for the duplicate samples"""

		#filkter the empty values of list
		self.s_dup = list(filter(None, self.s_dup))

		dup_assay = []

		for i in range(0, len(self.s_Id)):
			for j in range(0, len(self.s_dup)):
				if self.s_dup[j] == self.s_Id[i]:
					dup_assay.append(self.s_Assay1[i])

		return dup_assay

	def Onclose(self, event):

		sys.exit(0)


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()
