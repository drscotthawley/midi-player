# midi-player
Python launcher of the animated MIDI player by [@cifkao](https://github.com/cifkao) &amp; [@magenta](https://github.com/magenta)


# Installation

```
pip install midi-player
```

# Usage

Only tested with Jupyter Notebooks & Colab, but uses no IPython dependencies so it *should* work in other contexts.
```python

from midi_player import MIDIPlayer
from midi_player.stylers import basic, cifka_advanced

midi_file_url = "https://magenta.github.io/magenta-js/music/demos/melody.mid"
midi_file = "data/test_midi.mid"

MIDIPlayer(midi_file_url, 400)  
MIDIPlayer(midi_file, 160, styler=cifka_advanced)
```

With `wandb`:
```python
import wandb

wandb.login()
wandb.init(project="midi-player")
mp = MIDIPlayer(midi_file, 300, viz_type="waterfall")
wandb.log(wandb.Html(mp.html))
wandb.finish()

```

See `examples/` for more.

# Documentation

TO-DO. Particularly, people will want to know how to add/customize their own "stylers". 
See `midi_player/*.py` for now ;-).

# Known Issues
* Not sure why the staff view is putting out 32nd notes / how to tell it to do 8th notes instead. 
