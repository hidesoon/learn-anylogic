*来源 (Source): <https://anylogic.help/advanced/actionchart/return.html>*

---

# Return

* [Properties](#properties)

[Action charts. Defining algorithms visually](index.md)[Editing action chart blocks](editing-blocks-of-action-charts.md)[Creating an Action Chart. Tutorial.](action-chart-tutorial.md)

![AnyLogic: Actionchart: The Return block](https://anylogic.help/advanced/actionchart/images/return.png)

The **Return** block plays two roles: it specifies the value the action chart will return (if it’s **return type** is not **void**) and also causes that value to be returned immediately.

Each branch of the action chart should end with **Return** block. That is the reason that when you start drawing an action chart, one “return” block is automatically included into the action chart to make the construction complete.

To activate the Actionchart palette

1. Navigate to the bottom of the **Palette** view and click the button.

   ![](https://anylogic.help/advanced/actionchart/images/open-palette-list.png)
2. Select the **Actionchart** item from the displayed menu of available palettes and click it.

   ![](https://anylogic.help/advanced/actionchart/images/select-actionchart-palette.png)
3. **Actionchart** palette will appear in the **Palette** view.

To insert “return” block into an action chart

1. Drag the ![](https://anylogic.help/advanced/actionchart/images/Return_edit.gif) **Return** item from the ![](https://anylogic.help/anylogic/ui/images/palettes/ActionPalette_view.gif) **Actionchart** palette onto the diagram of agent. While moving the mouse over the graphical editor you will see insertion points of action chart(s) indicated with little blue circles. Release the mouse button over the insertion point where you want to place the block. New “return” block will be inserted into this place.
2. Go to the **Properties** view.
3. If the return type of this action chart is not **void**, type the value this block will return in the **Return** field.

### Properties

General
:   **Return** — [Visible if the action chart’s **Return type** is not **void**] The value this action chart will return on reaching this block. The value should be of **Return type** specified in the properties of this [**Action chart**](action-chart.md).

Advanced
:   **Name** — The name of the element.

    **Fill color** — Sets the fill color for the element. Click inside the control and choose a color from the set of most used ones, or choose some custom color using the [Colors](https://anylogic.help/anylogic/presentation/colors.html#dialog) dialog box.

When you insert a “return” block into your action chart, the branch starting from the point where you put the block get disconnected from the action chart. In the case you put your “return” block into any exit branch of the “decision” block, this branch will be drawn dashed to denote that control will never take this way.
