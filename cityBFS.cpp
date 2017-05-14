//#include "header.h"
/*
  Do not remove the "header.h" file.
*/

//-----Include any additional required headers here-----
#include <iostream>
#include <queue>
//-----End of additional headers-----

//-----Add new functions here(if any)-----


//-----New functions end here-----

/* You need to write the implementation of the given function.
             ( You may write any additional helper functions you want in the specified region only.
               Do not change the signature of the function already given)
               For detailed explanation of the question refer to the Description part) 
*/

void move(int coordinateX, int coordinateY, queue<int> & Qx, queue<int> & Qy, vector<vector<char> > & graph , vector<vector<bool> > & visited , vector <char> & answer)
{   // DO NOT CHANGE THIS!
    /*
    coordinateX, coordinateY are your current coordinates
    Qx,Qy are the queues where you have to store the coordinates of x and y for the valid blocks
    graph is the matrix representation for the city as a 2D vector
    */
    // start your code below this line
    Qx.push(coordinateX);
    Qy.push(coordinateY);
    visited[coordinateX][coordinateY] = true;

    while(graph[coordinateX][coordinateY] != 't'){
                //Look right
        if(coordinateY < 9){
            if(graph[coordinateX][coordinateY + 1] != 'x' && visited[coordinateX][coordinateY + 1] == false){
                Qx.push(coordinateX);
                Qy.push(coordinateY + 1);
                visited[coordinateX][coordinateY + 1] = true;
                answer.push_back(graph[coordinateX][coordinateY + 1]);
            }
        }
        //Look down
        if(coordinateX < 9){
            if(graph[coordinateX + 1][coordinateY] != 'x' && visited[coordinateX + 1][coordinateY] == false){
                Qx.push(coordinateX + 1);
                Qy.push(coordinateY);
                visited[coordinateX + 1][coordinateY] = true;
                answer.push_back(graph[coordinateX + 1][coordinateY]);
            }
        }
        //Look left
        if(coordinateY > 0){
            if(graph[coordinateX][coordinateY - 1] != 'x' && visited[coordinateX][coordinateY - 1] == false){
                Qx.push(coordinateX);
                Qy.push(coordinateY - 1);
                visited[coordinateX][coordinateY - 1] = true;
                answer.push_back(graph[coordinateX][coordinateY - 1]);
            }
        }
        //Look up
        if(coordinateX > 0){
            if(graph[coordinateX - 1][coordinateY] != 'x' && visited[coordinateX - 1][coordinateY] == false){
                Qx.push(coordinateX - 1);
                Qy.push(coordinateY);
                visited[coordinateX - 1][coordinateY] = true;
                answer.push_back(graph[coordinateX - 1][coordinateY]);
            }
        }

        Qx.pop();
        Qy.pop();
        if(Qx.empty()){
            break;
        }
        else{
            coordinateX = Qx.front();
            coordinateY = Qy.front();
        }
    }
    
}