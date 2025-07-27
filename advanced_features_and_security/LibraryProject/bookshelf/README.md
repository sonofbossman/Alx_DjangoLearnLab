## Permissions Setup Guide

**Model Permissions**:

- `can_view`: View books
- `can_create`: Add new books
- `can_edit`: Edit existing books
- `can_delete`: Delete books

**Groups**:

- `Viewers`: can_view
- `Editors`: can_view, can_create, can_edit
- `Admins`: all permissions

**Test Users**:

1. Assign user to a group via Django Admin
2. Log in and access protected views
3. Unauthorized users will see 403 Forbidden

**Decorators Used**:

- `@permission_required('relationship_app.can_edit')`
