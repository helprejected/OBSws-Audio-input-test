import configparser
import logging
import math
import threading
from pathlib import Path

import obsws_python


CONFIG = configparser.ConfigParser()
CONFIG_PATH = Path(__file__).with_name("setting.txt")
if not CONFIG.read(CONFIG_PATH, encoding="utf-8"):
    raise FileNotFoundError(f"Could not read settings file: {CONFIG_PATH}")

HOST = CONFIG.get("obs", "host")
PORT = CONFIG.getint("obs", "port")
PASSWORD = CONFIG.get("obs", "password")
INPUT_NAME = CONFIG.get("monitor", "input_name")
THRESHOLD_DB = CONFIG.getfloat("monitor", "threshold_db")
EVENT_INTERVAL_MS = 50

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)
above_threshold = None


def on_input_volume_meters(event):
    global above_threshold

    for input_meter in event.inputs:
        if input_meter["inputName"] != INPUT_NAME:
            continue

        levels_mul = input_meter["inputLevelsMul"]
        channel_levels_mul = [level for channel in levels_mul for level in channel]
        if not channel_levels_mul:
            return

        peak_level_mul = max(channel_levels_mul)
        current_db = (
            20 * math.log10(peak_level_mul) if peak_level_mul > 0 else float("-inf")
        )
        is_above_threshold = current_db >= THRESHOLD_DB
        if above_threshold is None:
            above_threshold = is_above_threshold
            if not is_above_threshold:
                return
            state = "passed" if is_above_threshold else "fell below"
        elif is_above_threshold != above_threshold:
            above_threshold = is_above_threshold
            state = "passed" if is_above_threshold else "fell below"
        else:
            return

        message = (
            "THRESHOLD REACHED"
            if state == "passed"
            else "Threshold no longer reached"
        )
        logger.info(
            "%s: %s is at %.1f dB (threshold: %.1f dB)",
            message,
            INPUT_NAME,
            current_db,
            THRESHOLD_DB,
        )
        return

def scene_visibility_changed(event):
    logger.info(
        "Scene visibility changed: %s is now %s",
        event.scene_name,
        "visible" if event.visible else "hidden",
    message = (
        "SENE VISIBILITY CHANGED"
        if state == "passed"
        else "Scene visibility changed"
    if 
    )
    )