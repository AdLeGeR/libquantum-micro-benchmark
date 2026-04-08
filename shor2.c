/* shor.c: Implementation of Shor's factoring algorithm

   Copyright 2003 Bjoern Butscher, Hendrik Weimer

   This file is part of libquantum

   libquantum is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published
   by the Free Software Foundation; either version 2 of the License,
   or (at your option) any later version.

   libquantum is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with libquantum; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
   USA

*/

#include <stdlib.h>
#include <stdio.h>
#if !defined(SPEC_CPU_WINDOWS_ICL)
#include <math.h>
#else
#include <mathimf.h>
#endif /* SPEC_CPU_WINDOWS_ICL */
#include <time.h>

#if !defined(SPEC_CPU)
#include <quantum.h>
#else
#include "quantum.h"
#endif /* SPEC_CPU */

/* Rahul: Must use SPEC's random number functions and not srandom and rand */
#if defined(SPEC_CPU)
#include "specrand.h"
#endif /* SPEC_CPU */

#include <string.h>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

struct log_struct{
    int control1;
    int control2;
    int target;
};

struct log_struct logs[] = {}
int main(int argc, char **argv) {

    double total_time = 0;
    size_t logs_length = sizeof(logs)/sizeof(logs[0]);
    for(int i = 0; i < logs_length; i++){
   
      // 1. читаем log_struct
      struct log_struct log = logs[i];

      int c1 = log.control1;
      int c2 = log.control2;
      int tg = log.target;

      // 2. читаем quantum_reg_struct (но указатели игнорируем!)
      quantum_reg* reg = malloc(sizeof(quantum_reg));
      struct quantum_reg_struct tmp_reg = log->reg;
      
      // копируем только полезные поля
      reg->width = tmp_reg.width;
      reg->size  = tmp_reg.size;
      reg->hashw = tmp_reg.hashw;

      // 3. выделяем память
      reg->node = (quantum_reg_node*)malloc(reg->size * sizeof(quantum_reg_node));
      reg->hash = (int*)malloc(reg->hashw * sizeof(int));

      // 4. читаем node массив
      //fread(reg->node, sizeof(struct quantum_reg_node_struct), reg->size, file);
      memcpy(reg->node, tmp_reg->node, reg->size);

      // 5. читаем hash массив
      //fread(reg->hash, sizeof(int), reg->hashw, file);
      memcpy(reg->hash, tmp_reg->hash, reg->hashw);


      // проверка
      //printf("%d %d %d %d %d %d\n", c1, c2, tg,
      //      reg->width, reg->size, reg->hashw);
      quantum_reg* temp_reg = malloc(sizeof(quantum_reg));
      temp_reg->node = malloc(sizeof(quantum_reg_node) * reg->size);
      temp_reg->hash = malloc(sizeof(int) * reg->hashw);
      double hotspot_time = 0;
      for(int j = 0 ; j < repeat_count; j++){
        temp_reg->width = reg->width;
        temp_reg->size  = reg->size;
        temp_reg->hashw = reg->hashw;

        memcpy(temp_reg->node, reg->node, sizeof(quantum_reg_node) * reg->size);

        memcpy(temp_reg->hash, reg->hash, sizeof(int) * reg->hashw);

        double start = omp_get_wtime();
        quantum_toffoli(c1, c2, tg, temp_reg);
        double end = omp_get_wtime();
        hotspot_time += end-start;
      }
      total_time += hotspot_time;

      free(temp_reg->hash);
      free(temp_reg->node);
      free(temp_reg);
      printf("hotspot time: %lf\n", (double)(hotspot_time));
    }
    printf("total time: %lf\n", total_time);
}
