//C Code for implementation of solving problem of Tower of Hanoi

#include <stdio.h>
#include <stdlib.h>
void towers_of_hanoi(int,int,int,int);
long long steps=0;
int main()
{
    int n;
    printf("ENTER THE NUMBER OF DISCS\n");
    scanf("%d",&n);
    towers_of_hanoi(n,1,2,3);
    printf("TOTAL STEPS ARE %d\n",steps);
    return 1;
}
void towers_of_hanoi(int n,int from_rod,int aux_rod,int to_rod)
{
    steps++;
    if(n==1){
        printf("MOVE FROM %d TO %d\n",from_rod,to_rod);
        return;
    }
    else
    {
       towers_of_hanoi(n-1,from_rod,to_rod,aux_rod);
       printf("MOVE FROM %d TO %d\n",from_rod,to_rod);
       towers_of_hanoi(n-1,aux_rod,from_rod,to_rod);
    }
    return;
}
