*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/ShapeUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class ShapeUsdRepresentation<C extends Shape>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractUsdRepresentation](AbstractUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<C>

com.anylogic.engine.omniverse\_connector.ShapeUsdRepresentation<C>

Type Parameters:
:   `C` - Shape class

All Implemented Interfaces:
:   `UsdRepresentation<C>`

---

```
public class ShapeUsdRepresentation<C extends Shape>
extends AbstractUsdRepresentation<C>
```

Associates a single shape element with a prim.

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeUsdRepresentation(UsdContext context, C object, String usdPrimPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static boolean` | `isVisible(Shape shape)` |  |
