#!/usr/bin/perl
use CGI;
#use Text::CSV;
$q = new CGI;
#my $csv = Text::CSV->new ({binary => 1, eol => "\n"}) or die "Cannot use CSV";

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
#get the current members.csv into an array
#open FH 'members.csv' or die $!;

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

#print "That username is taken. Please choose another one.</br>
#<a href="registration.html">Register</a></br>
#<a href="home.html">Home</a>";
}
else{
open(MEMBERS,'>>../members.csv') or die "oops";
print MEMBERS "$new\n";
close (MEMBERS);
}
