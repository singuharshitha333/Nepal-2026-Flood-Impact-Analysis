USE NepalFloodAnalysis;
SELECT DB_NAME() AS CurrentDatabase;

USE NepalFloodAnalysis;
GO

CREATE TABLE building_damage (
    asset_type VARCHAR(100),
    asset_description VARCHAR(200),
    damage_status VARCHAR(50),
    count INT
);
GO

CREATE TABLE building_aoi (
    asset_type VARCHAR(100),
    asset_description VARCHAR(200),
    damage_status VARCHAR(50),
    count INT
);
GO

CREATE TABLE transportation_impact (
    transportation_type VARCHAR(100),
    unit VARCHAR(20),
    destroyed_affected DECIMAL(10,2),
    possibly_damaged DECIMAL(10,2),
    total_affected DECIMAL(10,2),
    total_in_aoi DECIMAL(10,2)
);
GO

CREATE TABLE landuse_impact (
    land_use VARCHAR(100),
    affected_area_ha DECIMAL(10,2),
    total_area_ha DECIMAL(10,2)
);
GO

CREATE TABLE facilities_impact (
    facility_type VARCHAR(100),
    unit VARCHAR(20),
    affected_area_ha DECIMAL(10,2)
);
GO

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';

INSERT INTO building_damage
(asset_type, asset_description, damage_status, count)
VALUES
('Residential Buildings', 'Not Applicable', 'Destroyed', 159),
('Residential Buildings', 'Not Applicable', 'Damaged', 2),
('Residential Buildings', 'Not Applicable', 'Damaged', 10),
('Residential Buildings', 'Not Applicable', 'Destroyed', 123),
('Non-residential Buildings', 'Institutional', 'Destroyed', 1),
('Non-residential Buildings', 'Other non-residential buildings', 'Destroyed', 35),
('Non-residential Buildings', 'Buildings used as places of worship and for religious activities', 'Destroyed', 2),
('Non-residential Buildings', 'School, university and research buildings', 'Damaged', 1),
('Non-residential Buildings', 'Other non-residential buildings', 'Destroyed', 2);
GO

SELECT *
FROM building_damage;

INSERT INTO building_aoi
(asset_type, asset_description, damage_status, count)
VALUES
('Residential Buildings', 'Not Applicable', 'Destroyed', 160),
('Residential Buildings', 'Not Applicable', 'Damaged', 5),
('Residential Buildings', 'Not Applicable', 'No visible damage', 39),
('Residential Buildings', 'Not Applicable', 'Possibly damaged', 26),
('Residential Buildings', 'Not Applicable', 'Damaged', 26),
('Residential Buildings', 'Not Applicable', 'Destroyed', 123),
('Residential Buildings', 'Not Applicable', 'No visible damage', 86),
('Residential Buildings', 'Not Applicable', 'Possibly damaged', 52),
('Non-residential Buildings', 'Institutional', 'Destroyed', 1),
('Non-residential Buildings', 'Other non-residential buildings', 'Destroyed', 35),
('Non-residential Buildings', 'Worship/religious', 'Destroyed', 2),
('Non-residential Buildings', 'Other non-residential buildings', 'No visible damage', 1),
('Non-residential Buildings', 'School/university/research', 'Damaged', 1),
('Non-residential Buildings', 'Other non-residential buildings', 'Destroyed', 2);
GO

SELECT *
FROM building_aoi;

INSERT INTO transportation_impact
(transportation_type, unit, destroyed_affected, possibly_damaged, total_affected, total_in_aoi)
VALUES
('Helipad', 'ha', 0.01, 0, 0.01, 0.01),
('Primary Road', 'km', 4.70, 0.70, 5.40, 5.40),
('Local Road', 'km', 0.40, 0.60, 1.10, 3.30),
('Cart Track', 'km', 1.00, 0.10, 1.10, 2.80),
('Bridges/elevated highways', 'count', 5.00, 0.00, 5.00, 5.00);
GO

