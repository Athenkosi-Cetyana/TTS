
var song;
var record_button;
var stop_button;
var play_button;
var delete_button;
var say = document.getElementById("formz");
var button = document.getElementById("bx");

let mic, recorder, soundFile;

let state = 0; // mousePress will increment from Record, to Stop, to Play

function setup() {
  createCanvas(400, 400);
  background(200);
  fill(0);
  text('Enable mic and CLICK the mouse to begin recording', 20, 20);

  // create an audio in
  mic = new p5.AudioIn();

  // users must manually enable their browser microphone for recording to work properly!
  mic.start();

  // create a sound recorder
  recorder = new p5.SoundRecorder();

  // connect the mic to the recorder
  recorder.setInput(mic);

  // create an empty sound file that we will use to playback the recording
  soundFile = new p5.SoundFile();
}
function mousePressed() {  
  

  // use the '.enabled' boolean to make sure user enabled the mic (otherwise we'd record silence)
  if (state === 0 && mic.enabled) {
    // Tell recorder to record to a p5.SoundFile which we will use for playback
    recorder.record(soundFile);

    background(255, 0, 0);
    text('Recording now! Click to stop.', 20, 20);
    state++;
  } else if (state === 1) {
    recorder.stop(); // stop recorder, and send the result to soundFile

    background(0, 255, 0);
    text('Recording stopped. Click to play & save', 20, 20);
    state++;
  } else if (state === 2) {
    soundFile.play(); // play the result!
    saveSound(soundFile, 'mySound.wav'); // save file
    state++;
  }
}
button.addEventListener("click", createNew);
function createNew(){
  say.innerHTML = "Yes";
}






















/*
function setup() {
  createCanvas(400, 400);
  mic = new p5.AudioIn();
  mic.start();

  song = loadSound("song.mp3", loaded);

  // buttons and events
  record_button = createButton("Record");
  record_button.position(0, 410);
  record_button.mousePressed(togglePlaying);

  stop_button = createButton("Stop");
  stop_button.position(65, 410);
  stop_button.mousePressed(togglePlaying);

  play_button = createButton("Play");
  play_button.position(115, 410);
  play_button.mousePressed(togglePlaying);

  delete_button = createButton("Delete");
  delete_button.position(165, 410);
  delete_button.mousePressed(togglePlaying);
}

function draw() {
  background(color(0, 0, 255));
  fill(225);
  text('Recording ...', width / 2, 20);

  var micLevel = mic.getLevel();

  ellipse(200, 200, 200, micLevel * 1000);
  console.log(micLevel);
}

function loaded() {
  console.log("loaded");
}

function togglePlaying() {
  
  
  if(!song.isPlaying()){
    song.play();
    song.setVolume(1);
    play_button.html("Pause");
  }
  song.pause();
  play_button.html("Play");
}
*/