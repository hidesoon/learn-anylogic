*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/ALGISSafeAccess.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class ALGISSafeAccess

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.ALGISSafeAccess

---

```
@AnyLogicInternalAPI
public class ALGISSafeAccess
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static void` | `closeAllCaches()` | AnyLogicMapDB uses third-party org.mapdb whose jar may be not on the classpath, see AL-24153. |
