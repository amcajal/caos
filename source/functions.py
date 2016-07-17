# Proyect:      CAOS
# File:         functions.py        
# Description:  Code of core functionality: text processing,
#               file checking, results writing and so on.
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



import sys 
sys.dont_write_bytecode = True    # Avoid write '.pyc' files.

import os 
import re  
import time  
from programming_language import ProgrammingLanguage as pl


def load_language(language_name):
    """Load a ProgrammingLanguage object with the proper language rules.
    
    Create and return a ProgramminLanguage object, initialized with 
    the data of the chosen language.

    @param  language_name:  name of the programming language to be loaded.
    @return:                ProgrammingLanguage object initialized with 
                            the data related to the chosen language.
                            
    """
    if language_name == "ada":
        #   Name: "Ada"
        #   Extension_list: ['.ads', '.adb']
        #   Comment_list: ["--.*"]
        #   Division_list: ["/", "rem"]
        #   Float_list: ["digits", "float", "\d+\.\d+"]
        #   Arithmetic_list: ["\+", "-", "\*"]
        #   Ignore_list: ["/=", "\".*?\"", "'.*?'", '\Srem\S']
        #   Ignored situations: strings and char variables; 
        #                       not-equal operators (/=), and the words 
        #                       containing "rem" substring that are not 
        #                       "rem" operator.
        
        # TODO: single quotes are used in string and chars too.
        #       But single quote are used to access to objects attributes.
        #       Ideate a way to delete only chars and strings.
        
        language = pl(
                "Ada", ['.ads', '.adb'], ["--.*"], ["/", "rem"], 
                ["digits", "float", "\d+\.\d+"], ["\+", "-", "\*"], 
                ["/=", "\".*?\"", '\Srem\S'])
                
    elif language_name == "c":
        #   Name: "C"
        #   Extension_list: ['.c', '.h']
        #   Comment_list: ["//.*", '/\*.*?\*/']
        #   Division_list: ["/", "%", "remainder"]
        #   Float_list: ["float", "double", "\d+\.\d+"]
        #   Arithmetic_list: ["\+", "-", "\*", "pow"]
        #   Ignore_list: ["\".*?\"", "'.*?'"]
        #   Ignored situations in C are: strings and char variables.

        language = pl(
                "C", ['.c', '.h'], ["//.*", '/\*.*?\*/'], 
                ["/", "%", "remainder"], ["float", "double", "\d+\.\d+"], 
                ["\+", "-", "\*", "pow"], ["\".*?\"", "'.*?'"])
                
    elif language_name == "c++":
        #   Name: "C++"
        #   Extension_list: 
        #       ['.c', '.h', '.hpp', '.cpp', '.cc', '.c++', '.cp', '.cxx']
        #   Comment_list: ["//.*", '/\*.*?\*/']
        #   Division_list: ["/", "%", "remainder"]
        #   Float_list: ["float", "double", "\d+\.\d+"]
        #   Arithmetic_list: ["\+", "-", "\*", "pow"]
        #   Ignore_list: ["\".*?\"", "'.*?'"]
        #   Ignored situations in C++ are: strings and char variables. 

        language = pl(
                "C++", 
                ['.c', '.h', '.hpp', '.cpp', '.cc', '.c++', '.cp', '.cxx'], 
                ["//.*", '/\*.*?\*/'], ["/", "%", "remainder"], 
                ["float", "double", "\d+\.\d+"], ["\+", "-", "\*", "pow"], 
                ["\".*?\"", "'.*?'"])
                
    elif language_name == "java":
        #   Name: "Java"
        #   Extension_list: ['.java']
        #   Comment_list: ["//.*", '/\*.*?\*/']
        #   Division_list: ["/", "%"]
        #   Float_list: ["float", "double", "\d+\.\d+"]
        #   Arithmetic_list: ["\+", "-", "\*", "pow"]
        #   Ignore_list: ["\".*?\"", "'.*?'"]
        #   Ignored situations in Java are: strings and char variables.
         
        language = pl(
                "Java", ['.java'], ["//.*", '/\*.*?\*/'], ["/", "%"], 
                ["float", "double", "\d+\.\d+"], ["\+", "-", "\*", "pow"], 
                ["\".*?\"", "'.*?'"])
                
    else:
        print "\n" + "*" * 50 + "\nUnexpected error while trying to load" \
            + " programming language. Exit from application.\n" + "*" * 50
        sys.exit()
    
    return language

    
