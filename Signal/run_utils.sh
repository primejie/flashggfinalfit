whichAction=${1}
if [ $whichAction == 0 ]
    then
    cd /eos/user/z/zhenxuan/hhwwgg_root/ws_gghh/
    mv output_M300_hhwwgg_MC_gghh.root output_M300_hhwwgg_MC_pythia8_gghh.root 
    mv output_M700_hhwwgg_MC_gghh.root output_M700_hhwwgg_MC_pythia8_gghh.root 
    mv output_M1750_hhwwgg_MC_gghh.root output_M1750_hhwwgg_MC_pythia8_gghh.root 
    mv output_M3000_hhwwgg_MC_gghh.root output_M3000_hhwwgg_MC_pythia8_gghh.root 
fi
if [ $whichAction == 1 ]
    then
    echo 'running mv workspace to different directorys'
    cd /eos/user/z/zhenxuan/hhwwgg_root/ws_gghh/
    mv output_GGHH300_M125_13TeV_amcatnloFXFX_pythia8_gghh.root ../ws_gghh_300/
    mv output_GGHH700_M125_13TeV_amcatnloFXFX_pythia8_gghh.root ../ws_gghh_700/
    mv output_GGHH1750_M125_13TeV_amcatnloFXFX_pythia8_gghh.root ../ws_gghh_1750/
    mv output_GGHH3000_M125_13TeV_amcatnloFXFX_pythia8_gghh.root ../ws_gghh_3000/
fi
if [ $whichAction == 2 ]
    then
    echo 'check dir root files'
    cd /eos/user/z/zhenxuan/hhwwgg_root/
    ls *300
    ls *700
    ls *1750
    ls *3000
fi
if [ $whichAction == 3 ]
    then
    echo 'rm dir root files'
    cd /eos/user/z/zhenxuan/hhwwgg_root/
    rm ws_gghh_300/output_GGHH300_M125_13TeV_pythia8_gghh.root
    rm ws_gghh_700/output_GGHH700_M125_13TeV_pythia8_gghh.root
    rm ws_gghh_1750/output_GGHH1750_M125_13TeV_pythia8_gghh.root
    rm ws_gghh_3000/output_GGHH3000_M125_13TeV_pythia8_gghh.root
    
fi
