all:
	g++ -c src/comp.cpp -std=c++14
	g++ -c src/define.cpp -std=c++14
	g++ -c src/run.cpp -std=c++14
	g++ -c src/proto.cpp -std=c++14
	g++ comp.o define.o -o bin/comp
	g++ run.o define.o -o bin/run
	g++ proto.o define.o -o bin/proto 
	rm *.o
