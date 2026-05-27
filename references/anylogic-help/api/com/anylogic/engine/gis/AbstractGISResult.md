*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AbstractGISResult.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AbstractGISResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.AbstractGISResult

Direct Known Subclasses:
:   `GISResult`, `GISResultDouble`

---

```
@AnyLogicInternalAPI
public class AbstractGISResult
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `AbstractGISResult.Type` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `isEmpty()` | NB: In case of [`isError()`](#isError()), this method will return `false` |
| `boolean` | `isError()` | network error, or cache entry expired, etc. |
| `boolean` | `isPresent()` |  |
