from sqlalchemy import Enum

admin_sim_status_enum = Enum(
    "UNPROCESSED",
    "PENDING",
    "PROCESSING",
    "SUCCESS",
    "FAILURE",
    name="admin_sim_status",
)
surrounding_sources_enum = Enum("SWISSTOPO", "OSM", name="surrounding_sources")
simulation_type_enum = Enum("SUN", "VIEW", name="simulation_type")
simulation_version_enum = Enum(
    "PH_2020", "PH_01_2021", "PH_2022_H1", "EXPERIMENTAL", name="simulation_version"
)
potential_layout_enum = Enum("WITH_WINDOWS", name="potential_layout_mode")
potential_simulation_status_enum = Enum(
    "PENDING", "PROCESSING", "SUCCESS", "FAILURE", name="potential_simulation_status"
)
currency_enum = Enum("CHF", "EUR", "CZK", "USD", name="currency")
competition_features_enum = Enum(
    "RESIDENTIAL_USE",
    "RESIDENTIAL_USE_RATIO",
    "RESIDENTIAL_TOTAL_HNF_REQ",
    "BUILDING_AVG_MAX_RECT_ALL_APT_AREAS",
    "BUILDING_PCT_CIRCULATION_RESIDENTIAL",
    "BUILDING_BICYCLE_BOXES_AVAILABLE",
    "BUILDING_BICYCLE_BOXES_QUANTITY_PERFORMANCE",
    "BUILDING_MINIMUM_ELEVATOR_DIMENSIONS",
    "APT_RATIO_OUTDOOR_INDOOR",
    "APT_PCT_W_OUTDOOR",
    "APT_MAX_RECT_IN_PRIVATE_OUTDOOR",
    "APT_MIN_OUTDOOR_REQUIREMENT",
    "APT_RATIO_REDUIT_W_WATER_CONNEXION",
    "APT_HAS_WASHING_MACHINE",
    "APT_PCT_W_STORAGE",
    "APT_DISTRIBUTION_TYPES",
    "APT_DISTRIBUTION_TYPES_AREA_REQ",
    "APT_SHOWER_BATHTUB_DISTRIBUTION",
    "APT_BATHROOMS_TOILETS_DISTRIBUTION",
    "APT_RATIO_NAVIGABLE_AREAS",
    "APT_RATIO_BATHROOM_MIN_REQUIREMENT",
    "APT_RATIO_BEDROOM_MIN_REQUIREMENT",
    "APT_LIVING_DINING_MIN_REQ_PER_APT_TYPE",
    "APT_SIZE_DINING_TABLE_REQ",
    "JANITOR_HAS_WC",
    "JANITOR_HAS_STORAGE",
    "JANITOR_OFFICE_MIN_SIZE_REQUIREMENT",
    "JANITOR_STORAGE_MIN_SIZE_REQUIREMENT",
    "JANITOR_WC_CLOSENESS",
    "JANITOR_WATER_CONN_AVAILABLE",
    "ANALYSIS_GREENERY",
    "ANALYSIS_SKY",
    "ANALYSIS_BUILDINGS",
    "ANALYSIS_WATER",
    "ANALYSIS_RAILWAY_TRACKS",
    "ANALYSIS_STREETS",
    "APT_AVG_DARKEST_ROOM_SUMMER",
    "APT_AVG_BRIGHTEST_ROOM_WINTER",
    "APARTMENT_OUTDOOR_AREAS_TOTAL_HOURS_OF_SUN_SUMMER",
    "APARTMENT_OUTDOOR_AREAS_TOTAL_HOURS_OF_SUN_WINTER",
    "NOISE_STRUCTURAL",
    "NOISE_INSULATED_ROOMS",
    "DRYING_ROOM_SIZE",
    "JANITOR_OFFICE_LIGHT",
    "PRAMS_ROOM_BARRIER_FREE_ACCESS",
    "BIKE_BOXES_DIMENSIONS",
    "BIKE_BOXES_POWER_SUPPLY",
    "PRAMS_AND_BIKES_CLOSE_TO_ENTRANCE",
    "BASEMENT_COMPARTMENT_AVAILABLE",
    "BASEMENT_COMPARTMENT_SIZE_REQ",
    "GUESS_ROOM_SIZE_REQ",
    "KITCHEN_ELEMENTS_REQUIREMENT",
    "ENTRANCE_WARDROBE_ELEMENT_REQUIREMENT",
    "BEDROOM_WARDROBE_ELEMENT_REQUIREMENT",
    "SINK_SIZES_REQUIREMENT",
    "CAR_PARKING_SPACES",
    "TWO_WHEELS_PARKING_SPACES",
    "BIKE_PARKING_SPACES",
    "SECOND_BASEMENT_FLOOR_AVAILABLE",
    "AGF_W_REDUIT",
    name="competitionfeatures",
)
region_enum = Enum(
    "MC",
    "CH",
    "DK",
    "AT",
    "NO",
    "CZ",
    "ES",
    "AD",
    "DE_BADEN_WURTTEMBERG",
    "DE_BAYERN",
    "DE_BERLIN",
    "DE_BRANDENBURG",
    "DE_BREMEN",
    "DE_HAMBURG",
    "DE_HESSEN",
    "DE_MECKLENBURG_VORPOMMERN",
    "DE_NIEDERSACHSEN",
    "DE_NORDRHEIN_WESTFALEN",
    "DE_RHEINLAND_PFALZ",
    "DE_SAARLAND",
    "DE_SACHSEN",
    "DE_SACHSEN_ANHALT",
    "DE_SCHLESWIG_HOLSTEIN",
    "DE_THURINGEN",
    "US_GEORGIA",
    "US_PENNSYLVANIA",
    "SG",
    name="region",
)
classifications_enum = Enum("UNIFIED", name="classifications")
dms_permission_enum = Enum(
    "READ", "WRITE", "READ_ALL", "WRITE_ALL", name="dms_permission"
)
task_type_enum = Enum(
    "BIGGEST_RECTANGLE",
    "VIEW_SUN",
    "BASIC_FEATURES",
    "CONNECTIVITY",
    "SUN_V2",
    "NOISE",
    "NOISE_WINDOWS",
    "COMPETITION",
    name="task_type",
)
userrole_enum = Enum(
    "ADMIN",
    "POTENTIAL_API",
    "DMS_LIMITED",
    "COMPETITION_ADMIN",
    "COMPETITION_VIEWER",
    "TEAMMEMBER",
    "TEAMLEADER",
    "ARCHILYSE_ONE_ADMIN",
    name="user_role",
)
area_type_enum = Enum(
    "ARCADE",
    "BALCONY",
    "BASEMENT",
    "BASEMENT_COMPARTMENT",
    "BATHROOM",
    "BEDROOM",
    "BIKE_STORAGE",
    "CARPARK",
    "CORRIDOR",
    "DINING",
    "ELEVATOR",
    "FOYER",
    "GARAGE",
    "GARDEN",
    "KITCHEN",
    "KITCHEN_DINING",
    "LIGHTWELL",
    "LIVING_DINING",
    "LIVING_ROOM",
    "LOBBY",
    "LOGGIA",
    "NOT_DEFINED",
    "OFFICE",
    "OIL_TANK",
    "OUTDOOR_VOID",
    "PATIO",
    "PRAM",
    "PRAM_AND_BIKE_STORAGE_ROOM",
    "ROOM",
    "SHAFT",
    "STAIRCASE",
    "STOREROOM",
    "STUDIO",
    "TECHNICAL_AREA",
    "TERRACE",
    "VOID",
    "WASH_AND_DRY_ROOM",
    "WINTERGARTEN",
    "MOTORCYCLE_PARKING",
    "VEHICLE_TRAFFIC_AREA",
    "COMMUNITY_ROOM",
    "BREAK_ROOM",
    "WAITING_ROOM",
    "CANTEEN",
    "PRISON_CELL",
    "OFFICE_SPACE",
    "OPEN_PLAN_OFFICE",
    "MEETING_ROOM",
    "DESIGN_ROOM",
    "COUNTER_ROOM",
    "CONTROL_ROOM",
    "RECEPTION_ROOM",
    "OFFICE_TECH_ROOM",
    "FACTORY_ROOM",
    "WORKSHOP",
    "TECHNICAL_LAB",
    "PHYSICS_LAB",
    "CHEMICAL_LAB",
    "LIVESTOCK",
    "PLANTS",
    "COMMON_KITCHEN",
    "SPECIAL_WORKSPACE",
    "WAREHOUSE",
    "ARCHIVE",
    "COLD_STORAGE",
    "LOGISTICS",
    "SALESROOM",
    "EXHIBITION",
    "TEACHING_ROOM",
    "FLEXIBLE_TEACHING_ROOM",
    "DEDICATED_TEACHING_ROOM",
    "LIBRARY",
    "SPORTS_ROOMS",
    "ASSEMBLY_HALL",
    "STAGE_ROOM",
    "SHOWROOM",
    "CHAPEL",
    "MEDICAL_ROOM",
    "DEDICATED_MEDICAL_ROOM",
    "SURGERY_ROOM",
    "RADIATION_DIAGNOSIS",
    "RADATION_THERAPY",
    "PHYSIO_AND_REHABILITATION",
    "MEDICAL_BEDROOM",
    "DEDICATED_MEDICAL_BEDROOM",
    "SANITARY_ROOMS",
    "CLOAKROOM",
    "PASSENGER_PLATFORM",
    "HOUSE_TECHNICS_FACILITIES",
    "SHELTER",
    "WASTEWATER",
    "WATER_SUPPLY",
    "HEATING",
    "GAS",
    "ELECTRICAL_SUPPLY",
    "TELECOMMUNICATIONS",
    "AIR",
    "ELEVATOR_FACILITIES",
    "OPERATIONS_FACILITIES",
    "CORRIDORS_AND_HALLS",
    "TRANSPORT_SHAFT",
    "BUF10_1_AUSSEN_PP_FAHRZEUG",
    "BUF10_5_BEARB__AUSSENFLAECHE",
    "BUF10_3_AUSSEN_PP_MOTO",
    "BUF10_2_UEBERDACHTE_AUSSEN_PP_FAHRZEUG",
    "BUF10_4_AUSSEN_PP_FAHRRAD",
    "UUF11_1_UNBEARB__AUSSENFLAECHE",
    name="allareatypes",
)
unit_usage_enum = Enum(
    "RESIDENTIAL", "COMMERCIAL", "JANITOR", "PLACEHOLDER", "PUBLIC", name="unit_usage"
)