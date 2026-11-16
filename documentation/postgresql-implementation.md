PostgreSQL Implementation Plan

Purpose

PostgreSQL will be used as the primary database platform for the Asset Management Application.

Reason for Selection

PostgreSQL was selected because it is a reliable relational database platform and was identified within the approved project proposal.

Database Usage

The database will store:

- Asset Name
- Asset Type
- Serial Number
- Assigned User
- Asset Status
- Date Added

Application Integration

The Asset Management Application will connect to PostgreSQL using Python.

Functions supported:

- Create Asset
- View Assets
- Search Assets
- Update Assets
- Delete Assets

Deployment

PostgreSQL will be deployed alongside the application environment and used as the persistent data store for all asset records.
