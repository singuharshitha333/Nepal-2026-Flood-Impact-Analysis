import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\singu\OneDrive\Documents\Nepal-Flood-Impact-Analysis\data\nepal_flood_cleaned.xlsx.xlsx"

print("Python EDA started")

# --------------------------------------------------
# 1. Load cleaned analytical tables
# --------------------------------------------------

building_damage = pd.read_excel(
    file_path,
    sheet_name="building_damage",
    usecols="A:D"
)

building_aoi = pd.read_excel(
    file_path,
    sheet_name="building_aoi",
    usecols="A:D"
)

transportation = pd.read_excel(
    file_path,
    sheet_name="transportation_impact",
    usecols="A:F"
)

landuse = pd.read_excel(
    file_path,
    sheet_name="landuse_impact",
    usecols="A:C"
)

facilities = pd.read_excel(
    file_path,
    sheet_name="facilities_impact",
    usecols="A:C",
    header=None
)

facilities.columns = [
    "facility_type",
    "unit",
    "affected_area_ha"
]

facilities = facilities.iloc[2:].reset_index(drop=True)
# --------------------------------------------------
# 2. Clean missing rows
# --------------------------------------------------

building_damage = building_damage.dropna(
    subset=["asset_type", "damage_status", "count"]
)

building_aoi = building_aoi.dropna(
    subset=["asset_type", "damage_status", "count"]
)

transportation = transportation.dropna(
    subset=["transportation_type"]
)

landuse = landuse.dropna(
    subset=["land_use"]
)

facilities = facilities.dropna(
    subset=["facility_type"]
)

# --------------------------------------------------
# 3. Display dataset information
# --------------------------------------------------

print("\n--- BUILDING DAMAGE ---")
print(building_damage)
print("\nShape:", building_damage.shape)

print("\n--- BUILDING AOI ---")
print(building_aoi)
print("\nShape:", building_aoi.shape)

print("\n--- TRANSPORTATION ---")
print(transportation)
print("\nShape:", transportation.shape)

print("\n--- LAND USE ---")
print(landuse)
print("\nShape:", landuse.shape)

print("\n--- FACILITIES ---")
print(facilities)
print("\nShape:", facilities.shape)

print("\nPython EDA data loading and cleaning completed successfully.")










# --------------------------------------------------
# 4. Building damage analysis
# --------------------------------------------------

print("\n================ BUILDING DAMAGE ANALYSIS ================")

damage_summary = (
    building_damage
    .groupby(["asset_type", "damage_status"])["count"]
    .sum()
    .reset_index()
)

print("\nDamage by asset type:")
print(damage_summary)

overall_damage = (
    building_aoi
    .groupby("damage_status")["count"]
    .sum()
    .sort_values(ascending=False)
)

print("\nOverall building status:")
print(overall_damage)

# Total buildings
total_buildings = building_aoi["count"].sum()

# Affected buildings
affected_statuses = [
    "Destroyed",
    "Damaged",
    "Possibly damaged"
]

affected_buildings = building_aoi[
    building_aoi["damage_status"].isin(affected_statuses)
]["count"].sum()

affected_percentage = (
    affected_buildings / total_buildings
) * 100

print("\nTotal buildings in AOI:", total_buildings)
print("Total affected buildings:", affected_buildings)
print("Overall affected percentage:", round(affected_percentage, 2), "%")


# --------------------------------------------------
# 5. Residential vs non-residential
# --------------------------------------------------

print("\n================ ASSET TYPE ANALYSIS ================")

asset_summary = (
    building_aoi
    .groupby("asset_type")["count"]
    .sum()
    .reset_index()
)

print("\nTotal buildings by asset type:")
print(asset_summary)

for asset in building_aoi["asset_type"].unique():

    asset_data = building_aoi[
        building_aoi["asset_type"] == asset
    ]

    total = asset_data["count"].sum()

    affected = asset_data[
        asset_data["damage_status"].isin(affected_statuses)
    ]["count"].sum()

    percentage = (affected / total) * 100

    print(
        f"{asset}: {affected} affected out of "
        f"{total} ({percentage:.2f}%)"
    )


# --------------------------------------------------
# 6. Transportation analysis
# --------------------------------------------------

print("\n================ TRANSPORTATION ANALYSIS ================")

transportation["affected_percentage"] = (
    transportation["total_affected"]
    / transportation["total_in_aoi"]
) * 100

print(
    transportation[
        [
            "transportation_type",
            "unit",
            "total_affected",
            "total_in_aoi",
            "affected_percentage"
        ]
    ]
)


# --------------------------------------------------
# 7. Land-use analysis
# --------------------------------------------------

print("\n================ LAND USE ANALYSIS ================")

landuse["affected_percentage"] = (
    landuse["affected_area_ha"]
    / landuse["total_area_ha"]
) * 100

print(
    landuse[
        [
            "land_use",
            "affected_area_ha",
            "total_area_ha",
            "affected_percentage"
        ]
    ]
)

total_affected_land = landuse["affected_area_ha"].sum()
total_land = landuse["total_area_ha"].sum()

