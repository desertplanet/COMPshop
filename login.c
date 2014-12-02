#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct USER {
	char *fullName;
	char *userName;
	char *passWord;
	struct USER *next;
} aUser;

void populateVars(char *line, aUser *user) {

		int i = 0;
		int j = 0;

		while (*(i + line) != ',') {
			user->fullName[j] = *(i + line);
			i++;
			j++;
		}

		i++; //Deal with comma
		j = 0;

		while (*(i + line) != ',') {
			user->userName[j] = *(i + line);
			i++;
			j++;
		}

		i++; //deal with comma
		j = 0;

		while (*(i + line) != '\n') {
			user->passWord[j] = *(i + line);
			i++;
			j++;
		}
}

int main(void) {

	FILE *members = fopen("Members.csv","r");

	aUser *head = (aUser *)malloc(sizeof(aUser));

	head->next = NULL;

	aUser *currentUser = head;

	currentUser->fullName = (char *)calloc(40,1);
	currentUser->userName = (char *)calloc(30,1);
	currentUser->passWord = (char *)calloc(30,1);

	char line[100];

	if (fgets(line,100,members) != NULL) {

		populateVars(line,currentUser);

		while (fgets(line,100,members) != NULL) {

			currentUser->next = (aUser *)malloc(sizeof(aUser));
			currentUser = currentUser->next;

			currentUser->fullName = (char *)calloc(40,1);
			currentUser->userName = (char *)calloc(30,1);
			currentUser->passWord = (char *)calloc(30,1);

			populateVars(line,currentUser);
		}

		aUser *p;
		p = head;

		while (p != NULL) {
			aUser *m = p;
			printf("%s/%s/%s\n", p->fullName,p->userName,p->passWord);
			p = p->next;
			free(m);
		}	
	} else {
		printf("There are no registered members or there is a problem with the database.\n");
	}
}