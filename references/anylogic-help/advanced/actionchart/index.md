*来源 (Source): <https://anylogic.help/advanced/actionchart/index.html>*

---

# Action charts. Defining algorithms visually.

* [Action chart blocks](#action-chart-blocks)

[Action chart](action-chart.md)[Code](code.md)[Function](https://anylogic.help/anylogic/data/function.html)[Creating an Action Chart. Tutorial.](action-chart-tutorial.md)

Complex simulation modeling cannot go without algorithms that usually perform some data processing or calculations. AnyLogic supports **action charts** — structured block charts allowing defining algorithms graphically in the style of structured programming. We use widely known extension of an approach suggested by Dijkstra that splits algorithms into subsections with a single point of entry. It states that three ways of combining programs — sequencing, selection, and iteration — are sufficient to express any computable algorithm. The style reduces understanding an algorithm to understanding each structure on its own.

Action charts are very helpful since using them you can define algorithms even if you are not familiar with syntax of Java operators.

In fact, action chart visually defines a function and you can use ordinary AnyLogic functions as before. However, using **action charts** gives you one more evident benefit: it visualizes the implemented algorithm, making it more intuitive to other users.

It should be noted that as Java programming language develops, new Java operators appear that can only be represented in the AnyLogic action charts by writing actual code using the [**Code**](code.md) element. The logic of these code segments is not visualized in any way and using the action chart to define an algorithm makes less sense. In this case we recommend [converting](action-chart.md#convert) your action chart to a common AnyLogic [function](https://anylogic.help/anylogic/data/function.html). Note, that this is a one-way conversion and cannot be reverted.

Action chart is constructed from the blocks located in the **Actionchart** section of the **Palette** view. To access the blocks, you have to activate the **Actionchart** palette in the **Palette** view first.

To activate the Actionchart palette

1. Navigate to the bottom of the **Palette** view and click the button.

   ![](https://anylogic.help/advanced/actionchart/images/open-palette-list.png)
2. Select the **Actionchart** item from the displayed menu of available palettes and click it.

   ![](https://anylogic.help/advanced/actionchart/images/select-actionchart-palette.png)
3. **Actionchart** palette will appear in the **Palette** view.

## Action chart blocks

|  |  |  |
| --- | --- | --- |
|  | [Action Chart](action-chart.md) | **Action Chart** creates the basic action chart consisting of a starting point and "return" block. Defines the general action chart properties. |
|  | [Code](code.md) | **Code** block allows inserting a code snippet performing some action into your action chart. |
|  | [Decision](decision.md) | **Decision** block is the simplest way to route the algorithm flow depending on the condition. The block has two exit branches — **true** and **false**. When the control reaches the “decision” block, it decides which branch to take. If the **condition** defined for this block is met, **true** branch is taken. Otherwise, **false** branch is taken. |
|  | [Local Variable](local-variable.md) | Is used to declare local variable into an action chart. The local variable is visible only down the action chart starting from the declaration point. |
|  | [While Loop](while-loop.md) | Iteration loop. Loop actions are executed if the **condition** defined for this loop evaluates to true. The condition is evaluated once at the beginning of the loop and again before each further iteration of the action. |
|  | [Do While Loop](do-while-loop.md) | Iteration loop. Loop actions are executed if the **condition** defined for this loop evaluates to true. The condition is evaluated once at the beginning of the loop and again before each further iteration of the action. |
|  | [For Loop](for-loop.md) | Iteration loop. There are two forms of a “for loop”.  **Collection Iterator** allows iterating through a collection. On each iteration you can perform a set of actions with next in turn collection item. **Generic** “for loop” executes a set of actions several times, until the specified condition is met. |
|  | [Return](return.md) | **Return** block plays two roles: it specifies the value the action chart will return (if it’s **return type** is not **void**) and also causes that value to be returned immediately. |
|  | [Break](break.md) | **Break** block controls the flow of the loop. It stops the current iteration of the loop (and optionally quits the loop without executing the rest of the iterations). |

To draw an action chart, you first place ![](https://anylogic.help/advanced/actionchart/images/ActionChart_edit.gif) [**Action Chart**](action-chart.md) onto the graphical diagram. This creates the basic construction consisting of starting point and “return” block drawn. From this point on, you insert the required blocks into their place inside the created action chart according to the logic of the implemented algorithm.

Action charts are called in the same way as functions — you write the action chart name followed by parentheses. In the case action chart has some arguments, you should pass argument values separated by commas inside the parentheses. The values should be provided in the order they are defined in the **Action Chart**.
