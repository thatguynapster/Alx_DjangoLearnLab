# ALX Django Projects

## Permissions and Groups:

Custom permissions:

-   can_view: Allows viewing book list
-   can_create: Allows creating new books
-   can_edit: Allows editing books
-   can_delete: Allows deleting books

Groups:

-   Viewers: can_view
-   Editors: can_view, can_create, can_edit
-   Admins: Full access

Permissions are enforced using @permission_required decorator in views.
