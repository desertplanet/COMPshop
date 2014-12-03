#!/usr/bin/perl
use CGI;
$q = new CGI;


print "Content-type: text/html\n\n";

my $name = $q->param('name');
$theuser = '' unless $theuser;
my $username = $q->param('username');
my $password = $q->param('password');
my $verifypassword = $q->param('verifypassword');

if($name eq "" || $username eq "" || $password eq "" || $verifypassword eq "") {
print "Please go back and fill in missing fields";
}
elsif($password ne $verifypassword){
print "Passwords do not match";
}
else{
$new=join(',',$name,$username,$password);
}

my $file = '../Members.csv';
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
open(MEMBERS,'>>../members.csv') or die "oops";
print MEMBERS "$new\n";
close (MEMBERS);
}
