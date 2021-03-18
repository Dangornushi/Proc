#include "main.hpp"

void VM ( map<string, string> func, string funcname ) {
    vector<string> vec = split( func[funcname], "3b" ), vec2, vec3;
    map <string, string> strin;
    map <string, int> intvall;
    map <string, string> strvall;
    string vdata, ans, a, b, mode, anser;
    stringstream ss, ss2;

    int y, x;
    for ( int i = 0; i < vec.size(); i++ ) {
        vdata = vec[i];
        vdata = regex_replace( vdata, regex("22"),"20");
        if ( vdata != "" ) {
            if ( vdata.find( "61646420" ) != string::npos ) {
                a = hextostring( split( split( vdata, "2c" )[0], "61646420" )[1] );
                b = hextostring( split( vdata, "2c20" )[1] );
                ans = split( split( vdata, "2c" )[0], "61646420" )[1];
                if ( intkeyfind( intvall, a ) ) {
                    intvall[ans] = intvall[a] + y;
                }
                else {
                    intvall[ans] = atoi( a.c_str() );
                }
            }
            if ( vdata.find( "6d736720" ) != string::npos ) {
                cout << intvall[hextostring( split( vdata, "6d736720" )[1] )] << endl;
            }
            if ( vdata.find( "70757420" ) != string::npos ) {
                if ( vdata.substr( 8, 9 ) == "20" ) {
                    print(vdata.substr( 10, vdata.size() ));
                }
                else {
                    a = split( vdata, "20" )[1];
                    if ( keyfind( strvall, a ) ) {
                        print( strvall[a] );
                    }
                    else {
                        printint( intvall[a] );
                    }
                }
            }

            if ( vdata.find( "6d6f7620" ) != string::npos ) {
                string data, a;
                ans = split( split( vdata, "2c20" )[0], "6d6f7620" )[1];
                a = split( vdata, "2c20" )[1];
                a = strspli( ans.size(), a );
                vec = split( a, ":" );
                for ( int i = 0; i < vec.size(); ++i ) {
                    a += strpri( vec[i], ans );
                }
                //print(a);
                //vec2 = strpri( hextostring( vec[i] ) );
            }
            if ( vdata.find( "6d6f64653e" ) != string::npos ) {
                if ( split( vdata, "6d6f64653e" )[1] == "696e74" ) {
                    mode = "int";
                }
                else
                if ( split( vdata, "6d6f64653e" )[1] == "737472" ) {
                    mode = "str";
                }
            }
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
