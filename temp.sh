output=$(python3 kmeans.py 8 517log.txt)
run_hotspot=$(echo $output | sed -n '11p')
h_nums=$(echo $output | sed -n '9p')
