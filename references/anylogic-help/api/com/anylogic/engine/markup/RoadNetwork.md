*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RoadNetwork.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RoadNetwork

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<[Agent](../Agent.md "class in com.anylogic.engine")>

[com.anylogic.engine.markup.AbstractDrawableMarkupAggregator](AbstractDrawableMarkupAggregator.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.RoadNetwork

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `Serializable`

---

```
public class RoadNetwork
extends AbstractDrawableMarkupAggregator
implements LevelMarkup, AggregatableAnimationElement
```

CarNetwork

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RoadNetwork)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RoadNetwork(Agent owner, String name, ShapeDrawMode drawMode)` | Creates empty RoadNetwork with all parameters set by default. |
| `RoadNetwork(Agent owner, String name, ShapeDrawMode drawMode, boolean isPublic, boolean visible, RoadDrivingDirection drivingDirection, double laneWidthInMeters, Paint roadBackgroundColor, Paint lanesDelimitingLineColor, RoadLineStyle lanesDelimitingLineStyle, Paint directionsDelimitingLineColor, RoadLineStyle directionsDelimitingLineStyle, boolean isSignalStateAnimationVisible)` | Creates RoadNetwork but doesn't initialize it |
| `RoadNetwork(Agent owner, String name, ShapeDrawMode drawMode, boolean isPublic, boolean visible, RoadDrivingDirection drivingDirection, double laneWidthInMeters, Paint roadBackgroundColor, Paint lanesDelimitingLineColor, RoadLineStyle lanesDelimitingLineStyle, Paint directionsDelimitingLineColor, RoadLineStyle directionsDelimitingLineStyle, boolean isSignalStateAnimationVisible, TrafficLight<?>[] trafficLights, AbstractRoadMarkup... markupElements)` | Creates RoadNetwork and initializes it |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(BusStop element)` | Adds a specified bus stop to the network. |
| `void` | `add(Intersection element)` | Adds a specified intersection to the network. |
| `void` | `add(ParkingLot element)` | Adds a specified parking lot to the network. |
| `void` | `add(Road element)` | Adds a specified road to the network. |
| `void` | `add(StopLine element)` | Adds a specified StopLine to the network. |
| `void` | `add(TrafficLight<?> element)` | Adds a specified traffic light to the network. |
| `void` | `addAll(AbstractRoadMarkup... contents)` | Adds all arguments to the network |
| `Stream<? extends AbstractRoadMarkup>` | `elementsInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `List<BusStop>` | `getBusStops()` | Returns all bus stops contained in this RoadNetwork |
| `Color` | `getDirectionsDelimitingLineColor()` | Returns the color of the directions delimiting line color, or `null` if directions delimiting line color has no color or has textured (in this case `#getFillTexture()` should be used instead) |
| `RoadLineStyle` | `getDirectionsDelimitingLineStyle()` | Returns style of the directions delimiting line |
| `Texture` | `getDirectionsDelimitingLineTexture()` | Returns the texture of the directions delimiting line color, if the directions delimiting line color has texture |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `RoadDrivingDirection` | `getDrivingDirection()` | Returns driving direction |
| `List<Intersection>` | `getIntersections()` | Returns all intersections and lane mergings contained in this RoadNetwork |
| `Color` | `getLanesDelimitingLineColor()` | Returns the color of the road lanes delimiting line color, or `null` if road lanes delimiting line color has no color or has textured (in this case `#getFillTexture()` should be used instead) |
| `RoadLineStyle` | `getLanesDelimitingLineStyle()` | Returns style of the road lanes delimiting line |
| `Texture` | `getLanesDelimitingLineTexture()` | Returns the texture of the road lanes delimiting line color, if the road lanes delimiting line color has texture |
| `double` | `getLaneWidth()` | Returns lane width |
| `double` | `getLaneWidth(LengthUnits units)` | Returns lane width |
| `Level` | `getLevel()` | Returns level associated with this space markup element or `null` if this element has no level |
| `List<ParkingLot>` | `getParkingLots()` | Returns all parking lots contained in this RoadNetwork |
| `Color` | `getRoadBackgroundColor()` | Returns the road background color, or `null` if road has no background color or has texture (in this case `#getFillTexture()` should be used instead) |
| `Texture` | `getRoadBackgroundTexture()` | Returns the texture of the road background, if the road has background texture |
| `List<Road>` | `getRoads()` | Returns all roads contained in this RoadNetwork |
| `List<StopLine>` | `getStopLines()` | Returns all stop lines contained in this RoadNetwork |
| `List<TrafficLight<?>>` | `getTrafficLights()` | Returns all Traffic Lights contained in this RoadNetwork |
| `boolean` | `isSignalStateAnimationVisible()` | Returns `true` if configured to animate signal states of stop lines and lane connectors |
| `void` | `setDebugInfoVisible(boolean debugInfoVisible)` | Deprecated. TODO remove in release |
| `void` | `setDirectionsDelimitingLineColor(Color directionsDelimitingLineColor)` | Sets the color of the directions delimiting line. |
| `void` | `setDirectionsDelimitingLineColor(Paint directionsDelimitingLineColor)` | Sets the color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the directions delimiting line. |
| `void` | `setDirectionsDelimitingLineStyle(RoadLineStyle directionsDelimitingLineStyle)` | Sets style of the directions delimiting line |
| `void` | `setDrivingDirection(RoadDrivingDirection drivingDirection)` | Sets driving direction |
| `void` | `setLanesDelimitingLineColor(Color lanesDelimitingLineColor)` | Sets the color of the road lanes delimiting line color. |
| `void` | `setLanesDelimitingLineColor(Paint lanesDelimitingLineColor)` | Sets the color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the road lanes delimiting line color. |
| `void` | `setLanesDelimitingLineStyle(RoadLineStyle lanesDelimitingLineStyle)` | Sets style of the road lanes delimiting line |
| `void` | `setLaneWidth(double laneWidthInPixels)` | Sets lane width |
| `void` | `setLaneWidth(double laneWidth, LengthUnits units)` | Sets lane width |
| `void` | `setLevel(Level level)` |  |
| `void` | `setRoadBackgroundColor(Color roadBackgroundColor)` | Sets the color of the road background color. |
| `void` | `setRoadBackgroundColor(Paint roadBackgroundColor)` | Sets the background color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the road. |
| `void` | `setSignalStateAnimationVisible(boolean visible)` | Sets debug animation visibility. |
