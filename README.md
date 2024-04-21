# Implementation of compiler for LOGO programming language in 3D
By -   
Himani Panwar, 21114041  
Sahil Safy, 21114087  
Sanidhya Bhatia, 21114090
     
This is a compiler made for drawing exciting figures using logo programming language in 3D.

## Features

- Tokenizes input expressions into meaningful tokens.
- Parses and evaluates the logo commands.
- Makes figure in 3D using OpenGL and pygame libraries.

## Usage

1. Write a logo program in `[filename].lgo`.
2. Install pygame using `pip install pygame`
3. Use `pip install PyOpenGL PyOpenGL_accelerate` to install openGL.(Note: Refer to [Stackoverflow](https://stackoverflow.com/questions/26700719/pyopengl-glutinit-nullfunctionerror) if there is a problem.)
4. Run the command `python Logo3D.py [filename].lgo` to compile and execute the program.
5. Use `/r a:x:y:z (rotate at angle 'a' around '(x,y,z)')"` after the aforementioned command to use the feature of rotation.

## Example Usage
We can draw a square using this:

```
FD 3 RT 90
FD 3 RT 90
FD 3 RT 90
FD 3 RT 90
```

