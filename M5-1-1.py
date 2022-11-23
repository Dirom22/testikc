
fgr = {'1': 'один', '2':'два', '3':'три', '4':'четыре'}

class StringVar:
	
	def __init__(self, name):
		self.name = name

	def sett(self):
		self.fgr = fgr
		print(set(fgr))


	def gett(self):
		self.fgr = fgr
		print(fgr.keys())
		print(fgr.values())

d1 = StringVar('fgr')
d1.sett()
d1.gett()