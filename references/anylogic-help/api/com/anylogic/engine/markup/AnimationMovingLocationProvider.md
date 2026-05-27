*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AnimationMovingLocationProvider.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface AnimationMovingLocationProvider

All Superinterfaces:
:   `AnimationStaticLocationProvider`, `Serializable`

All Known Subinterfaces:
:   `IPath<N>`

All Known Implementing Classes:
:   `ConveyorPath`, `GISRoute`, `Path`

---

```
public interface AnimationMovingLocationProvider
extends AnimationStaticLocationProvider
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Position` | `getPosition(double value, double maxValue, Position out)` | Returns position with offset corresponding to the given `value`, assuming that `0` is start and `maxValue` is end |
| `double` | `length()` | Returns the length of markup element, used e.g. |
| `double` | `length(LengthUnits units)` | Returns the length of markup element, used e.g. |
