/* 2/5~ */
#pragma once
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <regex>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <utility>
#include <algorithm>

//----------------------

using namespace std;

//----------------------

void run ( string filename );
vector <string> split( string str, string separator ) ; 
map <string, string> todict ( string sent, map <string, string> dict ) ;
void print ( string word ) ;
void printint ( int word) ;
vector<string> import( string funcname, string filename ) ;
string replace( string data, string replace_word ) ;
vector<string> remove(vector<string> vector, int index) ;
bool keyfind(map<string, string> m, string v) ;
string calc( string data, map<string, string> valls, string mark ) ;
int ifj( string data, map<string, string> valls, string mark ) ;
void VM( map<string, string>func, string funcname ) ;
vector<string> inc ( string callfunc );
vector<int> hex(const char *string) ;
unsigned int binToUInt(const string &str) ;