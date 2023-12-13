# Callback functions to define and style the player/visualizer
import random 

src_header = '''<script src="https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.23.1/es6/core.js,npm/focus-visible@5,npm/html-midi-player@1.5.0"></script>'''

dl_str = lambda url, dl: f'<a href="{url}" target="_blank">Download MIDI</a><br>' if dl else ''



def basic(url, viz_type="piano-roll", dl=False, title=''):
    return f'''{src_header}  {title} {dl_str(url, dl)}
            <midi-player src="{url}" sound-font visualizer="#myVisualizer"></midi-player>
            <midi-visualizer type="{viz_type}" id="myVisualizer" style="background: #fff;"></midi-visualizer>'''


# source: Ondřej Cífka's "HTML MIDI Player Advanced Examples": https://codepen.io/cifkao/pen/GRZxqZN.  
cifka_css = '''<style>
/* Custom player style */
#section3 midi-player {
  display: block;
  width: inherit;
  margin: 4px;
  margin-bottom: 0;
  font-family: Arial;
}
p { margin:0 }

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
'''

def general(url, viz_type="piano-roll", dl=True, css='', title=''):
    secnum = random.randint(0,1000)  # randomize section number to avoid conflicts
    css = css.replace('#section3', f'#section{secnum}')
    header = '' if (title=='' or title=='&nbsp;') and dl==False else f'<p style="text-align:left;font-family:Arial;">{title}<span style="float:right;">{dl_str(url,dl)}</span></p>'
    return f'''{src_header}\n{css}
          <section id="section{secnum}">{header}
          <midi-player src={url} sound-font visualizer="#section{secnum} midi-visualizer"></midi-player>
          <midi-visualizer src={url} type={viz_type}></midi-visualizer>
          </section>
          '''

def cifka_advanced(url, viz_type="piano-roll", dl=True, css=cifka_css, title=''):
    return general(url, viz_type=viz_type, dl=dl, css=css, title=title)


# hawley modified based on cifka's, suggestions by ChatGPT since I don't know color theory
dark_css = '''
<style>
/* Custom player style */
p { 
  margin:0; 
  color: #c4c4c4; /* mid-lightness text color for title, intended for dark backgrounds */
}

#section3 midi-player {
  display: block;
  width: inherit;
  margin: 4px;
  margin-bottom: 0;
  color: #d4d4d4; /* Lighter text color for better readability */
}
#section3 midi-player::part(control-panel) {
  background: #222; /* Dark background */
  border: 2px solid #888; /* Lightened border color for contrast */
  border-radius: 10px 10px 0 0;
}
#section3 midi-player::part(play-button) {
  color: #ffffff; /* White text for visibility */
  border: 2px solid currentColor;
  background-color: #6c7a89; 
  border-radius: 20px;
  transition: all 0.2s;
  content: 'hello';
}
#section3 midi-player::part(play-button):hover {
  color: #00a; 
  background-color: #9fafc9; 
  border-radius: 10px;
}
#section3 midi-player::part(time) {
  font-family: monospace; /* Monospace font for time */
}

/* Custom visualizer style */
#section3 midi-visualizer .piano-roll-visualizer {
  background: #333; /* Dark background for visualizer */
  border: 2px solid #505050; /* Dark border for subtle appearance */
  border-top: none;
  border-radius: 0 0 10px 10px;
  margin: 4px;
  width: inherit;
  margin-top: 0;
  overflow: auto;
}
#section3 midi-visualizer svg rect.note {
  opacity: 0.9; 
  stroke-width: 1; /* Stroke width for note clarity */
}

/* Different instrument colors */
#section3 midi-visualizer svg rect.note[data-instrument="0"]{
  fill: #7aa6ed; /*  blue for Instrument 0 */
  stroke: #444; 
}
#section3 midi-visualizer svg rect.note[data-instrument="2"]{
  fill: #d586d0; /* purple for Instrument 2 for consistency */
  stroke: #444; /* White stroke for visibility */
}
#section3 midi-visualizer svg rect.note[data-is-drum="true"]{
  fill: brightorange; 
  stroke: #bbb;
}
#section3 midi-visualizer svg rect.note.active {
  opacity: 0.9; /* Highlight active notes */
  stroke: #ddd; /* White stroke for maximum contrast */
  stroke-width: 2; /* Thicker stroke for active notes */
}
</style>
'''

def dark(url, viz_type="piano-roll", dl=True, css=dark_css, title=''):
    return general(url, viz_type=viz_type, dl=dl, css=css, title=title)

