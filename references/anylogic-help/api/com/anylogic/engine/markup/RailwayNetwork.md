*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RailwayNetwork.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RailwayNetwork

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<[Agent](../Agent.md "class in com.anylogic.engine")>

[com.anylogic.engine.markup.AbstractDrawableMarkupAggregator](AbstractDrawableMarkupAggregator.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.RailwayNetwork

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `Serializable`

---

```
public class RailwayNetwork
extends AbstractDrawableMarkupAggregator
implements LevelMarkup, AggregatableAnimationElement
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RailwayNetwork)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RailwayNetwork(Agent owner, String name, ShapeDrawMode drawMode, double z)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases |
| `RailwayNetwork(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases |
| `RailwayNetwork(Agent owner, String name, ShapeDrawMode drawMode, double z, boolean isPublic, boolean visible, AbstractRailwayMarkup... contents)` | Deprecated. deprecated in version 8.5.0, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(PositionOnTrack pointOnTrack)` | Adds a PositionOnTrack object to the network. |
| `void` | `add(RailwaySwitch sw)` | Adds a RailwaySwitch object to the network. |
| `void` | `add(RailwayTrack track)` | Adds a RailwayTrack object to the network. |
| `void` | `addAll(AbstractRailwayMarkup... contents)` | Adds all arguments to the network |
| `Stream<? extends AbstractMarkup>` | `elementsInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `List<PositionOnTrack>` | `getPointOnTracks()` | Returns the list of all PositionOnTrack elements in this network. |
| `Agent` | `getSpace()` |  |
| `List<RailwaySwitch>` | `getSwitches()` | Returns the list of all switches in this network. |
| `List<RailwayTrack>` | `getTracks()` | Returns the list of all tracks in this network. |
| `double` | `getZ()` | Returns the base level z coordinate |
| `double` | `metersToPixels(double value)` | Converts specified value from meters to pixels in the space of this network |
| `double` | `pixelsToMeters(double value)` | Converts specified value from pixels to meters in the space of this network |
| `void` | `setLevel(Level level)` |  |
| `void` | `setZ(double z)` | Sets the base level z coordinate. |
