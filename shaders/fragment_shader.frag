#version 330

// in
in vec3 color;

void main()
{  
   // Main
   gl_FragColor = vec4(color, 1);
}
