#include <stdio.h>
#include <stdlib.h>

void main(void) {

	FILE *index = fopen("index.html","rt");


	system("python cgi-bin/createcatsplit.py null");

	char line[100];

	printf("content-type: text/html\n\n");

	while (fgets(line,100,index) != NULL) {
		printf("%s", line);
	}

	fclose(index);
}
