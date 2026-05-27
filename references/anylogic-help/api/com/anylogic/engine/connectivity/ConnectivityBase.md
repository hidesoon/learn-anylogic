*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/ConnectivityBase.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class ConnectivityBase

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.connectivity.ConnectivityBase

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `Database`, `DatabaseAccessor`

---

```
@Deprecated
public abstract class ConnectivityBase
extends Object
implements Serializable
```

Deprecated.

This class is deprecated and will be removed in future releases. Consider using [`Database`](Database.md "class in com.anylogic.engine.connectivity") API instead.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.ConnectivityBase)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final void` | `destroy()` | Deprecated.  Releases resources acquired by this object  Also destroys all not destroyed contributors associated with this object    Doest nothing if object is already destroyed |
| `final String` | `getName()` | Deprecated.  Returns the name of this object |
| `String` | `toString()` | Deprecated. |
