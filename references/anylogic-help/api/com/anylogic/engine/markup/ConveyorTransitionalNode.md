*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorTransitionalNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorTransitionalNode<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorNode](ConveyorNode.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorTransitionalNode<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `INetworkMarkupElement`, `INode<ConveyorNode<?>,ConveyorPath<?>>`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `ConveyorTransferTable`, `ConveyorTurnStation`, `ConveyorTurntable`

---

```
@AnyLogicInternalAPI
public abstract class ConveyorTransitionalNode<T extends Agent>
extends ConveyorNode<T>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorTransitionalNode)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract double` | `getSpeed(SpeedUnits units)` |  |
| `double` | `getTransferDistance(ConveyorPath<?> path1, ConveyorPath<?> path2)` |  |
| `ConveyorPath<T>` | `getTransition(ConveyorPath<?> path)` |  |
| `List<? extends ConveyorPath<T>>` | `getTransitions()` |  |
| `abstract boolean` | `isTakeSpeedOfConnectedConveyors()` |  |
