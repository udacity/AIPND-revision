#  Notes: Frequently Asked Questions for Classifying Images Project
These notes pertain to Frequently Asked Questions (FAQ) for the **_2. Intro to Python_**, **_Lesson 6. Project: Classify Images_** that were posted and addressed on AIPND slack. We recommend that you review these notes prior to starting the **_Classify Images Project_** to help clarify potential points of confusion regarding the Project.
&nbsp;  
&nbsp;     
    
## Quick Links to Frequently Asked Questions 
* [GitHub AIPND Repository Link](https://github.com/udacity/AIPND-revision)
* [Issues with the Project Workspace](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#issues-with-the-project-workspace)
* [Running the Project on a Local Computer](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#running-the-project-on-a-local-computer)
* [Files Required to Run **_check_images.py_** Locally](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#files-required-to-run-check_imagespy-locally)
* [Running Batch Files on Windows OS Locally](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#running-batch-files-on-windows-os-locally)
* [**_Hints_** for this Project](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#hints-for-this-project)
* [Eliminating Syntax Errors with Text Editor/Integrated Development Environment](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#eliminating-syntax-errors-with-text-editorintegrated-development-environment)
* [Cutting and Pasting Code in the Classroom](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#cutting-and-pasting-code-in-the-classroom)
* [Indention of Python Code](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#indention-of-python-code)
* [Replacing None and Pass Statements](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#replacing-none-and-pass-statements)
&nbsp;  
&nbsp;     
  
## Issues with the Project Workspace
While it is recommended that you work on the project within the **_Project Workspace_**, a few students _may_ have experienced issues trying to work within the _Project Workspace_.  Some students found these issues resolved when they switched their internet browsers.  Specifically, some students found that **_Chrome_** worked best; while others found that **_Firefox_** worked better for them.  If you are running into the problem where the _files_ in the workspace don't load and/or running code within the workspace runs extremely slowly; please try the following:
* Quit and exit out of the **_web browser_** you are using, then open it back up and restart it.
* Switch to a different **_web browser_**. 

If you run into issues with the **_Project Workspace_** and the above recommendations didn't work; alternatively, you are welcome to complete the project on a local computer using the instructions in the next [FAQ](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#running-the-project-on-a-local-computer). 
&nbsp;      
&nbsp;     
     
## Running the Project on a Local Computer
While it is recommended that you work on the project within the **_Project Workspace_**, to run the project on a local computer, you will have needed to have Python 3.6 intalled on your computer. 
### Installing Anaconda 
The easiest way to install python and the appropriate python modules is to install [Anaconda](https://www.anaconda.com/download). You will also have found the directions to install Anaconda in **_2. Intro to Python_**, **_Lesson 5. Scripting_**, **_Section 3. Install Python Using Anaconda_**. 
### Installing PyTorch and torchvision
### Linux, OSX(Mac), Windows
For this project you will also need to install the python packages pytorch and torchvision.  If your local computer has a Linux, OSX (Mac), or Windows operating system look to [*Get Started.*](http://pytorch.org/) for installation instructions. 
&nbsp;     
&nbsp;    
   
## Files Required to Run **_check_images.py_** Locally
The following files and folders need to be put in the same folder as the **_check_images.py_** python program on your local computer. You will find these files and folders within the [GitHub AIPND Repository](https://github.com/udacity/AIPND-revision/tree/master/intropyproject-classify-pet-images). There are more programs in the repository than you will need, these extra programs are there to provide the code within the lessons in a format that can be copied and pasted from.
### Needed Files:
* **pet_images**  (folder of 40 pet image)
* **uploaded_images** (a folder you will have to create to hold your uploaded images in that section of the project)
* **classifier.py** (classifier function you will be using to classify the images)
* **dognames.txt** (file that contains all the valid dog names from the classifier function and the pet image files)
* **imagenet1000_clsid_to_human.txt** (dictionary that converts the classifier function ids to text labels)
* **adjust_results4_isadog.py** (a program that contains the **adjust_results4_isadog** function that you will be defining as part of the project)
* **calculates_results_stats.py** (a program that contains the **calculates_results_stats** function that you will be defining as part of the project)
* **classify_images.py** (a program that contains the **classify_images** function that you will be defining as part of the project)
* **get_input_args.py** (a program that contains the **get_input_args** function that you will be defining as part of the project)
* **get_pet_labels.py** (a program that contains the **get_pet_labels** function that you will be defining as part of the project)
* **print_results.py** (a program that contains the **print_results** function that you will be defining as part of the project)
* **run_models_batch.sh** (a bash script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Unix/Linux/OSX/Project Workspace from a terminal window)
* **run_models_batch.bat** (a batch script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Windows from the Anaconda Prompt window)
* **run_models_batch_uploaded.sh** (a bash script that will run check_images.py sequentially for all 3 model architectures  on the uploaded images folder and output their results to text files - on Unix/Linux/OSX/Project Workspace from a terminal window)
* **run_models_batch_uploaded.bat** (a batch script that will run check_images.py sequentially for all 3 model architectures on the uploaded images folder and output their results to text files - on Windows from the Anaconda Prompt window)
* **test_classifier.py** (an example program that demonstrates how to use the classifier function)
* **print_functions_for_lab_checks.py** (a program that contains functions that will allow you to check your code)

Also be aware that instructor provided **_hints_** files are provided for each of the functions used within this project, these files will end with **_hints.py**. These **_hints_** files contain extra code to provide a few **_hints_** to help guide students to the solution. You will find these **_hints_** files within the **_Project Workspace_** and also within the [**_GitHub repository_**](https://github.com/udacity/AIPND-revision/tree/master/intropyproject-classify-pet-images) as the following files:
* **adjust_results4_isadog_hints.py** (a program that contains **_hints_** for the **adjust_results4_isadog** function that you will be defining as part of the project)
* **calculates_results_stats_hints.py** (a program that contains **_hints_** for the **calculates_results_stats** function that you will be defining as part of the project)
* **classify_images_hints.py** (a program that contains **_hints_** for the **classify_images** function that you will be defining as part of the project)
* **get_input_args_hints.py** (a program that contains **_hints_** for the **get_input_args** function that you will be defining as part of the project)
* **get_pet_labels_hints.py** (a program that contains **_hints_** for the **get_pet_labels** function that you will be defining as part of the project)
* **print_results_hints.py** (a program that contains **_hints_** for the **print_results** function that you will be defining as part of the project)
&nbsp;   
&nbsp;     
     
## Running Batch Files on Windows OS Locally
To run the files **_run_models_batch_** or **_run_models_batch_uploaded_** that run all 3 model architectures using **_check_images.py_** on a Windows OS locally; you will need to use the files that end with the extention **_.bat_** instead of the extension **_.sh_**.  You will have also needed to have installed Anaconda on your computer (see following [FAQ](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md#running-the-project-on-a-local-computer) for details on Anaconda installation).
### Directions:
* Open the **Anaconda Prompt** - either from typing **_Anaconda Prompt_** within the search bar and selecting it _or_ by clicking on it once it's found within the **Anaconda** folder of programs.
* Navigate to the _folder_ within the **Anaconda Prompt** that contains the _Project files_ including **_check_images.py_** and **_run_models_batch.bat_** using the command [_cd_](https://en.wikipedia.org/wiki/Cd_(command)).
* Type the command within the **Anaconda Prompt**:
```terminal
run_models_batch.bat
```
If instead you are working with the uploaded images , you will replace all instances of **_run_models_batch.bat_** from the _directions_ above with **_run_models_batch_uploaded.bat_**. 
&nbsp;     
&nbsp;         

## **_Hints_** for this Project
Instructor provided **_hints_** files are provided for each of the functions used within this project, these files will end with **_hints.py**. These **_hints_** files contain extra code to provide a few **_hints_** to help guide students to the solution. You will find these **_hints_** files within the **_Project Workspace_** and also within the [**_GitHub repository_**](https://github.com/udacity/AIPND-revision/tree/master/intropyproject-classify-pet-images) as the following files:   
* **adjust_results4_isadog_hints.py** (a program that contains **_hints_** for the **adjust_results4_isadog** function that you will be defining as part of the project)
* **calculates_results_stats_hints.py** (a program that contains **_hints_** for the **calculates_results_stats** function that you will be defining as part of the project)
* **classify_images_hints.py** (a program that contains **_hints_** for the **classify_images** function that you will be defining as part of the project)
* **get_input_args_hints.py** (a program that contains **_hints_** for the **get_input_args** function that you will be defining as part of the project)
* **get_pet_labels_hints.py** (a program that contains **_hints_** for the **get_pet_labels** function that you will be defining as part of the project)
* **print_results_hints.py** (a program that contains **_hints_** for the **print_results** function that you will be defining as part of the project)
&nbsp;   
&nbsp;   

## Eliminating Syntax Errors with Text Editor/Integrated Development Environment 
If you are experiencing a lot of syntax errors with your code, you may consider downloading your code and looking at it with your favorite text editor/IDE to help eliminate the syntax errors from your program.  Recall in **_2. Intro to Python_**, **_Lesson 5. Scripting_**, **_Section 6. Programming Environment Setup_** you were provided with a number of text editors that are available to use with python (like _Atom_, _Sublime Text_, _Notepad++_). Additionally, when you installed Anaconda, the Spyder IDE (Integrated Development Environment) for python should be available through the _Anaconda Navigator_. 
&nbsp;   
&nbsp;   
     
## Cutting and Pasting Code in the Classroom
If you cut and paste code directly from the classroom, it is very likely you will generate syntax errors with the single and double quotes. This is because the font type differences.  If you are going to cut and paste code from the classroom, you will need to erase and replace any copied double or single quotes.  Additionally, cutting and pasting code from the classroom may also result in issues regarding the proper code indention; therefore, it is not recommended to cut and paste code directly from the classroom.
&nbsp;    
&nbsp;   
     
## Indention of Python Code
Indention is used within Python to distinquish between blocks of code; whereas, with other programming languages, like Java and  C++,  they may have used curly brackets. The [PEP8 Style guide](https://www.python.org/dev/peps/pep-0008/) provides the standard for Python code and is what has been used for the programs within the Github respository and the Project workspace. The [PEP8 standard for indention](https://www.python.org/dev/peps/pep-0008/#indentation) is to use 4 spaces for each indention level. Not using 4 spaces for indention when editing **_check_images.py_**, will likely result in syntax errors. 

Be aware that using the _tab_ key within most text editors might not guarantee the proper 4 space indention.  Additionally, not all text editors (including the **_Project Workspace_**) provide the proper 4 space indention as is used in the Python programs within the repository for this project.
&nbsp;     
&nbsp;    
    
## Replacing None and Pass Statements
When editing the functions provided in **_check_images.py_** you will need to replace [_None_](https://docs.python.org/3/library/constants.html#None) or the [_pass_](https://docs.python.org/3/tutorial/controlflow.html#pass-statements) statement with your code for that function. The pass statement does nothing, it's used so that the program will still run even though the functions have not been fully defined. Similarly the value of _None_ represents the absence of a value, it's used so that the program will still run even though the functions have not been fully defined.
&nbsp;    
&nbsp;     
    
