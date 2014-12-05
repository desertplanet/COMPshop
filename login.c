#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define MAX_LEN 100
#define EXTRA 11
// "uName=" + "pwd=" + "&"
#define MAX_INPUT MAX_LEN+EXTRA+2
// "/0" and line break
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

	FILE *members = fopen("data/Members.csv","rt");

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
		// if (*input == '%' || *input == '+') {
		// 	printf("Your Username must not contain illegal characters or spaces");
		// 	exit(2);
		// }

		*uName = *input;
		input++;
		uName++;
	}

	input += 5; //Jump ampersand and "pwd="

	while (*input != '\0') {
		// if (*input == '%') {
		// 	printf("Your password must be composed of letters, numbers and spaces");
		// 	exit(3);
		// }

		if (*input == '+'){
			*pwd = ' ';
		} else {
			*pwd = *input;
		}

		input++;
		pwd++;
	}

}

int verifyInput(aUser endUser, aUser *m) {

	while (m != NULL) {
		if (strcmp(endUser.userName,m->userName) == 0) {
			if (strcmp(endUser.passWord,m->passWord) == 0){
				return 0;
			} else return 1;
		}
		m = m->next;
	}
	return 1;
}

void loginSuccess(aUser endUser) {
	FILE *loggedIn = fopen("data/LoggedIn.csv","a");
	if (loggedIn != NULL) {
		fprintf(loggedIn, "%s\n", endUser.userName);
		FILE *catalogue = fopen("catalogue.html","rt");

		char line[100];

		fgets(line,100,catalogue);

		while (line != "<form name=\"submit\" method=\"post\" action=\"cgi-bin/Purchase.py\">\0"){
			printf("%s\n",line);
			fgets(line,100,catalogue);
		}

		printf("<input name = \"username\" type = \"hidden\" value = \"%s\"></input>\n", endUser.userName);

		fgets(line,100,catalogue); //SKIP THE TAG WE JUST OVERWROTE
		fgets(line,100,catalogue);

		while (line != NULL) {
			printf("%s\n", line);
			fgets(line,100,catalogue);
		}

	} else {
		printf("Traffic Database error");
		exit(6);
	}
}

void loginFailure(void){
	FILE *error = fopen("pwderror.html","rt");

	char line[80];

	while (*(fgets(line,80,error)) != EOF) {
		printf("%s\n",line);
	}
}

int main(void) {

	printf("content-type: text/html\n\n");

	aUser *p = getMembersList();

	aUser endUser;
	endUser.userName = (char *)malloc(30);
	endUser.passWord = (char *)malloc(30);

	char *input = (char *)malloc(100);
	char *lengthstr;
	long lengthnum;

	lengthstr = getenv("CONTENT_LENGTH");

	if (lengthstr == NULL || sscanf(lengthstr,"%ld",&lengthnum)!=1 || lengthnum > MAX_LEN) {

	  	printf("<strong>Input Error </strong>");
		exit(5);
	} else {

		fgets(input,lengthnum+1,stdin);

		parseInput(endUser.userName, endUser.passWord, input);

		if (verifyInput(endUser,p) == 0) {
			loginSuccess(endUser);
		} else {
			loginFailure();
		}

	}
}
