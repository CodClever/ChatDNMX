const hour = new Date().getHours(); 
let greeting;

if (hour <= 9)
  greeting = "Good Morning"

if (hour < 18) {
  greeting = "Good Evening";
}  
if (hour < 12)
  greeting = "Good Afternoon"

if (hour < 24)
  greeting = "Good Night"

document.getElementById("demo").innerHTML = greeting;

const body = {
    steps: 40,
	width: 512,
	height: 512,
	seed: 0,
	cfg_scale: 5,
	samples: 1,
	text_prompts: [
	  {
	    "text": "dog",
	    "weight": 1
	  },
	  {
	    "text": "blurry, bad",
	    "weight": -1
	  }
	],
  };
