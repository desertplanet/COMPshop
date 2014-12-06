#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define MAX_LEN 100
// Combined limit for username and password

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
// This defines the type aUser with the desired features to be extracted from the db.

/*
 * The following function reads desired attributes from a line in Members.csv and
 * stores them, associating them with the user that is passed.
*/
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


/*
 * The following function uses popoulateVars() to parse a linked list of users from
 * the Members.csv database and returns a pointer to the head of the list.
*/
aUser *getMembersList(void) {

	FILE *members = fopen("data/Members.csv","rt");

	if (members == NULL) {
		printf("There was a problem loading the csv database.\n");
		exit(1);
	}

	aUser *head = (aUser *)malloc(sizeof(aUser));

	head->next = NULL;

	aUser *t = head;

	t->fullName = (char *)malloc(40);
	t->userName = (char *)malloc(30);
	t->passWord = (char *)malloc(30);

	char line[100];

	if (fgets(line,100,members) != NULL) {

		populateVars(line,t);

		while (fgets(line,100,members) != NULL) {

			t->next = (aUser *)malloc(sizeof(aUser));
			t = t->next;

			t->fullName = (char *)malloc(40);
			t->userName = (char *)malloc(30);
			t->passWord = (char *)malloc(30);

			populateVars(line,t);
		}
	} else {
		printf("There are no registered members.\n");
		exit(2);
	}
	return head;

	fclose(members);
}

/*
 * The following function takes an encoded input string and extracts the username and pwd
 * from the input and associates them respectively with the first two strings passed.
*/
parseInput(char *uName, char *pwd, char *input) {

	input += 6;

	int j = 0;

	while (*input != '&') {

		*uName = *input;
		input++;
		uName++;
	}

	input += 5; //Jump ampersand and "pwd="

	while (*input != '\0') {

		if (*input == '+'){
			*pwd = ' ';
		} else {
			*pwd = *input;
		}

		input++;
		pwd++;
	}

}


/*
 * The following function takes a user and a pointer to a user. It is used to check a new
 * potential user from input and then compare it against each user previously parsed from
 * Members.csv. It returns 0 if the uname and pwd of the new user matches those of one in the
 * db and returns 1 otherwise.
*/
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

/*
 * The following function provides the steps to be followed if a user successfully logs into 
 * the system. Their username is appended to LoggedIn.csv and the catalogue.html page is displayed
 * with one line in the form replaced to reflect the username of the newly logged in user.
*/
void loginSuccess(aUser endUser) {
	FILE *loggedIn = fopen("data/LoggedIn.csv","a");
	if (loggedIn != NULL) {
		fprintf(loggedIn, "%s\n", endUser.userName);

		char sysCmd[100];

		sprintf(sysCmd,"python cgi-bin/createCatalogue.py %s", endUser.userName);

		system(sysCmd);

		
		FILE *catalogue = fopen("catalogue.html","rt");

		char line[100];

		int i = 0;


		while (fgets(line,100,catalogue) != NULL) {	
			printf("%s", line);
		}

		fclose(catalogue);
	} else {
		printf("Traffic Database error");
		exit(6);
	}

	fclose(loggedIn);
}

/*
 * If the uname and pwd entered on the login page do not match any pair in the db, display
 * an error page with links back to login and to the homepage index.html.
*/
void loginFailure(void){
	
	FILE *error = fopen("pwderror.html","rt");

	char line[80];

	while (fgets(line,80,error) != NULL) {
		printf("%s\n",line);
	}

	fclose(error);
}

/*
 * The following function is used to cleanup an entire linked list of users and
 * free all the dynamic memory that was used in its creation. It uses a recursive definition.
*/
void freeUserList(aUser *p) {
	if (p != NULL){
		free(p->fullName);
		free(p->userName);
		free(p->passWord);
		if (p->next != NULL) freeUserList(p->next);
		free(p);
	}
}

/*
 * This is the main function. First, the linked list of members is parsed and a pointer to its head
 * is obtained. From there, a new user is defined to represent the person attempting to log in.
 * Their input is parsed and the username and pwd that they enter are associated with their user struct.
 * The uname and pwd are compared against the values in the db and then either a login success 
 * or a login failure action is fired as defined above. Finally there is some cleanup to be done.
*/
int main(void) {

	printf("content-type: text/html\n\n");

	aUser *head = getMembersList();

	aUser *p = head;

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

	//Cleanup

	freeUserList(head);
	free(endUser.userName);
	free(endUser.passWord);

	return(0);
}
