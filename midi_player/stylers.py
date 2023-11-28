# Callback functions to define and style the player/visualizer

def basic(url, viz_type="piano-roll"):
    return f'''
            <script src="https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.23.1/es6/core.js,npm/focus-visible@5,npm/html-midi-player@1.5.0"></script>
            <midi-player src="{url}" sound-font visualizer="#myVisualizer"></midi-player>
            <midi-visualizer type="{viz_type}" id="myVisualizer" style="background: #fff;"></midi-visualizer>'''



def cifka_advanced(midi_file_url, viz_type="piano-roll"):
# source: Ondřej Cífka's "HTML MIDI Player Advanced Examples": https://codepen.io/cifkao/pen/GRZxqZN.  
# Repeated use of "#section3" doesn't seem to be an issue...yet. Might have to give each section a unique/random id.
    return '''
<script src="https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.23.1/es6/core.js,npm/focus-visible@5,npm/html-midi-player@1.5.0"></script>

<style>
/* Custom player style */
#section3 midi-player {
  display: block;
  width: inherit;
  margin: 4px;
  margin-bottom: 0;
}
#section3 midi-player::part(control-panel) {
  background: #ff5;
  border: 2px solid #000;
  border-radius: 10px 10px 0 0;
}
#section3 midi-player::part(play-button) {
  color: #353;
  border: 2px solid currentColor;
  background-color: #4d4;
  border-radius: 20px;
  transition: all 0.2s;
  content: 'hello';
}
#section3 midi-player::part(play-button):hover {
  color: #0a0;
  background-color: #5f5;
  border-radius: 10px;
}
#section3 midi-player::part(time) {
  font-family: monospace;
}

/* Custom visualizer style */
#section3 midi-visualizer .piano-roll-visualizer {
  background: #ffd;
  border: 2px solid black;
  border-top: none;
  border-radius: 0 0 10px 10px;
  margin: 4px;
  width: inherit;
  margin-top: 0;
  overflow: auto;
}
#section3 midi-visualizer svg rect.note {
  opacity: 0.6;
  stroke-width: 2;
}
#section3 midi-visualizer svg rect.note[data-instrument="0"]{
  fill: #e22;
  stroke: #500;
}
#section3 midi-visualizer svg rect.note[data-instrument="2"]{
  fill: #2ee;
  stroke: #055;
}
#section3 midi-visualizer svg rect.note[data-is-drum="true"]{
  fill: #888;
  stroke: #888;
}
#section3 midi-visualizer svg rect.note.active {
  opacity: 0.9;
  stroke: #000;
  stroke-width: 3;
}
</style>
''' + f'''
<section id="section3">
<midi-player src={midi_file_url} sound-font visualizer="#section3 midi-visualizer"></midi-player>
<midi-visualizer src={midi_file_url} type={viz_type}></midi-visualizer>
</section>
'''
