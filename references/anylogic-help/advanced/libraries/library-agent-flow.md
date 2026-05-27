*来源 (Source): <https://anylogic.help/advanced/libraries/library-agent-flow.html>*

---

# Implementing agent flow in custom libraries

* [Sending agents between ports of custom library’s flowchart blocks](#sending)
* [Receiving agents in the ports of custom library’s flowchart blocks](#receiving)
* [Agent flow routing rules](#routing-rules)
* [Filtering agents-entities by type](#filter-by-type)
* [Filtering agents-entities by content](#filter-by-content)

[Ports](ports.md)

When you implement your own library containing flowchart blocks, you may want interface ports of your blocks to support certain agent flow rules. Agents-entities in your agent flow may simulate various objects of the real world — e.g., products, people, trucks, etc., depending on the purpose and application area of your library.

The tips and tricks that we offer in this article may be useful if you are developing your own custom library and need to implement agent flow.

## Sending agents between ports of custom library's flowchart blocks

#### How to send an agent?

To send an agent through an interface port, you should simply call the method send() of a port, providing the reference to the agent as a parameter. If you need to just signal an object, you can send an instance of class Object that does not carry any data by calling the method send() with omitted parameter.

For example, you can type the following line of code in the **Startup code** code section of an agent to send an agent of Message type via its portA port at the model startup.

portA.send(new Message());

#### Defining agent-entity sending handler

You can define the agent-entity sending handler in the **On send** property of the port. This code is executed each time an agent is sent via port. In that code you can use a local variable msg, which is a reference of type Object to a just sent agent. If true is returned, the agent-entity is processed further as defined by agent sending rules. The same happens by default when **On send** is left blank. If false is returned or if you write any code and return nothing, the default processing is omitted.

## Receiving agents in the ports of custom library's flowchart blocks

To react to an agent received at a port, you can choose one of the ways described below.

#### Defining agent-entity reception handler

You can define the agent-entity reception handler in the **On receive** property of the port. This code is executed each time an agent-entity is received at the port. In that code you can use a local variable msg, which is a reference to a just received agent-entity. The code may contain return statement returning true or false. If true is returned, the agent-entity is forwarded further as defined by the routing rules. The same happens by default when **On receive** is left blank. If false is returned or if you write any code and return nothing, the default processing is omitted — i.e., the received agent is not forwarded further.

#### Generating events for a statechart

You can [forward the received agent-message to a statechart](https://anylogic.help/anylogic/agentbased/communication.html). Then all agents accepted by the port are placed into the statechart queue as message events.

## Agent flow routing rules

When you [send an agent](#sending) via a port, it is forwarded along all port connections outside the agent this port belongs to.

When an [agent (entity) is received](#receiving) at a port, it is forwarded to all connected statecharts and along all port connections inside the agent this port belongs to.

When an agent-entity arrives at a port, it is processed depending on the direction the agent (entity) is going.

* If an agent arrives to a port of an agent from a port of its embedded agent/block, it is sent from this port further along the external connections of the port. In this case the method send() of the port is called and the code specified in the **On send** property of the port is executed.
* Otherwise, if an agent (entity) arrives to a port from the outside, it is received by a port and is forwarded along all port connections inside the agent this port belongs to. The method receive() of the port is called and the code specified in the port **On receive** property is executed.

When an agent (message) arrives at a statechart, it is received by the statechart and the method receiveMessage() of the statechart is called.

The agent routing rules are illustrated on the figure below:

![](https://anylogic.help/advanced/libraries/images/message_rules.png)

## Filtering agents-entities by type

Sometimes you may need to filter incoming and/or outgoing agents by agent type — i.e., send and receive only agents of the certain type and discard other ones. Agent type checking is implemented by specifying the type of agents that are allowed to be sent and received by the port. Those agents that cannot be cast to the specified agent type are discarded.

To make a port filter incoming/outgoing agents (entities) by type

1. Select the port in a graphical editor.
2. Go to the **Advanced** section of the **Properties** view.
3. Specify the type of agents that are allowed to be sent and received by the port in the **In message type** and **Out message type** edit boxes correspondingly. Use combo boxes to choose from all known agent types of this model. If you leave Object here, agent type checking will not be performed.

## Filtering agents-entities by content

Sometimes you may need to filter incoming in a port agents-entities by contents — i.e. accept only agents containing the required information, or matching the specified format, and discard other ones.

In AnyLogic you can easily implement any contents checking mechanism in the **On receive** property of the port. Here you can specify your own contents checking algorithm and ignore or accept the arrived agent-entity by writing return false; or return true; statement correspondingly.

To make a port filter incoming agents (entities) by contents

1. For instance, we have a client-server model, where a server processes only valid client requests containing customer name and address. (Request is
   represented with the Request agent type with String parameters name
   and address). We want requests with some of the required fields unfilled to be ignored.
2. Select the port, whose incoming agents-entities you want to filter by contents.
3. Specify Request as port's **In message type**.
4. Define agent contents checking operations in the **On receive** property of the port. In our case your code should look like this:

   ```
   if ( msg.name==null || msg.address==null )
       return false;
       else {
       // process the request
       return true;
       }
   ```

By returning false we prohibit the default processing of the incoming agent. Now received agents will not be forwarded further according to the [agent routing rules](#routing-rules).
