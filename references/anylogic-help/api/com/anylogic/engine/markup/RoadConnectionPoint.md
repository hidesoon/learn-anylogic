*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RoadConnectionPoint.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RoadConnectionPoint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.RoadConnectionPoint

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public class RoadConnectionPoint
extends Object
implements Serializable
```

RoadConnectionPoint

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RoadConnectionPoint)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `canConnectTo(RoadConnectionPoint otherConnectionPoint)` | Returns possibility of connection the otherConnectionPoint to this RoadConnectionPoint |
| `void` | `connectTo(RoadConnectionPoint otherConnectionPoint)` | Connects otherConnectionPoint to this RoadConnectionPoint |
| `RoadConnectionPoint` | `createConnectedPoint(AbstractRoadConnectableElement parent)` | Creates a new RoadConnectionPoint, connected to this RoadConnectionPoint |
| `Point` | `getCentralPoint()` | Returns the start point of direction segment |
| `RoadConnectionPoint` | `getConnectedPoint()` | Returns connection point, if exists. |
| `MarkupSegmentLine` | `getConnectionSegment()` | Returns connection segment |
| `MarkupSegmentLine` | `getDirectionSegment()` | Returns direction segment |
| `AbstractRoadConnectableElement` | `getOwner()` | Returns AbstractRoadElement to which the created RoadConnectionPoint belongs to. |
| `boolean` | `isIncoming()` | Returns incoming or outgoing direction of RoadConnectionPoint |
