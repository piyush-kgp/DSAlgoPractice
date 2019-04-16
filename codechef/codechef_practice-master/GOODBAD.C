#include <stdio.h>
 
void main(){
    char S[1000];
    int t,n,k,u,l;
    scanf("%d", &t);
    while(t>0){
    scanf("%d %d", &n, &k);
    scanf("%s", S);
    char c;
    char A='A';
    char Z='Z';
    char a='a';
    char z='z';
    u=l=0;
    while(n>=0){
        c=S[n];
        if(c>=A&&c<=Z){
            u++;
        }
        if(c>=a&&c<=z){
            l++;
        }
        n--;
    }
    //printf("%d %d\n", u, l);
    int chef, bro;
    chef = bro=0;
    if(u<=k){
        chef++;
    }
    if(l<=k){
        bro++;
    }
    if(chef==1&bro==0){
        printf("chef\n");
    }
    if(chef==0&bro==1){
        printf("brother\n");
    }
    if(chef==1&bro==1){
        printf("both\n");
    }
    if(chef==0&bro==0){
        printf("none\n");
    }
        t--;
    }
    
}
 
        