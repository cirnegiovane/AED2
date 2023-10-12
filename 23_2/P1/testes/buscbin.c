#include <stdio.h>
#define max 10
int buscbin(int v[],int n, int inicio, int fim);

int main(){
    int n;
    int v[max] = {2,4,8,16,32,64,128,256,512,2014};
    printf("Vetor: ");
    for(int i = 0; i<10;i++){
        printf("%d ",v[i]);
    }
    printf("\nDigite qual vc quer achar: ");
    scanf("%d",&n);
    int id = buscbin(v,n,0,max);
    if(id != -1)
        printf("O seu elemento esta na posicao %d.",id);
    else
        printf("Elemento nao encontrado.");
    
    
}

int buscbin(int v[],int n, int inicio, int fim){
    int meio = fim/2;
    if(v[meio] == n)
        return v[meio];
    else if(v[meio]>n){
        printf("meio > n Retornando: vetor %d %d %d\n",n,0,meio);
        return buscbin(v,n,inicio,meio);
    }else{
        printf("meio < n Retornando: vetor %d %d %d\n",n,meio+1,fim);
        return buscbin(v,n,meio+1,fim);
    }
    return -1;
}