*来源 (Source): <https://anylogic.help/advanced/code/adding-java-class.html>*

---

# Java classes

* [Examples](#examples)

[Java editor](java-editor.md)[Java interface](adding-java-interfaces.md)

AnyLogic allows the user to create their own Java classes in the model with any required functionality.

To add a Java class

1. In the **Projects** view, right-click (macOS: Ctrl + click) the model item you are currently working with, and choose **New > Java Class…** from the popup menu.
2. The **New Java Class** wizard is displayed.

   ![](https://anylogic.help/advanced/code/images/newJavaClass_1.png)
3. On the first page of the wizard, specify the name of the new Java class in the **Name** field and optionally type in the superclass name in the **Superclass** edit box.
4. Click **Next** to go to the next page of the wizard.

   ![](https://anylogic.help/advanced/code/images/newJavaClass_2.png)
5. On the second page of the wizard, specify Java class fields. Fields are specified in the table, each class field is defined in the separate row. Enter the type of the field in the **Type** cell, name of the field in the **Name** cell and optionally name the access modifier in the **Access** cell and specify the initial value in the **Initial value** cell.
6. Using **Create constructor** and **Create toString() method** check boxes, specify whether you want default class constructor and toString() method to be created automatically.
7. Click **Finish** to complete the process. You will see the code editor for the created class opened.

   ![](https://anylogic.help/advanced/code/images/JavaEditor.png)

In the **Projects** view, Java classes are visualized with the ![](https://anylogic.help/advanced/code/images/java-class.gif) icon:

![](https://anylogic.help/advanced/code/images/java-class-projects.png)

You write Java code for your Java class in [Java editor](java-editor.md), which can be opened by double-clicking the required Java class in the **Projects** view.

Java class has the only property, **Ignore**, allowing you to exclude the class from the model.

## Examples

In AnyLogic you can create your own Java classes and include them in the model. This may serve various purposes.

For example:

* To define entities in process models with additional fields and/or functions (and nothing else). Usually, an object of the modeled system is defined as an agent. But you can define such an object using a Java class instead: if multiple objects of this class are dynamically generated in the model, you can do this to improve the performance of your model. Defining data structure as a Java class, not an agent type, may reduce model's memory footprint. But if the model performance is not an issue, we recommend you to use an agent type instead - it will be more flexible and will allow you to add any other functionality (e.g. statecharts) to these entities if required. In the example model below you will find the Task Java class used for this purpose.
[**Demo model:** Exposure to Radiation

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/5f5c733f-9c70-41e5-b780-d6748b2093a3?mode=SETTINGS)
[**Demo model:** Exposure to RadiationOpen the model in your AnyLogic desktop installation.](alp:Exposure to Radiation)

![](https://anylogic.help/advanced/code/images/java-class-example-1.png)

* To create auxiliary data structures or algorithms.
[**Demo model:** Product Portfolio Management

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/68fc076c-c3d4-4e78-9224-cfc37a40a1fc?mode=SETTINGS)
[**Demo model:** Product Portfolio ManagementOpen the model in your AnyLogic desktop installation.](alp:Product Portfolio Management)* To create a Java class which will be launched in case you develop a complex simulation application.
[**Demo model:** Launching AnyLogic Model from External Application

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/67c1fa4f-7de2-4ac9-b80e-086a4b484e0a?mode=SETTINGS)
[**Demo model:** Launching AnyLogic Model from External ApplicationOpen the model in your AnyLogic desktop installation.](alp:Launching AnyLogic Model from External Application)* To include classes borrowed from somewhere else in source code form and used in the model, such as problem-oriented optimization algorithms.
[**Demo model:** Optimization in Custom Experiment

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/b0ce4b4c-325f-4c82-8c3d-b6e89c81ca18?mode=SETTINGS)
[**Demo model:** Optimization in Custom ExperimentOpen the model in your AnyLogic desktop installation.](alp:Optimization in Custom Experiment)
