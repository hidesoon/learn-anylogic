*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IUnits.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IUnits<T extends IUnits<T>>

Type Parameters:
:   `T` - the self-type of units enum

All Known Implementing Classes:
:   `AccelerationUnits`, `AmountUnits`, `AngleUnits`, `AreaUnits`, `FlowRateUnits`, `LengthUnits`, `RateUnits`, `RotationSpeedUnits`, `SpeedUnits`, `TimeUnits`

---

```
public interface IUnits<T extends IUnits<T>>
```

Base interface for all units enumerations

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final List<Class<? extends IUnits<?>>>` | `ALL_UNIT_TYPES` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertTo(double value, T units)` | Converts the given value from **this** units to the given `units` |
| `String` | `getName()` | Returns human-readable name (e.g. |
| `double` | `modifier(T units)` |  |
| `String` | `name()` | Returns the name of the constant (e.g. |
