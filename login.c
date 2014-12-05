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

aUser *getMembersList(void) {

	FILE *members = fopen("Members.csv","rt");

	if (members == NULL) {
		printf("There was a problem loading the csv database.\n");
		exit(1);
	}

	aUser *head = (aUser *)malloc(sizeof(aUser));

	head->next = NULL;

	aUser *currentUser = head;

	currentUser->fullName = (char *)malloc(40);
	currentUser->userName = (char *)malloc(30);
	currentUser->passWord = (char *)malloc(30);

	char line[100];

	if (fgets(line,100,members) != NULL) {

		populateVars(line,currentUser);

		while (fgets(line,100,members) != NULL) {

			currentUser->next = (aUser *)malloc(sizeof(aUser));
			currentUser = currentUser->next;

			currentUser->fullName = (char *)malloc(40);
			currentUser->userName = (char *)malloc(30);
			currentUser->passWord = (char *)malloc(30);

			populateVars(line,currentUser);
		}
	} else {
		printf("There are no registered members.\n");
	}

	return head;
}

int verifyUser(char *uName, char *pwd) {

}

int main(void) {

	aUser *p = getMembersList();

	aUser endUser;

	char *input = (char *)malloc(100);

	endUser.fullName = (char *)malloc(40);
	endUser.userName = (char *)malloc(30);
	endUser.passWord = (char *)malloc(30);

	fgets(input,100,stdin);

	printf("content-type: text/html\n\n");

	printf("<h1>%s</h1>",input);



	// while (p != NULL) {
	// 	aUser *m = p;
	// 	printf("%s/%s/%s\n", p->fullName,p->userName,p->passWord);
	// 	p = p->next;
	// 	free(m);
	// }		
}
