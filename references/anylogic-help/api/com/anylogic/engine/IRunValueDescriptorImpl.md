*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IRunValueDescriptorImpl.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class IRunValueDescriptorImpl<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.IRunValueDescriptorImpl<T>

All Implemented Interfaces:
:   `IRunValueDescriptor<T>`

---

```
@AnyLogicInternalCodegenAPI
public class IRunValueDescriptorImpl<T>
extends Object
implements IRunValueDescriptor<T>
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `IRunValueDescriptorImpl(String name, Class<T> type, IUnits<?> units)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getName()` |  |
| `Class<T>` | `getType()` |  |
| `IUnits<?>` | `getUnits()` |  |
