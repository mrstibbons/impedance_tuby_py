import pyaudio

pa = pyaudio.PyAudio()
api_count = pa.get_host_api_count()
dev_count = pa.get_device_count()
api_infos = []

print "Avaiable Host-Apis:"
for i in range(api_count):
    api_info = pa.get_host_api_info_by_index(i)
    api_infos.append(api_info)
    print "  name: " + str(api_info['name'])
    print "    device count: " + str(api_info['deviceCount'])
    print "    default input: " + str(api_info['defaultInputDevice'])
    print "    default output: " + str(api_info['defaultOutputDevice'])

print "---------------------------------------------------------------------"

print "Available Devices: "

for dev in range(dev_count):
    dev_info = pa.get_device_info_by_index(dev)
    print "Name: " + dev_info['name']
    print "  Device Index: " + str(dev)
    print "  Host Api: " + api_infos[dev_info['hostApi']]['name']
    print "  Input Channels: " + str(dev_info['maxInputChannels'])
    print "  Output Channels: " + str(dev_info['maxOutputChannels'])
    print "  Default Sampling Rate: " + str(dev_info['defaultSampleRate'])