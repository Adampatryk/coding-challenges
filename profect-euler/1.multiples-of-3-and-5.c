#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

unsigned long long sumMultiples(unsigned long long n){
    unsigned long long sum3 = 3 * (n/3) * ((n/3)+1)/2;
    unsigned long long sum5 = 5 * (n/5) * ((n/5)+1)/2;
    unsigned long long sum15 = 15 * (n/15) * ((n/15)+1)/2;
    unsigned long long sum = sum3 + sum5 - sum15;
    
    if (n % 5 == 0 || n % 3 == 0) return sum - n;
    
    return sum;      
}

int main(){
    int t; 
    scanf("%d",&t);
    
    for(int a0 = 0; a0 < t; a0++){
        unsigned long long int n;
        scanf("%llu",&n);
        unsigned long long result = sumMultiples(n);
        printf("%llu\n", result); 
    }
    return 0;
}
