#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct USER {
	char *userName;
	struct USER *next;
} aUser;

void populateU(char *line, aUser *user) {

	int i = 0;

	while (line[i] != '\n') {
		user->userName[i] = line[i];
		i++;
	}
}

aUser *getLoggedInList(void){

	FILE *loggedIn = fopen("data/LoggedIn.csv","rt");

	if (loggedIn == NULL) {
		printf("There was a problem loading the csv database.\n");
		exit(1);
	}

	aUser *head = (aUser *)malloc(sizeof(aUser));

	head->next = NULL;

	aUser *t = head;

	t->userName = (char *)malloc(30);

	char line[100];

	if (fgets(line,100,loggedIn) != NULL) {

		populateU(line,t);

		while (fgets(line,100,loggedIn) != NULL) {

			t->next = (aUser *)malloc(sizeof(aUser));
			t = t->next;

			t->userName = (char *)malloc(30);
			t->next = NULL;

			populateU(line,t);
		}
	} else {
		printf("There are user logged in.\n");
		exit(2);
	}

	fclose(loggedIn);
	return head;
}

void freeUserList(aUser *p) {
	if (p != NULL){
		free(p->userName);
		if (p->next != NULL) freeUserList(p->next);
		free(p);
	}
}

int main (void) {
	
	aUser *head = getLoggedInList();
	aUser *p = head;

	char line[40];

	fgets(line,40,stdin);

	printf("content-type: text/html\n\n");

	printf("%s", line);

	// while (p != NULL) {
	// 	printf("%s\n", p->userName);
	// 	p = p->next;
	// }

	freeUserList(head);
}