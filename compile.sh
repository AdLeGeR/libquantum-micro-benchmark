gcc -DSPEC_CPU -DSPEC_CPU_LINUX -DLOGS_PATH=\"../logs/${3:-arglog}\" -DCALL_NUMBERS=$1 -DCALL_COUNT=$2 *.c -o ../bin/bin_log -lm
