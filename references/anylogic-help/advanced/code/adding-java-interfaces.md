*来源 (Source): <https://anylogic.help/advanced/code/adding-java-interfaces.html>*

---

# Java interfaces

[Java editor](java-editor.md)[Java class](adding-java-class.md)

AnyLogic allows the user to add Java interfaces to a model.

Please refer to [Interfaces](https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html) section of Java online tutorials for more information on Java interfaces.

To add a Java interface

1. In the **Projects** view, right-click (macOS: Ctrl + click) the model item you are currently working with, and choose **New > Java Interface…** from the popup menu.
2. The **New Java Interface** dialog box is displayed.

   ![](https://anylogic.help/advanced/code/images/newInterface.png)
3. Specify the name of the new Java interface in the **Name** field and click **Finish** to complete the process.
4. You will see Java editor opened prompting you to write Java code for the just defined interface.

   ![](https://anylogic.help/advanced/code/images/Interface_Editor.png)

In the **Projects** view, Java interfaces are visualized with the ![](https://anylogic.help/advanced/code/images/java-interface.gif) icon:

![](https://anylogic.help/advanced/code/images/java-interface-projects.png)

You write Java code for your Java interface in [Java editor](java-editor.md), which can be opened by double-clicking the required Java interface in the **Projects** view.

Java interface has the only property, **Ignore**, allowing you to exclude the interface from model.

To use an interface, you write a class that implements the interface. When an instantiable class implements an interface, it provides a method body for each of the methods declared in the interface.

To make agent class implementing an interface

1. Select the agent type in the **Projects** view.
2. In the **Advanced Java** section of the **Properties** view, type the interface name in the **Implements (comma-separated list of interfaces)** field.

To make Java class implementing an interface

1. Double-click the Java class in the **Projects** view to open its code in the Java editor.
2. Complete the first code line containing the class name with the string **implements** <*interface name*>:

   ```
   public class MyClass implements Animatable
   { ... }
   ```
