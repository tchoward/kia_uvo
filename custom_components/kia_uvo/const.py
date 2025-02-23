import logging

from datetime import tzinfo
from dateutil import tz
from enum import Enum

from homeassistant.const import LENGTH_KILOMETERS, LENGTH_MILES

# Configuration Constants
DOMAIN: str = "kia_uvo_2"
CONF_PIN: str = "pin"
CONF_STORED_CREDENTIALS: str = "stored_credentials"
CONF_SCAN_INTERVAL: str = "scan_interval"
CONF_FORCE_SCAN_INTERVAL: str = "force_scan_interval"
CONF_NO_FORCE_SCAN_HOUR_START: str = "no_force_scan_hour_start"
CONF_NO_FORCE_SCAN_HOUR_FINISH: str = "no_force_scan_hour_finish"
CONF_ENABLE_GEOLOCATION_ENTITY: str = "enable_geolocation_entity"
CONF_USE_EMAIL_WITH_GEOCODE_API: str = "use_email_with_geocode_api"
CONF_BRAND: str = "brand"

# I have seen that many people can survive with receiving updates in every 30 minutes. Let's see how KIA will respond
DEFAULT_SCAN_INTERVAL: int = 30
# When vehicle is running/active, it will update its status regularly, so no need to force it. If it has not been running, we will force it every 240 minutes
DEFAULT_FORCE_SCAN_INTERVAL: int = 240
DEFAULT_NO_FORCE_SCAN_HOUR_START: int = 22
DEFAULT_NO_FORCE_SCAN_HOUR_FINISH: int = 6
DEFAULT_ENABLE_GEOLOCATION_ENTITY: bool = False
DEFAULT_USE_EMAIL_WITH_GEOCODE_API: bool = False
TIME_ZONE_EUROPE = tz.gettz("Europe/Berlin")

# Integration Setting Constants
PARALLEL_UPDATES: int = 1
CONFIG_FLOW_VERSION: int = 1
PLATFORMS = ["binary_sensor", "device_tracker", "sensor", "lock"]
TOPIC_UPDATE: str = f"{DOMAIN}_update_{0}"

# Home Assistant Data Storage Constants
DATA_VEHICLE_INSTANCE: str = "vehicle"  # Vehicle Instance
DATA_VEHICLE_LISTENER: str = (
    "vehicle_listener"  # Vehicle Topic Update Listener Unsubcribe Caller
)
DATA_CONFIG_UPDATE_LISTENER: str = (
    "config_update_listener"  # Config Options Update Listener Unsubcribe Caller
)

# action status delay constants
INITIAL_STATUS_DELAY_AFTER_COMMAND: int = 15
RECHECK_STATUS_DELAY_AFTER_COMMAND: int = 10
# Retry Specific Constants
START_FORCE_UPDATE_AFTER_COMMAND: int = 10  # Trigger first force update after a command
INTERVAL_FORCE_UPDATE_AFTER_COMMAND: int = 30  # Consecutive force update calls interval
COUNT_FORCE_UPDATE_AFTER_COMMAND: int = (
    5  # Number of force update calls after a command
)

# Sensor Specific Constants
NOT_APPLICABLE: str = "Not Applicable"
DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S.%f"
DYNAMIC_DISTANCE_UNIT: str = "dynamic_distance_unit"
DISTANCE_UNITS = {1: LENGTH_KILOMETERS, 3: LENGTH_MILES}
DYNAMIC_TEMP_UNIT: str = "dynamic_temp_unit"

REGION_EUROPE = "Europe"
REGION_CANADA = "Canada"
REGION_USA = "USA"
REGIONS = {1: REGION_EUROPE, 2: REGION_CANADA, 3: REGION_USA}
DEFAULT_REGION = 1
DEFAULT_PIN = ""

BRAND_KIA = "Kia"
BRAND_HYUNDAI = "Hyundai"
BRANDS = {1: BRAND_KIA, 2: BRAND_HYUNDAI}
DEFAULT_BRAND = 1

EU_TEMP_RANGE = [
    14,
    14.5,
    15,
    15.5,
    16,
    16.5,
    17,
    17.5,
    18,
    18.5,
    19,
    19.5,
    20,
    20.5,
    21,
    21.5,
    22,
    22.5,
    23,
    23.5,
    24,
    24.5,
    25,
    25.5,
    26,
    26.5,
    27,
    27.5,
    28,
    28.5,
    29,
    29.5,
    30,
]
CA_TEMP_RANGE = [
    16,
    16.5,
    17,
    17.5,
    18,
    18.5,
    19,
    19.5,
    20,
    20.5,
    21,
    21.5,
    22,
    22.5,
    23,
    23.5,
    24,
    24.5,
    25,
    25.5,
    26,
    26.5,
    27,
    27.5,
    28,
    28.5,
    29,
    29.5,
    30,
    30.5,
    31,
    31.5,
    32,
]
USA_TEMP_RANGE = range(62, 82)


class VEHICLE_ENGINE_TYPE(Enum):
    EV = 1
    PHEV = 2
    IC = 3


class VEHICLE_LOCK_ACTION(Enum):
    LOCK = "close"
    UNLOCK = "open"
