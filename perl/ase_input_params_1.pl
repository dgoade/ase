#!/usr/bin/perl
use strict;

# Automation Scripting Essential Skills 
# Perl

# Input: Parsing command-line parameters
# Technique #1 -- Use the @ARGV array 

our $numArgs = $#ARGV;

if( $numArgs >= 0 )
{
    print ("There were " . ($numArgs + 1) . " args passed.\n");
    for (my $ndx = 0 ; $ndx <= $numArgs ; $ndx += 1 )
    {
        print "$ARGV[$ndx]\n";
    }
}

