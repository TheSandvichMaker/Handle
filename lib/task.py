class Task(object):
	'''
	HDL_COMMAND			line
	HDL_EXIT			None
	HDL_UPDATE			None
	HDL_CHECKUP			None
	NET_JOB				None
	NET_SCREEN			None
	NET_VERSION			None
	NET_LINEUP			line
	NET_UPPKG
	SRV_START			None
	SRV_STOP			None
	SRV_RESTART			None
	SRV_INPUT			line
	SRV_BACKUP			None
	CLT_UPDATE			data
	CLT_INPUT			line
	CLT_LINEUP			line
	CLT_EXIT			None
	CLT_CLOSE			None
	SCH_ADD				(task, delay, [repeat])
	SCH_REMOVE			Event
	SCH_UPDATE			None
	API_REGISTER		ApiObj
	API_REMOVE			ApiObj
	API_GET				ApiObj
	API_UPDATE			ApiObj
	API_CONNECT			None
	ON_CONNECT			None
	'''
	HDL_COMMAND, HDL_EXIT, HDL_UPDATE, HDL_CHECKUP, NET_JOB, NET_SCREEN, NET_VERSION, NET_LINEUP, NET_UPPKG, SRV_START, SRV_STOP, SRV_RESTART, SRV_INPUT, SRV_BACKUP, CLT_UPDATE, CLT_INPUT, CLT_LINEUP, CLT_EXIT, CLT_CLOSE, SCH_ADD, SCH_REMOVE, API_REGISTER, API_REMOVE, API_GET, API_UPDATE, API_CONNECT, ON_CONNECT, SCH_UPDATE  = range(28)
	stype = {
		0:'HDL_COMMAND',
		1:'HDL_EXIT',
		2:'HDL_UPDATE',
		3:'HDL_CHECKUP',
		4:'NET_JOB',
		5:'NET_SCREEN',
		6:'NET_VERSION',
		7:'NET_LINEUP',
		8:'NET_UPPKG',
		9:'SRV_START',
		10:'SRV_STOP',
		11:'SRV_RESTART',
		12:'SRV_INPUT',
		13:'SRV_BACKUP',
		14:'CLT_UPDATE',
		15:'CLT_INPUT',
		16:'CLT_LINEUP',
		17:'CLT_EXIT',
		18:'CLT_CLOSE',
		19:'SCH_ADD',
		20:'SCH_REMOVE',
		21:'API_REGISTER',
		22:'API_REMOVE',
		23:'API_GET',
		24:'API_UPDATE',
		25:'API_CONNECT',
		26:'ON_CONNECT',
		27:'SCH_UPDATE'
		}

	def __init__(self, type, data=None):
		self.type = type
		self.data = data
		#self.types = self.stype['type']