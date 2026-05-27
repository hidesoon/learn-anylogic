*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gui/IExperimentHost.IValue.html>*

---

Package [com.anylogic.engine.gui](package-summary.md)

# Interface IExperimentHost.IValue

Enclosing interface:
:   [IExperimentHost](IExperimentHost.md "interface in com.anylogic.engine.gui")

---

```
@AnyLogicInternalAPI
public static interface IExperimentHost.IValue
```

Used for converting String/JSON input data to arbitrary java classes
requested by Engine. This is delegated to Cloud impl, here we have interface
only.
 should be a non-primitive type.

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `<T> T` | `get(Class<T> type)` | Converts the value to the given type |
