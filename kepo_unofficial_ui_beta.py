# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		self.NPM = ""
		self.Nilai=""
		self.Bimbingan=""
		self.pertemuan=""
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 197,201 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1111 = wx.StaticText( self, wx.ID_ANY, u"Mhs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )
		bSizer2111.Add( self.m_staticText1111, 0, wx.ALL|wx.EXPAND, 5 )
		
		comboMhsChoices = [ u"Luthfi", u"Hagan" ]
		self.comboMhs = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboMhsChoices, 0 )
		bSizer2111.Add( self.comboMhs, 0, wx.ALL|wx.FIXED_MINSIZE, 5 )
		
		
		bSizer1.Add( bSizer2111, 1, wx.ALIGN_RIGHT|wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		bSizer211.Add( self.m_staticText111, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.progressInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.progressInput, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer211, 1, wx.ALIGN_RIGHT|wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Nilai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer21.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.nilaiInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.nilaiInput, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer21, 1, wx.ALIGN_RIGHT, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Pertemuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer22.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.pertemuanInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.pertemuanInput, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();
		
		bSizer1.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		# Connect Events
		self.comboMhs.Bind( wx.EVT_COMBOBOX, self.GantiConfig )
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.tampilData )
		self.progressInput.Bind( wx.EVT_CHAR, lambda event:self.CharEventProgress(event, "progress") )
		self.nilaiInput.Bind( wx.EVT_CHAR, lambda event:self.CharEventProgress(event, "nilai"))
		self.pertemuanInput.Bind( wx.EVT_CHAR, lambda event:self.CharEventProgress(event, "pertemuan"))
	
	def __del__( self ):
		pass
	
	def CharEventProgress( self, event, inputreq):
		if event.GetKeyCode() == 13:
			self.tampilData(event)
		elif event.GetKeyCode() == 9:
			if inputreq == "progress":
				self.nilaiInput.SetFocus()
			if inputreq == "nilai":
				self.pertemuanInput.SetFocus()
			if inputreq == "pertemuan":
				self.progressInput.SetFocus()
		event.Skip()

	# Virtual event handlers, overide them in your derived class
	def tampilData( self, event ):
		event.Skip()
		self.Nilai = self.nilaiInput.GetValue()
		self.Bimbingan = self.progressInput.GetValue()
		self.pertemuan = self.pertemuanInput.GetValue()
		self.generateQR()

	def GantiConfig( self, event ):
		self.PROYEK="Proyek 3"
		self.PASSWORD="sariasih54"
		self.Pembimbing="MHK"
		if event.GetString() == "Luthfi":
			self.NPM = "1174035"
			self.userrepo="sspitzenreiter"
			self.namarepo="Aplikasi-Sidang-Poltekpos"
		if event.GetString() == "Hagan":
			self.NPM = "1174040"			
			self.userrepo="sspitzenreiter"
			self.namarepo="Aplikasi-Sidang-Poltekpos"
		event.Skip()
		
	def generateQR( self ):
		if (self.Bimbingan != "" and self.Nilai != "" and self.pertemuan != "" and self.NPM != ""):
			NPM, PROYEK, PASSWORD, Pembimbing, Bimbingan, Nilai, userrepo, namarepo, pertemuan = self.NPM, self.PROYEK, self.PASSWORD, self.Pembimbing, self.Bimbingan, self.Nilai, self.userrepo, self.namarepo, self.pertemuan
			print(NPM+userrepo)
			import kepo
			import qrcode
			saya = kepo.Kepo()
			crot=saya.generateURL(NPM, PASSWORD, PROYEK, Nilai, Bimbingan, Pembimbing,userrepo,namarepo,pertemuan)
			if crot != '':
				img = qrcode.make(crot)
				img.save("./"+NPM+".png")
				print("File QrCode Telah Dibuat")
		elif self.NPM=="":
			print("Pilih MHS")
		else :
			print("Data Masih Kosong")


app = wx.App(False)
frame = MyFrame1(None)
frame.Show(True)
app.MainLoop()