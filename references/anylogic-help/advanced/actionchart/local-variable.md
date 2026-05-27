*来源 (Source): <https://anylogic.help/advanced/actionchart/local-variable.html>*

---

# Local variable

* [Properties](#properties)

[Action charts. Defining algorithms visually](index.md)[Editing action chart blocks](editing-blocks-of-action-charts.md)[Creating an Action Chart. Tutorial.](action-chart-tutorial.md)

When defining some algorithm using action chart, you may need some local variables e.g. to store intermediate calculation results.You define variables using **Local Variable** blocks. Please note that local variable is visible only down the action chart starting from the declaration point.

![](https://anylogic.help/advanced/actionchart/images/local_variable.png)

To activate the Actionchart palette

1. Navigate to the bottom of the **Palette** view and click the button.

   ![](https://anylogic.help/advanced/actionchart/images/open-palette-list.png)
2. Select the **Actionchart** item from the displayed menu of available palettes and click it.

   ![](https://anylogic.help/advanced/actionchart/images/select-actionchart-palette.png)
3. **Actionchart** palette will appear in the **Palette** view.

To declare a local variable in an actionchart

1. Drag the ![](https://anylogic.help/advanced/actionchart/images/LocalVariable_edit.gif) **Local Variable** from the ![](https://anylogic.help/anylogic/ui/images/palettes/ActionPalette_view.gif) **Actionchart** palette onto the diagram of agent. While moving the mouse over the graphical editor you will see insertion points of action chart(s) indicated with little blue circles. Release the mouse button over the insertion point where you want to place the block. New “local variable” block will be inserted into this place.
2. Go to the **Properties** view.
3. Type the name of the local variable in the **Name** edit box. The name of the variable will be shown inside the block on the diagram.
4. Specify the type of the local variable. You can choose one of the most-used types (**int**, **double**, **boolean**, **String**) using the corresponding option from the **Type** group of buttons. However, if you need to define a variable of some other Java class, choose **Other** button and type the required class name in the edit box to the right.
5. Specify the variable’s initial value in the **Initial value** edit box.
6. Some variables in your model do not change during the algorithm lifetime. Such variables should be declared as constants. A **constant** has the same value at all times and cannot be changed. Making variable a constant, you prevent it from unwanted modifying. To make local variable a constant, select the **Constant** check box.

### Properties

General
:   **Name** — The name of the “local variable” element. The name is used to identify the element within its action chart.

    **Type** — The type of the local variable. Choose, whether you want a variable of some most-used type (**int**, **double**, **boolean**, **String**), or of some **Other** Java class using the controls to the right.

    **Initial value** — You can define the initial value for the variable here. The initial value of the variable can be changed afterwards during the model simulation. If an initial value is not specified, Java rules apply, for example a variable of type double is set to 0, a variable of type boolean is false.

    **Constant** — If selected, the local variable is made constant, that is, it has the same value at all times and cannot be changed during the simulation.

Advanced
:   **Label** — You can add here some comments, explaining the meaning of the local variable. The comments will be shown inside the block instead of the name of the variable.

    **Fill color** — Sets the fill color for the element. Click inside the control and choose a color from the set of most used ones, or choose some custom color using the [Colors](https://anylogic.help/anylogic/presentation/colors.html#dialog) dialog box.
