#include "main.hpp"

int main( int argc, char **arg ){
    
    ifstream fin( split( arg[1], "." )[0], ios::in | ios::binary );
    string data;
    string funcname;
    vector<string> vec;
    map<string, string> func;
    
    if (!fin){
        cout << "ファイル file.txt が開けません";
        return 1;
    }
    char buf[16];
    while(!fin.eof()) {
        fin.read(buf,sizeof(1));
        string data2( buf, 16 );
        data += data2;
    }

    vec = split( data, "3b" );
    for ( int i =0; i < vec.size(); i++ ) {
        if ( vec[i].find("3a") != string::npos ) {
            funcname = split( vec[i], "3a" )[0];
            func[funcname] = split( vec[i], "3a" )[1];
        }
        else {
            func[funcname] += vec[i];//+"3a";
        }
    }
    VM( func, funcname );
    fin.close();
    return 0;
}

void VM( map<string, string>func, string funcname ) {
    vector<string> vec = split( func[funcname], "3a" );
    for ( int i = 0; i < vec.size(); i++ ) {
        print(vec[i]);
    }
}
