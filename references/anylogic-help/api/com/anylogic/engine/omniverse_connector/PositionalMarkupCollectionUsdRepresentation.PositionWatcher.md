*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/PositionalMarkupCollectionUsdRepresentation.PositionWatcher.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class PositionalMarkupCollectionUsdRepresentation.PositionWatcher

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractPositionWatcher](AbstractPositionWatcher.md "class in com.anylogic.engine.omniverse_connector")<[AbstractPositionalMarkup](../markup/AbstractPositionalMarkup.md "interface in com.anylogic.engine.markup")>

com.anylogic.engine.omniverse\_connector.PositionalMarkupCollectionUsdRepresentation.PositionWatcher

Enclosing class:
:   [PositionalMarkupCollectionUsdRepresentation](PositionalMarkupCollectionUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<[C](PositionalMarkupCollectionUsdRepresentation.md "type parameter in PositionalMarkupCollectionUsdRepresentation") extends [AbstractPositionalMarkup](../markup/AbstractPositionalMarkup.md "interface in com.anylogic.engine.markup")>

---

```
public static class PositionalMarkupCollectionUsdRepresentation.PositionWatcher
extends AbstractPositionWatcher<AbstractPositionalMarkup>
```

## Nested Class Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PositionWatcher(com.anylogic.engine.internal.presentation.PresentationObjectCoordinatesCache cache)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default String` | `getFieldPath()` |  |
| `PositionAndScale` | `getPosition(AbstractPositionalMarkup markup)` |  |
