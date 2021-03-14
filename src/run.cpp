#include "main.hpp"

int main( int argc, char **arg ){
    ifstream file;
    char buf[16];
    int i2;
    map<int, string> map1;
    map<string, string> func;
    vector<string> vec;
    
    file.open(split( arg[1], "." )[0],std::ios::in|std::ios::binary);
    if ( !file.is_open() ) {
        cout <<  "file open error" << endl;
        return EXIT_FAILURE;
    }
    
    while( !file.eof() ) {
        i2 = 0;
        file.read(buf,sizeof(1));
        for(int i=0,size=file.gcount();i<size;++i) {
            string bu( 1, buf[i] );
            map1[i2] += bu;
            i2 ++;
        }
    }

    vec = split( map1[0], ";" );
    string funcname;
    for ( int i = 0; i < vec.size(); i++ ) {
        if ( vec[i].find(":") != string::npos ) {
            funcname = "";
            funcname = split( vec[i], ":" )[0];
            func[funcname] += split( vec[i], ":" )[1]+";";
        }
        else {
            func[funcname] += vec[i]+";";
        }
    }
    if ( funcname != "main" ) {
        print(funcname);
    }

    file.close();
    return 0;
}
