
gcc -DSPEC_CPU -DSPEC_CPU_LINUX -fopenmp -DLOGS_PATH=\"../logs/${1:-"log.txt"}\" *.c -o ../bin/time_logs -lm
