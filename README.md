![caos_logo](https://github.com/amcajal/caos/blob/master/images/readme_caos_logo.png)

Project structure:

- **Source**: folder with the source code files –the application itself.
- **Examples**: folder containing example files -both input and output -to dive in the app.
- **Images**: folder containing images to be used in the README.
- **API**: CAOS Application Programming Interface, generated using [Epydoc](http://epydoc.sourceforge.net/).
- **LICENSE**: license applicated to this software.
- **DEVELOPER_NOTES**: TODO list, future improvements, bug tracking or any other developer-side consideration.
- **README**: You can read it below.
 
---

### What is CAOS

**CAOS** is a simple Python application designed to search for critical arithmetic operations in source code files of a small but expandable variety of programming languages. Aimed mainly -but not only- to the aeronautics and space industry related fields (embedded software, RTOS, On-board systems). 

- **Current critical operations**: Divisions, Floating point operations.
- **Current supported languages**: Ada, Java, C, C++.

**CAOS** uses a set of well-tested operations based on regular expressions and basic syntax rules of the target programming language, in order to iterate over each line of the source code file (or files) to be analyzed, detecting any division or floating point operation, and retrieving them into a clear results file.

**CAOS** does not emit any judgement about the operations. Instead, the application output facilitates the programmers work, making them able to focus their efforts on issuing a verdict about the safety of the found operations.

**CAOS** main features:

- **Configurable**: CAOS input parameters allow a decent grade of customization to the searching process, such as iterate recursively over projects, or ignore code comments.
- **Expandable**: CAOS has been designed with modularity in mind, making easy to add new programming languages or consider new operations to be searched.
- **Portable**: written in Python, it does not need installation and works on any Python compatible platform. It is lightweight and fast too.
- **Straightforward**: CAOS has been designed following Clean Code principles and Python Coding Conventions -and it's fully commented!-, trying to make it easy to understand and beauty as possible (more info in [What is behind](#what-is-behind) section).

---

### Index

1. [Requirements](https://github.com/amcajal/caos/blob/master/README.md#requirements)
2. [Installation](https://github.com/amcajal/caos/blob/master/README.md#installation)
3. [Quickstart](https://github.com/amcajal/caos/blob/master/README.md#quickstart)
4. [Motivation](https://github.com/amcajal/caos/blob/master/README.md#motivation)
5. [How it works](https://github.com/amcajal/caos/blob/master/README.md#how-it-works)
6. [How it's built](https://github.com/amcajal/caos/blob/master/README.md#how-its-built)
7. [How use it](https://github.com/amcajal/caos/blob/master/README.md#how-use-it)
8. [Examples](https://github.com/amcajal/caos/blob/master/README.md#examples)
9. [Developer Notes](https://github.com/amcajal/caos/blob/master/README.md#developer-notes)
10. [Used tools](https://github.com/amcajal/caos/blob/master/README.md#used-tools)
11. [What is behind](https://github.com/amcajal/caos/blob/master/README.md#what-is-behind)
12. [License](https://github.com/amcajal/caos/blob/master/README.md#license)
13. [Contact](https://github.com/amcajal/caos/blob/master/README.md#contact)

---

### Requirements
[Python](https://www.python.org/) 2.7 previously installed.


### Installation
**CAOS** does not need to be installed. To use it:
-	Download the [source files](https://github.com/amcajal/caos/tree/master/source), and put them –preferable- in a dedicated folder.
-	If you want, download the [example files](https://github.com/amcajal/caos/tree/master/examples).
-	That is! You can now launch CAOS.

For example: if CAOS has been downloaded in dir **/users/commander_tom/caos_app/**, navigate to that folder, and launch the following command:
	
    $> python ./caos.py –h

### Quickstart
Print help message:

	$> python ./caos.py –h
    
Analize Java file called 'space_ship.java' (located in './code' folder):

	$> python ./caos.py -p Java -t ./code/space_ship.java'

Same as above, but store results in './results' folder:

	$> python ./caos.py -p Java -t ./code/space_ship.java' -o ./results
    
Analize all Java files inside the project folder './mySpaceGame', including comments:

	$> python ./caos.py -p Java -d ./mySpaceGame -c
    
Check [How use it](#how-use-it) for a full explanation of the input arguments, and [Examples](#examples) for a full set of examples covering all posibilities.

### Motivation
Safety-critical software development shall be performed following guidelines like DO-178B. Due to the impact of certain operations, these cannot be fully automated by computer tools–unless they are certified to do so by an official entity- being driven manually by the software engineers. Problem is that certain operations contain a phase where straightforward but repetitive steps are executed. These phases are resource consuming –time, staff- and error-prompt due to the fatigue caused in the user. In this situation, simply, well tested applications can be used to, without interfering in the data, complete those phases, allowing the developers to focus its efforts in the decision-making process, where a human judgment is required.

In this context, **CAOS** is an open-source, free, very simple application based in well tested operations that aids the software engineers in the analysis of potential critical operations (like divisions by zero and floating point operations), performing the straightforward but repetitive phase –text searching of syntax patterns- and leaving the developers the low-level decision making (if the operation can lead to a failure or not). **CAOS** then saves time and resources without interfering in DO-178B: text searching does not modify any of the analyzed source code.

### How it works
**CAOS** workflow is represented in this very basic diagram (generated using [draw.io](https://www.draw.io/)):

![caos_flowchart](https://github.com/amcajal/caos/blob/master/images/caos_flowchart.png)

Basically, it analyzes each source code file with the selected configuration.

The analysis is very basic: using the syntax of the chosen programming language, returns the lines that contain a critical operation. For example: a line with a division (that can cause a division by zero), or a multiplication with floats involved (that can cause a float overflow or a accuracy lost).

If the chosen language is Java, a line as follows will be detected as 'division operation':

	int offset = a + b / c;
    
And a line as follows will be detected as 'float operation':

	float result = 3.0 * init_value;
    
All performed with regular expressions. Of course, depends on the configuration, the analysis can be more or less detailed (ignoring or including comments, for example).

**CAOS** usually generates three output files -depending on the configuration-:
- **caos__analysis__day_month_year_hour_minute_second**: the analysis results, containing the analyzed files and the lines where the critical operations appear.
- **caos__ignored__day_month_year_hour_minute_second**: list of files that has been ignored (no analysis has been performed), due to several reasons, like invalid file extension (if a flag to do so is enabled), corrupted file, no permissions and so on.
- **caos__log__day_month_year_hour_minute_second**: log with the messages generated about the execution (operations executed, warnings, errors and so on).

An example of each of this output files can be found in the [example folder](https://github.com/amcajal/caos/tree/master/examples).


One question to clarify: 'Apply configuration' operation is not performed just once, but several times during the applications life-cicle. It is represented in that way just to simplify the diagram.

For further information, check the [API](https://github.com/amcajal/caos/tree/master/API), or dive in the source code.


### How it's built
**CAOS** is compound of three modules, called 'caos', 'functions' and 'programming_language'.

- **caos**: it's the main module, and works as entry point to the application. It contains the argument parser ([argparse](https://docs.python.org/2.7/library/argparse.html)). Checks if input parameters are correct, and launches the analysis process or prints the 'help' info is something is wrong. It contains the 'supported_language' list, with the names of all supported languages (that is, languages that can be analyzed). This list shall concur with the 'load_language' method in 'functions' module.
- **functions**: contains the core functionality of the application. 'start_analysis' is the main function, from where processes are called -source code file retrieval, apply configuration, text searching, write results and so on-.
- **programming_language**:  OOP class, representing a programming language (name,        syntax, special cases to be considered and so on). An object of this class contains the information required to process a certain source code in the proper language.

Again, for further information, check the [API](https://github.com/amcajal/caos/tree/master/API).

### How use it
_NOTE: What follows is just an extended version of the 'help' message obtained when the command `python caos.py -h` is executed._

**CAOS** is configured using a wide set of parameters or flags, some of them mandatory and some of them optional:

Mandatory flags are:
- -p: Indicates the Programming Language in which the source code files to be analyzed are written. For example: 'Java' or 'Ada'. The supported programming languages are printed in the 'help' message.

_(The following parameter is mandatory in case the flag -i is not used)_
- -t: Indicates the 'targets' to be analyzed. A target can be a single source code file, or a directory containing a set of source code files. For example: 'main.java' or 'myClass.java' -for single files-; '/project/java_project/' for directories.


Optional flags are:
- -i: Indicates that a list of targets are passed as input argument. A list is a .txt file with a list of absolute paths to source code files or folders. That is: instead of passing a lot of targets using the -t target, in certain situations is easier to put all files or directories to be analyzed in a file, and pass this file as argument. For example: 'analyze_this.txt'.
- -o: Indicates the folder where the output results will be stored. For example: './test/results'.
- -l: Indicates a 'label' to add at the end of the output file name. This is usefull to quickly identify the file by its name. For example: '_v_1_0'. In this way, the output file will be called 'caos__v_1_0...'
- -r: Indicates if a folder shall be iterate recursively. By default, if a folder or directory is passed as target (using the -t flag), only the source code files of the first level are analyzed. However, with this flag, all sub-folders are iterated.
- -c: Indicates if the comments shall be ignored or not. By default, source code comments are ignored (because they have no impact in the program functionality), but  with this flag, they are analyzed as normal code lines.
- -v: Starts the verbose mode, that is, instead saving a log file with the execution messages, they are printed in the command line.
- -d: Indicates if the program shall discriminate wrong source code files. By default, all source code files are analyzed. However, when active, if the programming language chosen is Java, for example, any source code file that does not end in a Java related extension is ignored.


 

### Examples
Next, a set of ready-to-use CAOS execution commands, using the explained configuration options. The commands use the sample elements located in [examples folder](https://github.com/amcajal/caos/tree/master/examples) (all of them in Java language).

Example 1: Analyze a single source code file in Java language. This will generate the three output files -one with the critical operations found, one with the ignored files, and another one with the log-.

	$> python caos.py -p Java -t VectorOps.java
    
Example 2: Analyze more than one source code file in Java language.
    
    $> python caos.py -p Java -t VectorOps.java Calculator.java
    
Example 3: Analyze the folder 'simple' instead of a single source code file.

	$>python caos.py -p Java -t /simple
    
Example 4: Analyze the targets indicated in the file list 'analyze_this.txt'. This is similar to use the '-t' target and put one by one the source code files or folders, but faster obviously.

	$> python caos.py -p Java -i list_to_analyze.txt
    
Example 5: Analyze the 'simple' folder recursively, storing the results in the folder called '/output/', ignoring files that does not have a valid Java extension, and including comments in the analysis process. The results file will have a label called '_awsome', and the verbose mode is active.

	$> python caos.py -p Java -t /simple -o /output -l _awsome -r -d -c -v


### Developer Notes
'DEVELOPER_NOTES.txt' file contains:
- TODO list.
- Future improvements.
- Bug tracking .
- Any other developer-side consideration.

Check it to obtain a general overview of the application develop status.

### Used tools
Summary of tools used in this project:
- [Epydoc](http://epydoc.sourceforge.net/): for API documentation.
- [Argparse](https://docs.python.org/2.7/library/argparse.html): for argument parsing.
- [Draw.io](https://www.draw.io/): for flowchart.
- [Paint Shop Pro](http://www.paintshoppro.com/en/): for logo design.
- [Online Markdown editor](https://jbt.github.io/markdown-editor/): credis to jbt.github.io
- [Notepad ++](https://notepad-plus-plus.org/): best 'IDE' in the world.

### What is behind
Beside [Motivation](#motivation) section reasons, there are many other things that inspired this project: learning of Python, clean code, code conventions, docstrings, modularity, agile methodology (scrum)... Specially usefull was the [97 things every programmer should know](http://programmer.97things.oreilly.com/wiki/index.php/97_Things_Every_Programmer_Should_Know).

But the main reason was the fun of doing it. Like Asimov said: 

>The most exciting phrase to hear in science, the one that heralds new discoveries, is not 'Eureka!' but 'That's funny...'

### License
Alberto Martin Cajal is the original author of **CAOS** project.
**CAOS** project is released under GNU GPL version 3.0 license. Check 'LICENSE' for a full version of the license, or visit the official [GNU webpage](https://www.gnu.org/licenses/gpl-3.0.html).

### Contact

Alberto Martin Cajal at:
 
- Gmail: amartin.glimpse23@gmail.com (amartin DOT glimpse23 AT gmail DOT com)
- [Blogspot](http://glimpse-23.blogspot.com.es/)
- [LinkedIn](https://es.linkedin.com/in/alberto-martin-cajal-b0a63379)
- Twitter: @amartin_g23