def code_searching(input_file, language, operation, comments):
    """Search critical operations occurrences in a certain code.
    
    Iterate over the lines of a source code files, search for occurrences
    of the target operation (division or floating point op), and retrieve
    positive cases.

    @param  input_file: source code file to be analyzed.
    @param  language:   ProgrammingLanguage object. Match with the programming
                        language of the source code file.                  
    @param  operation:  target operation to be searched.
    @param  comments:   flag to either ignore or include source code comments 
                        in the analysis process.    
    @return             data to be printed in the results file, composed by the 
                        found occurrences in the analyzed code.
    
    """
    data_to_print = ""    # Lines with found occurrences.
    line_number = 1    # Line counter.
    
    # Establish target operation.
    if operation == global_division:
        operation_match = language.division_list 
        
    elif operation == global_float:
        # TO DO
        # This is going to produce a huge output, because the matching conditions 
        # are many, so a lot of lines will match it, but as false positives. 
        # In further implementations of Pycriks, "Float searching" shall match 
        # the lines that actually uses float variables (that is, lines with 
        # variables declared in the language as properly Float or Double types)

        # Search for operations that involve float type variables.
        operation_match = []
        operation_match.extend(language.float_list)
        operation_match.extend(language.arithmetic_list)
        operation_match.extend(language.division_list)
        
    else:
        print "*" * 50 + "\nUnexpected error. Closing application.\n" \
            + "*" * 50
        sys.exit()
    
    # Create the patter to search in each code line (if a line contains 
    # this pattern, it is a target to be added -a true positive-).
    pattern = re.compile('|'.join(operation_match)) 
    
    # Store file content in a single variable.
    file_reader = open(input_file, "r") 
    file_content = file_reader.read()
    file_reader.close() 
    
    # If comments are not allowed, delete then from the extracted content
    # (all types: single-line, multi-line, in-line, docstring).
    if comments == False: 
        file_content = re.sub(
                re.compile('|'.join(language.comment_list)), 
                "", file_content) 

    # Split the file content in lines, using newline char as separator. 
    # Empty lines are not deleted because they are required 
    # to correctly count the lines.
    file_content = file_content.split("\n")
    
    aux_data_to_print = ""    # Auxiliary results value.
    
    # For each line, remove cases that shall be ignored
    for line in file_content:
        clean_line = re.sub(
                re.compile('|'.join(language.ignore_list)), 
                "", line.lower())    # Lowercase to avoid case sensitivity.
        
        # If the line contains the searched operation, add it
        # to the auxiliary return value.
        if pattern.findall(clean_line): 
            aux_data_to_print += ">>> Line " + str(line_number) \
                                + ": " + line + "\n\n" 
            
        line_number += 1    # Increase the line counter.
    
    # Avoid write "empty" data in the output (making the results file messy).
    if aux_data_to_print != "":
        data_to_print = print_file_header(input_file) + aux_data_to_print 
        data_to_print += "\n\n"
    
    return data_to_print


def print_section_header(flag):
    """Print a section header in the output file.
    
    A section header separates the obtained results about a certain operation
    from the other analyzed operations.
    
    @param  flag:   flag that represents the analyzed operation, and determines
                    the value of a header section.
    @return:        header to be printed as section separator.

    """
    # Build header depending on the received flag.
    if flag == global_division:
        header = "-" * 75 + "\nDIVISION BY ZERO ANALYSIS\n" \
                    + "-" * 75 + "\n\n\n"
    elif flag == global_float:
        header = "-" * 75 + "\nFLOATING POINT ANALYSIS\n" + "-" * 75 + "\n\n\n"
    else:
        print "*" * 50 + "\nUnexpected error. Clossing application.\n" \
            + "*" * 50
        sys.exit()
        
    return header
   
   
def print_file_header(file_name):
    """Print a file header in the output file.
    
    A file header contains the absolute path of the analyzed file. It is
    used to separate the results from one file to another.
    
    @param  file_name:  name of the file being analyzed.
    @return             header to be printed as file separator.

    """
    header = "@" * 50 + "\n" + "@@@ FILE: " + file_name + "\n" \
            + "@" * 50 + "\n"
    return header
    

def print_main_header(file_name):
    """Print header to appear first in the output file.
    
    Main header appears at the top of the results file, acting as a title.
    
    @param  file_name:  name of the output file (the results file).
    @return:            header to be printed in the top of the file.

    """
    header = ">" * 75 + "\n" + file_name + "\n" + ">" * 75 + "\n\n\n"
    return header


def remove_discriminant (target_list, ignored_list, extensions):
    """Remove files with invalid extensions.
    
    Remove from the list of files to be analyzed, those with invalid extensions
    (extensions that are not related to the selected programming language.)
    
    @param  target_list:    list of files to be analyzed.
    @param  ignored_list:   list with already ignored files (wont be analyzed).
    @param  extensions:     list of allowed extensions. 
    @return:                (Tuple) updated ignored_list (files with invalid 
                            extensions has been added to the list) and 
                            updated target_list (files with invalid extensions 
                            have been deleted).
                            
    """
    # Auxiliar list (copy of input target_list).
    aux_target_list = target_list 
    
    # Auxiliar ignored list (copy of ignored_list).
    aux_ignored_list = ignored_list     
    
    # Add header to the list.
    aux_ignored_list.append(
            "\n\n" + "*" * 50 + "\n" + "INVALID EXTENSION FILES:\n" 
            + "*" * 50 + "\n") 
    
    # Obtain list of files with valid extension.
    aux_target_list = [x for x in target_list if (x.endswith(extensions))]
    
    # Add files with invalid extensions to the current ignored files.
    aux_ignored_list.extend(
            [x for x in target_list if not (x.endswith(extensions))])
    
    return aux_target_list, aux_ignored_list
    
    
