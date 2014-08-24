#!/usr/bin/perl
use strict;

# Automation Scripting Essential Skills 
# Perl

# Input: Parsing command-line parameters
# Technique #1 -- Use getopt or getoptlong
use Getopt::Long;

our $Action;
our $Help;
our $LogLevel;
our $NoOp;
our $Verbose;

GetOptions (
    "a|action=s"   => \$Action,
    "h|help"       => \$Help,     
    "l|loglevel=s" => \$LogLevel,     
    "n|noop"       => \$NoOp,     
    "v|verbose"    => \$Verbose
    );  

print "Parameters you passed:\n";
print "action=$Action\n";
print "help=$Help\n";
print "loglevel=$LogLevel\n";
print "noop=$NoOp\n";
print "verbose=$Verbose\n";
