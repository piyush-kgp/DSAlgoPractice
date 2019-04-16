
#include <stdio.h>
void main(){
    int t, a, b, c, d;
    scanf("%d", &t);
    while(t>0){
        scanf("%d %d %d %d", &a, &b, &c, &d);
        if(a==b&c==d||a==c&&b==d||a==d&&b==c){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
        t--;
    }
}
 