# %%
import leafmap
import geopandas as gpd
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="FloodDEM",
    user="postgres",
    password="12345"
)

# Read the shapefiles from the PostgreSQL database
shapefiles = [
    {"table_name": "township_dd", "style": {"fillColor": "blue", "color": "black", "weight": 1, "fillOpacity": 0.6}},
    {"table_name": "whk_psu_region", "style": {"fillColor": "green", "color": "black", "weight": 1, "fillOpacity": 0.6}},
    {"table_name": "Windhoek", "style": {"fillColor": "yellow", "color": "black", "weight": 1, "fillOpacity": 0.6}}
]

# Create a Leafmap Map instance with Namibia as the center and appropriate zoom level
m = leafmap.Map(center=(-22, 17), zoom=6)

# Loop through the shapefiles
for shapefile in shapefiles:
    # Read the shapefile from the PostgreSQL database
    sql = f"SELECT *, geom FROM {shapefile['table_name']}"
    gdf = gpd.read_postgis(sql, conn)

    # Set the CRS of the GeoDataFrame
    gdf.crs = "EPSG:4326"

    # Add the GeoDataFrame to the map with custom style
    m.add_gdf(gdf, layer_name=shapefile['table_name'], style=shapefile['style'])

# Display the map
m


