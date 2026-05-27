*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorPortImpl.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorPortImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorNode](ConveyorNode.md "class in com.anylogic.engine.markup")<[Agent](../Agent.md "class in com.anylogic.engine")>

com.anylogic.engine.markup.ConveyorPortImpl

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `INetworkMarkupElement`, `INode<ConveyorNode<?>,ConveyorPath<?>>`, `MarkupPort`, `NetworkPort`, `SVGElement`, `UsdElement`, `Serializable`

---

```
@AnyLogicInternalAPI
public class ConveyorPortImpl
extends ConveyorNode<Agent>
implements NetworkPort, AbstractPositionalMarkup
```

This class has no user constructors.
Network ports should be created using factory, ConveyorNetwork.createPort(..).

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorPortImpl)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorPortImpl(Agent owner, ShapeDrawMode drawMode, boolean isPublic, PathEnd<ConveyorPath<?>> pathEnd)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(ConveyorPath<?> path, PathEndType type)` |  |
| `MarkupPort` | `getPairedPort()` | Returns the paired port for this markup port. |
| `Position` | `getPosition()` | Returns the location (with rotation) of this element |
| `Position` | `getPosition(Position out)` | Returns the location (with rotation) of this element |
| `double` | `getTransferDistance(ConveyorPath<?> path1, ConveyorPath<?> path2)` |  |
| `Point` | `getXYZ()` | Returns the location of this element |
| `Point` | `getXYZ(Point out)` | Returns the location of this element |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setPairedPort(MarkupPort pairedPort)` | Sets the paired port for this markup port. |
