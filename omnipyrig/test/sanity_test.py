import omnipyrig

#create a new instance
OmniClient = omnipyrig.OmniRigWrapper()

'''
OmniClient.setActiveRig(1)
RigType = OmniClient.getParam("RigType")
print(f'Rig 1: {RigType}')
'''

OmniClient.setActiveRig(2)
RigType = OmniClient.getParam("RigType")
print(f'Rig 2: {RigType}')

OmniClient.setFrequency("A",14255000)
OmniClient.setMode(OmniClient.MODE_SSB_U)
OmniClient.setRitOffset(50)
OmniClient.setRit(OmniClient.RIT_ON)
#OmniClient.setXit(OmniClient.XIT_OFF)
OmniClient.setSplit(OmniClient.SPLIT_OFF)
OmniClient.setVfoA()

'''
StatusStr = OmniClient.getParam("StatusStr")
print(StatusStr)
ClearRit = OmniClient.getParam("ClearRit")
print(ClearRit)
Freq = OmniClient.getParam("Freq")
print(Freq)
FreqA = OmniClient.getParam("FreqA")
print(FreqA)
FreqB = OmniClient.getParam("FreqB")
print(FreqB)
FrequencyOfTone = OmniClient.getParam("FrequencyOfTone")
print(FrequencyOfTone)
GetRxFrequency = OmniClient.getParam("GetRxFrequency")
print(GetRxFrequency)
GetTxFrequency = OmniClient.getParam("GetTxFrequency")
print(GetTxFrequency)
IsParamReadable = OmniClient.getParam("IsParamReadable")
print(IsParamReadable)
Mode = OmniClient.getParam("Mode")
print(Mode)
Pitch = OmniClient.getParam("Pitch")
print(Pitch)
cts,dsr,dtr,rts = OmniClient.getParam("PortBits")
print(f'{cts},{dsr},{dtr},{rts}')
ReadableParams = OmniClient.getParam("ReadableParams")
print(ReadableParams)
RigType = OmniClient.getParam("RigType")
print(RigType)
Rit = OmniClient.getParam("Rit")
print(Rit)
RitOffset = OmniClient.getParam("RitOffset")
print(RitOffset)
Split = OmniClient.getParam("Split")
print(Split)
Status = OmniClient.getParam("Status")
print(Status)
Tx = OmniClient.getParam("Tx")
print(Tx)
Vfo = OmniClient.getParam("Vfo")
print(Vfo)
WriteableParams = OmniClient.getParam("WriteableParams")
print(WriteableParams)
Xit = OmniClient.getParam("Xit")
print(Xit)
'''