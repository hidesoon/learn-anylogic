*来源 (Source): <https://anylogic.help/advanced/teamwork/svn/update.html>*

---

# Updating from SVN

While you are working on a project, other members of your team may be committing changes to the project repository. To get these changes, you have to update your working copy.

To update your working copy from SVN repository

1. Right-click (macOS: Ctrl + click) the model item (the item of the uppermost level) in the **Projects** tree and choose **SVN > ![](https://anylogic.help/advanced/teamwork/svn/images/Update_edit.gif) Update** from the popup menu, or
   Select any element of the model and choose **File > SVN > ![](https://anylogic.help/advanced/teamwork/svn/images/Update_edit.gif) Update** from the main menu.
2. If everything is OK, you will just see a progress dialog shown shortly. This means that the operation was successful.
3. Otherwise, if there are some conflicts (see the detailed information below), you will see the dialog that prompts you to resolve the conflict either by using the incoming or local copy of the resource:

   ![](https://anylogic.help/advanced/teamwork/svn/images/update_conflict.png)

There are three different kinds of incoming changes:

#### Non-conflicting

A non-conflicting change occurs when a file has been changed remotely but has not been modified locally.

#### Conflicting, but auto-mergeable

An auto-mergeable conflicting change occurs when an ASCII file has been changed both remotely and locally (i.e. has non-committed local changes) but the changes are on different lines.

#### Conflicting

A conflicting change occurs when one or more of the same lines of an ASCII file have been changed both remotely and locally. Binary files are never auto-mergeable and are conflicting by default.

When you perform an update, the contents of your working copy will be updated with the latest version of the resource available in the repository. For non-conflicting and auto-mergeable conflicts, there is no additional action required. The repository contents are not changed when you update When you accept incoming changes, these changes are applied to your working copy only. The repository is only changed when you commit your outgoing changes.
