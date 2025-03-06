#include <iostream>
#include <vector>

typedef std::string text_t;
typedef int number;
using number =int;// equals using typedef
int main(){
    using std::cout;
    text_t firstname="blah"; // instead of using std::string ana 3rft string k text_t bra7ty
    number x=10;
    cout<<x<<" "<<firstname<<std::endl;

//pointers= variable that stores address of a variable
//& address of operator
//* derefrence operator
// 

std::string name="bro";
std::string *pName=&name;
cout<<*pName;
    return 0;
}


