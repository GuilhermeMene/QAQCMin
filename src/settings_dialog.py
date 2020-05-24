# -*- coding: utf-8 -*-

##########################################
#Name: Guilherme Mene Ale Primo
#Date: 23/05/2020
# QAQC geochemical data control and report
##########################################

#imports 

import wx
import wx.xrc
import os


class SETDialog ( wx.Frame ):

	def SET_GetSet(self):
		""" This function get settings info		
		"""

		#read setting file 
		self.set_path = os.path.normpath(os.getcwd()) + "/setting"
		with open(self.set_path, "r") as set_file:

			project_settings = []
			for line in set_file:
				line = line.rstrip('\n')
				project_settings.append(line)

		return project_settings

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_path = wx.StaticText( self, wx.ID_ANY, u"Logo path: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_path.Wrap( -1 )

		bSizer3.Add( self.txt_path, 0, wx.ALL, 5 )

		self.logo_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer3.Add( self.logo_path, 0, wx.ALL, 5 )

		self.set_browse_btn = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )

		#Set button function
		self.set_browse_btn.Bind(wx.EVT_BUTTON, self.SET_browse)

		bSizer3.Add( self.set_browse_btn, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_unit = wx.StaticText( self, wx.ID_ANY, u"Unit (e.g. ppm; ppb; %) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_unit.Wrap( -1 )

		bSizer4.Add( self.txt_unit, 0, wx.ALL, 5 )

		self.sample_unit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer4.Add( self.sample_unit, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer4, 1, wx.EXPAND|wx.TOP, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.set_save_btn = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.set_save_btn.SetBitmap( wx.Bitmap( u"img/save_47.png", wx.BITMAP_TYPE_ANY ) )

		bSizer5.Add( self.set_save_btn, 0, wx.ALL, 5 )

		#Set button function
		self.set_save_btn.Bind(wx.EVT_BUTTON, self.SET_save)

		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.set_cancel_btn = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.set_cancel_btn.SetBitmap( wx.Bitmap( u"img/exit_47.png", wx.BITMAP_TYPE_ANY ) )

		bSizer5.Add( self.set_cancel_btn, 0, wx.ALL, 5 )

		#Set button function
		self.set_cancel_btn.Bind(wx.EVT_BUTTON, self.SET_cancel)

		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer2.Add( bSizer5, 1, wx.EXPAND|wx.TOP, 5 )

		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		#Get setting of sile 
		proj_settings = self.SET_GetSet()

		#set settings info into textctrl 
		self.logo_path.SetValue(proj_settings[0])
		self.sample_unit.SetValue(proj_settings[1])


	def __del__(self):
		pass

	def SET_browse(self, event):
		"""This function set the path of logo
		"""
		
		with wx.FileDialog(self, "Open Logo", wildcard="JPEG Files (*.jpeg)|*.jpeg| GIF Files (*.gif)|*.gif",
							style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as imgDialog:

			if imgDialog.ShowModal() == wx.ID_CANCEL:
				return #If the user cancel

			img_path = imgDialog.GetPath()

			self.logo_path.SetValue(img_path)
		
		return img_path


	def SET_save(self, event):
		"""This funciton save the settings of program
		"""

		#get the values of TextCtrl
		l_path_toSave = self.logo_path.GetValue()
		s_unit_toSave = self.sample_unit.GetValue()

		if not l_path_toSave:
			wx.MessageBox("Path of logo is empty", "Path of logo is empty.")

		if not s_unit_toSave:
			wx.MessageBox("Unit is empty", "Unit is empty.")

		else: 

			#Saving the settings to file
			open(self.set_path, "w").close() #Erase previous data in the text 

			with open(self.set_path, "w") as t_file: 
				t_file.write(f"{l_path_toSave}\n")
				t_file.write(f"{s_unit_toSave}")
				t_file.close()

			wx.MessageBox("The file was saved sucessfully.", "File saved ")

	def SET_cancel(self, event):
		self.Close(True)



