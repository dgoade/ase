#!/usr/bin/perl
use strict;
use YAML::Tiny;

# Automation Scripting Essential Skills 
# Perl

# Input: Reading configuration files
# Technique #2 -- Use YAML::Tiny

our $Yaml;
our $Config;
our $Setting;
our $Value;

if( -f $ARGV[0] )
{
    # Open the config
    $Yaml = YAML::Tiny->read($ARGV[0]);
    # Get the setting
    $Value = $Yaml->[0]->{$ARGV[1]};
    print "Setting = $Value\n";

}
else
{
    print "first arg not a file.\n";
}
