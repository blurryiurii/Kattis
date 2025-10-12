#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef union {
  uint32_t raw;
  struct {
    uint8_t row, col, value;
  };
} node_t;

typedef char __invalid_union_size[(sizeof(node_t) == 4) - 1];

int main() {
  int rows, cols;
  scanf("%d %d", &rows, &cols);
  int row_start, col_start;
  scanf("%d %d", &row_start, &col_start);
  int row_end, col_end;
  scanf("%d %d", &row_end, &col_end);

  
}