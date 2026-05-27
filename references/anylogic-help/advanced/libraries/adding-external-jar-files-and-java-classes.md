*来源 (Source): <https://anylogic.help/advanced/libraries/adding-external-jar-files-and-java-classes.html>*

---

# External Java classes

* [Referring the external Java classes within AnyLogic model](#refer-external-java-class)
* [Removing the Java classes from the model dependencies](#removing-the-java-classes-from-the-model-dependencies)

AnyLogic provides you with the unique ability to use any external Java classes in your model.

To do this, you should:

1. Import archive files (\*.jar, \*.zip) with Java classes, or external class folder to your AnyLogic model.
2. Add import statements in the model, or [refer](#refer-external-java-class) instances of external Java classes by full classpath

Users typically refer to external class folders when the model development is in progress and Java classes are frequently modified. After you finish the development, we recommend you to archive your Java classes in a JAR file and link it to the model instead of external class folder.

Java archive files and class folders needed by a model should be added to the model dependencies list. You can manage it in the **Dependencies** section of the model's properties view. When [exporting](https://anylogic.help/anylogic/running/export-java-application.html) your model, all resources defined in this list will be copied in the destination folder of the exported model.

To add external Java classes (as Java archive file, or external class folder) to a model dependencies list

1. Select the model in the **Projects** view (the top-level item in the project tree).

   ![](https://anylogic.help/advanced/libraries/images/Model_projects.png)
2. Go to the **Dependencies** section of the **Properties** view. You manage the list of external JAR files and Java classes used by the model in the **Jar files and class folders required to build the model** table (the second one in the **Dependencies** section).

   ![](https://anylogic.help/advanced/libraries/images/properties.png)
3. In the model dependencies section, click **Add** ![](https://anylogic.help/anylogic/ui/images/add_palette.png) button to the right of the **Jar files and class folders required to build the model** table. This opens the **Add Classpath Entry** dialog box.

   ![](https://anylogic.help/advanced/libraries/images/jar_dialog.png)
4. Choose the **Type** of the added resource: **Java Archive File(\*.jar, \*.zip)**, or **External Class Folder**.
5. If you are plugging in the Java archive file, you can import Java file(s) to the model folder by selecting the **Import to model folder** option. Importing Java archive file to the model folder, you make this model easily portable (when delivering the model to some customer, you have just to copy the whole model folder). Alternatively, you can choose the option **Access file(s) from original location**. In this case the JAR file will not be copied to the model folder, and the model will access the file from its current location. It can be helpful when you have several models accessing the same JAR file. If for example, you will need to update the JAR file, you will be able to update it just in one place (in its current location), and all the models will automatically refer to the updated version without any changes.
6. Specify the path to the file/folder in the **File** / **Folder** field. You can refer to the files using either absolute, or relative path. Select the corresponding option below (**Use absolute path**, or **Use relative path**), and then specify the path in the **File** / **Folder** field, or browse to it using the standard file chooser window that opens on clicking the **Browse** button.
7. Click **Finish**. Upon completions of this operation, the source file will automatically appear in the model's [Resource](https://anylogic.help/anylogic/connectivity/resources.html) folder in the **Projects** view. This way you will be able to track the current state of the source file, switch between the [absolute and relative file paths](https://anylogic.help/anylogic/ui/relative-filepaths.html), etc

### Referring the external Java classes within AnyLogic model

After setting the dependencies, you can use external Java classes in your model.

The following demo model demonstrates how you can refer the external Java classes within the model. In this model we use external Java library, JAMA. JAMA is a basic linear algebra package for Java. In our model we have three variables (A, B, C) — instances of external Jama.Matrix class, designed as the standard matrix class for Java.

[**Demo model:** External JAR files

Open the model page in AnyLogic Cloud. There you can run the model or download it (by clicking Model source files).](https://cloud.anylogic.com/model/ec631da6-f048-4e94-b804-33d65002a796?mode=SETTINGS)
[**Demo model:** External JAR filesOpen the model in your AnyLogic desktop installation.](alp:External JAR files)

There are two alternative ways to refer to external Java classes from your AnyLogic model.

* Declare and refer to the instances of external Java classes using full class names (prefixed with the package name), as we do with A
  variable in the demo model. You can see that we use the full class name as the **Type** of the variable (Jama.Matrix), and we also use the full class name when we initialize this variable with the Java constructor, see the variable's **Initial value** property:
  > new Jama.Matrix( 2, 5 )

  We recommend to follow this way only when you have the limited number of references to external Java classes in your model.
* Import the classes in the model by adding the import statement(s) in the model’s agent properties. Having done this, you can refer the classes using the short class names, without package name prefixes. To add import statement, open the properties of the agent type that references to the external Java classes (in this model it is Main).
  Open the **Advanced Java** section of its properties, and type
  > import package\_name.class\_name;

  to import some specific class of the plugged-in Java library. Example:
  > import Jama.Matrix;

  Even easier is to import the whole package once by typing there
  > import package\_name.\*;

  Example:
  > import Jama.\*;

  ![](https://anylogic.help/advanced/libraries/images/jama.png)

  Having imported the Java package, you can refer to its classes easier (as we do with the variable B in the demo model), it is just of **Type** Matrix.

  We recommend to follow this particular way: import the whole package and simplify access to the external Java classes within your model.

### Removing the Java classes from the model dependencies

If some resource is not used by a model anymore, it can be removed from the dependencies of this model.

To remove an external JAR file or a class folder from a model dependencies list

1. Select the model in the **Projects** view (the top-level item in the project tree).
2. Go to the **Dependencies** section of the **Properties** view.
3. In the **Jar files and class folders required to build the model** table (the second one in the **Dependencies** section), select the resource you do not need anymore, and want to remove from the dependencies list.
4. Click **Remove** ![](https://anylogic.help/anylogic/ui/images/ge_close.png) button to the right of the **Jar files and class folders required to build the model** table.

   ![](https://anylogic.help/advanced/libraries/images/remove.png)
