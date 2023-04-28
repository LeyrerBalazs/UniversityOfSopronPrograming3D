// Verzió.
#version 330


// Bemeneti adatok

// .vert-től kapott bemeneti adatok.
in vec3 color;
in vec4 world_position;
in vec2 texCoord;

// Uniform által bemeneti adatok.
uniform vec3 lightPos;
uniform vec3 viewPos;
uniform sampler2D s_texture;


// .frag main-je.
void main()
{  
   vec3 lightDir = normalize( vec4(lightPos, 1.0) - world_position  ).xyz;
   float diffColor = max(dot(normalize(color), lightDir), 0.0) * 0.2;
   vec3 color = texture(s_texture, texCoord).rgb + diffColor;
   vec3 viewDir = normalize(viewPos - world_position.xyz);
   vec3 reflectDir = reflect(-lightDir, color); 
   float spec = pow(max(dot(viewDir, reflectDir), 0.0), 100.0) * 0.8;
   vec4 specColor = vec4(1, 1, 1, 1) * spec;
   gl_FragColor = vec4(color, 1) + specColor;
}