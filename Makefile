all:
	gcc torifier.c -o torifier.so -fPIC -shared -ldl -D_GNU_SOURCE
