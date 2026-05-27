*来源 (Source): <https://anylogic.help/advanced/teamwork/svn/commit.html>*

---

# Committing to SVN

The commit process is initiated via the **SVN > Commit** menu option. This command commits the changes in your local working copy to the repository.

To commit a resource to SVN repository

1. Right-click (macOS: Ctrl + click) the model item (the item of the uppermost level) in the **Projects** tree and choose **SVN > ![](https://anylogic.help/advanced/teamwork/svn/images/Commit_edit.gif) Commit...** from the popup menu.
2. Alternatively, you can select any element of the model and choose **File > SVN > ![](https://anylogic.help/advanced/teamwork/svn/images/Commit_edit.gif) Commit...** from the main menu.
3. If there were no changes made since the last commit operation, you will see the dialog with the corresponding message shown:

   ![](https://anylogic.help/advanced/teamwork/svn/images/nothing_to_commit.png)
4. Otherwise, you will see the **Commit** dialog.

   ![](https://anylogic.help/advanced/teamwork/svn/images/commit_svn.png)
5. Enter a comment to associate with the commit or choose a previously entered comment from the list.
6. In the **Changes** field you should specify which particular changes you want to commit to SVN repository. The scope of the commit operation is relative to the resource(s) you have selected, and will list modified, added, deleted, and unknown resources. All modified, added and deleted resources will be selected by default. You select/deselect a resource by ticking on/off checkboxes to the left of its tree item. To select all resources, right-click (macOS: Ctrl click) in the empty area of the
   **Changes** field and choose **Select All** from the popup menu. Conversely, to deselect all resources, click **Deselect All**.
   In the **Changes** tree, resources may have specific icon modifiers that may help you:

   | Icon modifier | Description |
   | --- | --- |
   |  | The resource was added locally. |
   |  | The resource was modified locally. |
   |  | Conflicting resources. The local and incoming versions of the resource are conflicting. |
   |  | The resource was deleted locally. |
7. When finished, click **OK** to commit the selected changes to the SVN repository.

If the commit was successful, you should see that the information in the model tag (the revision number and the timestamp) was updated:

![](https://anylogic.help/advanced/teamwork/svn/images/tag_2.png)

Your working copy must be up-to-date with respect to the resources you are committing. This is ensured by using **SVN > Update**, just prior to committing, resolving conflicts and retesting as needed, as described in the [typical work cycle](work-cycle.md).
