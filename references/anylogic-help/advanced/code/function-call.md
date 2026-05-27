*来源 (Source): <https://anylogic.help/advanced/code/function-call.html>*

---

# Function call

Function calls are described in the [Functions](functions.md) section. It is worth adding that even if a function returns a value, it still can be called as a statement if the returned value is not needed. For example, the following statement removes a person from the list of friends:

> friends.remove( victor );

The function remove() returns true if the object to be removed was in the list. If we are sure it was there (or if we do not care if it was there), we can discard the returned value.

кот
