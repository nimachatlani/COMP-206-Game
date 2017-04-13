my $date = `/bin/date`;
chomp( $date );
print "date: $date<br>\n\n";
print "</body>\n";
print "</html>\n";

my $output = "../OutPut.txt";

if ($theuser eq "PLAY") {
print "If statement entered \n";
open my $in,  '<',  $output      or die "Can't read old file: $!";
open my $out, '>', "$output.new" or die "Can't write new file: $!";

print $out "You are now playing the game!\n";

while( <$in> )
    {
    s/\b(perl)\b/Perl/g;
    print $out $_;
    }

close $out;
}
