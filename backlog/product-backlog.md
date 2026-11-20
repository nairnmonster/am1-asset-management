Product Backlog

US01 - Create Asset
Priority: High

As an IT Administrator I want to create a new asset So that organisational equipment can be tracked and managed.

Acceptance Criteria:

Asset Name can be entered
Asset Type can be entered
Serial Number can be entered
Asset Owner can be entered
Status can be selected
Asset is saved to the database

--------------------------------------------------

US02 - View Assets
Priority: High

As an IT Administrator I want to view all recorded assets So that I can see all managed devices.

Acceptance Criteria:

Asset list displayed
Database records retrieved successfully
Asset details displayed correctly

--------------------------------------------------

US03 - Search Assets
Priority: High

As an IT Administrator I want to search for assets So that I can quickly locate device records.

Acceptance Criteria:

Search by Asset Name
Matching assets returned
No match message displayed if nothing found

--------------------------------------------------

US04 - Update Asset
Priority: High

As an IT Administrator I want to update asset records So that information remains accurate.

Acceptance Criteria:

Existing asset identified
Fields can be updated
Changes saved to database

--------------------------------------------------

US05 - Delete Asset
Priority: High

As an IT Administrator I want to remove decommissioned assets So that records remain accurate.

Acceptance Criteria:

Asset selected
Asset deleted
Asset removed from database

--------------------------------------------------

US06 - PostgreSQL Database Integration
Priority: High

As a DevOps Engineer I want asset data stored in PostgreSQL So that information persists reliably.

Acceptance Criteria:

PostgreSQL database deployed successfully
Application connects to PostgreSQL
Asset records persist after application restart
Database queries return expected results

--------------------------------------------------

US07 - Docker Containerisation
Priority: High

As a DevOps Engineer I want the application containerised So that deployment is consistent.

Acceptance Criteria:

Dockerfile created
Docker image builds successfully
Container starts successfully
Application accessible through container
Container can connect to PostgreSQL

--------------------------------------------------

US08 - Jenkins CI/CD Pipeline
Priority: High

As a DevOps Engineer I want code changes automatically built and deployed So that releases are consistent.

Acceptance Criteria:

Jenkins pipeline created
Pipeline retrieves code from GitHub
Automated testing executes successfully
Docker image built automatically
Deployment stage executes successfully

--------------------------------------------------

US09 - Automated Testing
Priority: High

As a DevOps Engineer I want automated tests executed So that defects are identified before deployment.

Acceptance Criteria:

Pytest implemented
Tests execute successfully
Tests integrated into Jenkins pipeline
Test results visible in build output

--------------------------------------------------

US10 - Security Scanning
Priority: Medium

As a DevOps Engineer I want security scanning included in the pipeline So that vulnerabilities can be identified.

Acceptance Criteria:

Bandit integrated into pipeline
pip-audit integrated into pipeline
Trivy container image scanning implemented
Security findings reviewed before deployment

--------------------------------------------------

US11 - AWS Deployment
Priority: High

As a DevOps Engineer I want the application deployed to AWS So that users can access it remotely.

Acceptance Criteria:

EC2 instance deployed
Application deployed to EC2
Docker container running on EC2
Application accessible through public IP address
