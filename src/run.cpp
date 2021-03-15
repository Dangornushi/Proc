#include "main.hpp"

void VM ( map<string, string> func, string funcname ) {
    vector<string> vec = split( func[funcname], "3b" );
    string vdata;
    for ( int i = 0; i < vec.size(); i++ ) {
        vdata = vec[i];
        if ( vdata != "" ) {
            cout << vdata << endl;
        }
    }
}

int main( int argc, char **arg ){
    
    ifstream fin( split( arg[1], "." )[0], ios::in | ios::binary );
    string funcname, data;
    vector<string> vec;
    map<string, string> func;
    int hex;

    char buf[16];
    while(!fin.eof()) {
        fin.read(buf,sizeof(16));
        string data2( buf, 4 );
        data += data2;
    }
    vec = split( data, "3b" );
    for ( int i = 0; i < vec.size(); i++ ) {
        vec[i] = vec[i] + "3b";
        if ( vec[i].find("3a") != string::npos ) {
            funcname = split( vec[i], "3a" )[0];
            func[funcname] += split( vec[i], "3a" )[1];
        }
        else {
            func[funcname] += vec[i];
        }
    }
    VM( func, funcname );
    return 0;
}

//mode>int
