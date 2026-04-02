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

struct log_struct{
    int control1;
    int control2;
    int target;
}

int main(int argc, char **argv) {

