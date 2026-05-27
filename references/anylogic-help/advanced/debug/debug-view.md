*来源 (Source): <https://anylogic.help/advanced/debug/debug-view.html>*

---

# Debug view

[Working with views](https://anylogic.help/anylogic/ui/working-with-views.html)

The **Debug** view allows you to manage the debugging or running of a Java program your model actually is. It displays the stack frame for the suspended threads for each target you are debugging. Each thread in your program appears as a node in the tree. It displays the process for each target you are running. If the thread is suspended, its stack frames are shown as child elements.

![](https://anylogic.help/advanced/debug/images/debug_view.png)The Debug view

To show/hide the Debug view

1. Choose **View >** ![](https://anylogic.help/anylogic/ui/images/views/Debug_view.gif) **Debug** from the main menu.

When a thread is suspended, the step controls can be used to step through the execution of the program line-by-line. If a breakpoint is encountered while performing a step operation, the execution will suspend at the breakpoint and the step operation is ended.

The **Debug** view provides a set of toolbar buttons for stepping through the execution of the currently debugged model.

| Command | Action |
| --- | --- |
| Remove All Terminated Launches | The **Debug** view is cleared of all terminated launches |
| Resume | The thread resumes its execution and stack frames are no longer displayed for the thread. The [**Variables**](variables-view.md) view is also cleared. |
| Suspend | Suspends the selected thread of a target so that you can browse or modify code, inspect data, step, and so on. |
| Terminate | Terminates the selected debug target. |
| Disconnect | Disconnects the debugger from the selected debug target when debugging remotely. |
| Step Into | The next expression on the currently selected line to be executed is invoked, and execution suspends at the next executable line in the function that is invoked. |
| Step Over | The currently selected line is executed and suspends on the next executable line. |
| Step Return | Execution resumes until the next return statement in the current function is executed, and execution suspends on the next executable line. |
| Drop to Frame | This command lets you drop back and re-enter a specified stack frame. This feature is similar to "running backwards" and restarting your program part-way through. To drop back and re-enter a specified stack frame, select the stack frame that you want to "drop" to, and select Drop to Frame. |
| Use Step Filter | Toggles step filters on/off. When on, all step functions apply step filters. |
