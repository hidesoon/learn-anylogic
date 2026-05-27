*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GISResult.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GISResult<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISResult](AbstractGISResult.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.GISResult<T>

---

```
@AnyLogicInternalAPI
public class GISResult<T>
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
| `static <T> GISResult<T>` | `empty()` |  |
| `static <T> GISResult<T>` | `error()` | network error, or cache entry expired, etc. |
| `GISResultDouble` | `flatMapToDouble(Function<T,GISResultDouble> mapper)` |  |
| `T` | `get()` |  |
| `GISResultDouble` | `mapToDouble(ToDoubleFunction<T> mapper)` |  |
| `static <T> GISResult<T>` | `of(T value)` |  |
| `T` | `orElse(T other)` | Returns `other` object in case of [`AbstractGISResult.isEmpty()`](AbstractGISResult.md#isEmpty()) of [`AbstractGISResult.isError()`](AbstractGISResult.md#isError()) |
