*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/AbstractPositionWatcher.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class AbstractPositionWatcher<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.omniverse\_connector.AbstractPositionWatcher<T>

Direct Known Subclasses:
:   `PositionalMarkupCollectionUsdRepresentation.PositionWatcher`, `ShapePositionWatcher`

---

```
public abstract class AbstractPositionWatcher<T>
extends Object
```

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `AbstractPositionWatcher.BasisType` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractPositionWatcher(com.anylogic.engine.internal.presentation.PresentationObjectCoordinatesCache cache)` |  |
| `AbstractPositionWatcher(com.anylogic.engine.internal.presentation.PresentationObjectCoordinatesCache cache, boolean updateScale)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static final void` | `addGlobalTransformator(Consumer<PositionAndScale> transformator)` |  |
| `final void` | `addTransformator(Consumer<PositionAndScale> transformator)` |  |
| `static double` | `fixRotation(double angle)` |  |
| `final String` | `getFieldName()` |  |
| `default String` | `getFieldPath()` |  |
| `String` | `getFieldValue(T t)` |  |
| `static PositionAndScale` | `getPositionAndScaleForMatrix(org.joml.Matrix4d matrix4d)` |  |
| `void` | `setBasis(AbstractPositionWatcher.BasisType basis)` |  |
| `static void` | `setFixBasisMirroring(boolean fixBasisMirroring)` |  |
| `void` | `setTopLevelAgent(Agent agent)` |  |
