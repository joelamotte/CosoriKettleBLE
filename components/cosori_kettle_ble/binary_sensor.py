"""Binary sensor platform for Cosori Kettle BLE."""
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID
from . import CosoriKettleBLE, CONF_COSORI_KETTLE_BLE_ID, cosori_kettle_ble_ns

CONF_ON_BASE = "on_base"
CONF_HEATING = "heating"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_COSORI_KETTLE_BLE_ID): cv.use_id(CosoriKettleBLE),
        cv.Optional(CONF_ON_BASE): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_HEATING): binary_sensor.binary_sensor_schema(),
    }
)


async def to_code(config):
    """Code generation for binary sensor platform."""
    parent = await cg.get_variable(config[CONF_COSORI_KETTLE_BLE_ID])

    if CONF_ON_BASE in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_ON_BASE])
        cg.add(parent.set_on_base_binary_sensor(sens))

    if CONF_HEATING in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_HEATING])
        cg.add(parent.set_heating_binary_sensor(sens))
