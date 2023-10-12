#include <stdio.h>



long int exp(long int a,long int n);

int main(){
    long int a,n;
    for(int i =0;i<10;i++){
    printf("Digite o valor de a e n: ");
    scanf("%ld %ld",&a,&n);
    if(exp(a,n)!=-1)
        printf("O valor de a^n eh: %ld.\n",exp(a,n));
    else
        printf("Indeterminacao! (0^0)\n");
    }
    return 0;
}

long int exp(long int a,long int n){
    if(!(a==0 && n == 0)){
        if(a==1 || a==0)
            return a;
        if(n==0)
            return 1;
        else{
            if(n%2==0){
                return exp(a,n/2)*exp(a,n/2);
            }else{
                return a*exp(a,n/2)*exp(a,n/2);
            }
        }
    }
    else
        return -1;
}