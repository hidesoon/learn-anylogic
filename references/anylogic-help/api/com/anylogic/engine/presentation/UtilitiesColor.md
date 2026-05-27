*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/UtilitiesColor.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class UtilitiesColor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.UtilitiesColor

All Implemented Interfaces:
:   `ColorConstants`

---

```
public final class UtilitiesColor
extends Object
implements ColorConstants
```

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Texture` | `brickRedTexture` |  |
| `static final Texture` | `brickWhiteTexture` |  |
| `static final Texture` | `concreteTexture` |  |
| `static final Texture` | `earthTexture` |  |
| `static final Texture` | `floorCarpetTexture` |  |
| `static final Texture` | `floorLinoTexture` |  |
| `static final Texture` | `floorMetalTexture` |  |
| `static final Texture` | `floorWoodTexture` |  |
| `static final Texture` | `grassTexture` |  |
| `static final Texture` | `gravelTexture` |  |
| `static final Texture` | `metalTexture` |  |
| `static final Texture` | `roofCeramicTexture` |  |
| `static final Texture` | `roofMetalTexture` |  |
| `static final Texture` | `sandTexture` |  |
| `static final Texture` | `snowTexture` |  |
| `static final Texture` | `tarmacTexture` |  |
| `static final Texture` | `waterTexture` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static Color` | `darker(Color c, double factor)` | Creates a new color darker than the original color by a given factor. |
| `static final Color` | `getStandardColor(int index)` | Returns a standard color with the given index, or null if the index is out of range [0..`ColorConstants.MAX_COLORS`]. |
| `static final Integer` | `indexToIntColorConstant(int indexc)` | Deprecated. |
| `static Color` | `lerpColor(double frac, Color from, Color to)` | Returns a new Color - a point on a linear interpolation between from and to Colors, whose position is defined by `frac`: if `frac <= 0` `from` is returned, if `frac >= 1`, `to` is returned, otherwise a color in between. |
| `static Color` | `semiTransparent(Color c)` | Creates a semitransparent version of the given color, regardless of its original transparency. |
| `static Color` | `spectrumColor(int index, int period)` | Returns a good looking spectrum color constructed from a given integer repeated with a given period. |
| `static Color` | `transparent(Color c, double fraction)` | Creates a transparent version of the given color, regardless of its original transparency. |
