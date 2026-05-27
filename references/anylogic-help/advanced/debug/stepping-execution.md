*来源 (Source): <https://anylogic.help/advanced/debug/stepping-execution.html>*

---

# Stepping through the execution of a model

[Evaluating expressions](evaluating-expressions.md)[Expressions view](expressions-view.md)[Breakpoints](breakpoints.md)

When a thread is suspended, the step controls can be used to step through the execution of the program line-by-line. If a breakpoint is encountered while performing a step operation, the execution will suspend at the breakpoint and the step operation is ended.

Stepping through the execution of a model in a debug mode is controlled using toolbar buttons of the [**Debug** view](debug-view.md):

![](https://anylogic.help/advanced/debug/images/debug_toolbar.png)Toolbar of the Debug view

| Command | Action |
| --- | --- |
| **Resume** | The thread resumes its execution and stack frames are no longer displayed for the thread. The [**Variables** view](variables-view.md) is also cleared. |
| **Step Over** | The currently selected line is executed and suspends on the next executable line. |
| **Step Into** | The next expression on the currently selected line to be executed is invoked, and execution suspends at the next executable line in the function that is invoked. |
| **Step Return** | Execution resumes until the next return statement in the current function is executed, and execution suspends on the next executable line. |
