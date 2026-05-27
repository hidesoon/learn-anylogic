*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/ShapeCollectionUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class ShapeCollectionUsdRepresentation<C extends Shape>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractInstancingUsdRepresentation](AbstractInstancingUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<A>

[com.anylogic.engine.omniverse\_connector.CollectionUsdRepresentation](CollectionUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<C>

com.anylogic.engine.omniverse\_connector.ShapeCollectionUsdRepresentation<C>

All Implemented Interfaces:
:   `InstancingUsdRepresentation<C>`, `UsdRepresentation<C>`

Direct Known Subclasses:
:   `Shape3DObjectCollectionUsdRepresentation`

---

```
@AnyLogicInternalAPI
public class ShapeCollectionUsdRepresentation<C extends Shape>
extends CollectionUsdRepresentation<C>
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeCollectionUsdRepresentation(UsdContext context, Iterable<C> population, List<String> assetPath, String containerPath, String innerPath, String parentContainerPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static boolean` | `isShapeChanged(Shape item)` |  |
| `static boolean` | `isShapeChanged(Shape item, Predicate<Shape> check, Consumer<Shape> change)` | Check shape was changed using provided check function. |
