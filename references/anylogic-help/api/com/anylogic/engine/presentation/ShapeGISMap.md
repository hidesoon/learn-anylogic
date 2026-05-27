*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeGISMap.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeGISMap

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeGISMap

All Implemented Interfaces:
:   `AbstractShapeGISMap`, `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeGISMap
extends Shape3D
implements AbstractShapeGISMap
```

GIS map projection manager and map renderer (persistent GIS Map shape which
displays and map projection)
GIS map is a [`Shape`](Shape.md "class in com.anylogic.engine.presentation") and it can be placed on the model animation: it
renders the associated map projection on the screen
This class provides several projection methods

General information:
Coordinates of any point are presented as:

* the latitude of point, measured in degrees (-90 ... (South) ... 0 ...
  (North) ... +90)
* the longitude of point, measured in degrees (-180 ... (West) ... 0 ...
  (East) ... +180)

The following order of coordinates is assumed: (latitude, longitude)
Implementation is based on OpenMap and GeoTools GIS libraries

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeGISMap)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `ShapeGISMap.Layer` | Class which stores GIS map layer information |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final AbstractGISRouteProvider` | `STRAIGHT` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeGISMap(Presentable presentable, ShapeDrawMode drawMode, boolean ispublic, double x, double y, double width, double height, String packagePrefix, ShapeGISMap.Layer[] layers, double centerLatitude, double centerLongitude, double mapScale, Color mapBorderColor, Color mapBackgroundColor, boolean showTiles, TileURLProviderType tileURLProviderType, String[] tileURLs, IGISRouteProvider routeProvider, int searchPrecisionInMeters)` | Constructs a GIS Map shape with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(GISMultiRegion markupElement)` | Adds GIS markup element to drawing set of elements. |
| `void` | `add(GISMarkupElement markupElement)` | Adds GIS markup element to drawing set of elements. |
| `void` | `changeViewPosition(double latitude, double longitude, double zoom)` | Remember user changes of the map view position. |
| `final ShapeGISMap` | `clone()` | **Cloning of GIS is not supported**  (Other shapes except controls and charts allow cloning)  This method throws `UnsupportedOperationException` if called |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `destroy()` | Deprecated. |
| `void` | `dispose()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `fitBounds(double bottomLat, double leftLon, double topLat, double rightLon)` | Make map fits specified bounds. |
| `double` | `fromLengthUnits(double length, LengthUnits units)` | Convert value of length measured in given units to meters |
| `double` | `getCenterLatitude()` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `getCenterLongitude()` | Deprecated. this function is deprecated and will be removed in the next release |
| `double` | `getDistance(double latFrom, double lonFrom, double latTo, double lonTo)` | Returns distance, in meters, between 2 given points |
| `double` | `getDistance(GISPoint fromPoint, GISPoint toPoint)` | Returns distance, in meters, between 2 given points |
| `double` | `getDistanceByRoute(double latFrom, double lonFrom, double latTo, double lonTo)` | Calculates length of route from one point to another. |
| `double` | `getDistanceByRoute(GISPoint fromPoint, GISPoint toPoint)` | Calculates length of route from one point to another. |
| `double` | `getHeight()` | Returns the height of the shape. |
| `ShapeGISMap.Layer[]` | `getLayers()` | Returns the array of layers used in this GIS Map  Returned array shouldn't be modified structurally: only items can be accessed for modification |
| `LegacyShapeGISMapProjection` | `getLegacyProj()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `getMapScale()` | Deprecated. this function is deprecated and will be removed in the next release |
| `Presentable` | `getPresentable()` | Returns the Presentable object ([`Agent`](../Agent.md "class in com.anylogic.engine") or [`Experiment`](../Experiment.md "class in com.anylogic.engine")) where this shape belongs to, or null. |
| `GISRoute` | `getRoute(double startLatitude, double startLongitude, double endLatitude, double endLongitude)` | Creates an unidirectional route from one geographic point to another. |
| `GISRoute` | `getRoute(double startLatitude, double startLongitude, double endLatitude, double endLongitude, boolean bidirectional)` | Creates route from one geographic point to another. |
| `GISRoute` | `getRoute(GISPoint start, GISPoint end)` | Creates an unidirectional route from one geographic point to another. |
| `GISRoute` | `getRoute(GISPoint start, GISPoint end, boolean bidirectional)` | Creates route from one geographic point to another. |
| `IGISRouteProvider` | `getRouteProvider()` | Retrieves default route provider for all agents in GIS space. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `double` | `getWidth()` | Returns the width of the shape. |
| `boolean` | `isLayerVisible(String shapeFileName)` | Tests if a shapefile layer is visible |
| `boolean` | `isMouseNavigationEnabled()` | Returns `true` if panning and zooming with a mouse are allowed. |
| `static double` | `normalizeLatitude(double degrees)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static double` | `normalizeLongitude(double degrees)` | Returns given longitude adjusted to be in `-180...180` interval  (Sometimes longitude might be specified with precision 360\*n) |
| `static double` | `normalizeScale(double mapScale)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `onClick(double latitude, double longitude)` | Should be overridden to define the shape reaction on mouse click. |
| `void` | `pan(double toEast, double toNorth)` | Moves the map projection center  Parameters are amounts of delta in the resulting offset  One horizontal delta is a half of longitude difference from map projection center to the west/east bound of projection  One vertical delta is a half of latitude difference from map projection center to the south/north bound of projection |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `void` | `remove(GISMultiRegion markupElement)` | Removes GIS markup element from drawing set of elements. |
| `void` | `remove(GISMarkupElement markupElement)` | Removes GIS markup element from drawing set of elements. |
| `void` | `resetSVGComponent()` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `List<GISPoint>` | `search(String query)` |  |
| `List<GISNode>` | `search(String query, boolean area, boolean visibleAreaOnly)` |  |
| `GISPoint` | `searchFirst(String query)` | Search for a point on the Earth corresponding to the user's query. |
| `GISMultiRegion` | `searchFirstMultiRegion(String query)` |  |
| `GISRegion` | `searchFirstRegion(String query)` |  |
| `List<GISMultiRegion>` | `searchMultiRegion(String query)` |  |
| `List<GISRegion>` | `searchRegion(String query)` |  |
| `void` | `setCenterLatitude(double centerLatitude)` | Sets the latitude of the map projection center, measured in degrees (-90 ... |
| `void` | `setCenterLongitude(double centerLongitude)` | Sets the longitude of the map projection center, measured in degrees (-180 ... |
| `void` | `setHeight(double height)` | Sets the height of the shape. |
| `void` | `setLayerVisibility(String shapeFileName, boolean visible)` | Shows or hides a shapefile layer. |
| `void` | `setMapScale(double mapScale)` | Sets the scale of map projection |
| `void` | `setMouseNavigationEnabled(boolean mouseNavigationEnabled)` | Manage ability to pan and zoom the map with a mouse. |
| `void` | `setProjectionCenter(double centerLatitude, double centerLongitude)` | Sets the center of the map projection |
| `void` | `setSearchBounds(double bottomLatitude, double leftLongitude, double topLatitude, double rigthLongitude)` | Sets bounds for search area. |
| `void` | `setWidth(double width)` | Sets the width of the shape. |
| `double` | `toLengthUnits(double length, LengthUnits units)` | Convert value of length measured in meters to given length units |
| `boolean` | `updateDynamicPropertiesStructural(boolean publicOnly)` |  |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
| `void` | `zoomIn()` | Increases scale of map projection (`x 2`) |
| `void` | `zoomOut()` | Decreases scale of map projection (`x 1/2`) |
