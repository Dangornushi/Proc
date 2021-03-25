all:
	g++ -c src/comp.cpp -std=c++14
	g++ -c src/define.cpp -std=c++14
	g++ -c src/run.cpp -std=c++14
	g++ -c src/proto.cpp -std=c++14
	g++ -c src/include.cpp -std=c++14
	g++ comp.o define.o include.o -o bin/proc
	g++ run.o define.o include.o -o bin/prun
	g++ proto.o define.o include.o -o bin/proto
	rm *.o
