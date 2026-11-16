Asset Management Database Design

Purpose

The PostgreSQL database will store all asset records used by the Asset Management Application.

Database Platform

PostgreSQL

Table Name

assets

Fields

asset_id
Data Type: SERIAL PRIMARY KEY
Description: Unique asset identifier

asset_name
Data Type: VARCHAR(100)
Description: Name of the asset

asset_type
Data Type: VARCHAR(50)
Description: Asset category

serial_number
Data Type: VARCHAR(100)
Description: Manufacturer serial number

assigned_user
Data Type: VARCHAR(100)
Description: User assigned to the asset

status
Data Type: VARCHAR(20)
Description: Active, In Repair or Retired

date_added
Data Type: TIMESTAMP
Description: Date asset was added

Purpose of Database

The database provides persistent storage for all asset management records and allows application users to create, view, search, update and delete assets.
