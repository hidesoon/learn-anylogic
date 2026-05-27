*来源 (Source): <https://anylogic.help/advanced/code/pypeline.html>*

---

# Python in AnyLogic: Pypeline library

* [Requirements](#requirements)
* [Functions](#functions)
* [Examples](#examples)

[Pypeline - Repository](https://github.com/the-anylogic-company/AnyLogic-Pypeline)[Managing libraries](../libraries/managing-libraries.md)

Each model developed in AnyLogic is a Java application that can be natively customized using the Java programming language. However, it is possible to introduce Python as an auxiliary programming language within your models, allowing you to make use of Python-based libraries and algorithms.

To take advantage of Python in your AnyLogic models, use **Pypeline**: a custom library that is tailored to work with AnyLogic. It connects the virtual Java machine and the local Python installation, allowing you to run the Python code without porting it to Java.

Pypeline allows any kind of multi-run experiments (such as [parameter variation](https://anylogic.help/anylogic/experiments/parameter-variation.html) or [optimization](https://anylogic.help/anylogic/experiments/optimization.html)) to be performed without additional code. It also supports JSON, with a number of functions for converting data to and from single agents or populations.

To learn more about Pypeline, visit its [GitHub page](https://github.com/the-anylogic-company/AnyLogic-Pypeline).

**Disclaimer**: The AnyLogic Company has developed Pypeline as a third-party library that is free, open source, and an optional connectivity tool, with no obligation to provide official support or promise of compatibility of any kind. Users of the library can post questions or provide comments on the **Issue** or **Discussion** tabs of the GitHub page.

## Requirements

* Pypeline requires **Python 3+** to be installed on your machine.
* The location of the Python executable should be specified in the PATH environment variable.

Due to architectural limitations, the Python installation available from the Microsoft Store is not supported.

To install Pypeline

1. Download the JAR file of Pypeline from its [releases page](https://github.com/the-anylogic-company/AnyLogic-Pypeline/releases).
2. Place the file in a location on your machine where it won’t be moved or suddenly deleted.
3. Run AnyLogic.
4. Add Pypeline to your workspace: see [Managing libraries](../libraries/managing-libraries.md#add).
5. A new **Pypeline** palette should appear in the **Palette** view, containing the **PyCommunicator** element.

To test the connection

1. Create a new empty model.
2. Drag and drop the **PyCommunicator** element from the **Pypeline** palette into the diagram.
   Keep its default name (pyCommunicator).
3. Run the model.
4. In the model window, click the **PyCommunicator** element.
5. In the inspect window, you should see the version of Python running on your machine and the location of the Python executable.
   If an error appears, check the error text to troubleshoot.

## Functions

The **PyCommunicator** object has multiple basic functions with a number of notations.

Some of them return an Attempt object, which you can then parse to include the results in your Java code. Others allow to typecast the returned result explicitly, passing the desired output format as a function argument.

Basic
:   One-way functions execute commands in the Python context and do not return a result. They are useful for calling imports and declaring variables.

    | Function | Description |
    | --- | --- |
    | Attempt run(String code) | Executes a single line of code that returns no value. Returns an Attempt object.  For example, pyCommunicator.run("x = 3") will create a variable named x in the Python context and assign 3 as its value.    code — a statement to execute. |
    | Attempt run(String... lines) | Executes several statements that return no value. Returns an Attempt object.  For example, pyCommunicator.run("import random", "rolld20 = random.randint(1, 20)") will import the random library in the Python context, then use one of this library’s functions to generate a random integer value between 1 and 20 and assign it to the rolld20 variable.  Use it to execute one-directional commands in Python, such as value imports and variable declarations.   lines — Multiple statements to execute. |
    | Attempt run(String codeFmt, Object... args) | Executes multiple statements that return no value, while allowing data from AnyLogic to be passed as arguments using placeholder strings (%s).  For example, pyCommunicator.run("utilization = %s", resourcePool.utilization()) will create the utilization variable in the Python context and assign the utilization of the AnyLogic **ResourcePool** block named resourcePool as its value.  Multiple arguments should be separated by commas.   codeFmt — The mapping between placeholder strings and Python variables.  args — The list of AnyLogic data values to pass to Python. |

Returning a result
:   These functions are designed for two-way commands in Python, such as getting variable values and calling Python functions. There are two primary flavors of them: without typecasting and with typecasting.

    Like the [one-directional functions](#one-directional) above, they support multiple notations:

    * For executing a single line of code;
    * For executing multiple statements;
    * For passing data from AnyLogic as arguments.

    | Function | Description |
    | --- | --- |
    | Attempt runResults(String code) | Executes a single line of code that returns a value.  For example, pyCommunicator.run("5 + 3") will perform the addition operation and return the result as an Attempt object.   code — A statement to execute. |
    | T runResults(Class<T>  returnType, String code) | Executes a single line of code returns a value of the specified type.  For example, pyCommunicator.run(int.class, "5 + 3") will perform the addition operation and return the result as an int object.   returnType — The type of value to return.  code — A statement (or multiple statements) to execute. For multiple lines, the actual number of spaces in the indentation is irrelevant, although you must maintain consistency (double the number of spaces for double indentation, and so on). |

Executing scripts
:   These functions are designed for running standalone scripts in Python, which reside in the separate .py files.

    Like the [one-directional functions](#one-directional) above, they support multiple notations:

    * For passing data from AnyLogic as arguments,
    * For typecasting the result returned,
    * For specifying the Python version to execute the code.

    | Function | Description |
    | --- | --- |
    | Attempt runFile(Object... args) | Executes a Python script that may or may not produce a result. Returns the Attempt object regardless.  For example, pyCommunicator.runFile("class.py", "--foo", "5.2", "--bar", "0.3") will run the class.py script with the variables foo and bar equal to 5.2 and 0.3 respectively.   args — The arguments to the script. Should contain the relative path to the script you want to run. |
    | FutureAttempt runFileHeadless(Object... args) | Runs a Python script that returns the value of the specified type.  Same as runFile(), but executed in parallel with the running model. Designed for running long scripts whose results you don’t need immediately.  Does not support typecasting, but allows the Python version to be specified in a separate argument.  Returns a FutureAttempt object, which has its own separate set of functions.   args — The arguments to the script. Should contain the relative path to the script you want to run. |

Attempt object
:   The Attempt object is the result of a run(), runResults(), or runFile() function call.

    The following is a brief summary of the primary functions of the Attempt object. For more information about the functions of Pypeline objects, see the library’s [wiki](https://github.com/the-anylogic-company/AnyLogic-Pypeline/wiki/Usage-(basic)).

    | Function | Description |
    | --- | --- |
    | boolean isSuccessful() | Returns true if the Python call was successful, false otherwise. |
    | String getFeedback() | Returns the result of the Python call as a string. |
    | T getFeedback(Class<T> type) | Returns the result of the Python call as an object of the specified type.   type — The type of object for the expression to return. |

FutureAttempt object
:   The FutureAttempt object is the result of the runFileHeadless() function call.

    | Function | Description |
    | --- | --- |
    | boolean isSuccessful() | Returns true if the Python call was successful, false otherwise. |
    | Attempt getFeedback(long duration, TimeUnits units) | Returns the result of the Python call as an Attempt object.  May be called with no arguments. In this case, returns all output collected by Python at the time of the function call.  When called with duration and units, waits for the specified time to elapse before returning outputs.  To parse the output, use the Attempt object functions described [above](#attempt).   duration — The amount of time that must pass before the function collects output.  units — The [time units](../functions/constants-time-units.md#time) used to calculate the duration. |

Jsonifier
:   Jsonifier is a simple utility available in the Pypeline palette. Its purpose is to convert data (such as agent populations) to and from the JSON format readable by Python. To do this, Jsonifier exposes a set of functions.

    To use these functions, drag and drop the **Jsonifier** element from the **Pypeline** palette into the graphical editor. The functions should be called by referring the element, for example:
    > String agentAsJson = jsonifier.toJson(agent);

    | Function | Description |
    | --- | --- |
    | String toJson(Object object, boolean prettyPrint) | Converts the specified object to a JSON string.   object — An object to convert (any Java object of AnyLogic).  prettyPrint — (optional) If true, the resulting string will contain spaces and newlines. |
    | T fromJson(String json, Class<T> clazz) | Converts the given JSON string into the specified class.   json — The JSON string to convert.  clazz — The preferred resulting object class. |

    More information about the **Jsonifier** utility and its functions, as well as examples and usage cases, can be found in the official [Pypeline documentation](https://github.com/the-anylogic-company/AnyLogic-Pypeline/wiki/Usage-(advanced)).

## Examples

To view models that demonstrate various use cases of Python in AnyLogic, go to the **Example models** section of the [welcome page](https://anylogic.help/anylogic/ui/welcome-page.html) by selecting **Help** > ![](https://anylogic.help/anylogic/ui/images/toolbars/Open_co.gif) **Example Models** from AnyLogic main menu.
Type python in the search bar, then click on the link pointing to the model and it will open in the graphical editor.
