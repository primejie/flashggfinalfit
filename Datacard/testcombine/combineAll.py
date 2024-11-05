import os.path
import shutil,subprocess

# MX 
#                                                             900     1000 1100 1200 1300 1400 1500 1600 1700 1800 1900 2000 2200 2400 2600 2800 3000 3500 4000 bbbb boosted
#       300           400     500     600     700     800     900     1000 1100 1200      1400      1600      1800      2000                                   bbbb
#       300 350       400 450 500 550 600 650 700 750 800 850 900 950 1000 1100 1200      1400      1600      1800      2000                                      bbgg 
# 240 280 320 360 450 400     500 550 600     700     800     900     1000      1200      1400      1600      1800      2000                2500 3000 bbtt 

# MX_to_combine = [240, 280, 300, 400, 500, 600, 700, 800, 900, 1000 ]
MX_to_combine = [1600]


# MY
# 60 70 80 90 100 125 150 200 250 300 350 400 450 500 600 bbbb boosted
# 60 70 80 90 100 125 150 200 250 300     400     500 600     700 800 900 1000      1200      1400 1600 1800 bbbb
# 60 70 80 90 100     150     250 300     400     500 600 650 700 800 900 1000 1100 1200 1300 1400 1600 1800 2000 2200 2400 2600 2800 bbtt
#          90 100     150 200 250 300     400     500 600     700 800 900 1000      1200      1400 1600 1800 bbgg 

MY_to_combine = [ 80, 90, 100, 150, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400 ]
# MY_to_combine = [100 ]


folders_to_combine = {
    "bbbb_hy" : "/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Datacard/4b_res/datacard_mass_Xxx_Yyy.txt", # scalling all signals to 1 fb X BR (H)
    "bbgg_hy" : "/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Datacard/bbgg/datacard_mass_Xxx_Yyy.txt", # scalling all signals to 1 fb X BR (H)
    # "bbtt_hy" : "bbtt/HY/v3/datacard_mass_Xxx_Yyy.txt", # scalling all signals to 1 fb X BR (H)
    "bbbb_boosted_hy" : "/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Datacard/4b_boost/datacard_mass_Xxx_Yyy.txt", # scalling all signals to 1 fb X BR (H)
}
   
for MX in MX_to_combine :
    for MY in MY_to_combine :
        command = "combineCards.py "
        counter = 0
        for channel in folders_to_combine.keys() :
            file_to_test = "%s" % folders_to_combine[channel].replace("xx", str(MX)).replace("yy", str(MY))
            print(file_to_test)
            if os.path.isfile(file_to_test) :
                command += "%s=%s " % (channel, file_to_test)
                counter += 1
        command += " > datacard_mass_X%s_Y%s.txt" % (str(MX), str(MY))
        
        if counter > 0 :
            print(MX, MY, command)
            proc=subprocess.Popen([command],shell=True,stdout=subprocess.PIPE)
            out = proc.stdout.read()


