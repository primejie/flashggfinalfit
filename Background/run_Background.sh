############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "Add description of the script functions here."
   echo
   echo "options:"
   echo "h     Print this Help."
   echo "f     Print flag we need to run."
   echo
}

############################################################
# Process the input options. Add options as needed.        #
############################################################
# Set flag
flag="nothing"
# Get the options
while getopts ":hf:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      f) # Enter a name
         flag=$OPTARG;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done
########### begin your code ####################
if [ "$flag" = "BkgFit" ]; then
   echo "running $flag"
   python RunBackgroundScripts.py --inputConfig config_SL.py --mode fTestParallel
fi
if [ "$flag" = "cpBkg" ]; then
    # need to mv the output file(CMS-HGG_multipdf_*.root) to */ws/
   echo "running $flag"
   cp outdir_test/CMS-HGG_multipdf_RECO_untagged.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws/
   
fi
