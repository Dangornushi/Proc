#include "main.hpp"

int main( int argc, char **arg ){
    
    ifstream fin( split( arg[1], "." )[0], ios::in | ios::binary );
    string data;
    string funcname;
    vector<string> vec;
    map<string, string> func;
    int hex;

    char buf[16];
    while(!fin.eof()) {
        fin.read(buf,sizeof(1));
        //print(buf);
        cout << buf << endl;
    }
    return 0;
}
