*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Obstacle.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Obstacle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.Obstacle

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public final class Obstacle
extends Object
implements Serializable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Obstacle)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Obstacle(Point p1, Point p2)` |  |
| `Obstacle(Point p1, Point p2, AbstractMarkup parent)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `AbstractMarkup` | `getMarkup()` | Currently used only for: Lift, OverheadCrane, JibCrane, PalletRack, Storage |
| `Point` | `getP1()` |  |
| `Point` | `getP2()` |  |
| `double` | `getX1()` |  |
| `double` | `getX2()` |  |
| `double` | `getY1()` |  |
| `double` | `getY2()` |  |
| `void` | `setP1(Point p1)` |  |
| `void` | `setP2(Point p2)` |  |
