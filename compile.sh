gcc -DSPEC_CPU -DSPEC_CPU_LINUX -fopenmp $(ls *.c | grep -v 'shor.c') -o ../bin/run_hotspot -lm
