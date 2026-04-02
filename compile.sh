gcc -DSPEC_CPU -DSPEC_CPU_LINUX $(ls *.c | grep -v 'shor.c') -o ../bin/pure -lm
