#include <stdlib.h>
#include <stdio.h>

int main (int argc, char *argv[]) {

	if (argc == 2) {
		FILE *f = fopen(argv[1],"rt");

		char line[120];

		printf("content-type: text/html");

		while (fgets(line,120,f) != NULL) {
			printf("%s", line);
		}

	} else {
		printf("FILE ERROR\n");
		return(1);
	}

	return(0);
}