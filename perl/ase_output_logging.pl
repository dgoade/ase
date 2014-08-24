#!/usr/bin/perl
use strict;

# Automation Scripting Essential Skills 
# Perl

# Input: Parsing command-line parameters
# Technique #1 -- Use log4perl 
use Log::Log4perl;

Log::Log4perl::init_and_watch("./log4perl.conf", 10);
our $logger = Log::Log4perl->get_logger('root');

$logger->debug("This is a  debug message.");
$logger->info("This is a  info message.");
$logger->warn("This is a  warn message.");
$logger->error("This is an error message.");
$logger->fatal("This is a  fatal message.");
