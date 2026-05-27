*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/DensityMap.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class DensityMap

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.DensityMap

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class DensityMap
extends AbstractLevelMarkup
```

Markup element Density Map. Enables collecting statistics on the density of moving units
in the simulated space and displaying this information on animation as a density map. This functionality
is supported for pedestrians and transporters with free space navigation.

Having added the Density Map element, you enable showing the density map of the specified type
(pedestrian or transporter) for your simulation model. If you have transporters and pedestrians
moving on the same level and need to track the density for both, you have to add two Density Map
elements: one per type. Note, that the density maps located on one level must be of different types,
otherwise an error will occur.

You will see that as pedestrians or transporters move in the simulated space, the layout is gradually
painted in different colors. The color of every point of the space corresponds to the current density in
this particular area. The density map is constantly repainted according to the actual values: when the density
changes in some point, the color changes dynamically to reflect this change. In case of zero density the area
is not painted at all. If you have transporters and pedestrians moving in the same area, the density maps won't
display the aggregate density, only separate one for each type.

The element itself acts as the color legend for the density map. It displays the correspondence between
density values and colors on the map.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.DensityMap)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DensityMap()` | Creates markup object Density Map with default parameters. |
| `DensityMap(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double width, double height, double transparency, double criticalDensity, DensityMapDisplayedValue displayedValue, boolean slidingWindow, double windowTimeMTU, boolean enableAttenuation, DensityMapType type, DensityMapColorScheme colorScheme)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `currentDensity(double x, double y)` | Returns the current density value in the area neighboring the specified point, units/m2. |
| `Color` | `customColor(double density)` | This method should be overridden to return color in `CUSTOM` color scheme |
| `void` | `display(boolean flag)` | Shows the density map if `flag == true` and hides otherwise. |
| `Color` | `getColor(double density)` | Returns the color matching for the specified density value |
| `Color` | `getColor(double density, boolean reducePrecision)` | Deprecated. - A possibility to get non-reduced color is eliminated. |
| `DensityMapColorScheme` | `getColorScheme()` | Returns the color scheme of this density map |
| `double` | `getCriticalDensity()` | Returns the critical density for the density map, in selected units / m^2. |
| `DensityMapDataStorage` | `getDataStorage()` |  |
| `DensityMapDisplayedValue` | `getDensityValue()` | Returns the 'Displayed density value' parameter. |
| `double` | `getHeight()` | Returns height of the density map legend |
| `double` | `getSlidingWindow()` | Returns sliding window time in model time units. |
| `double` | `getSlidingWindow(TimeUnits units)` | Returns sliding window in specified time units. |
| `double` | `getTransparency()` | Returns the density map transparency |
| `DensityMapType` | `getType()` | Returns the type of density map. |
| `double` | `getWidth()` | Returns width of the density map legend |
| `double` | `getX()` | Returns x coordinate of the density map legend |
| `double` | `getY()` | Returns y coordinate of the density map legend |
| `void` | `hide()` | Hides the density map. |
| `boolean` | `isEnableAttenuation()` | Returns true if the density map is shown with attenuation; returns false otherwise. |
| `double` | `maximumDensity(double x, double y)` | Returns maximum observed density at the specified point |
| `double` | `meanDensity(double x, double y)` | Returns mean density at the specified point |
| `void` | `onDestroy()` |  |
| `void` | `prepareGridBasedMap(double xUpperLeftPx, double yUpperLeftPx, int xCellCount, int yCellCount, double cellSizePx)` |  |
| `void` | `reset()` | Resets maximum density to current density |
| `void` | `setColorScheme(DensityMapColorScheme colorScheme)` | Defines the color scheme for density map. |
| `void` | `setCriticalDensity(double criticalDensity)` | Sets the critical density for the density map, in selected units / m^2. |
| `void` | `setDensityValue(DensityMapDisplayedValue valueType)` | Sets the 'Displayed density value' parameter. |
| `void` | `setEnableAttenuation(boolean enable)` | Enables/disables attenuation for the density map. |
| `void` | `setHeight(double height)` | Sets height of the density map legend |
| `void` | `setOwner(Agent owner)` | Sets the owner of the markup element |
| `void` | `setSlidingWindow(double time)` | Enables sliding window with specified time. |
| `void` | `setSlidingWindow(double time, TimeUnits units)` | Enables sliding window with specified time. |
| `void` | `setTransparency(double transparency)` | Set the density map transparency. |
| `void` | `setType(DensityMapType type)` | Sets the density map type. |
| `void` | `setWidth(double width)` | Sets width of the density map legend |
| `void` | `setX(double x)` | Sets x coordinate of the density map legend |
| `void` | `setY(double y)` | Sets y coordinate of the density map legend |
| `void` | `show()` | Shows the density map. |
