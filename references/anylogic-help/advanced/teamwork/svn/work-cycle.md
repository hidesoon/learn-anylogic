*来源 (Source): <https://anylogic.help/advanced/teamwork/svn/work-cycle.html>*

---

# Typical SVN work cycle: edit, update, commit

Often with SVN (and most other SCM systems), once you have checked out your project, or shared it, you work in a simple cycle:

1. [**Update**](update.md). First of all we recommend you to update your working copy of the project with the last version from the repository.
2. **Edit**. Then you can edit your working copy.
3. [**Update**](update.md) your working copy with other people’s committed changes. While your are working, editing, debugging, etc., others (if you are working in a team) may commit changes to the project. To keep up, you have to update whenever you are ready to do so, e.g. when your changes are stable. You should also always update immediately before your commit your work.
   Should an update concern one of the resources that you had modified, SVN will try to merge those changes. This will work if your changes do not overlap the changes made in the repository, but in case of a conflicting change (e.g. in case the same line of model code was edited locally and by some other’s people), the affected resources in your working copy are marked as being conflicted. In this case you can use whether you want to use your local copy or the incoming copy from the SVN repository.
4. [**Commit**](commit.md) your changes to the repository. Once you are pleased with all your changes, it is time to commit them to the repository. SVN will never let you commit changes that are out-of-sync, and will force you to update in the event of a collision, but this only covers the cases when the affected resources require updating. This is why you need to update first and review your change.
