*来源 (Source): <https://anylogic.help/advanced/libraries/managing-model-dependencies.html>*

---

# Adding libraries to model dependencies

If you are using blocks of some AnyLogic library in your model, this library must be listed in the model dependencies list. Model dependencies list defines libraries needed by this model to compile successfully. You can manage it in the **Dependencies** section of the model’s properties view. When [exporting](https://anylogic.help/anylogic/running/export-java-application.html) your model, all libraries defined in this list will be copied in the destination folder of the exported model.

Please note that if you have already created instances of any classes defined in a library, this library should be already present in the model dependencies list.

To add a library to model dependencies list

1. Select the model in the **Projects** view (the top-level item in the project tree).
2. Go to the **Dependencies** section of the **Properties** view.
3. Click **Add** button to the right of the **AnyLogic libraries/models required to build the model** table. This opens the **Libraries** dialog box, that lists all libraries currently loaded into AnyLogic workspace.
4. Select the library you want to add to the model dependencies and click **OK**.

If some library is not used by a model anymore, it can be removed from the dependencies of this model.

To remove a library from model dependencies list

1. Select the model in the **Projects** view.
2. Go to the **Dependencies** section of the **Properties** view.
3. Select the library you want to remove from the model dependencies list in the **AnyLogic libraries/models required to build the model** table and click the **Remove** button to the right of the table.
