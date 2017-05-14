/*
Note: It is guaranteed that p1, p2, p3 form a valid triangle with non-zero area. Also the x & y coordinate of all the points are integers.
Note: Point is a structure, whose definition is provided in student.cpp

struct Point{

 int x;

 int y;

 Point(int a, int b) : x(a), y(b) {}

};

*/

// Don't remove the next line
#include "point.h"

// create extra functions here
int side(Point p1, Point p2, Point p3)
{
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
}


bool is_inside_triangle(Point p1, Point p2, Point p3, Point x)
{
    // fill in your code here
    bool a, b, c;
    a = side(x, p1, p2) < 0;
    b = side(x, p2, p3) < 0;
    c = side(x, p3, p1) < 0;
    return ((a==b) && (b==c));
}
