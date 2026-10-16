#include <stdio.h>
#include <string.h>
char *gets(char *);
FILE *flag;
void win(void) {
  puts("You Win!");
  flag = fopen("flag.txt", "r");
  char buf[100];
  fgets(buf, 100, flag);
  printf("%s", buf);
  fflush(stdout); 
  fclose(flag);
}
void vuln(const char *buff) {
 gets(buff);
 printf("Selamat datang %s",buff);
}
int main(void) {
  char input[64];
  printf("Siapa Namanua? \n");
  vuln(input);
  return 0;
}