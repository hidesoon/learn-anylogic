*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AnyLogicInternalAPI.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Annotation Interface AnyLogicInternalAPI

---

```
@Target({TYPE,METHOD,FIELD,CONSTRUCTOR})
@Retention(RUNTIME)
@AnyLogicInternalAPI
@Documented
public @interface AnyLogicInternalAPI
```

Classes, methods and fields marked with this annotation should not be called by user
These members are invoked by engine internals and are public only due to restrictions
of java language (inter-package visibility, interface members etc.)
This annotation is used only inside the Engine for development purposes

Methods and fiend annotated using this annotation may have names ending
with `"_xjal"` suffix as well

Author:
:   AnyLogic North America, LLC <https://anylogic.com>
