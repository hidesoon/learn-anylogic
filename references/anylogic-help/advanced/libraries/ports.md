*来源 (Source): <https://anylogic.help/advanced/libraries/ports.html>*

---

# Ports

* [Properties](#properties)
* [Custom port classes](#custom-port)

[Connecting ports at runtime](connecting-ports-at-runtime.md)[Implementing agent flow in custom libraries](library-agent-flow.md)[API reference - Port class](https://anylogic.help/api/com/anylogic/engine/Port.html)

Ports are used in flowchart blocks as interface points for the agent flow mechanism. Agents are sent and received through ports. The ways of sending agents (entities) through ports are described [here](library-agent-flow.md).

Flowchart blocks of AnyLogic libraries already have the required ports defined. You may need adding ports into your model only if you create your own [custom library](index.md) or create custom flowchart blocks to make your flowchart simpler (see the how-to video referenced below).

To create a port

1. Drag the **Port** ![](https://anylogic.help/advanced/libraries/images/Port_obj%20%282%29.gif) element from the **Agent** palette onto the diagram of agent.

## Properties

General
:   **Name** — The name of the port. The name is used to identify and access the port from code.

    **Show name** — If selected, the port name is displayed on a presentation diagram.

    **Ignore** — If selected, the port is excluded from the model.

    **Visible on upper agent** — If selected, the port is also visible on the upper agent where this agent lives.

    **Visible** — If selected, the port is visible on a presentation at runtime.

Message handling actions
:   These properties are visible only if the [Library Developer Mode](library-developer-mode.md) is switched on.

    **On receive** — [Visible if the advanced option **Custom port** is not selected] The code executed each time a message is received by the port (when the user calls the method receive() of the port, or when this port receives a message from a port of some embedded object). Here you can access just received message as msg (local variable of type Object).\*

    **On send** — [Visible if the advanced option **Custom port** is not selected] The code executed each time a message is sent by the port (when the user calls the method send() of the port, or when this port relays message received "from outside" (i.e. from a port of agent located on the same or higher level in the model hierarchy)). Here you can access the message as msg (local variable of type Object).\*

    \* If the field is left blank, or true is returned, the message is processed further as defined by [message routing rules](library-agent-flow.md#routing-rules), otherwise it is discarded.

Advanced
:   These properties are visible only if the [Library Developer Mode](library-developer-mode.md) is switched on.

    **Custom port** — If selected, the port will be an instance of the [custom port class](#custom-port) specified in the **Constructor code**. This is needed, when you have a number of ports with the same custom functionality (e.g. the same **On receive** message handler) in your model, and you want to define this functionality once in a custom port class and then simply use instances of that port class.

    **In message type** — [Enabled if the **Custom port** option is not selected] The type of messages that are allowed to be received by the port. If you leave **Object** here, message type checking will not be performed and all messages will be allowed to be received.

    **Out message type** — [Enabled if the **Custom port** option is not selected] The type of messages that are allowed to be sent by the port. If you leave **Object** here, message type checking will not be performed and all messages will be allowed to be sent.

    **Constructor code** — [Visible if the **Custom port** option is selected] Here you can type the constructor of the created port class, e.g. MyPort(this)

## Custom port classes

You can customize the port behavior by writing your own code in **On send** and **On receive** port properties.

These properties are visible only if the [Library Developer Mode](library-developer-mode.md) is switched on.

However, if the defined port functionality is frequently needed, defining your own port class is preferable. Thus, instead of writing the same code for all the port instances in your model, you need just to create new port class once and specify this class as the port class for the ports you need. Create your own port class as a new Java class, or in a library. Defining port class in a library has an advantage of future reuse of your custom ports in other models as well.

To define a custom port class

1. In the **Projects** view, right-click (macOS: Ctrl + click) the model item, and choose **New > Java Class…** from the popup menu.
2. The **New Java Class** dialog box is displayed.
3. Specify the name of the new class in the **Name** edit box.
4. Specify the name of the base class. Type in **Superclass** edit box. Port class is the base class for all port classes in AnyLogic. This class provides basic port functionality and if you want to customize the default behavior of ports, you need to derive your own port classes from Port class.
5. Click **Finish** to complete the process.
6. You will see that the code editor for the just created class is opened. Write there code for your port. Here you can override some functions of the base class
   [Port](https://anylogic.help/api/com/anylogic/engine/Port.html). When finished, you can use this class as a port class for any port instances in your model.

To set the created class as a port class for a port instance

1. Select the port in the graphical editor.
2. In the **Advanced** section of the **Properties** view, select the **Custom port** check box.
3. In the **Constructor code** field, type the constructor of the created port class, e.g. MyPort(this)
