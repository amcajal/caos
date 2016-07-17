# Proyect:      CAOS
# File:         programming_language.py        
# Description:  Class that represents a "programming language": name,
#               syntax, special cases to be considered and so on. An
#               object of this class contains the information required 
#               to process a certain source code 
#               in the proper language. 
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

""" Module programming_language.py

Class that represents a "programming language": name, syntax, special cases 
to be considered and so on. An object of this class contains the information 
required  to process a certain source code in the proper language. 

"""


import sys
sys.dont_write_bytecode = True    # Avoid write '.pyc' files.

class ProgrammingLanguage:
    """Represents a programming language.

    The class variables stores the necessary data to process a certain
    programming language, mainly syntax rules. This variables must
    match with the real language rules. Variables can contain regular
    expressions, but they shall be in a valid Python format.
    
    """
    def __init__(
            self, name, extension_list, comment_list, division_list, 
            float_list, arithmetic_list, ignore_list):
        """Constructor.
        
        Initializes an object with the data related to a 
        certain programming language.
        
        @param  name:           name of the programming language (e.g.: Java).
        @param  extension_list: list of file extensions related to the language 
                                (e.g.: in C language, .c, .h).                      
        @param  comment_list:   list of regular expressions that represent 
                                the comments (single or multi-line) in the 
                                related language
                                (e.g: for Java ['//.*', '/\*.*?\*/']; that is, 
                                all text that comes after a double slash and 
                                all text between /* and */).                            
        @param  division_char:  list of characters used to perform divisions 
                                -or related operations- in the language
                                (e.g: for Java, [/, %]).                        
        @param  float_list:     list of keywords and regular expressions, used
                                to define and represent "float" variables in 
                                the related language
                                (e.g: for C ["float", "double", "\d+\.\d+"]; 
                                that is, variables with "double" keyword, 
                                "float" keyword, or numerical values in the 
                                format <number>DOT<number>).              
        @param  arithmetic_list:    Char list used to perform arithmetic ops.
                                DIVISION chars already considered
                                (e.g: for Java, ["+", "-", "*", "pow"];
                                Increment, decrement, and exponent operations 
                                can be generated from the previous set of 
                                characters, thus no need to include them).    
        @param  ignore_list:    list of special cases -substrings or regex- 
                                that shall be ignored when searching for 
                                critical operations, in order to avoid 
                                false positives. 
                                (e.g: in Ada, division char is slash char ("/") 
                                but there is a relational operator -"not equal" 
                                operator- that is represented by "/=". When 
                                searching for divisions, a "not equal" 
                                comparison will be added as false positive. 
                                Adding the char "/=" to the ignore_list, allows 
                                the script to ignore them). 
        
        """
        self.name = name
        self.extension_list = extension_list
        self.comment_list = comment_list
        self.division_list = division_list
        self.float_list = float_list
        self.arithmetic_list = arithmetic_list
        self.ignore_list = ignore_list
        
        
