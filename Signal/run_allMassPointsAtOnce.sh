# run all the mass point at once
# This is zhenxuan first try on a big code of shell hopefully not too bad!!!
#!/bin/bash
#bash variables
# show each line and return the error line for debug
getopts "debug:" DEBUG
test -z "${DEBUG}" || set -o xtrace
set -o errexit
#------------#
File=''
EXT='auto'
PROC='ggh'
CATS="UntaggedTag_0"
SCALES=""
#SCALESCORR=""
SCALESCORR=""
#SCALESGLOBAL=""
SCALESGLOBAL=""
SMEARS="" #DRY RUN
MASSLIST="125"
ANALYSIS=""
ANALYSIS_TYPE=""
FINALSTATE="WW4q" # for HHWWgg
YEAR="2017"
FTESTONLY=0
CALCPHOSYSTONLY=0
SIMULATENOUSMASSPOINTFITTING=0
USEDCBP1G=0
SIGFITONLY=0
DONTPACKAGE=0
PACKAGEONLY=0
SIGPLOTSONLY=0
INTLUMI=1
BATCH=""
QUEUE=""
VERBOSITY=""
BS=""
SYSTEMATICS="1"

usage(){
	echo "The script runs three signal scripts in this order:"
		echo "signalFTest --> determines number of gaussians to use for fits of each Tag/Process"
		echo "calcPhotonSystConsts --> scale and smear ets of photons systematic variations"
		echo "SignalFit --> actually determine the number of gaussians to fit"
		echo "options:"
               echo "-h|--help) "
		echo "-i|--inputFile) "
		echo "-w|--website) "
		echo "-p|--procs) "
		echo "-f|--flashggCats) (default UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,UntaggedTag_4,VBFTag_0,VBFTag_1,VBFTag_2,TTHHadronicTag,TTHLeptonicTag,VHHadronicTag,VHTightTag,VHLooseTag,VHEtTag)"
		echo "--analysis) Specifies the replacement dataset to use"
                echo "--useDCB_1G) Use the functional form ofi a Double Crystal Ball + one Gaussian (same mean) (default $USEDCBP1G)"
                echo "--useSSF) SSF = Simultaneous Signal Fitting. Do a fit where the mass points are all fitted at once where the parameters have MH dependence (default $SIMULATENOUSMASSPOINTFITTING)"
		echo "--analysis_type) Analysis type used for HHWWgg. Ex) Res, EFT, NMSSM"
    echo "--FinalState) Final state used for HHWWgg. Ex) qqlnu, lnulnu, qqqq"
    echo "--ext)  (default auto)"
		echo "--fTestOnly) "
		echo "--calcPhoSystOnly) "
		echo "--sigFitOnly) "
		echo "--dontPackage) "
		echo "--packageOnly) "
		echo "--sigPlotsOnly) "
		echo "--intLumi) specified in fb^-{1} (default $INTLUMI)) "
		echo "--year) Dataset year (default $YEAR)) "
		echo "--batch) which batch system to use (None (''),LSF,IC) (default '$BATCH')) "
		echo "--queue) queue to submit jobs to (specific to batch)) "
    echo "--systematics) 0: run with empty dat file for systematics. 1: run with properly written and filled dat file for photon systematics"
}

# # options may be followed by one colon to indicate they have a required argument
# if ! options=$(getopt -u -o hi:w:p:f: -l help,inputFile:,website:,procs:,bs:,smears:,massList:,scales:,scalesCorr:,useSSF:,useDCB_1G:,scalesGlobal:,flashggCats:,analysis:,analysis_type:,FinalState:,ext:,fTestOnly,calcPhoSystOnly,sigFitOnly,dontPackage,packageOnly,sigPlotsOnly,intLumi:,year:,batch:,queue:,verbosity:,systematics:, -- "$@")
# then
# # something went wrong, getopt will put out an error message for us
# exit 1
# fi
# set -- $options

while getopts "a:pZ:" options;do
  case "${options}" in 
    a)
      NAME=${OPTARG}
      ;;
    Z)
      TIMES=${OPTARG}
  esac
done
echo $NAME
echo $TIMES
# echod

echo ${FILE}
echo ${fileDir}