SELECT *
FROM transportation_impact;

INSERT INTO landuse_impact
(land_use, affected_area_ha, total_area_ha)
VALUES
('Forests', 61.60, 228.80),
('Shrub/herbaceous', 31.80, 93.10),
('Inland wetlands', 12.10, 14.60),
('Other', 3.40, 4.30),
('Heterogeneous agricultural', 2.10, 5.10);
GO

SELECT *
FROM landuse_impact;

INSERT INTO facilities_impact
(facility_type, unit, affected_area_ha)
VALUES
('Power plant constructions', 'ha', 0.80);
GO

SELECT *
FROM facilities_impact;





SELECT 'building_damage' AS table_name, COUNT(*) AS row_count
FROM building_damage

UNION ALL

SELECT 'building_aoi', COUNT(*)
FROM building_aoi

UNION ALL

SELECT 'transportation_impact', COUNT(*)
FROM transportation_impact

UNION ALL

SELECT 'landuse_impact', COUNT(*)
FROM landuse_impact

UNION ALL

SELECT 'facilities_impact', COUNT(*)
FROM facilities_impact;




DELETE FROM facilities_impact;

INSERT INTO facilities_impact
(facility_type, unit, affected_area_ha)
VALUES
('Power plant constructions', 'ha', 0.80);

SELECT *
FROM facilities_impact;



SELECT
    asset_type,
    damage_status,
    SUM(count) AS total_buildings
FROM building_aoi
GROUP BY
    asset_type,
    damage_status
ORDER BY
    asset_type,
    total_buildings DESC;


SELECT
    damage_status,
    SUM(count) AS total_buildings
FROM building_aoi
GROUP BY damage_status
ORDER BY total_buildings DESC;


SELECT
    asset_type,
    SUM(count) AS total_buildings,
    SUM(CASE
        WHEN damage_status <> 'No visible damage'
        THEN count
        ELSE 0
    END) AS affected_buildings,
    ROUND(
        100.0 * SUM(CASE
            WHEN damage_status <> 'No visible damage'
            THEN count
            ELSE 0
        END) / SUM(count),
        2
    ) AS affected_percentage
FROM building_aoi
GROUP BY asset_type;


SELECT
    damage_status,
    SUM(count) AS total_buildings,
    ROUND(
        100.0 * SUM(count) /
        (SELECT SUM(count) FROM building_aoi),
        2
    ) AS percentage_of_aoi
FROM building_aoi
WHERE damage_status <> 'No visible damage'
GROUP BY damage_status
ORDER BY total_buildings DESC;


SELECT
    asset_type,
    damage_status,
    SUM(count) AS total_buildings
FROM building_aoi
WHERE damage_status IN ('Destroyed', 'Damaged', 'Possibly damaged')
GROUP BY
    asset_type,
    damage_status
ORDER BY
    asset_type,
    total_buildings DESC;

    SELECT
    transportation_type,
    unit,
    destroyed_affected,
    possibly_damaged,
    total_affected,
    total_in_aoi
FROM transportation_impact
ORDER BY total_affected DESC;


SELECT
    transportation_type,
    unit,
    total_affected,
    total_in_aoi,
    ROUND(
        100.0 * total_affected / NULLIF(total_in_aoi, 0),
        2
    ) AS affected_percentage
FROM transportation_impact
ORDER BY affected_percentage DESC;


SELECT
    land_use,
    affected_area_ha,
    total_area_ha,
    ROUND(
        100.0 * affected_area_ha / NULLIF(total_area_ha, 0),
        2
    ) AS affected_percentage
FROM landuse_impact
ORDER BY affected_percentage DESC;

SELECT
    SUM(affected_area_ha) AS total_affected_land_area_ha,
    SUM(total_area_ha) AS total_land_area_ha,
    ROUND(
        100.0 * SUM(affected_area_ha) /
        NULLIF(SUM(total_area_ha), 0),
        2
    ) AS overall_affected_percentage
FROM landuse_impact;