def remove_duplicates(target_list, ignored_list):
    """Remove duplicated entries from a list.
    
    Remove duplicated entries in the list of files to be analyzed.
    
    @param  target_list:    list with files to be analyzed.
    @param  ignored_list:   list with already ignored files (wont be analyzed).
    @return:                (Tuple) updated ignored_list (duplicated entries 
                            have been added) and updated ignored_list 
                            (each file appear just once).

    """
    # Auxiliar list (copy of input target_list).
    aux_target_list = target_list 
    
    # Auxiliar list (copy of ignored_list).
    aux_ignored_list = ignored_list
    
    # Add header to the list.
    aux_ignored_list.append(
            "\n\n" + "*" * 50 + "\n" + "DUPLICATED FILES:\n" + "*" * 50 + "\n") 
    
    # Create set to delete duplicated objects, and store them back into a list.
    seen = set()
    seen_add = seen.add
    aux_target_list = [x for x in target_list 
        if not (x in seen or seen_add(x))]

    # Update list of ignored files with the duplicated entries
    # (duplicated entries appears more than one time in the list
    # so method "count" can be used to discover them).
    aux_ignored_list.extend(
            set([x for x in target_list if target_list.count(x) > 1]))
    
    return aux_target_list, aux_ignored_list  
    
    
def write_list (list, output_file):
    """Write list entries into a file.
    
    @param  list:           list to be written.
    @param  output_file:    absolute path to the output file.

    """
    # Open output file, write list entries, and close it.
    file_writer = open(output_file, "w")
    for entry in list: 
        file_writer.write(entry)     
    file_writer.close()


def abspath_retrieval (full_list, ignored_list, recursivity):
    """Obtain the absolute paths of the files to be processed.
    
    Obtain the absolute path of each file listed in the file with the
    targets to be processed.
    
    @param  full_list:      list with target elements to be processed.
    @param  ignored_list:   list with current ignored elements.
    @param  recursivity:    flag to establish if directories shall be iterated
                            recursively or not.
    @return:                (Tuple) list with the absolute paths, and updated 
                            'ignored_list' (targets that does not exist 
                            has been added).

    """
    target_list = []    # Auxiliary target list.
    aux_ignored_list = ignored_list    #Copy of 'ignored_list' to be increased.
    
    # Add header to the list.
    aux_ignored_list.append("\n\n" + "*" * 50 + "\n" 
            + "INVALID ABSOLUTE PATHS:\n" + "*" * 50 + "\n") 
    
    # If target is file, obtain absolute path. If directory, iterate over
    # it depending on the 'recursivity' option, analyzing inside files.
    # If target does not exist, add it to the list of ignores.
    for target in full_list: 
        if os.path.isfile(target): 
            target_list.append(
                    os.path.abspath(target)
                    .replace('\\', '/')
                    .replace(' ', '')) 
                    
        elif os.path.isdir(target):
            if recursivity == True:
                for subdir, dirs, files in os.walk(target): 
                    for file in files:
                        target_list.append(
                                os.path.join(subdir, file).replace('\\', '/') \
                                .replace(' ', ''))
                                
            else:    # Only "root" level is considered.
                for item in os.listdir(target):
                    temp = os.path.join(target, item).replace('\\', '/') \
                            .replace(' ', '')  
                    if os.path.isfile(temp):
                        target_list.append(temp)
        else: 
            aux_ignored_list.append(
                    os.path.abspath(target).replace('\\', '/')
                    .replace(' ', '') + "\n") 
            # Visual feedback.    
            print "     >>>" + target \
                + " has been ignored. File or directory does not exist"
            
    return target_list, aux_ignored_list
    
    
