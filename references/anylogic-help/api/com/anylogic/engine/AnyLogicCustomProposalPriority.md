*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AnyLogicCustomProposalPriority.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Annotation Interface AnyLogicCustomProposalPriority

---

```
@Target({TYPE,METHOD,FIELD,CONSTRUCTOR,LOCAL_VARIABLE})
@Retention(CLASS)
@AnyLogicInternalAPI
public @interface AnyLogicCustomProposalPriority
```

Users should ignore this annotation.
This annotation is used only inside the AnyLogic, for code completion purposes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `AnyLogicCustomProposalPriority.Type` |  |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `FULLY_QUALIFIED_STATIC_ELEMENT` |  |
| `static final int` | `P_CODEGEN_API` | A little bit more than [`AnyLogicInternalCodegenAPI`](AnyLogicInternalCodegenAPI.md "annotation interface in com.anylogic.engine") |
| `static final int` | `P_DRAW_API` |  |
| `static final int` | `P_DRAW_CONTAINS_API` |  |
| `static final int` | `P_LIBRARY_DEVELOPER_API` | For elements which are used by libraries but may be rarely used by modelers (therefore they don't have [`AnyLogicInternalAPI`](AnyLogicInternalAPI.md "annotation interface in com.anylogic.engine") annotation) |
| `static final int` | `P_PORT_API` |  |
