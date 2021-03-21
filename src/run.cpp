#include "main.hpp"

void VM ( map<string, string> func, string funcname, map <string, int> intvall, map <string, string> strvall ) {
    vector<string> vec = split( func[funcname], "3b" ), vec2, vec3;
    map <string, string> strin;
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
                if ( keyfind( strvall, hextostring( split( vdata, "6d736720" )[1] )  ) ) {
                    cout << strvall[hextostring( split( vdata, "6d736720" )[1] ) ] << endl;
                }
                else
                if ( intkeyfind(intvall, hextostring( split( vdata, "6d736720" )[1] )  ) ) {
                    cout << intvall[hextostring( split( vdata, "6d736720" )[1] ) ] << endl;
                }
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
                ans = hextostring( split( split( vdata, "2c20" )[0], "6d6f7620" )[1] );
                a = split( vdata, "2c20" )[1];
                data = strpri( a );
                if( mode == "int" ) {
                    intvall[ans] = atoi( data.c_str() );
                }
                else
                if ( mode == "str" ) {
                    strvall[ans] = data;
                }
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
            if ( vdata.find( "63616c6c" ) != string::npos ) {
                intvall.clear();
                strvall.clear();
                VM( func, split( split( vdata, "63616c6c20" )[1], "3a" )[0], intvall, strvall );
            }
            if ( vdata.find( "6a6e7020" ) != string::npos ) {
                string base, c, badata;
                base = split( vdata, "6a6e7020" )[1];
                c = split( base, "0c20" )[1];
                badata = strpri( vdata );
                if ( intifj( badata, intvall, "jnp" ) == 0 ) {
                    VM( func, c, intvall, strvall );
                }
            }
            if ( vdata.find( "6a6120" ) != string::npos ) {
                string base, c, badata;
                base = split( vdata, "6a6120" )[1];
                c = split( base, "0c20" )[1];
                badata = strpri( vdata );
                if ( intifj( badata, intvall, "ja" ) == 1 ) {
                    VM( func, c, intvall, strvall );
                }
            }
            if ( vdata.find( "6a616520" ) != string::npos ) {
                string base, a, c;
                base = split( vdata, "6a616520" )[1];
                a = strpri( split( base, "2c20" )[0] );
                b = strpri( split( split( base, "2c20" )[1], "0c20" )[0] );
                c = split( base, "0c20" )[1];
                if ( intkeyfind( intvall, a ) ) {
                    if ( intkeyfind( intvall, b ) ) {
                        if ( atoi( a.c_str() ) == atoi( b.c_str() ) ) {
                            VM( func, c, intvall, strvall );
                        }
                    }
                    else 
                    if ( atoi( a.c_str() ) == intvall[b] ) {
                        VM( func, c, intvall, strvall );
                    }
                }                
                //VM( func, c, intvall, strvall );
            }
        }
    }
}

int main( int argc, char **arg ){
    
    ifstream fin( split( arg[1], "." )[0], ios::in | ios::binary );
    string funcname, data;
    vector<string> vec;
    map<string, string> func;
    map <string, string> strvall;
    map <string, int> intvall;
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
    VM( func, "6d61696e", intvall, strvall );
    return 0;
}
