*来源 (Source): <https://anylogic.help/advanced/actionchart/for-loop.html>*

---

# For loop

* [Properties](#properties)

[Action charts. Defining algorithms visually](index.md)[Editing action chart blocks](editing-blocks-of-action-charts.md)[Creating an Action Chart. Tutorial.](action-chart-tutorial.md)

![](https://anylogic.help/advanced/actionchart/images/for_loop.png)

**For Loop** is one of three “loop” blocks that are used to implement iterations. The other two are [**While loop**](while-loop.md) and [**Do While loop**](do-while-loop.md).

For detailed information on For loop please refer [here](../code/for.md).

There are two forms of a “for loop” — **Generic** and **Collection iterator**.

As its name says, **Collection iterator** allows iterating through a collection. On each iteration you can perform a set of actions with next in turn collection item.

**Generic** “for loop” executes a set of actions several times, until the specified condition is met. This “for loop” performs **initialization** before the first iteration. Then it checks whether the specified **condition** is true. If not, action chart takes all actions defined in the “loop” branch. Then a kind of “stepping” or “counting” is performed — usually the variable used as counter is incremented or decremented here. After that, the loop starts one more iteration, and so on until the condition is met.

To activate the Actionchart palette

1. Navigate to the bottom of the **Palette** view and click the button.

   ![](https://anylogic.help/advanced/actionchart/images/open-palette-list.png)
2. Select the **Actionchart** item from the displayed menu of available palettes and click it.

   ![](https://anylogic.help/advanced/actionchart/images/select-actionchart-palette.png)
3. **Actionchart** palette will appear in the **Palette** view.

To insert “for loop” into action chart

1. Drag the ![](https://anylogic.help/advanced/actionchart/images/ForLoop_edit.gif) **For Loop** from the ![](https://anylogic.help/anylogic/ui/images/palettes/ActionPalette_view.gif) **Actionchart** palette onto the diagram of agent. While moving the mouse over the graphical editor you will see insertion points of action chart(s) indicated with little blue circles. Release the mouse button over the insertion point where you want to place the block. New "for loop" block will be inserted into this place.
2. Go to the **Properties** view and choose the type of the loop — **Generic** or **Collection iterator**.
3. If you want this loop to iterate through a collection, choose **Collection iterator**, then specify the collection in the **Collection** field and type the class of the collection item and the name, which you will use to access the next in turn collection item in the “loop” iteration, in the **Item** field.
4. Otherwise, choose **Generic** and specify the required **Initialization**, **Condition** and **Counting** codes. The figure below shows the example of a generic “for loop”. It will perform 10 iterations and then will pass control further down the action chart.

   ![](https://anylogic.help/advanced/actionchart/images/for_loop_1.png)
5. Insert action chart blocks defining the action you want to execute on each iteration of the loop. Place blocks into the insertion point shown in the figure below:

   ![](https://anylogic.help/advanced/actionchart/images/decision_insertion.png)

### Properties

General
:   **Type** — The type of the “for” loop. There are two available types:

    * **Generic** — Such a loop executes a set of actions several times, until the specified condition is met. It performs code defined in the **Initialization** field before the first iteration. Then it checks whether the specified **Condition** is true. If not, action chart takes all actions defined in the “loop” branch. Then code defined in the **Counting** field is executed - usually the variable used as counter is incremented or decremented here. After that, the loop starts one more iteration, and so on until the **Condition** is met.
    * **Collection iterator** — The loop iterates through the specified **Collection**. On each iteration you can perform a set of actions with next in turn collection **Item**. In the **Item** field you should specify the class of the collection item and the name, which you will use to access a collection item in the “loop” iteration. For instance, if your collection holds elements of class String, you can type String element here. In this case collection element will be available from all blocks located inside this “for” loop as element.

Advanced
:   **Name** — The name of the element.

    **Label** — You can add here some comments, explaining the meaning of this “for loop”. The comments will be shown inside the block instead of Java code corresponding to this loop.

    **Fill color** — Sets the fill color for the element. Click inside the control and choose a color from the set of most used ones, or choose some custom color using the [Colors](https://anylogic.help/anylogic/presentation/colors.html#dialog) dialog box.
