*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/PositionAndScale.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class PositionAndScale

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.PositionAndScale

---

```
@AnyLogicInternalAPI
public class PositionAndScale
extends Object
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `double` | `rotationX` |  |
| `double` | `rotationY` |  |
| `double` | `rotationZ` |  |
| `double` | `scaleX` |  |
| `double` | `scaleY` |  |
| `double` | `scaleZ` |  |
| `org.joml.Matrix4d` | `transformMatrix` |  |
| `double` | `x` |  |
| `double` | `y` |  |
| `double` | `z` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PositionAndScale(double x, double y, double z, double rotationX, double rotationY, double rotationZ, double scale)` |  |
| `PositionAndScale(double x, double y, double z, double rotationX, double rotationY, double rotationZ, double scaleX, double scaleY, double scaleZ)` |  |
| `PositionAndScale(Agent agent, boolean setScale)` |  |
| `PositionAndScale(AbstractPositionalMarkup shape)` |  |
| `PositionAndScale(Position position, double scale)` |  |
| `PositionAndScale(Shape shape)` |  |
| `PositionAndScale(ShapeGroup shape)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Position` | `getPosition()` |  |
