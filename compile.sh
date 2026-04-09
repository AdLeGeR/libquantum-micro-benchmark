riscv64-linux-gnu-gcc -static -g -O0 -DSPEC_CPU -DSPEC_CPU_LINUX -fopenmp $(ls *.c | grep -v 'shor.c') -o ../bin/riscv_run_hotspot -lm
