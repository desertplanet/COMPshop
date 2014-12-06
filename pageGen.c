#include <stdlib.h>
#include <stdio.h>

int main (int argc, char *argv[]) {

	
		char syscmd[50];

		char input[40];

		char uName[30];

		fgets(input,40,stdin);

		int i = 9;

		while (input[i] != '\0') {
			uName[i] = input[i];
		}

		scanf(syscmd,"python createCatalogue.py %s", uName);
		
		system(syscmd);

	
		FILE *f = fopen("catalogue.html","rt");

		char line[120];

		printf("content-type: text/html");

		while (fgets(line,120,f) != NULL) {
			printf("%s", line);
		}

	return(0);
}