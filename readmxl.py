import os
import xml.etree.ElementTree as ET


def parseMusicXMLFile(file):
    tree = ET.parse(file)
    root = tree.getroot()
    part=root.find('part')
    timesignum=0
    timesigden=0
    divisions=0
    for attribute in part.find('measure').findall('attributes'):
        time = attribute.find('time')
        if time is not None:
            timesignum = time.find('beats').text
            timesigden = time.find('beat-type').text
        div = attribute.find('divisions')
        if div is not None:
            divisions=div.text
    if timesignum!='4' or timesigden!='4':
        return
    if divisions is None:
        print "divisions is none...uh oh"
    
    for part in root.findall('part'):
        for measure in part.findall('measure'):
            measurestr = ""
            measureLength = 0
            for note in measure.findall('note'):
                if note.find('grace') is not None:
                    print "grace note" 
                else:
                    duration = int(note.find('duration').text)
                    durations.append(duration)
                    measureLength +=duration
                    measurestr += str(duration) + " "
            print measurestr, measureLength, "divisions: ", divisions
        print "next part"

os.chdir('musicxmlset')
files=os.listdir('.')
durations=[]
for file in files:
    print "for file " + file
    parseMusicXMLFile(file)
##parseMusicXMLFile(files[0])
