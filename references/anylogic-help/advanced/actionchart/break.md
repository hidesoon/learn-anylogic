*来源 (Source): <https://anylogic.help/advanced/actionchart/break.html>*

---

# Break

* [Properties](#properties)

[Action charts. Defining algorithms visually](index.md)[Editing action chart blocks](editing-blocks-of-action-charts.md)[Creating an Action Chart. Tutorial.](action-chart-tutorial.md)

<![](https://anylogic.help/advanced/actionchart/images/break.png)>

The **Break** block controls the flow of the loop. It stops the current iteration of the loop (and optionally quits the loop without executing the rest of the iterations).

To activate the Actionchart palette

1. Navigate to the bottom of the **Palette** view and click the button.

   ![](https://anylogic.help/advanced/actionchart/images/open-palette-list.png)
2. Select the **Actionchart** item from the displayed menu of available palettes and click it.

   ![](https://anylogic.help/advanced/actionchart/images/select-actionchart-palette.png)
3. **Actionchart** palette will appear in the **Palette** view.

To insert “break” block into an action chart

1. Drag the ![](https://anylogic.help/advanced/actionchart/images/Break_obj.gif) **Break** element from the ![](https://anylogic.help/anylogic/ui/images/palettes/ActionPalette_view.gif) **Actionchart** palette onto the diagram of agent. While moving the mouse over the graphical editor you will see insertion points of action chart(s) indicated with little blue circles. Release the mouse button over the insertion point where you want to place the block. New “break” block will be inserted into this place.
2. Go to the **Properties** view and choose the behavior you need to implement.
3. Select **Break and exit loop** option if this block should stop the execution of the current iteration and also quit the loop without executing the rest of the statements in the loop.
4. Otherwise, if you want to stop the execution of the current iteration and go back to the beginning of the loop to begin the next iteration, choose **Break and continue loop** option.

### Properties

General
:   **Type** — Defines the behavior of the break element:

    * **Break and exit loop** — if selected, the block stops the execution of the current iteration and also quits the loop without executing the rest of the statements in the loop.
    * **Break and continue loop** — if selected, the block stops the execution of the current iteration and goes back to the beginning of the loop to begin the next iteration.

Advanced
:   **Name** — The name of the element.

    **Fill color** — Sets the fill color for the element. Click inside the control and choose a color from the set of most used ones, or choose some custom color using the [Colors](https://anylogic.help/anylogic/presentation/colors.html#dialog) dialog box.
