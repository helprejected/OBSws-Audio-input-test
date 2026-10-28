## OBS audio threshold example

This example subscribes to OBS WebSocket's `InputVolumeMeters` event and
prints a clear message when the selected input crosses the configured
threshold in either direction.

### Setup

1. In OBS, open **Tools > WebSocket Server Settings** and enable the WebSocket
   server. Set a password if desired.
2. Copy the server port and password into `setting.txt`. The default port is
   `4455`.
3. Set `input_name` to the exact name of the audio input shown in OBS.
4. Install the dependency with `python -m pip install -r requirements.txt`.
5. Run `python main.py`. Press Ctrl+C to stop.

The script uses OBS's live meter data, not `GetInputVolume` (which reports the
input's configured volume/gain). The protocol sends `InputVolumeMeters` every
50 ms, which is 20 Hz. OBS controls this event rate; it cannot provide a true
50 Hz live meter stream through this event.

Terminal logging suppresses per-event DEBUG output. A crossing to -40 dB or
higher prints `THRESHOLD REACHED` once; a crossing back below it prints
`Threshold no longer reached` once.
