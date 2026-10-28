## OBS audio threshold example

***Janky example trying to use threads for obsws***

### Setup

1. In OBS, open **Tools > WebSocket Server Settings** and enable the WebSocket
   server. Set a password if desired.
2. Copy the server port and password into `setting.txt`. The default port is
   `4455`.
3. Set `input_name` to the exact name of the audio input shown in OBS.
4. Install the dependency with `python -m pip install -r requirements.txt`.
5. Run `python main.py`. Press Ctrl+C to stop.

The script uses OBS's live meter data, not `GetInputVolume` (which reports the
input's configured volume/gain). 

Older method involved requiring obsws data with a polling rate of 50hz (Which is laggy and inefficient)
-> **Trying to implement threading (learning)**

Terminal logs prints `THRESHOLD REACHED` once threshold reached, crossing back below it prints 
`Threshold no longer reached`.
