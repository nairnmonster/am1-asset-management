Asset Management Application Design
Purpose
The Asset Management Application will provide a centralised platform for recording, updating, searching and managing organisational assets.

The application will be developed using Python and deployed through an automated CI/CD pipeline using Jenkins.

Asset Record Structure
Field	Description
asset_id	Unique identifier
asset_name	Name of the asset
asset_type	Type of asset
serial_number	Manufacturer serial number
assigned_user	User assigned to asset
status	Active, In Repair, Retired
date_added	Date asset was added
Application Functions
Create Asset
Create a new asset record and save to PostgreSQL.

View Assets
Display all assets stored within PostgreSQL.

Search Assets
Search assets by name.

Update Asset
Update asset information.

Delete Asset
Remove asset records.

Technology Stack
Python
PostgreSQL
GitHub
Jenkins
Docker
Terraform
AWS
CloudWatch
Grafana
Deployment Overview
Source code will be stored in GitHub.

Code changes will trigger Jenkins CI/CD processes.

Jenkins will:

Execute automated tests
Perform security checks
Build Docker images
Deploy the application
The application will be hosted within AWS infrastructure provisioned using Terraform.

Monitoring will be provided through CloudWatch and Grafana.
