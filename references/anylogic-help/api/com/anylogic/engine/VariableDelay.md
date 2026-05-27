*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/VariableDelay.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class VariableDelay

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.VariableDelay

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalCodegenAPI
public abstract class VariableDelay
extends Object
implements Serializable
```

*This class is designed for internal use inside AnyLogic code generation,
it shouldn't be explicitly accessed by users.*
VariableDelay object accumulates a history of an expression (of type double
or HyperArray and generates delayed values of the expression using the
accumulated information. The capacity depends on engine integration step. An
object registers itself in continuous engine upon creation and then is
updated by the engine.
Is designed for fixed step integration

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.VariableDelay)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `VariableDelay.Type` | Type of delay object, see description on items |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `VariableDelay(VariableDelay.Type type, Agent ao)` | Constructor |
| `VariableDelay(VariableDelay.Type type, Agent ao, Dimension... dimensions)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final HyperArray` | `getArray()` | Returns delayed arrayed value  **This method should be called only for arrayed delays** |
| `abstract double` | `getDelayTime()` | This method should be overridden |
| `double` | `getInitialValue()` | Returns value of the expression being delayed  This method should be overridden in scalar delays having custom (non-zero) initial value |
| `void` | `getInitialValue(HyperArray array)` | Tags default arrayed sample into `array`  This method should be overridden in arrayed delays with custom (non-zero) initial value to fill the **whole `array` data** |
| `double` | `getInput()` | Returns value of the expression being delayed  This method should be overridden in scalar delays |
| `void` | `getInput(HyperArray array)` | Tags arrayed sample into `array`  This method should be overridden in arrayed delays to fill the **whole `array` data** |
| `double` | `getMissingValue()` | Returns value to be returned by this object when delay time increases and when no output is available at the time  This method should be overridden in scalar delays with variable delay time which have custom 'missing value' |
| `void` | `getMissingValue(HyperArray array)` | Tags arrayed value to be returned by this object when delay time increases and when no output is available at the time  This method should be overridden in arrayed delays with variable delay time which have custom 'missing value' to fill the **whole `array` data** |
| `final double` | `getScalar()` | Returns scalar delayed value  **This method should be called only for scalar delays** |
| `final void` | `storeSample()` | Stores sample if needed |
