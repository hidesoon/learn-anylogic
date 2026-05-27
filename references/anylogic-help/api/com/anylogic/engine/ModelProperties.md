*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ModelProperties.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ModelProperties

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.ModelProperties

---

```
@AnyLogicInternalAPI
public class ModelProperties
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `FILE_NAME` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ModelProperties()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `getBooleanProperty(Object propertyName)` |  |
| `EnumSet<LoggingType>` | `getLoggingTypes(Engine engine)` |  |
| `String` | `getStringProperty(ModelPropertyName propertyName)` |  |
| `String` | `getStringProperty(Object propertyName)` |  |
| `void` | `load(Class<?> c)` |  |
| `void` | `load(String packageNameOrPrefix)` |  |
| `void` | `setBooleanProperty(Object propertyName, boolean value)` |  |
| `void` | `setStringProperty(Object propertyName, String value)` |  |
| `void` | `store(OutputStream stream)` |  |
