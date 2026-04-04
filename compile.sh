
gcc -DSPEC_CPU -DSPEC_CPU_LINUX -fopenmp -DLOGS_PATH=\"../logs/${1:-"log.txt"}\" -DLOGS_COUNT=${2:-50000} *.c -o ../bin/time_logs -lm
