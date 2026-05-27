*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Scale.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Scale

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Scale

All Implemented Interfaces:
:   `Serializable`

---

```
public class Scale
extends Object
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Scale)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Scale` | `DEFAULT_SCALE` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Scale(double pixelsPerMeter)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `pixelsPerUnit(LengthUnits unit)` | Returns the number of pixels corresponding to one given unit, according to the scaling settings of this objects |
| `double` | `toLengthUnits(double lengthInPixels, LengthUnits units)` | Converts the given pixel length to the length units |
| `double` | `toPixels(double lengthInUnits, LengthUnits units)` | Converts the length in the given length units to pixels |
