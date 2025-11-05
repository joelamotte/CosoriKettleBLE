"""Constants for the Cosori Kettle BLE component."""

# BLE Service and Characteristic UUIDs
COSORI_SERVICE_UUID = "0000fff0-0000-1000-8000-00805f9b34fb"
COSORI_RX_CHAR_UUID = "0000fff1-0000-1000-8000-00805f9b34fb"  # Notify
COSORI_TX_CHAR_UUID = "0000fff2-0000-1000-8000-00805f9b34fb"  # Write

# Protocol Constants
MIN_SETPOINT_F = 104
MAX_SETPOINT_F = 212
DEFAULT_SETPOINT_F = 212

# Registration handshake fragments (HELLO_MIN)
# These must be sent verbatim at connection start
HELLO_MIN = [
    bytes.fromhex("a5 22 00 24 00 8a 00 81 d1 00 36 34 32 38 37 61 39 31 37 65"),
    bytes.fromhex("37 34 36 61 30 37 33 31 31 36 36 62 37 36 66 34 33 64 35 63"),
    bytes.fromhex("62 62"),
]

# Frame types
FRAME_TYPE_A5_22 = 0x22  # Compact status / commands
FRAME_TYPE_A5_12 = 0x12  # Extended status / control

# Packet structure markers
FRAME_START = 0xA5
COMPACT_STATUS_MARKER = bytes([0x01, 0x41, 0x40, 0x00])
EXTENDED_STATUS_MARKER = bytes([0x01, 0x40, 0x40, 0x00])

# Temperature validation range
MIN_TEMP_F = 40
MAX_TEMP_F = 230

# Mode values
MODE_BOIL = 0x04        # 212°F full boil
MODE_KEEP_WARM = 0x06   # <212°F keep warm

# Checksum base values (rolling sequence formulas)
CHECKSUM_POLL = 0xB4
CHECKSUM_HELLO5 = 0x7C
CHECKSUM_SETPOINT = 0x7D
CHECKSUM_F4 = 0x9D
CHECKSUM_CTRL = 0xC3

# Connection health
MAX_NO_RESPONSE_COUNT = 10  # Mark offline after 10 missed polls
POLL_INTERVAL_MS = 1000     # Poll every 1 second
