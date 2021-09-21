#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  uint8_t *buffer;
  uint32_t len;
  uint32_t capacity;
} vector;

vector *table[10] = {NULL};

uint64_t next_pow2(uint64_t x) {
  if (x <= 1) {
    return x;
  }
  return 1 << (64 - __builtin_clz(x - 1));
}

void append(vector *v, uint8_t *buffer, uint32_t len) {
  if (v->len + len > v->capacity) {
    uint32_t next = next_pow2(v->len + len);
    v->buffer = realloc(v->buffer, next);
    v->capacity = next;
  }
  memcpy(&v->buffer[v->len], buffer, len);
  v->len += len;
}

void destroy(vector *v) {
  if (v->buffer != NULL) {
    free(v->buffer);
  }
  v->buffer = NULL;
  v->len = 0;
  v->capacity = 0;
}

void create_vector(int index) {
  if (index < 0 || index >= 10) {
    return;
  }
  table[index] = malloc(sizeof(vector));
  printf("Done!\n");
}

void destroy_vector(int index) {
  if (index < 0 || index >= 10) {
    return;
  }

  if (table[index] == NULL) {
    printf("No vector there!\n");
    return;
  }
  destroy(table[index]);
  free(table[index]);
  table[index] = NULL;
  printf("Done!\n");
}

void append_vector(int index) {
  if (index < 0 || index >= 10) {
    return;
  }

  if (table[index] == NULL) {
    printf("No vector there!\n");
    return;
  }
  printf("Length?\n");
  printf("> ");
  char buf[5];
  fgets(buf, 5, stdin);
  int length = atoi(buf);
  if (length < 0) {
    printf("Invalid!\n");
    return;
  }
  uint8_t *temp = malloc(length);
  fread(temp, 1, length, stdin);
  append(table[index], temp, length);
  free(temp);
  printf("Done!\n");
}

void show_vector(int index) {
  if (index < 0 || index >= 10) {
    return;
  }

  if (table[index] == NULL) {
    printf("No vector there!\n");
    return;
  }
  if (table[index]->buffer == NULL) {
    printf("Vecc is empty!\n");
    return;
  }
  vector *v = table[index];
  fwrite(v->buffer, 1, v->len, stdout);
  printf("\n");
}