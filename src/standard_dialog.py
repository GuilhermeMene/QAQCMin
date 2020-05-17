# -*- coding: utf-8 -*-

##########################################
#Name: Guilherme Mene Ale Primo
#Date: 18/01/2020
# QAQC geochemical data control and report
##########################################

#import libraries
import wx
import wx.grid
import sqlite3 as sqlite
import numpy as np


#Set class of dialog
class STDDialog( wx.Dialog ):

	def __init__( self, parent):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Standard Database", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.main = parent

		box4 = wx.BoxSizer( wx.HORIZONTAL )

		self.std_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.std_grid.CreateGrid( 100, 4 )
		self.std_grid.EnableEditing( True )
		self.std_grid.EnableGridLines( True )
		self.std_grid.EnableDragGridSize( False )
		self.std_grid.SetMargins( 30, 0 )

		# Columns
		self.std_grid.SetColSize( 0, 80 )
		self.std_grid.SetColSize( 1, 150 )
		self.std_grid.SetColSize( 2, 150 )
		self.std_grid.SetColSize( 3, 150 )
		
		self.std_grid.EnableDragColMove( False )
		self.std_grid.EnableDragColSize( False )
		self.std_grid.SetColLabelSize( 30 )
		self.std_grid.SetColLabelValue( 0, u"Id" )
		self.std_grid.SetColLabelValue( 1, u"Standard" )
		self.std_grid.SetColLabelValue( 2, u"Certified Value" )
		self.std_grid.SetColLabelValue( 3, u"Standard Deviation" )
		self.std_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.std_grid.EnableDragRowSize( True )
		self.std_grid.SetRowLabelSize( 50 )
		self.std_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.std_grid.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		box4.Add( self.std_grid, 0, wx.ALL, 5 )


		box4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		box5 = wx.BoxSizer( wx.VERTICAL )


		box5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Save Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		box5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.std_save = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.std_save.SetBitmap( wx.Bitmap( u"img/save_47.png", wx.BITMAP_TYPE_ANY ) )
		box5.Add( self.std_save, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#Set button function
		self.std_save.Bind(wx.EVT_BUTTON, self.STD_Save)


		box5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Read from File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		box5.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.std_read = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.std_read.SetBitmap( wx.Bitmap( u"img/opendata_47.png", wx.BITMAP_TYPE_ANY ) )
		box5.Add( self.std_read, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#Set button function
		self.std_read.Bind(wx.EVT_BUTTON, self.STD_ReadFile)

		box5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Remove Standard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		box5.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.std_remove = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.std_remove.SetBitmap( wx.Bitmap( u"img/remove_47.png", wx.BITMAP_TYPE_ANY ) )
		box5.Add( self.std_remove, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#Set button function
		self.std_remove.Bind(wx.EVT_BUTTON, self.STD_Remove)

		box5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Clear Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		box5.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.std_trash = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.std_trash.SetBitmap( wx.Bitmap( u"img/trash_47.png", wx.BITMAP_TYPE_ANY ) )
		box5.Add( self.std_trash, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#Set button function
		self.std_trash.Bind(wx.EVT_BUTTON, self.STD_Del)

		box5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		box5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.std_close = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.std_close.SetBitmap( wx.Bitmap( u"img/exit_47.png", wx.BITMAP_TYPE_ANY ) )
		box5.Add( self.std_close, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#Set button function
		self.std_close.Bind(wx.EVT_BUTTON, self.STD_Close)


		box5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		box4.Add( box5, 1, wx.EXPAND, 5 )

		box4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.SetSizer( box4 )
		self.Layout()

		self.Centre( wx.BOTH )

		self.STD_Load()

	def __del__( self ):
		pass

	def STD_Load(self):

		""" This fuction connect to database and get the list of standards
		"""
		#Connect to database and get count
		self.conn = sqlite.connect('db/standard_db.db')
		self.cursor = self.conn.cursor()

		self.cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Standards'""")

		#Load data from database and populate the datagrid
		if self.cursor.fetchone()[0] ==1:
			self.stds = self.cursor.execute("""SELECT * FROM Standards ORDER BY Id;""")

			j = 0

			for line in self.stds:

				row_num = line[0]
				cells = line

				for i in range(0, len(cells)):					
					if cells[i] != None and cells[i] != "null":
						self.std_grid.SetCellValue(j, i, str(cells[i]))
				j+=1

		else:
			self.cursor.execute("""create table if not exists Standards (Id INTEGER PRIMARY KEY, 
								std_name text, certified_value real, std_deviation real);""")

		#close connection with database
		self.conn.close()
		#Fill the datagrid with Standards

	def STD_Save(self, event):
		""" This fuction save the Standard database into database
		"""
		#connect to database
		self.conn = sqlite.connect('db/standard_db.db')
		self.cursor = self.conn.cursor()

		#self.nrows = int(self.std_grid.GetNumberRows())

		for row in range(0, 100):

			col1 = self.std_grid.GetCellValue(row, 0)
			col2 = self.std_grid.GetCellValue(row, 1)
			col3 = self.std_grid.GetCellValue(row, 2)
			col4 = self.std_grid.GetCellValue(row, 3)

			if len(col1) != 0:

				#self.cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Standards'""")

				count = self.cursor.execute("""SELECT count(*) FROM Standards""").fetchall()

				if count[0][0] > 0:

					self.cursor.execute("""INSERT OR REPLACE INTO Standards  (Id, std_name, certified_value, std_deviation) VALUES (?, ?, ?, ?)""", (col1, col2, col3, col4))

				else:
					self.cursor.execute("""INSERT INTO Standards  (Id, std_name, certified_value, std_deviation) VALUES (?, ?, ?, ?)""", (col1, col2, col3, col4))

			else:
				pass

		#commit and close db
		self.conn.commit()
		
		self.conn.close()

		#Message for user
		wx.MessageBox("Database saved! ", 'File Saved!')


	def STD_ReadFile(self, event):
		""" This function import the standard text file based to datagrid.
		"""

		#Open File Dialog 
		with wx.FileDialog(self, "Open Data File", wildcard="CSV Files (*.csv)|*.csv| TXT Files (*.txt)|*.txt",
							style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return #If the user cancel

			pathname = fileDialog.GetPath()

			#get data and fill datagrid
			try:			

				s1, s2, s3 = np.loadtxt(pathname, dtype=str, delimiter=',', skiprows=1, unpack=True)

				for i in range(0, len(s1)):
					self.std_grid.SetCellValue(i, 0, str(i+1))
					self.std_grid.SetCellValue(i, 1, str(s1[i]))
					self.std_grid.SetCellValue(i, 2, str(s2[i]))
					self.std_grid.SetCellValue(i, 3, str(s3[i]))


			except IOError:
				wx.MessageBox( "Cannot open data file {}.".format(pathname)+ "\n Incorrect file format. ", 'Error File')

			except ValueError:
				wx.MessageBox("Cannot open data file {}.".format(pathname)+ "\n Incorrect file format. ", 'Error File')

	def STD_Remove(self, event):
		""" This fuction remove the standard of datagrid and database
		"""

		self.std_grid.SelectRow(self.std_grid.GetGridCursorRow(),True)
		row = self.std_grid.GetGridCursorRow()
		idx = self.std_grid.GetCellValue(row, 0)
		self.std_grid.SetCellValue(row, 0, str(""))
		self.std_grid.SetCellValue(row, 1, str(""))
		self.std_grid.SetCellValue(row, 2, str(""))
		self.std_grid.SetCellValue(row, 3, str(""))

		#connect to database
		self.conn = sqlite.connect('db/standard_db.db')
		self.cursor = self.conn.cursor()

		#delete the record in database
		self.cursor.execute("""DELETE FROM Standards WHERE id = ? """, (idx,))

		#commit and close db
		self.conn.commit()
		self.conn.close()

		#Clear Datagrid and Reload database
		self.std_grid.ClearGrid()
		self.STD_Load()

		#set message for user
		wx.MessageBox("Standard removed! ", 'Data deleted!')


	def STD_Del(self, event):
		""" This fuction delete the database and all of standard previously saved.
		"""

		self.resp = wx.MessageBox(' Are you sure about that ?\n This will remove all records from database...', 'Warning',
									wx.OK | wx.CANCEL | wx.ICON_WARNING)

		if self.resp == wx.OK:

			#connect to database
			self.conn = sqlite.connect('db/standard_db.db')
			self.cursor = self.conn.cursor()

			#Delete all data in table Standard 
			self.cursor.execute("""DELETE FROM Standards""")
			self.conn.commit()
			self.conn.close()

			#Clear all data of Datagrid 
			self.std_grid.ClearGrid()

			#set message for user
			wx.MessageBox("Database cleaned! ", 'All data erased!')

		else: 
			pass


	def STD_Close(self, event):
		"""This fuction close the STD Dialog
		"""
		self.Close(True)