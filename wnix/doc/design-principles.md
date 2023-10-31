# Design Principles

Modern generative AI involves building large systems that contain both:
- software 1.0 (traditional programming: files, directories, binary data, text data)
- software 2.0 (artificial intelligence: soft, differentiable, learnable operations)

Imagine a differentiable operating system, with kernel that supports the basic sensory IO operations such as image to text, audio to text. Suppose vision and audition are implemented as kernel modules.

What coreutils would this system have?

What programs would we run from its command line shell?

Ignoring edge cases, the design principles of Unix are:

Principles of the Unix Shell
- Everything is a file.
- Everything is text.
- This gives us one universal data type for both input and output.
- Since there's only one type, all functions compose.
- Pipes are function composition.
- Pipes can be used to connect any two commands in ways their authors never imagined.

Principles of the Wnix Shell
- Same as above, replacing "text" with "embedding."