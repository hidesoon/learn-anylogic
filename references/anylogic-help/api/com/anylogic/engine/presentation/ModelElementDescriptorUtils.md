*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ModelElementDescriptorUtils.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ModelElementDescriptorUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.ModelElementDescriptorUtils

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public final class ModelElementDescriptorUtils
extends Object
implements Serializable
```

As long as at runtime the information about the model elements
such as position of their icons, visibility of labels, and sometimes even type
is lost, this class should contain all info needed for displaying the
element and its info at runtime, including the reference to the element itself.

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ModelElementDescriptorUtils)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `final int` | `index` |  |
| `final boolean` | `isPublic` |  |
| `final String` | `name` |  |
| `final boolean` | `showLabel` |  |
| `final String` | `staticData` |  |
| `final ModelElementTypeUtils` | `type` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ModelElementDescriptorUtils(ModelElementDescriptor d)` |  |
| `ModelElementDescriptorUtils(ModelElementTypeUtils type, String name, boolean showLabel, String staticData, boolean isPublic, int index)` |  |

## Method Summary
