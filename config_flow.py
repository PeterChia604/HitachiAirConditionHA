"""Config flow for HitachiAirConditionHA integration."""
import logging
import asyncio
import voluptuous as vol

from homeassistant import config_entries, core, exceptions
from homeassistant.const import HitachiAccount_CONF_EMAIL, HitachiAccount_CONF_PASSWORD


