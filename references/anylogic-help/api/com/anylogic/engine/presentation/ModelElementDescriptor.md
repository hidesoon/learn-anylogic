*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ModelElementDescriptor.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ModelElementDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.ModelElementDescriptor

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public final class ModelElementDescriptor
extends Object
implements Serializable
```

As long as at runtime the information about the model elements
such as position of their icons, visibility of labels, and sometimes even type
is lost, this class should contain all info needed for displaying the
element and its info at runtime, including the reference to the element itself.

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ModelElementDescriptor)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `final int` | `index` |  |
| `final boolean` | `isPublic` |  |
| `final String` | `name` |  |
| `final boolean` | `showLabel` |  |
| `final String` | `staticData` |  |
| `final ModelElementType` | `type` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ModelElementDescriptor(ModelElementType type, String name, boolean showLabel, String staticData, boolean isPublic, int index)` |  |

## Method Summary
