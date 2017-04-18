s.shutdown;
s = Server.local.boot;

// statements enclosed in ( ) on separate lines should be executed
// together, either by double clicking on the first parenthesis and
// evaluating the region, or by pressing C-M-x inside the expression.

(
// create a new SynthDef and send it to the server
SynthDef("tutorial-sine", { arg out=0, amp=1.0, freq=440, i_dur=1.0;
	var env, sine;
	// i_* arguments are fixed at instantiation time and cannot be modulated
	// doneAction 2 means free the synth node when the envelope has finished
	env = Line.kr(1, 0, i_dur, doneAction: 2, mul: amp);
	// the mul ugen input is usually more efficient than *
	sine = SinOsc.ar(freq, mul: env);
	//sine = SinOsc.ar(freq, mul: amp);
	// output two channels on bus 0
	Out.ar(0, [sine, sine]);
}).send(s);
)

(
// node object style
Task({
	var freq1, freq2, dur;
	freq1 = 440;
	freq2 = 440;

	dur = 0.3;
	10.do { arg i;
		// use Synth.grain rather than Synth.new because the
		// Synth deallocates itself, so we don't need a node id
		Synth.grain(
			// see C-c C-h Synth
			"tutorial-sine",
			["amp", 1, "freq", freq1, "i_dur", dur],
			s
		);
		dur.wait;
		Synth.grain(
			// see C-c C-h Synth
			"tutorial-sine",
			["amp", 0.1, "freq", freq2, "i_dur", dur],
			s
		);
		dur.wait;
	}
}).play
)

MouseX

{ SinOsc.ar(MouseX.kr(100, 400, 0), 0, 0.2) + SinOsc.ar(MouseY.kr(100, 400, 0), 0.2) }.scope;
var n=10;

{ SinOsc.ar( MouseX.kr(40, 2000, 1), .6) }.scope;

{ SinOsc.ar( (MouseX.kr(200, 2000, 1)/MouseY.kr(10, 300, 0)).floor * MouseY.kr(10, 300, 0), 0, 0.6) }.scope;


