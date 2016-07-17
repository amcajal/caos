# Proyect:      CAOS
# File:         caos.py        
# Description:  Main function (entry point) of CAOS application. 
#               It contains the argparse module to check the input
#               parameters and launch the analysis process. 
# Python:       2.7      
# Contact:      Alberto Martin Cajal <amartin.glimpse23@gmail.com>
# Website:      https://github.com/amcajal/caos
# Copyrigth:    GNU General Public License, version 3.0.
#
# CAOS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CAOS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CAOS.  If not, see <http://www.gnu.org/licenses/>.

"""Module caos.py

Main function (entry point) of CAOS application. It contains the argparse module
to check the input parameters and launch the analysis process. 

"""

import sys 
sys.dont_write_bytecode = True    # Avoid write '.pyc' files.

import argparse
import os  
import re  
from functions import start_analysis


def main(argv):
    """Perform input argument checking and launch analysis.
    
    Main function of the module. It performs the input argument checking,
    ends execution if there are errors on them, or launch the analysis
    process if everything is correct.
    
    @param argv:    Input arguments vector, retrieved from the command line 
                    with the options selected by the user.
                    
    """
    
    error_list = []    # List of encountered errors while checking parameters.
   
    # List of supported languages. The names loaded in the list shall concur
    # with those specified in 'load_language' function, 
    # inside functions.py
    supported_languages = ["ada", "c", "c++", "java"]

    # Input argument parser, using argparse module.
    parser = argparse.ArgumentParser(
            description = 'CAOS: Python Script for critical arithmetic' 
                + ' operations searching in source code.',
            epilog = 'Example: $> python .\caos.py -p Java -t ./main.java')
    
    parser.add_argument(
            '-o', '--output', default = './', 
            help = 'Output directory where results (and log if enabled) file'
                + ' is stored (I.E: ./program/results). By default,'
                + ' output directory is current script directory (./)')
        
    parser.add_argument(
            '-l', '--label', default = '', 
            help = 'Custom label (string) to add at the end of' 
                + ' the results file, in order to differentiate it'
                + ' (I.E: "version_1_1"). By default, no label is added.')
        
    parser.add_argument(
            '-r', '--recursive', default = False, action = 'store_true', 
            help = 'Flag. It enables recursive analysis in case' 
                + ' analysis target contains directories. By default' 
                + ' recursivity is disabled.')
        
    parser.add_argument(
            '-d', '--discriminant', default = False, action = 'store_true', 
            help = 'Flag. It enables discriminant analysis, ignoring files' 
                + 'with invalid extensions. By default, all files' 
                + 'are analyzed, no matter their extension.')
        
    parser.add_argument(
            '-c', '--comments', default = False, action = 'store_true', 
            help = 'Flag. It enables comments analysis, treating them' 
                + ' like normal source code lines. By default, comments'
                + ' (single or multi-line) are ignored.')
        
    parser.add_argument(
            '-v', '--verbose', default = False, action = 'store_true', 
            help = 'Flag. It enables verbose mode, printing' 
                + ' in the command line several messages, instead of'
                + ' saving them in a log file.')
        
    parser.add_argument(
            '-i', '--list', default = [], metavar = '<fileList>', nargs = '+', 
            help = 'File(s) with a list of source code files or directories'
                + ' to be analyzed.')
        
    parser.add_argument(
            '-t',  '--target', default = [], metavar = '<target>', nargs = '+',
            help = 'Target element(s) to be analyzed. A target element can be' 
                + ' a single source code file or a directory.')
        
    # This argument type is 'str.lower' in order to avoid case sensitivity.                                   
    parser.add_argument(
            '-p', '--programming', metavar = '<programmingLanguage>', 
            type = str.lower, required = True, choices = supported_languages, 
            help = 'Programming language of the target source code. Current'
                + ' supported languares are: \n' 
                + str(supported_languages))
        
    args = parser.parse_args()


    # Following operations can be performed using custom argparse 'Actions', 
    # but due to simplicity, this way has been considered easier.

    # Check that output directory exists. If not, abort script.
    if not os.path.isdir(args.output): 
        error_list.append("Output directory error: " + args.output
                + " does not exist or is not available.")

    # Check that label has not invalid characters. Allowed characters are 
    # numbers 0-9, letters a-z (both lower case and upper case), 
    # underscores and hyphens.
    if not re.match("^[\w_-]*$", str(args.label)):
        error_list.append( "Label error: " + args.label
                + " contains invalid characters (Allowed are" 
                + " 0-9, a-Z, underscores and hyphens)")
        
    # Check that user specified at least one target element to be processed.
    if not args.list and not args.target:
        error_list.append("Target and list error: No target elements" 
                + " to analyze (neither source code files,"
                + " nor directories, nor list files.")

    # If any error has been encountered, show it and abort script.
    # Else, start analysis process.
    if error_list:
        print "\nCAOS found errors:"
        for error in error_list:
            print "     >>> " + error         
        print "\n Execute $> python caos -h for more information\n"
        sys.exit()
    else:
        print "\n" + ">"*50 + "\n\nStarting analysis..."
        start_analysis(args)
    
    # Return standard out to its initial state, 
    # in case it has been changed inside 'main' function.
    sys.stdout = sys.__stdout__ 
    
    # Visual feedback.
    print "\nResults file and Ignored list saved at " \
        + os.path.abspath(args.output)
    print "\nCAOS finished successfully\n\n" + ">"*50 + "\n"


# ENTRY POINT.
if __name__ == '__main__':
    main(sys.argv)
    
    
    
