*来源 (Source): <https://anylogic.help/advanced/libraries/adding-library-objects-to-active-object-classes.html>*

---

# Adding library blocks into a model

All libraries loaded into the AnyLogic workspace are displayed as stencils of the **Palette** view. Each library block is represented with the icon designed for it. You add library blocks into agent types of your model in the same way as any other palette elements.

To add a library block to a model

1. Open the diagram of the agent type (for example, Main) to which you want to add the library block.
2. Open the stencil of the required library in the **Palette**.
3. Drag the required block from the palette into the graphical editor.

If for some reason you do not see the library stencil in the **Palette**, it means that this library is probably not loaded into the AnyLogic workspace or is hidden. See [Managing libraries](managing-libraries.md) to learn how to load libraries into the workspace and make them visible in the **Palette**.

Having added some library block into your model, this library is automatically added to the list of libraries required by this model for successful compilation. You can [manage model dependencies](managing-model-dependencies.md) by yourself on the **Dependencies** page of the model’s **Properties** view. In addition to libraries, you can also specify JAR files and class folders that are required by this model.