def list_file_retrieval (list_file_list):
    """Extract targets to be analyzed from the input files.

    An input file contains a series of text lines, each one representing 
    either a file or a directory. These lines are extracted and loaded 
    in a list.
    
    @param  list_file_list: list of files, each one containing a list of 
                            source code files or directories to be analyzed.
    @return:                (Tuple) list with all targets to be analyzed 
                            and list with ignored targets.

    """
    aux_full_list = []    # Auxiliary list with the extracted files.
    aux_ignored_list = []    # Auxiliary list with the ignored files.

    
    # Add header to the list.
    aux_ignored_list.append(
            "\n\n" + "*" * 50 + "\n" + "INVALID \"list files\" FILES:\n" 
            + "*" * 50 + "\n") 
    
    # For each of the input files, try to open them, read their content,
    # split it by "new line" character, and store the entries 
    # in the proper list. If cannot be read, add to the ignored list.
    for listFile in list_file_list: 
        try:
            list_file_reader = open(listFile, "r") 
            aux_file_list = list_file_reader.read().split('\n') 
            list_file_reader.close()
            
            # Delete empty entries and add results to the output list.
            aux_file_list = filter(None, aux_file_list) 
            aux_full_list.extend(aux_file_list)
        except IOError:
            # Visual feedback.
            print "       >>>ERROR WHILE TRYING TO OPEN LIST FILE " \
                + listFile + " : its content has been ignored"
            aux_ignored_list.append(listFile)

    return aux_full_list, aux_ignored_list  
    
    
def start_analysis (args):
    """Start the analysis of the source code targets.
    
    @param  args:   user input parameters (received from app. entry point).

    """
    # Strings working as enumeration-alike options.
    global global_division
    global global_float
    global_division = "DIVISION"
    global_float = "FLOAT"
    
    # List with all the target elements grouped
    # (both from "list file" arguments, and from "target" arguments).
    full_list = [] 
    
    # List (absolute paths) with all the files (targets) to be analyzed.
    target_list = [] 
    
    # List (absolute paths) with ignored files, due to wrong path, 
    # read permission disabled or any other error.
    ignored_list = [] 
    
    # Auxiliary variables containing text to be printed in the results file 
    # (obtained from the critical op. methods).
    divisions_to_print = ""
    float_to_print = ""

    # If verbose mode is NOT enabled, redirect all "print" messages 
    # to the log file.
    if args.verbose != True:
        print "\nLog file created in " + os.getcwd()
        sys.stdout = open(
                os.path.join(args.output, "caos_" + args.label + "_log__" \
                + time.strftime("%d_%m_%Y_%H_%M_%S")), "w") 
    
    # Obtain data of the chosen language.
    language = load_language(args.programming)
    
    # Name of the output file with the analysis results.
    results_file_name = 'caos_' + args.label + '_analysis__' \
        + time.strftime("%d_%m_%Y_%H_%M_%S") 
        
    # Name of the output file with the ignored files. 
    ignored_file_name = 'caos_' + args.label + '_ignored__' \
        + time.strftime("%d_%m_%Y_%H_%M_%S") 
    
    # Print main header in the ignored files file.
    ignored_list.append(ignored_file_name + "\n\n\n") 
    
    # Obtain the directories and source-code files 
    # included in the "list files".
    print "\nObtaining data from \"list files\"..."
    full_list, ignored_list = list_file_retrieval(args.list)
    
    # Add to the full list, the source code files 
    # or directories from the "target" parameter.
    full_list.extend(args.target) 

    # Obtain final list of source code files to analyze -target list-, 
    # and the ignored source code files.
    print "\nObtaining absolute paths of source code files..."
    target_list, ignored_list = abspath_retrieval(
            full_list, ignored_list, args.recursive) 
    
    # Remove duplicates in order to avoid process twice 
    # (or more times) the same target.
    print "\nIgnoring duplicates..."
    target_list, ignored_list = remove_duplicates(target_list, ignored_list) 
    
    # Delete files with invalid extensions in case discriminant is active.
    if args.discriminant == True:
        print "\nIgnoring files with invalid extensions..."
        extension_tuple = tuple(language.extension_list)
        target_list, ignored_list = remove_discriminant(
                target_list, ignored_list, extension_tuple)
    
    # Visual feedback.
    print "\nThe following files will be analyzed:"
    for entry in target_list:
        print entry
    print "\nStarting search for critical operations...\n"
    
    # Search for divisions and floating point operations.
    for source_code in target_list:
        print "     Analyzing " + source_code + "..."
        divisions_to_print += code_searching(
                source_code, language, global_division, args.comments)
        float_to_print += code_searching(
                source_code, language, global_float, args.comments)
    print "Analysis finished \n"
    
    # Open results files in append mode (so data will be overwritten).
    results_file = open(os.path.join(args.output,results_file_name), 'a')
    results_file.write(print_main_header(results_file_name))
    
    # Print headers first (to easy identification of the sections in the file), 
    # and then the results.
    results_file.write(print_section_header(global_division))
    results_file.write(divisions_to_print)
    divisions_to_print = ""    # Release resources.
    
    results_file.write(print_section_header(global_float))
    results_file.write(float_to_print)
    float_to_print = ""    # Release resources. 
    
    # Close results file and write ignored list.
    results_file.close()
    write_list(ignored_list, os.path.join(args.output, ignored_file_name))
    
    
    