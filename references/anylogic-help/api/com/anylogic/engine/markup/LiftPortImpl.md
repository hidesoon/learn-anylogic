*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/LiftPortImpl.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class LiftPortImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.LiftPortImpl

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `MarkupPort`, `NetworkPort`, `SVGElement`, `UsdElement`, `Serializable`

---

```
@AnyLogicInternalAPI
public class LiftPortImpl
extends MarkupShape
implements NetworkPort, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.LiftPortImpl)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `Lift<?>` | `getLift()` |  |
| `String` | `getName()` | If the markup shape is declared as field in an agent class, e.g. |
| `INetwork<?,?>` | `getNetwork()` | Returns the network this network port belongs to. |
| `MarkupPort` | `getPairedPort()` | Returns the paired port for this markup port. |
| `Agent` | `getSpace()` | Returns the agent where the markup element is defined |
| `double` | `getX()` |  |
| `Point` | `getXYZ()` |  |
| `double` | `getY()` |  |
| `double` | `getZ()` |  |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setPairedPort(MarkupPort pairedPort)` | Sets the paired port for this markup port. |
