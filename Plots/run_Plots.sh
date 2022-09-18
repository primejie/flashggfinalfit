WhichSamples=${1}
if [ ${WhichSamples} -eq 0 ]
  then
    echo 'run plot_limits'
    python plot_limits.py --resultType 'WWgg' --unit 'fb' --ymin 0 --ymax 2 --year 2017 --yboost 0 
fi
