*来源 (Source): <https://anylogic.help/advanced/actionchart/code.html>*

---

# Code

* [Properties](#properties)

[Action charts. Defining algorithms visually](index.md)[Editing action chart blocks](editing-blocks-of-action-charts.md)[Creating an Action Chart. Tutorial.](action-chart-tutorial.md)

[Action chart](index.md) element.

The **Code** block allows inserting a code snippet performing some action into your action chart. **Code** can be either a simple Java statement, or a set of statements, each one terminated by a semicolon. This code will be executed when the action chart control will reach the “code” block.

To activate the Actionchart palette

1. Navigate to the bottom of the **Palette** view and click the button.

   ![](https://anylogic.help/advanced/actionchart/images/open-palette-list.png)
2. Select the **Actionchart** item from the displayed menu of available palettes and click it.

   ![](https://anylogic.help/advanced/actionchart/images/select-actionchart-palette.png)
3. **Actionchart** palette will appear in the **Palette** view.

To insert a “code” block into an action chart

1. Drag the ![](https://anylogic.help/advanced/actionchart/images/Code_edit.gif) **Code** element from the ![](https://anylogic.help/anylogic/ui/images/palettes/ActionPalette_view.gif) **Actionchart** palette onto the diagram of agent. While moving the mouse over the graphical editor you will see insertion points of action chart(s) indicated with little blue circles. Release the mouse button over the insertion point where you want to place the block. New “code” block will be inserted into this place.

   ![](https://anylogic.help/advanced/actionchart/images/code.png)
2. Go to the **Properties** view.
3. In the **Code** field, type Java code you want to be executed when the control of the action chart will reach this block. This code will be shown inside the block on the diagram.

### Properties

General
:   **Code** — The code that will be executed when the control of the action chart will reach this block. This code will be shown inside the block on the diagram.

Advanced
:   **Name** — The name of the element.

    **Label** — You can add here some comments, explaining the meaning of this code snippet. The comments will be shown inside the block instead of the code.

    **Fill color** — Sets the fill color for the element. Click inside the control and choose a color from the set of most used ones, or choose some custom color using the [Colors](https://anylogic.help/anylogic/presentation/colors.html#dialog) dialog box.
