#!/usr/bin/perl
use CGI;
$q = new CGI;


print "Content-type: text/html\n\n";

my $name = $q->param('name');
$theuser = '' unless $theuser;
my $username = $q->param('username');
my $userBadChar = 0;
my $pwBadChar = 0;
if ($username =~ m/[^a-zA-Z0-9]/){
$userBadChar=1;
}
my $password = $q->param('password');
if ($password =~ m/[^a-zA-Z0-9 ]/){
$pwBadChar=1;
}

my $verifypassword = $q->param('verifypassword');

if($name eq "" || $username eq "" || $password eq "" || $verifypassword eq "") {
	print 'Please go back and fill in missing fields </br>
	<a href="../registration.html">Go back</a>';
}
elsif($userBadChar == 1 || $pwBadChar == 1){
	print 'Usernames can only contain alphanumeric characters. Passwords can only contain alphanumeric characters and spaces.</br><a href="../registration.html">Go back</a>';
}
elsif($password ne $verifypassword){
	print 'Passwords do not match.</br><a href="../registration.html">Go back</a>';
}
else{
	$new=join(',',$name,$username,$password);
}

my $file = '../data/Members.csv';
open(MEMBERS, "<$file") or die "Could not access member directory\n";
my @members = <MEMBERS>;
close(MEMBERS);

my $taken=0;
foreach $line (@members)
{
	my @userdata = split ",", $line;
	if ($userdata[1] eq username){
		$taken=1;
	}
}

if ($taken == 1){
	print ('Sorry that username is taken. Please choose another one. </br>
		<a href="../home.html">Go home.</a></br>
		<a href="../registration.html">Register</a>
		');

}
else{
	open(MEMBERS,'>>../data/Members.csv') or die "oops";
	print MEMBERS "$new\n";
	close (MEMBERS);
print('You have been registered!</br><a href="../login.html">Login</a>');

}
