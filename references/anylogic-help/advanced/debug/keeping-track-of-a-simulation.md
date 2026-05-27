*来源 (Source): <https://anylogic.help/advanced/debug/keeping-track-of-a-simulation.html>*

---

# Keeping track of a simulation

[trace()](../functions/trace.md)[traceln()](../functions/traceln.md)

You can output textual information during the model execution. You can use it for tracing the model execution by writing specific text on different occurrences. It can also be used as a debugging tool, for example, to find out what is the order in which the model executes actions of different objects. This possibility is convenient for output of information across several model runs, because information you write is not reset in between model runs.

The log is displayed in the [**Console**](https://anylogic.help/anylogic/ui/console-view.html) view as a read-only text, which can be copied onto the clipboard. By default, the **Console** view opens at the bottom of the application window when you run your model.

You write to log using the functions trace() and traceln() in the same way as you write in Java using System.out.print() and System.out.println() Java functions.

[**Demo model:** Event Writes to the Log

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/d1c79d2f-d22c-4f75-ba04-96f39085879c?mode=SETTINGS)
[**Demo model:** Event Writes to the LogOpen the model in your AnyLogic desktop installation.](alp:Event Writes to the Log)
