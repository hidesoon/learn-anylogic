*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeInspect.FakeInspectedShape.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Record Class ShapeInspect.FakeInspectedShape

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html "class or interface in java.lang")

com.anylogic.engine.presentation.ShapeInspect.FakeInspectedShape

All Implemented Interfaces:
:   `Serializable`

Enclosing class:
:   [ShapeInspect](ShapeInspect.md "class in com.anylogic.engine.presentation")

---

```
public static record ShapeInspect.FakeInspectedShape(double x, double y, Object originalShape)
extends Record
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeInspect.FakeInspectedShape)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `FakeInspectedShape(double x, double y, Object originalShape)` | Creates an instance of a `FakeInspectedShape` record class. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final boolean` | `equals(Object o)` | Indicates whether some other object is "equal to" this one. |
| `final int` | `hashCode()` | Returns a hash code value for this object. |
| `Object` | `originalShape()` | Returns the value of the `originalShape` record component. |
| `final String` | `toString()` | Returns a string representation of this record class. |
| `double` | `x()` | Returns the value of the `x` record component. |
| `double` | `y()` | Returns the value of the `y` record component. |
