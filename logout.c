#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct USER {
	char *userName;
	struct USER *next;
} aUser;

aUser *parseLoggedIn(void) {
	FILE *loggedin = fopen("data/LoggedIn.csv","rt");

	aUser *head = (aUser *)malloc(sizeof(aUser));

	aUser *p = head;
	p->userName = (char *)calloc(30,1);
	p->next = NULL;

	char *line = (char *)calloc(30,1);

	fgets(line,30,loggedin);

	int i = 0;

	while (*(i+line) != '\n' && *(i+line) != '\0') {
		p->userName[i] = *(i+line);
		i++;
	}	

	while (fgets(line,30,loggedin) != NULL) {
		i = 0;
		p->next = (aUser *)malloc(sizeof(aUser));
		p = p->next;
		p->userName = (char *)calloc(30,1);
		p->next = NULL;

		while (*(i+line) != '\n' && *(i+line) != '\0') {
			p->userName[i] = *(i+line);
			i++;
		}		
	}

	fclose(loggedin);
	free(line);

	return head;
}

void updateUsers(aUser endUser, aUser *head) {
	aUser *t = head;
	aUser *m = NULL;

	while (t != NULL) {

		if (strcmp(endUser.userName,t->userName) == 0) {
			if (m != NULL) {
				m->next = t->next;
				t = m->next;
				continue;
			} else {
				head->next = t->next;
				t = m->next;
				continue;
			}
		}

		m = t;
		t = t->next;
	}

	FILE *loggedin = fopen("data/LoggedIn.csv","w");

	aUser *p = head;

	char newLine[30];

	while (p != NULL) {
		fprintf(loggedin, "%s\n", p->userName);
		p = p->next;
	}

	fclose(loggedin);
}

void freeUserList(aUser *p) {
	if (p != NULL){
		free(p->userName);
		if (p->next != NULL) freeUserList(p->next);
		free(p);
	}
}

void main(void) {

	char *input = (char *)calloc(40,1);

	fgets(input,40,stdin);

	input += 9;

	aUser endUser;

	endUser.userName = (char *)calloc(30,1);

	int i = 0;

	while (*input != '\0') {
		endUser.userName[i] = *input;
		input++;
		i++;
	}


	FILE *index = fopen("index.html","rt");


	system("python cgi-bin/createcatsplit.py null");

	char line[100];

	printf("content-type: text/html\n\n");

	aUser *t = parseLoggedIn();

	updateUsers(endUser,t);

	// while (t != NULL) {
	// 	printf("%s\n",t->userName);
	// 	t = t->next;
	// }
	

	while (fgets(line,100,index) != NULL) {
		printf("%s", line);
	}

	freeUserList(t);

	fclose(index);
}
