import os
import multiprocessing
import time
import sys
from concurrent.futures import ProcessPoolExecutor
import logging
import subprocess
sys.path.append('/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Trees2WS/')
logging.basicConfig(filename='processing.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
num_cores = multiprocessing.cpu_count()

files_2017 = ['/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2017/root/addsys/' + f for f in os.listdir('/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2017/root/addsys/') if f.endswith('.root')]
files_2018 = ['/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2018/root/addsys/' + f for f in os.listdir('/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2018/root/addsys/') if f.endswith('.root')]
files_2016pre = ['/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016pre/root/addsys/' + f for f in os.listdir('/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016pre/root/addsys/') if f.endswith('.root')]
files_2016post = ['/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016post/root/addsys/' + f for f in os.listdir('/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016post/root/addsys/') if f.endswith('.root')]
files_data=['/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/data/root/' + f for f in os.listdir('/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/data/root/') if f.endswith('.root')]

def Treews(file):
    try:
        command = ["python", "trees2ws.py", "--inputConfig", "config_sys.py", "--inputTreeFile", file, "--inputMass", "125", "--productionMode", "gghh", "--year", "2017", "--doSystematics"]

        subprocess.Popen(command)
        # result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        logging.exception(e)
    

config_2017= ['/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Signal/allsys/2017_1000/' + f for f in os.listdir('/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Signal/allsys/2017_1000/') if f.endswith('.py')]


def signalM(file):
    try:
        command1=["python", "RunSignalScripts.py" ,"--inputConfig", file , "--mode" , "fTest"]
        subprocess.Popen(command1)
        command2=["python", "RunSignalScripts.py" ,"--inputConfig", file , "--mode" , "calcPhotonSyst"]
        subprocess.Popen(command2)
        command3=["python", "RunSignalScripts.py" ,"--inputConfig", file , "--mode" , "signalFit"]
        subprocess.Popen(command3)
    except Exception as e:
        logging.exception(e)

def signalPack(file):
    name = os.path.splitext(os.path.basename(file))[0]
    cat=name.split("_")[-2]
    mass=name.split("_")[-1]

    ext=["dcb_1000_M"+mass+"_"+cat+"_2017","dcb_1000_M"+mass+"_"+cat+"_2018","dcb_1000_M"+mass+"_"+cat+"_2016pre","dcb_1000_M"+mass+"_"+cat+"_2016post"]
    year=["2017","2018","2016pre","2016post"]
    command1=["python","RunPackager.py","--cats","resolved_"+cat,"--exts",ext,"--batch","local","--massPoints","125","--mergeYears","--outputExt","packaged_mergeyears_1000_M"+mass+"_"+cat]
    subprocess.run(command1)
    command2=["python","RunPlotter.py","--procs","all","--cats","resolved_"+cat,"--years",year,"--ext","packaged_mergeyears_1000_M"+mass+"_"+cat]
    subprocess.run(command2)

def muti_process():
    with ProcessPoolExecutor(max_workers=num_cores) as pool:
        pool.map(signalM,config_2017)



if __name__ == "__main__":
    start_time = time.time()
    new_dir = '/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Signal'
    os.chdir(new_dir)
    muti_process()


    end_time = time.time()
    execution_time = end_time - start_time
    print("time",execution_time ,"s")