overall_land_percentage = (
    total_affected_land / total_land
) * 100

print("\nTotal affected land:", total_affected_land, "ha")
print("Total represented land:", total_land, "ha")
print(
    "Overall affected land percentage:",
    round(overall_land_percentage, 2),
    "%"
)


# --------------------------------------------------
# 8. Facilities analysis
# --------------------------------------------------

print("\n================ FACILITIES ANALYSIS ================")

print(facilities)

print("\nPython EDA calculations completed successfully.")






# --------------------------------------------------
# 9. Visualization - Building Damage Status
# --------------------------------------------------

damage_chart = (
    building_aoi
    .groupby("damage_status")["count"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

damage_chart.plot(kind="bar")

plt.title("Building Status in Nepal Flood AOI")
plt.xlabel("Damage Status")
plt.ylabel("Number of Buildings")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    r"C:\Users\singu\OneDrive\Documents\Nepal-Flood-Impact-Analysis\visualizations\building_damage_status.png",
    dpi=300
)

plt.show()

print("\nBuilding damage chart saved successfully.")





# --------------------------------------------------
# 10. Visualization - Affected Buildings by Asset Type
# --------------------------------------------------

asset_impact = []

for asset in building_aoi["asset_type"].unique():

    asset_data = building_aoi[
        building_aoi["asset_type"] == asset
    ]

    total = asset_data["count"].sum()

    affected = asset_data[
        asset_data["damage_status"].isin(affected_statuses)
    ]["count"].sum()

    percentage = (affected / total) * 100

    asset_impact.append({
        "asset_type": asset,
        "affected_percentage": percentage
    })

asset_impact = pd.DataFrame(asset_impact)

plt.figure(figsize=(8, 5))

plt.bar(
    asset_impact["asset_type"],
    asset_impact["affected_percentage"]
)

plt.title("Affected Buildings by Asset Type")
plt.xlabel("Asset Type")
plt.ylabel("Affected Buildings (%)")

plt.ylim(0, 100)
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    r"C:\Users\singu\OneDrive\Documents\Nepal-Flood-Impact-Analysis\visualizations\affected_buildings_by_asset_type.png",
    dpi=300
)

plt.show()

print("\nAsset-type impact chart saved successfully.")





# --------------------------------------------------
# 11. Visualization - Transportation Impact
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    transportation["transportation_type"],
    transportation["total_affected"]
)

plt.title("Transportation Impact in Nepal Flood AOI")
plt.xlabel("Transportation Type")
plt.ylabel("Total Affected")

plt.xticks(rotation=30, ha="right")

plt.tight_layout()

plt.savefig(
    r"C:\Users\singu\OneDrive\Documents\Nepal-Flood-Impact-Analysis\visualizations\transportation_impact.png",
    dpi=300
)

plt.show()

print("\nTransportation impact chart saved successfully.")






# --------------------------------------------------
# 12. Visualization - Land Use Impact
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    landuse["land_use"],
    landuse["affected_percentage"],
    color=["forestgreen", "goldenrod", "steelblue", "darkorange", "mediumpurple"]
)

plt.title("Land Use Affected by Flood")
plt.xlabel("Land Use")
plt.ylabel("Affected Area (%)")

plt.ylim(0, 100)
plt.xticks(rotation=25, ha="right")

plt.tight_layout()

plt.savefig(
    r"C:\Users\singu\OneDrive\Documents\Nepal-Flood-Impact-Analysis\visualizations\landuse_impact.png",
    dpi=300
)

plt.show()

print("\nLand-use impact chart saved successfully.")




# --------------------------------------------------
# 13. Visualization - Transportation Impact Percentage
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    transportation["transportation_type"],
    transportation["affected_percentage"],
    color=["crimson", "royalblue", "darkorange", "seagreen", "mediumpurple"]
)

plt.title("Transportation Affected by Flood")
plt.xlabel("Transportation Type")
plt.ylabel("Affected (%)")

plt.ylim(0, 110)
plt.xticks(rotation=25, ha="right")

plt.tight_layout()

plt.savefig(
    r"C:\Users\singu\OneDrive\Documents\Nepal-Flood-Impact-Analysis\visualizations\transportation_affected_percentage.png",
    dpi=300
)

plt.show()

print("\nTransportation percentage chart saved successfully.")





# --------------------------------------------------
# 14. Visualization - Land Use Affected Area
# --------------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    landuse["land_use"],
    landuse["affected_area_ha"],
    color=["forestgreen", "darkorange", "steelblue", "goldenrod", "mediumpurple"]
)

plt.title("Affected Land Use Area")
plt.xlabel("Land Use")
plt.ylabel("Affected Area (ha)")

plt.xticks(rotation=25, ha="right")

plt.tight_layout()

plt.savefig(
    r"C:\Users\singu\OneDrive\Documents\Nepal-Flood-Impact-Analysis\visualizations\landuse_affected_area.png",
    dpi=300
)

plt.show()

print("\nLand-use affected area chart saved successfully.")