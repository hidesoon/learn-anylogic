*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PalletRackLocation.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PalletRackLocation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.PalletRackLocation

All Implemented Interfaces:
:   `Serializable`

---

```
public class PalletRackLocation
extends Object
implements Serializable
```

Location in [`PalletRack`](PalletRack.md "class in com.anylogic.engine.markup")

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PalletRackLocation)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `int` | `level` | Level (0, 1, ...) |
| `int` | `position` | Position in row (0, 1, ...) |
| `int` | `row` | The number of pallet rack (0 or 1). |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PalletRackLocation()` | Default constructor |
| `PalletRackLocation(int row, int position, int level)` | Constructor initializing the fields |
| `PalletRackLocation(PalletRackLocation location)` | Copy constructor |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `toString()` |  |
