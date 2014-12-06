#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main (void) {

	
		char *syscmd = (char *)calloc(50,1);

		char *input = (char *)calloc(40,1);

		char *uName = (char *)calloc(40,1);


		fgets(input,40,stdin);

		int i = 0;

		while (*(i+input) != '\0') {
			*(i+uName) = *(9+i+input);
			i++;
		}

		sprintf(syscmd,"python cgi-bin/createCatalogue.py %s",uName);

		printf("content-type: text/html\n\n");

		printf("%s\n", syscmd);

		
		system(syscmd);

	
		FILE *f = fopen("catalogue.html","rt");

		char line[120];

		

		while (fgets(line,120,f) != NULL) {
			printf("%s", line);
		}

	return 0;
}