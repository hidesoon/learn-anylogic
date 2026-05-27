*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RailwaySwitch.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RailwaySwitch

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRailwayMarkup](AbstractRailwayMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.RailwaySwitch

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `RailMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class RailwaySwitch
extends AbstractRailwayMarkup
implements AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RailwaySwitch)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static interface` | `RailwaySwitch.IRailwaySwitchType` |  |

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RailwaySwitch()` |  |
| `RailwaySwitch(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `RailwaySwitch(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double radius, Color selectionColor, Paint color, RailwaySwitch.IRailwaySwitchType type, RailwayTrack... tracks)` |  |
| `RailwaySwitch(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double radius, Color selectionColor, Paint color, RailwayTrack track, RailwayTrack... alternativeTracks)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `connectTracks(RailwayTrack source, RailwayTrack target)` | The switch is set to the state (one of them, if several) which allows the travel from source to target track |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `RailwayTrack` | `currentStateNextTrack(RailwayTrack source)` | Returns the next track (for the current state), if the switch is approached from a given track. |
| `List<RailwayTrack>` | `getAlternativeTracks()` | Deprecated. Switches with more than 3 connected tracks do not have a notion of "Alternative Tracks" |
| `List<RailwayTrack>` | `getAvailableTracks(RailwayTrack source)` | Finds all the tracks that are available to go to if we approach the switch from source track |
| `Paint` | `getColor()` | Returns the color (or texture) of the switch. |
| `SwitchDataSource` | `getDataSource()` |  |
| `RailwayTrack` | `getMainTrack()` | Deprecated. Switches with more than 3 connected tracks do not have a notion of "Main Track" |
| `double` | `getRadius()` | Returns the radius of this switch |
| `RailwayTrack` | `getSelectedTrack()` | Deprecated. Switches with more than 3 connected tracks do not have a notion of "Selected Track". |
| `Color` | `getSelectionColor()` | Returns the color of the line animating the current switch position at model runtime. |
| `int` | `getToggleCount()` | Get the number of times the switch was toggled |
| `RailwayTrack` | `getTrack(int index)` | Returns the track with a given index connected to the switch. |
| `List<RailwayTrack>` | `getTracks()` | Returns the list of all tracks connected to this switch |
| `double` | `getX()` | Returns X coordinate of this element |
| `double` | `getY()` | Returns Y coordinate of this element |
| `double` | `getZ()` | Returns Z coordinate of this element |
| `boolean` | `isTrailingPoint(RailwayTrack from)` | Tests if movement from a given track through the switch is a trailing point movement or face point. |
| `RailwayTrack` | `nextTrack(RailwayTrack source)` | Returns the next track, if the switch is approached from a given track. |
| `boolean` | `onClick(double clickx, double clicky)` | Should be overridden to define the shape reaction on mouse click. |
| `void` | `setAllToAllType()` | Sets the type of the switch to All to All. |
| `void` | `setColor(Paint color)` | Sets the color (or texture) of the switch. |
| `void` | `setDoubleSlipType()` | Sets the type of the switch to Double Slip. |
| `void` | `setNextFeasibleState(RailwayTrack source)` |  |
| `void` | `setRadius(double radius)` | Sets the radius of this switch |
| `void` | `setSelectedTrack(RailwayTrack track)` | Deprecated. Switches with more than 3 connected tracks do not have a notion of "Selected Track" Use [`connectTracks(RailwayTrack, RailwayTrack)`](#connectTracks(com.anylogic.engine.markup.RailwayTrack,com.anylogic.engine.markup.RailwayTrack)) to set a switch state in which 2 specified tracks are connected (if such state exists) |
| `void` | `setSelectionColor(Color selectionColor)` | Sets the color of the line animating the current switch position at model runtime. |
| `void` | `setSingleSlipType(RailwayTrack track)` | Sets the type of the switch to Single Slip. |
| `void` | `setSwitch(RailwayTrack track, RailwayTrack... alternativeTracks)` | Deprecated. use [`setTracks(RailwayTrack...)`](#setTracks(com.anylogic.engine.markup.RailwayTrack...)) and one of the methods to set switch type: [`setAllToAllType()`](#setAllToAllType()), [`setSingleSlipType(RailwayTrack)`](#setSingleSlipType(com.anylogic.engine.markup.RailwayTrack)) , [`setDoubleSlipType()`](#setDoubleSlipType()) |
| `void` | `setTracks(RailwayTrack... tracks)` | Sets the tracks that are connected to the switch. |
| `void` | `setType(RailwaySwitch.IRailwaySwitchType type)` |  |
| `boolean` | `stateExists(RailwayTrack source, RailwayTrack target)` | Checks if there is a state in which you can travel through switch from source track to target track |
| `void` | `toggle()` | Toggles the selected tracks. |
| `boolean` | `trackStarts(RailwayTrack track)` | Returns true if a given track start at the switch, and false if it ends there. |
