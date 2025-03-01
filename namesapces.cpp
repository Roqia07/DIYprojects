// this contains basic cpp function 
/////////////
// namespaces: gives a unique vlaue even if the variable is repeated 
// a namespace is a global declaration can't be used inside functions even main
//:: scope resolution operator : specifies which namesapce i am using for which variable 
# include <iostream> //includes all input and output operations such as cin, cout etc which are accessed via std::cin
namespace first{
    int x=1;
}
namespace second{
    int x=2;
}
int main(){
    using namespace std; // adds all the functions in std without having to specify std eachtime but contains many functions with common names that may cause error
    using std::cout; // better form in that way you can use cout 3latol
    int x =0;
    std::cout<<x;
    using namespace second;
    std::cout<<first::x;
    return 0;
}
