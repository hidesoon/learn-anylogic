*来源 (Source): <https://anylogic.help/advanced/debug/expressions-view.html>*

---

# Expressions view

[Working with views](https://anylogic.help/anylogic/ui/working-with-views.html)[Evaluating expressions](evaluating-expressions.md)[Stepping through the execution of a model](stepping-execution.md)

The **Expressions** view enables users to inspect results of defined expressions while debugging a model. The **Expressions** view opens automatically when an item is added to the view. Entries in the **Expressions** view can be selected to have more detailed information be displayed in the **Detail Pane**. When debugging a model, data that contains variables can be expanded to show the variables and the fields the variables contain.

![](https://anylogic.help/advanced/debug/images/expressions_view.png)The Expressions view. The detail pane is the area at the bottom of the view displaying text.
You can evaluate expressions in the context of a stack frame when the VM suspends a thread.

To evaluate an expression

1. Suspend the stack frame (for example, by creating a [breakpoint](breakpoints.md)) in which expression is to be evaluated. You can inspect the variables accessible in the current evaluation context using the [Variables](variables-view.md) view.
2. Click the ![](https://anylogic.help/advanced/debug/images/AddExpression_co.gif) **Add Expression** button on the **Expressions** view toolbar and construct a Java expression in the **New watch expression** dialog box that opens.

   ![](https://anylogic.help/advanced/debug/images/add_expression.png)
3. Click **OK** to save the expression. It will be evaluated for the current step and re-evaluated during the subsequent execution steps. You can also evaluate it manually by clicking the ![](https://anylogic.help/advanced/debug/images/ReevaluateExpression_co.gif) **Reevaluate Expression** button on the **Expressions** view toolbar.

To show or hide the Expressions view

1. Choose **View > ![](https://anylogic.help/anylogic/ui/images/views/Expressions_view.gif) Expressions** from the main menu.

You can manage the set of expressions using the number of toolbar buttons of the **Expressions** view:

| Command | Action |
| --- | --- |
| **Edit Expression** | Allows you to edit the currently selected expression. |
| **Reevaluate Expression** | Re-evaluates the currently selected expression(s). |
| **Add Expression** | Allows you to add a watch expression. |
| **Remove Expression** | Removes the currently selected expression(s) from the view. |
