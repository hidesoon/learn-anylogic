*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Pair.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Pair<FIRST,SECOND>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Pair<FIRST,SECOND>

All Implemented Interfaces:
:   `Serializable`

---

```
public final class Pair<FIRST,SECOND>
extends Object
implements Serializable
```

A pair of two (possibly `null`) elements, may be used as key in maps.
Overrides [`equals(Object)`](#equals(java.lang.Object)) and [`hashCode()`](#hashCode()).
Objects of this class are immutable: they have no setter methods.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Pair)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Pair(FIRST first, SECOND second)` | Creates a new pair of two elements |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Object` | `clone()` |  |
| `boolean` | `equals(Object obj)` |  |
| `FIRST` | `getFirst()` | Returns the first (left) element from this pair |
| `SECOND` | `getSecond()` | Returns the second (right) element from this pair |
| `int` | `hashCode()` |  |
| `static <F, S> Pair<F,S>` | `of(F first, S second)` | Creates and returns new pair of two elements |
| `String` | `toString()` |  |
