"""Termux/Android setup: Android grants USB access through ``wifi4``'s startup ``termux-usb`` prompt."""
from __future__ import annotations

from wifi4.models import DeviceID
from wifi4.setup.base import Prompter, Setup, SetupResult


class SetupTermux(Setup):
    """No privileged step: the ``termux-usb -r`` permission dialog is the setup."""

    async def install(self, device_id: DeviceID, ui: Prompter) -> DeviceID | None:
        ui.error(
            "USB access",
            "Android grants USB access when an adapter is attached. Plug it in and accept "
            "the permission dialog.\n\n"
            "The Termux:API app must be installed (the termux-api package alone is not enough).\n\n"
            "List attached devices with: wifi4 --list-usb",
        )
        return None

    async def uninstall(self, device_id: DeviceID, ui: Prompter) -> SetupResult:
        return SetupResult(ok=True, message="Android grants USB access per app; nothing to remove.")
