#include "header.h"

using namespace std;

double NewtonRaphsonStudent::NewtonRaphson(func Function, func Derivative, double start, double accu)
{
    //write your code here
    double xi = start;
    while(abs(Function(xi) - 0) > accu)
    {
        double xi1 = xi - Function(xi) / Derivative(xi);
        xi = xi1;
    }
    
    return xi;
}
