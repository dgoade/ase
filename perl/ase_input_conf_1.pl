#!/usr/bin/perl
use strict;

# Automation Scripting Essential Skills 
# Perl

# Input: Reading configuration files
# Technique #1 -- Use angle brackets and a regex

our $Setting;
our $Value;

if( $#ARGV >= 1 )
{
    $Setting = $ARGV[1];
    # pop the second arg off so that the 
    # while loop below doesn't try to open
    # a file named after the setting.
    $ARGV = pop @ARGV;
}

while (<>)
{
    if( /^([^=]+)\s*=\s*(.*)$/ )
    { 
        my $thisSetting = $1;
        my $thisValue = $2;
        if( $thisSetting =~ /^$Setting$/ ) 
        {
            print "thisSetting = $thisValue\n";
        }
        else
        {}
    }
    else
    {
        print "no match\n";
    }
}
