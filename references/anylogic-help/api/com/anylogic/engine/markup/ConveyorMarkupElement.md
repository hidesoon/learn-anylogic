*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorMarkupElement.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorMarkupElement<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.ConveyorMarkupElement<T>

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `INetworkMarkupElement`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `ConveyorNode`, `ConveyorPath`, `ConveyorPathPart`

---

```
public abstract class ConveyorMarkupElement<T extends Agent>
extends MarkupShape
implements INetworkMarkupElement
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorMarkupElement)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `ConveyorNetwork` | `getNetwork()` |  |
| `void` | `setNetwork(ConveyorNetwork network)` | Sets the network for this element. |
