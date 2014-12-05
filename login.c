#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define MAX_LEN 100
#define EXTRA 11
//"uName=" + "pwd=" + "&"
#define MAX_INPUT MAX_LEN+EXTRA+2
//"/0" and line break
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


parseInput(char *uName, char *pwd, char *input) {

	input += 6;

	int j = 0;

	while (*input != '&') {
		if (*input == '%' || *input == '+') {
			printf("Your Username must not contain illegal characters or spaces");
			break;
		}

		*uName = *input;
		input++;
	}

	input++;

	while (*input != '\0') {
		if (*input == '%') {
			printf("Your password must be composed of letters, numbers and spaces");
			break;
		}

		if (*input == '+'){
			*pwd = ' ';
		} else {
			*pwd = *input;
		}

		input++;
	}

}

int main(void) {

	printf("content-type: text/html\n\n");

	aUser *p = getMembersList();

	aUser endUser;
	endUser.fullName = (char *)malloc(40);
	endUser.userName = (char *)malloc(30);
	endUser.passWord = (char *)malloc(30);

	char *input = (char *)malloc(100);
	char *lengthstr;
	long lengthnum;

	lengthstr = getenv("CONTENT_LENGTH");

	if (lengthstr == NULL || sscanf(lengthstr,"%ld",&lengthnum)!=1 || lengthnum > MAX_LEN) {

	  	printf("<strong>Input Error </strong>");

	} else {

		fgets(input,lengthnum+1,stdin);

		parseInput(endUser.userName, endUser.passWord, input);

		printf("<h1>%s <br/> %s</h1>",endUser.userName,endUser.passWord);
	}


	// while (p != NULL) {
	// 	aUser *m = p;
	// 	printf("%s/%s/%s\n", p->fullName,p->userName,p->passWord);
	// 	p = p->next;
	// 	free(m);
	// }		
}
