*来源 (Source): <https://anylogic.help/advanced/debug/checking-model-syntax.html>*

---

# Checking model syntax

[Runtime errors](runtime-errors.md)[Custom error handler](custom-error-handler.md)

AnyLogic supports on-the-fly checking of types, parameters, and diagram syntax. The errors found during code generation and compilation are displayed in the **Problems** view. For each error, the **Problems** view displays description and location.

![](https://anylogic.help/anylogic/ui/images/problems_view.png)The Problems view

To show/hide the Problems view

1. Choose **View > ![](https://anylogic.help/anylogic/ui/images/views/ProblemsView_view.gif) Problems** from the main menu.

The first column of the **Problems** view displays an icon that denotes the type of the item. Click on the item to open the file in an editor, the line containing the problem will be highlighted.

You can open an error. Depending on the error, opening it may result in displaying different views If, for example, it is a graphical error, the corresponding diagram is opened in the graphical editor with invalid shapes highlighted.

To open an error

1. Double-click the error in the **Problems** view.

It is not always possible to give an exact error location in AnyLogic windows. For example, if you are trying to use an identifier Java cannot resolve, it could be an undeclared variable, or a parameter, or anything else. In such cases, AnyLogic displays a .java file and positions the cursor at the error location. This file is opened read-only and it is up to you to track down the real error location in AnyLogic.

You can filter errors in the **Problems** view, to view only warnings and errors for a particular element.

To show all errors in the workspace, or errors for a selected element only

1. Click the **Filter problem by selection** ![](https://anylogic.help/advanced/debug/images/filter_ps.png) button in the **Problems** view.

The **Problems** view displays information about problems of two types:

* ![](https://anylogic.help/anylogic/ui/images/toolbars/Error_misc.gif) **Error** — a critical problem that makes the model non-working and should be necessarily fixed.
* ![](https://anylogic.help/anylogic/ui/images/toolbars/Warning_misc.gif) **Warning** — information about some non-critical issue that may potentially lead to some problems, or just an advice how to optimize the implementation (e.g. information about use of deprecated function). Warnings do not to prevent you from running the model.

You can easily distinguish errors from warnings. Just look at the icon shown in the leftmost column of the corresponding entry in the **Problems** view.

By default the information about warnings is hidden to concentrate only on critical errors that should be fixed.

To show warnings

1. Click the **Show warnings** ![](https://anylogic.help/anylogic/ui/images/ShowWarnings_edit.gif) button in the **Problems** view. When the button is shown pressed, the warnings are shown, otherwise — not.
