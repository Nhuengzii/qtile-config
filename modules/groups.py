from libqtile.config import DropDown, Key, Group, Match, ScratchPad
from libqtile.command import lazy
from .keys import keys, mod

groups = [Group(i) for i in "123456"]
groups.append(Group("7", matches=[Match(wm_class=["discord"])]))

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
keys.append(
    Key([mod, "shift"], "d", lazy.group["7"].toscreen(), desc="Switch to group 7")
)
groups.append(ScratchPad("scratchpad", [
    DropDown("term", "kitty -e tmux", opacity=0.8,
             height=0.8, width=0.8, x=0.1, y=0.1),
    DropDown("slack", "slack", match=Match(wm_class="slack"), opacity=1,
             height=0.8, width=0.8, x=0.1, y=0.1),
    DropDown("microsoft-edge-stable", "microsoft-edge-stable", match=Match(wm_class="microsoft-edge"), opacity=1,
             height=0.8, width=0.8, x=0.1, y=0.1),
]))
keys.extend([
    Key([mod, "shift"], "Return", lazy.group["scratchpad"].dropdown_toggle(
        "term"), desc="Toggle terminal"),
    Key([mod, "shift"], "s", lazy.group["scratchpad"].dropdown_toggle(
        "slack"), desc="Toggle slack"),
    Key([mod, "shift"], "w", lazy.group["scratchpad"].dropdown_toggle(
        "microsoft-edge-stable"), desc="Toggle microsoft-edge-stable"),
])
