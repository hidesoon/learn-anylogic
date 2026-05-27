*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractMarkupAggregator.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractMarkupAggregator<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.AbstractMarkupAggregator<T>

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `AbstractDrawableMarkupAggregator`, `AbstractNetwork`

---

```
@AnyLogicInternalAPI
public abstract class AbstractMarkupAggregator<T>
extends Object
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractMarkupAggregator)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract Stream<? extends AggregatableAnimationElement>` | `elementsInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final RuntimeException` | `error(String errorText)` | Signals an error during the model run by throwing a RuntimeException with errorText preceded by the agent full name. |
| `String` | `getName()` |  |
| `T` | `getOwner()` |  |
| `final void` | `initializeInternal()` | Initialization of markup aggregator (e.g. |
| `boolean` | `isVisible()` | Returns the visibility of the markup container. |
| `void` | `onAggregatorVisibilityChanged()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setVisible(boolean v)` | Sets the visibility of all the markup container. |
