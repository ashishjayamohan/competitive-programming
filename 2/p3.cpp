#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
const double eps=1e-5;
struct point
{
    double x,y;
    double r;
}p[3];
double dist(double x, double y,point tp){
    return sqrt((x-tp.x)*(x-tp.x)+(y-tp.y)*(y-tp.y));
}
double cost(double x, double y){
    double ang[3];

    for(int i=0;i<3;++i){
        ang[i]=dist(x,y,p[i])/p[i].r; //sin
    }
    double d[3];
    for(int i=0;i<3;++i){
        d[i]=ang[i]-ang[(i+1)%3]; //the difference between the angles of view
    }
    double ans=0;
    for(int i=0;i<3;++i){
                 Ans+=d[i]*d[i] ; //similar variance
    }
    return ans;
}
main(){

    for(int i=0;i<3;i++){
        scanf("%lf%lf%lf",&p[i].x,&p[i].y,&p[i].r);
    }
    double x=0,y=0;
    for (int i = 0; i < 3; ++i)
    {
                 x+=p[i].x/3;y+=p[i].y/3; //Search in the center of gravity attachment
    }
    double t=1.0;
    while(t>eps){
        int kase=0;
        double tp=cost(x,y);
        if(cost(x+t,y)<tp){
            x+=t;kase=1;
        }else if(cost(x-t,y)<tp){
            x-=t;kase=1;
        }else if(cost(x,y-t)<tp){
            y-=t;kase=1;
        }else if(cost(x,y+t)<tp){
            y+=t;kase=1;
        }
                 If (!kase) //No better solutions around the world
        {
            t/=2;
        }
    }
        if(fabs(cost(x,y)<eps)){
            printf("%lf %lf\n",x,y);
        }
    return 0;
}
