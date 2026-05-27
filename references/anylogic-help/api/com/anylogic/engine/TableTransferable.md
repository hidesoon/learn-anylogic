*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/TableTransferable.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class TableTransferable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.TableTransferable

All Implemented Interfaces:
:   `Transferable`

---

```
@AnyLogicInternalAPI
public class TableTransferable
extends Object
implements Transferable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final DataFlavor` | `textDataFlavor` |  |
| `static final DataFlavor` | `xmlDataFlavor` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TableTransferable(List<List<Object>> table)` |  |
| `TableTransferable(List<List<Object>> table, List<Integer> sqlTypes)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static byte[]` | `getExcelClipboardData()` |  |
| `static List<List<Pair<Integer,Object>>>` | `getExcelData(byte[] bytes)` |  |
| `Object` | `getTransferData(DataFlavor flavor)` |  |
| `DataFlavor[]` | `getTransferDataFlavors()` |  |
| `boolean` | `isDataFlavorSupported(DataFlavor flavor)` |  |
| `static String` | `toString(List<List<Object>> lists)` |  |
| `static String` | `toXmlString(List<List<Object>> table, List<Integer> sqlTypes)` |  |
