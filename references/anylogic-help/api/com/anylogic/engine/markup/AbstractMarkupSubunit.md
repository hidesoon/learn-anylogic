*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractMarkupSubunit.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractMarkupSubunit<OWNER extends MarkupShape>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.AbstractMarkupSubunit<OWNER>

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `Attractor`, `Escalator`, `QueuePath`, `ServiceUnit`

---

```
public abstract class AbstractMarkupSubunit<OWNER extends MarkupShape>
extends Object
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractMarkupSubunit)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractMarkupSubunit()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getName()` | If the markup shape is declared as field in an agent class, e.g. |
| `OWNER` | `getOwner()` |  |
