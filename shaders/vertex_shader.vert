// Verzió.
#version 330

// Bementi adatok

// Pointer által bemeneti adatok.
layout(location = 0) in vec3 v_coord;
layout(location = 1) in vec3 v_normal_color;
layout(location = 2) in vec2 v_texCoord;

// Uniform által bemeneti adatok.
uniform mat4 modelView;
uniform mat4 perspectiveMatrix;
uniform mat4 camera;


// Kimeneti adatok

// Tovább a fragmentnek.
out vec3 color;
out vec4 world_position;
out vec2 texCoord;


// .vert main-je.
void main() {
   world_position = modelView * vec4(v_coord, 1.0);
   gl_Position = perspectiveMatrix * camera * world_position;
   color = normalize( mat3(transpose(inverse(modelView))) * v_normal_color);
   texCoord = v_texCoord;
}