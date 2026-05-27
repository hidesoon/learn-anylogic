*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorPathPart.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorPathPart<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorPathPart<T>

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `INetworkMarkupElement`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `ConveyorSpur`, `ConveyorStation`, `PositionOnConveyor`

---

```
public abstract class ConveyorPathPart<T extends Agent>
extends ConveyorMarkupElement<T>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorPathPart)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ConveyorPath<? extends T>` | `getConveyor()` | Returns conveyor on which the conveyor part is located. |
| `double` | `getOffset()` | Returns offset from the beginning of conveyor to the end of this conveyor part in XY-projection, **in pixels**. |
| `double` | `getOffset(LengthUnits units)` | Returns offset from the beginning of conveyor to the end of this conveyor part in XY-projection, measured in the given units. |
| `void` | `setConveyor(ConveyorPath<? extends T> conveyor)` | Sets conveyor on which the conveyor part is located. |
| `void` | `setOffset(double offset)` | Sets offset from the beginning of conveyor to the end of this conveyor part in XY-projection, **in pixels**. |
| `void` | `setOffset(double offset, LengthUnits units)` | Sets offset from the beginning of conveyor to the end of this conveyor part in XY-projection, measured in the given units. |
