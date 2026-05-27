*来源 (Source): <https://anylogic.help/advanced/libraries/connecting-ports-at-runtime.html>*

---

# Connecting ports at runtime

* [Connecting ports of Process Modeling Library blocks](#connecting-ports-of-process-modeling-library-blocks)

[Ports](ports.md)

AnyLogic supports creation of truly dynamic models – the ones with dynamically evolving structure and component interconnection.

You can programmatically change port connections at runtime to model systems with dynamically changing connections.

You can write this code anywhere you like in the agent type.

| Connection case | Connection method | Disconnection method |
| --- | --- | --- |
| A port with a port of a flowchart block | port.map(source.out); | port.unmap(source.out); |
| It is significant that the method map()/unmap() of the port and not of the port of a flowchart block should be called. The following line of code is invalid:  source.out.map(port); | |
| Ports of flowchart blocks | source.out.connect(sink.in); | source.out.disconnect(sink.in); |
| This approach does not work for Fluid Library blocks. While the connect() method will not throw an error, the fluid will not flow between the programmatically connected blocks. | |

AnyLogic also provides you the ability to programmatically disconnect a port from all connected ports using the following method of [Port](https://anylogic.help/api/com/anylogic/engine/Port.html) class:

void disconnectAndUnmapAll();

## Connecting ports of Process Modeling Library blocks

If you rewire the connections dynamically (by calling connect()/disconnect() or map()/unmap() methods of ports of Process Modeling Library blocks), the end ports will not notice that and will continue behaving according to the out-of-date connections that were established at startup.

[**Demo model:** Connecting Library Objects Dynamically

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/e14c6484-d2ac-40ac-8520-337a5fa7a22c?mode=SETTINGS)
[**Demo model:** Connecting Library Objects DynamicallyOpen the model in your AnyLogic desktop installation.](alp:Connecting Library Objects Dynamically)

This demo model illustrates how to connect Process Modeling Library blocks dynamically. It has two separate parts of a flowchart that are connected by clicking on the button placed between them. Take a look at the button's **Action** to understand the approach.
