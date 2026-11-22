from collections.abc import Sequence
from typing import Dict, Optional, Protocol

from textual.screen import ModalScreen

from wifi4.models import ToolName
from wifi4.persist.ap_state import DatedHashline
from wifi4.ui.vault.modals.cpu_crack import CpuCrackConfigModal
from wifi4.ui.vault.modals.hashcat import HashcatConfigModal
from wifi4.ui.vault.modals.hashtopolis import HashtopolisConfigModal


class LaunchModalConstructor(Protocol):
    """The constructor every Vault tool's launch modal shares."""

    def __call__(self, confirm_label: str = "Launch", bssid: Optional[str] = None,
                 probed_ssids: Sequence[str] = (),
                 hashlines: Sequence[DatedHashline] = ()) -> ModalScreen[dict]: ...


UI_TOOLS: Dict[ToolName, LaunchModalConstructor] = {
    ToolName.HASHCAT: HashcatConfigModal,
    ToolName.CPU_CRACK: CpuCrackConfigModal,
    ToolName.HASHTOPOLIS: HashtopolisConfigModal,
}
