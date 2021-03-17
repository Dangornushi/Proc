#include "main.hpp"

void VM ( map<string, string> func, string funcname ) {
    vector<string> vec = split( func[funcname], "3b" ), vec2, vec3;
    map <string, string> strin;
    map <string, int> intvall;
    map <string, string> strvall;
    string vdata, ans, a, b, mode;
    stringstream ss, ss2;

    strin["30"] = "0";
    strin["31"] = "1";
    strin["32"] = "2";
    strin["33"] = "3";
    strin["34"] = "4";
    strin["35"] = "5";
    strin["36"] = "6";
    strin["37"] = "7";
    strin["38"] = "8";
    strin["39"] = "9";

    int y, x;
    for ( int i = 0; i < vec.size(); i++ ) {
        vdata = vec[i];
        vdata = regex_replace( vdata, regex("22"),"20");
        if ( vdata != "" ) {
            if ( vdata.find( "61646420" ) != string::npos ) {
                a = split( split( vdata, "2c" )[0], "61646420" )[1];
                b = split( vdata, "2c20" )[1];//3536
                ans = split( split( vdata, "2c" )[0], "61646420" )[1];
                ss << hex << atoi( b.substr( 0, 2 ).c_str() );
                ss2 << hex << atoi( b.substr( 2, 4 ).c_str() );
                a = ss.str();
                b = ss2.str();
                a = a+b;

                if ( intkeyfind( intvall, a ) ) {
                    intvall[ans] = intvall[a] + y;
                }
                else {
                    intvall[ans] = atoi( a.c_str() );
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
                ans = split( split( vdata, "2c20" )[0], "6d6f7620" )[1];
                int x, i2 = 0;
                string c, d;
                b = split( vdata, "2c20" )[1];
                vec2 = split( b, "3" );
                for ( int i = 0; i < vec2.size(); i++ ) {
                    a = strin["3"+vec2[i]];
                    c += a;
                }
                if ( mode == "int" ) {
                    intvall[ans] = atoi( c.c_str() );
                }
                else
                if ( b.find( "20" ) != string::npos && mode == "str" ) {
                    b = regex_replace( b, regex( "20" ), "" );
                    for ( int  i = 0; i < b.size()-3; i++ ) {
                        d += stoi( b.substr( i, i+2 ), NULL, 16 );
                    }
                    strvall[ans] = d;
                }
                else
                if ( mode == "str" ) {
                    strvall[ans] = c;
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
