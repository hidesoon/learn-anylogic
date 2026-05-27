*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/DensityMapGridDataStorage.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class DensityMapGridDataStorage

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.DensityMapGridDataStorage

All Implemented Interfaces:
:   `DensityMapDataStorage`, `Serializable`

---

```
@AnyLogicInternalAPI
public class DensityMapGridDataStorage
extends Object
implements DensityMapDataStorage
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.DensityMapGridDataStorage)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getValue(int xIndex, int yIndex)` |  |
| `void` | `initializeDensity(int xIndex, int yIndex, double initialDensity)` |  |
| `void` | `reset()` |  |
| `void` | `setAttenuationType(com.anylogic.engine.markup.DensityMapGridDataStorage.AttenuationType type)` |  |
| `void` | `setDensity(int xIndex, int yIndex, double newValue)` |  |
