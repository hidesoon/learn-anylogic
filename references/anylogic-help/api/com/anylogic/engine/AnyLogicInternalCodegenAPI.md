*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AnyLogicInternalCodegenAPI.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Annotation Interface AnyLogicInternalCodegenAPI

---

```
@Target({TYPE,METHOD,FIELD,CONSTRUCTOR,LOCAL_VARIABLE})
@Retention(CLASS)
@AnyLogicInternalAPI
@Documented
public @interface AnyLogicInternalCodegenAPI
```

Classes, methods and fields marked with this annotation should not be called by user
These members are usually invoked by automatically generated code
This annotation is used only inside the Engine for development purposes

Methods and fiend annotated using this annotation may have names ending
with `"_xjal"` suffix as well

Author:
:   AnyLogic North America, LLC <https://anylogic.com>
