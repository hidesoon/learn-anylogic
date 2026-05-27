*来源 (Source): <https://anylogic.help/advanced/actionchart/do-while-loop.html>*

---

# Do While loop

* [Properties](#properties)

[Action charts. Defining algorithms visually](index.md)[Editing action chart blocks](editing-blocks-of-action-charts.md)[While loop](while-loop.md)[Creating an Action Chart. Tutorial.](action-chart-tutorial.md)

![](https://anylogic.help/advanced/actionchart/images/do_while_loop.png)

**Do While loop** is one of three “loop” blocks that are used to implement iterations. The other two are [**For Loop**](for-loop.md) and [**While Loop**](while-loop.md).

For detailed information on Do While loop please refer [here](../code/while.md).

In “do while loop” you define some action or a sequence of actions using other action chart blocks. These actions are executed if the **condition** defined for this loop evaluates to true.

**Do While Loop** resembles [**While Loop**](while-loop.md) in many respects. The difference between “while loop” and “do while loop” is that the statement of a “do while loop” is always executed at least once, even if the specified expression evaluates to false the first time. Whereas in a “while loop”, if the condition is false the first time the statement is never executed.

To activate the Actionchart palette

1. Navigate to the bottom of the **Palette** view and click the button.

   ![](https://anylogic.help/advanced/actionchart/images/open-palette-list.png)
2. Select the **Actionchart** item from the displayed menu of available palettes and click it.

   ![](https://anylogic.help/advanced/actionchart/images/select-actionchart-palette.png)
3. **Actionchart** palette will appear in the **Palette** view.

To insert “do while loop” into action chart

1. Drag the ![](https://anylogic.help/advanced/actionchart/images/DoWhileLoop_edit.gif) **Do While Loop** from the ![](https://anylogic.help/anylogic/ui/images/palettes/ActionPalette_view.gif) **Actionchart** palette onto the diagram of agent. While moving the mouse over the graphical editor you will see insertion points of action chart(s) indicated with little blue circles. Release the mouse button over the insertion point where you want to place the block. New “do while loop” block will be inserted into this place.
2. Go to the **Properties** view.
3. In the **Condition** field, type the **condition** — the boolean expression that will be evaluated to decide whether the action of the “do while loop” should be performed once more.
4. Insert action chart blocks defining the action you want to execute on each iteration of the loop into the insertion point shown inside this block.

### Properties

General
:   **Condition** — Boolean expression that will be evaluated to decide whether the action of the “do while loop” should be performed once more.

Advanced
:   **Name** — The name of the element.

    **Label** — You can add here some comments, explaining the meaning of this “do while loop”. The comments will be shown inside the block instead of Java code corresponding to this loop.

    **Fill color** — Sets the fill color for the element. Click inside the control and choose a color from the set of most used ones, or choose some custom color using the [Colors](https://anylogic.help/anylogic/presentation/colors.html#dialog) dialog box.
