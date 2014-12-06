#include <stdlib.h>
#include <stdio.h>

int main (int argc, char *argv[]) {

	
		char syscmd[50];

		scanf(syscmd,"python %s %s", &argv[1], &argv[2]);
		system(syscmd);

	
		FILE *f = fopen(argv[3],"rt");

		char line[120];

		printf("content-type: text/html");

		while (fgets(line,120,f) != NULL) {
			printf("%s", line);
		}

	return(0);
}