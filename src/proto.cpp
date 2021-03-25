#include "main.hpp"

int main( int argc, char **arg ) {

    string comp = "./proc ";
    string passbuf = "./prun ";
    string name = arg[1];

    string pythonrun = "python3 main.py "+name;
    comp = comp + arg[1];
    passbuf = passbuf + split( arg[1], "." )[0];

    system(pythonrun.c_str());
    system(comp.c_str());
    //system(passbuf.c_str());

    return 0;
}
