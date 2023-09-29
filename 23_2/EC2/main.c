#include <stdio.h>
#include <string.h>

int memoria[50][50];

int min(int a, int b, int c);

int calcdistancia(char *cad1,char *cad2,int i,int j);

int main(){
    memset(memoria,-1,sizeof(memoria));
    char x[] = "erro";
    char y[] = "acerto";
    int i = strlen(x);
    int j = strlen(y);
    printf("%d",calcdistancia(x,y,i,j));
}

int min(int a, int b, int c){
    if(a<=b && a<=c) 
        return a;
    if(b<=a && b<=c)
        return b;
    else
        return c;
}

int calcdistancia(char *cad1,char *cad2,int i,int j){
    int inserir,remover,substituir;
    if(j==0)
        return i;
    if(i==0)
        return j;
    if(memoria[i][j] != -1)
        return memoria[i][j];
    if(cad1[i-1]==cad2[j-1])
        memoria[i][j] = calcdistancia(cad1,cad2,i-1,j-1);
    else{
        inserir = 1+calcdistancia(cad1,cad2,i,j-1);
        remover = 1+calcdistancia(cad1,cad2,i-1,j);
        substituir = 1+calcdistancia(cad1,cad2,i-1,j-1);
        memoria[i][j] = min(inserir,remover,substituir);
    }
    return memoria[i][j];
}