*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/ShapePositionWatcher.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class ShapePositionWatcher<C extends Shape>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractPositionWatcher](AbstractPositionWatcher.md "class in com.anylogic.engine.omniverse_connector")<C>

com.anylogic.engine.omniverse\_connector.ShapePositionWatcher<C>

---

```
public class ShapePositionWatcher<C extends Shape>
extends AbstractPositionWatcher<C>
```

## Nested Class Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapePositionWatcher(com.anylogic.engine.internal.presentation.PresentationObjectCoordinatesCache cache, boolean updateScale)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default String` | `getFieldPath()` |  |
| `PositionAndScale` | `getPosition(C shape)` |  |
