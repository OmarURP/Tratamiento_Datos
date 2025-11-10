//+
Point(1) = {0, 0, 0, 0.01};
//+
Point(2) = {0.1, 0, 0, 0.01};
//+
Point(3) = {0.1, 0.1, 0, 0.01};
//+
Point(4) = {0, 0.1, 0, 0.01};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1};
//+
Transfinite Curve {2, 3, 4, 1} = 20 Using Progression 1;
//+
Transfinite Surface {1};
//+
Recombine Surface {1};
//+
Extrude {0, 0, 0.01} {
  Surface{1}; 
  Layers{1};      // Número de capas de elementos en la extrusión
  Recombine;      // Genera hexaedros en lugar de tetraedros
}
//+
Physical Surface("movingWall", 27) = {13};
//+
Physical Surface("fixedWalls", 28) = {17, 21, 25};
//+
Physical Surface("frontandback", 29) = {1, 26};
//+
Physical Volume("internal", 30) = {1};