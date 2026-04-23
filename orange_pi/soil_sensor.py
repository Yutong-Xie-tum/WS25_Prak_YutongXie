#!/usr/bin/env python3
from bottle import route, run, response
import OPi.GPIO as GPIO
import time
import json

SENSOR_PIN = "PH2"   # Orange Pi Zero 2W, physical pin 11

GPIO.setmode(GPIO.SUNXI)
GPIO.setup(SENSOR_PIN, GPIO.IN)

@route('/')
def get_moisture():
    response.content_type = 'application/json'

    try:
        state = GPIO.input(SENSOR_PIN)

        result = {
            "success": True,
            "sensor_pin": SENSOR_PIN,
            "raw_state": int(state),
            "soil_status": "dry" if state else "wet",
            "timestamp": int(time.time())
        }
        return json.dumps(result)

    except Exception as e:
        response.status = 500
        return json.dumps({
            "success": False,
            "error": str(e)
        })

run(host='0.0.0.0', port=18080)