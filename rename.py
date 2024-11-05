import os,re
directory = os.listdir('/afs/cern.ch/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Signal')
os.chdir('/afs/cern.ch/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Signal')
key = 'config_2018'
for file in directory:
    if key in file:
        open_file = open(file,'r')
        read_file = open_file.read()
        regex =re.compile('2018')
        read_file = regex.sub('2017',read_file)
        refile = file.split("_2018_")[-1]
        write_file = open("config_2017_"+refile,'w')
        write_file.write(read_file)