#!/usr/bin/perl
use strict;
use Pod::Usage;

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

if( $Help )
{
    pod2usage(-verbose => 5);
}
else
{
    print "Parameters you passed:\n";
    print "action=$Action\n";
    print "help=$Help\n";
    print "loglevel=$LogLevel\n";
    print "noop=$NoOp\n";
    print "verbose=$Verbose\n";
}

__END__

=head1 NAME

ase_input_params_2.pl - Parsing command-line parameters example

=head1 SYNOPSIS

    ase_input_params.pl 
                   [-a|--action [action]]
                   [-h|--help]
                   [--l|--loglevel [level]]
                   [--n|--noop]
                   [-v|--verbose]

Required Arguments:

    -a|--action       The action to take 


Optional Arguments:

    -l|--loglevel     Logging level to use 

    -n|--noop         Run in no-op mode

    -h|--help         display usage

    -v|--verbosity      level to log (debug info warn error fatal)

=head1 EXAMPLES

=over 8

=item 1) Run an action called 'normal'

C<./ase_input_params_2.pl --action normal  

=item 2) Run an action called 'normal' in no-op mode

C<./ase_input_params_2.pl --action normal --noop

=item 3) Run an action called 'special' with log level of 5 in verbose mode

C<./ase_input_params_2.pl --action special -l 5 -v

=back
