ARTWORK PLACEMENT GUIDE – ARYNWOOD 3D GALLERY

This guide explains how to place and rotate artwork inside the 3D gallery using Three.js. Each wall in the gallery has a coordinate boundary. Artwork is placed using .position.set(x, y, z) and .rotation.y values.

⸻

WALL COORDINATES OVERVIEW
	•	Back Wall: z = -24.5 (faces forward)
	•	Front Wall: z = 24.5 (faces backward)
	•	Left Wall: x = -24.5 (faces right)
	•	Right Wall: x = 24.5 (faces left)

⸻

PLACEMENT TEMPLATE

artwork.position.set(x, y, z);
artwork.rotation.y = THREE.MathUtils.degToRad(degrees);

⸻

BACK WALL (default)
artwork.position.set(0, 5, -24.5);
artwork.rotation.y = 0;

FRONT WALL
artwork.position.set(0, 5, 24.5);
artwork.rotation.y = Math.PI;

LEFT WALL
artwork.position.set(-24.5, 5, 0);
artwork.rotation.y = THREE.MathUtils.degToRad(90);

RIGHT WALL
artwork.position.set(24.5, 5, 0);
artwork.rotation.y = THREE.MathUtils.degToRad(-90);

⸻

HEIGHT GUIDELINES

Use y = 5 for eye-level center (assuming artwork height is about 5 units).
Adjust up or down if the artwork is larger or smaller.

⸻

ROTATION TIPS

Three.js uses radians for rotation. To convert degrees:

THREE.MathUtils.degToRad(90); // returns 1.5708

Use .rotation.y to turn side to side.
Use .rotation.x or .rotation.z for tilting.

⸻

FLOOR OR TABLE DISPLAY EXAMPLE

artwork.rotation.x = THREE.MathUtils.degToRad(-90); // lays flat

⸻

FUTURE FEATURES (planned)
	•	Add title labels next to each artwork
	•	Grid layout script for even spacing
	•	GUI editor for live positioning

⸻

LICENSE

Open-source under the MIT License.
Created by Lorelei Noble for the Arynwood 3D gallery project.