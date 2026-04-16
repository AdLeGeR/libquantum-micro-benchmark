
for ((i=0; i<$1; i++)); do
  echo "iter $i"
  gcc -DSPEC_CPU -DSPEC_CPU_LINUX -fopenmp -DLOGS_PATH=\"../logs/logarr$i.txt\" -DLOGS_COUNT=${2:-50000} *.c -o ../bin/many_time_logs -lm
  ../bin/many_time_logs $3
done

