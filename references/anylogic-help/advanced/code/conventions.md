*来源 (Source): <https://anylogic.help/advanced/code/conventions.html>*

---

# Naming conventions

Take a moment to familiarize yourself with the naming conventions. Names you give to the model objects are important. A good naming system simplifies development process a lot. We recommend you to keep to Java naming conventions throughout the model, not just when writing Java code.

The name of the object should indicate the intent of its use.

Ideally a casual observer should be able to understand the role of the object from its name and, on the other hand, when looking for an object serving a particular purpose, he should be able to easily guess its name.

You can compose a name of several words. Use mixed case with the first letter of each word capitalized. Do not use underscores.

You should never use meaningless names like “a”, “b”, “x23”, “state1”, “event14”. One-character variable names should only be used for temporary "throwaway" variables such as loop indices. Avoid acronyms and abbreviations unless they are more common than the long form, for example: NPV, ROI, ARPU. Remember that when using the object name in an expression or code, you will not need to type it: AnyLogic [code completion](https://anylogic.help/anylogic/ui/using-intelli-sense.html) will do the work for you, so multi-word names are perfectly fine.

Keep to one naming system. Names must be uniformly structured.

It makes sense to develop a naming system for your models and keep to it. Large organizations sometimes standardize the naming conventions across all modeling projects.

A couple of important facts: Java is a case-sensitive programming language: Anylogic and AnyLogic are different names that will never match. Spaces are not allowed in Java names.

In the Table below we summarize the naming recommendations for various types of model objects.

| Object | Naming rules | Examples |
| --- | --- | --- |
| * Java variable * Parameter of agent * Collection * Table function * Statistics | First letter can be lowercase or uppercase (here we relax Java conventions), first letter of each internal word capitalized.  Should be a noun.  Use plurals for collections.  Sometimes adding a suffix or prefix indicating the type of the object helps to understand its meaning and to avoid name conflicts. For example, AgeDistribution can be a custom distribution constructed from the table function AgeDistributionTable. | rate  Income  DevelopmentCost  inventory  AgeDistribution  AgeDistributionTable  friends |
| * Function | First letter must be lowercase, first letter of each internal word capitalized.  Should be a verb.  If the function returns a property of the object, its name should start with the word "get", or "is" for boolean return type. If the function changes a property of the object, it should start with "set".  There are some exceptions created to make the code more compact, such as AnyLogic system functions time() and date(), or functions size() of Java collection. | resetStatistics  getAnnualProfit  goHome  speedup  getEstimatedROI  setTarget  inState  isVisible  isEnabled |
| * Function argument * Local variable in the code | If possible, short, lowercase. If consists of more than one word, first letter of each internal word should be capitalized  Common names for temporary integer variables are i, j, k, m, and n. | cost  sum  total  baseValue  i  n |
| * Java constant | All uppercase with words separated with underscores “\_”. | TIME\_UNIT\_MONTH |
| Classes:   * Agent type * User's Java class * Dynamic event | First letter must be capitalized, first letter of each internal word capitalized as well.  Should be a noun except for process model components that have a meaning of action, in which case it can be a verb. | Consumer  Project  UseNurse  RegistrationProcess  HousingSector  PhoneCall  Order  Arrival |
| * Agent population, including the library objects | First letter must be lowercase, first letter of each internal word capitalized.  Use plurals for replicated objects. | project  consumers  people  doTriage  registrationProcess  stuffAndMailBill |
| Dynamic variables:   * Stock * Flow * Dynamic variable | Long multi-word variable names are very common in system dynamics models. As in Java and in AnyLogic spaces are not allowed in names, you should use other ways to separate words. We recommend to use mixed case with the first letter of each word capitalized. The use of underscore "\_" is not recommended, although it is allowed. | BirthRate  Population  DrugsUnderConsideration  TimeToImplementStrategies |
| * Events (not dynamic) * Statechart * States * Transition | First letter can be lowercase or uppercase, first letter of each internal word capitalized. | overflow  at8AMEveryDay  purchaseBehavior  InWorkForce  discard |
