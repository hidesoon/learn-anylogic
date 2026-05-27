*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GISResultDouble.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GISResultDouble

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISResult](AbstractGISResult.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.GISResultDouble

---

```
@AnyLogicInternalAPI
public class GISResultDouble
extends AbstractGISResult
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static GISResultDouble` | `empty()` |  |
| `static GISResultDouble` | `error()` | network error, or cache entry expired, etc. |
| `double` | `getAsDouble()` |  |
| `static GISResultDouble` | `of(double value)` |  |
| `double` | `orElse(double other)` | Returns `other` value in case of [`AbstractGISResult.isEmpty()`](AbstractGISResult.md#isEmpty()) of [`AbstractGISResult.isError()`](AbstractGISResult.md#isError()) |
