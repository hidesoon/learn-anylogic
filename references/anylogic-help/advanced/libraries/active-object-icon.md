*来源 (Source): <https://anylogic.help/advanced/libraries/active-object-icon.html>*

---

# Icon

* [Use cases](#use-cases)
  + [Custom flowchart block icon](#custom-flowchart-block-icon)
  + [Icon for an agent with interface elements](#icon-for-an-agent-with-interface-elements)
  + [Custom icon for an agent population](#custom-icon-for-an-agent-population)

[Creating a population of agents](https://anylogic.help/anylogic/agentbased/creating-agent.html)[Ports](ports.md)

Each agent type may have specific icon associated with it. Icon is drawn in the graphical editor of the agent type using the same shapes (ovals, rectangles, images, etc.) you use to draw agent’s presentation. Therefore, you should explicitly specify shapes that are components of the agent’s icon.

To add a shape to an icon

1. In the graphical editor, select the shape by clicking.
2. In **Properties**, select the **Icon** checkbox.

Icon also contains agent’s interface elements ([ports](ports.md) and public system dynamics [variables](https://anylogic.help/anylogic/system-dynamics/variables-connection.html)). Thus you are enabled to connect these elements to interface elements of another agents.

The shapes making up an icon do not belong to any level.

In fact, all flowchart blocks available in AnyLogic libraries have icons drawn with standard AnyLogic presentation shapes. For example, here you can see how the icon of the Delay block looks like:

![](https://anylogic.help/anylogic/presentation/images/icon.png)

The icon of the Delay block is composed of a blue rectangle, and white circle and two lines depicting the clock. Two ports are placed on the icon’s border.

The icon size is set automatically to fit all icon shapes. You can see that all icon elements are outlined with a frame named **Icon**.

## Use cases

Let us describe the most popular use cases of icons.

### Custom flowchart block icon

There are a few example models in AnyLogic examples set, featuring custom flowchart blocks with custom icons, you can study the following one for example.

[**Demo model:** Emergency Department

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/6e194505-23a9-4029-8b3d-411b99d61451?mode=SETTINGS)
[**Demo model:** Emergency DepartmentOpen the model in your AnyLogic desktop installation.](alp:Emergency Department)

In this model, there are two agent types acting as custom flowchart blocks: USoundProcess and XRayProcess.

![](https://anylogic.help/anylogic/presentation/images/custom_blocks_icons.png)

When you create a custom flowchart block as described [here](https://anylogic.help/library-reference-guides/process-modeling-library/custom-block.html), the icon is created automatically, and all the block’s ports are placed on the icon’s border.

You can study the whole process of creating a custom flowchart block, including the icon creation, in the following video:

### Icon for an agent with interface elements

If your agent type contains interface elements and is intended to be connected to other agents via these elements, you need to create an icon for this agent type so that you can place the agent’s interface elements on the icon’s border.

[**Demo model:** Population

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/d0600d8d-775a-4792-bc8b-d6a511d00ed4?mode=SETTINGS)
[**Demo model:** PopulationOpen the model in your AnyLogic desktop installation.](alp:Population)

In the given demo model the stock-and-flow diagram is decomposed into two separate agent types (HousingSector and PopulationSector) that interact via public [dynamic variables](https://anylogic.help/anylogic/system-dynamics/dynamic-variable.html). The custom icons are created for these agent types to distinguish them on the Main diagram and to place the interface variables as you require on the icon’s border.

![](https://anylogic.help/anylogic/presentation/images/icon_sd_hierarchy.png)

### Custom icon for an agent population

When you create a population of agents, the default icon ![](https://anylogic.help/anylogic/ui/images/Agent_icon.gif) is displayed on the diagram. In most cases, it works for users and they keep the default icons. But sometimes, users may want to create an individual design of their models, including different icons for agent populations of different types.

It is very rare use case. Usually the highly proficient users who create their own libraries with custom components may require this if they plan to distribute their libraries among other users. We don’t have any examples with custom agent population icons since we don’t find this case practically useful.
