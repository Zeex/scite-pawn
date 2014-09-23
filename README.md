Installation
------------

1. Copy pawn.properties and pawn.api to your SciTE installation directory,
   e.g. `C:\wscite`.
2. Copy SciTEUser.properties to your home directory. On Windows it's usually
   `C:\Users\your_name` (optional).
3. Open SciTEGlobal.properties (Tools -> Open Global Options File) and add
   `import pawn` in the end. This will enable Pawn syntax highlighting for
   *.pwn and *.inc files.
4. Set `SAMP_SERVER_ROOT` environment variable to the full path to your server
   root folder, e.g. `C:\samp-server`. On Windows this can be done via
   Control Panel -> System -> Advanced system settings -> Advanced ->
   Environment variables -> New...
5. Add `%SAMP_SERVER_ROOT%\pawno` to your `PATH` or edit pawn.properties and
   replace `pawncc` with the full path to the compiler.

Key bindings
------------

The following key bindings are available by default:

* `Ctrl + 1` - compile in Release mode (with `-d0`)
* `Ctrl + 2` - compile in Debug mode (with `-d3`)
* `Ctrl + 3` - preprocess only (`-l`)
* `Ctrl + 4` - write assembly code listing (`-a`)
* `Ctrl + 5` - disassemble .amx file (`pawndisasm` must be present in `PATH`)

You can change them or create your own by editing pawn.properties (go to menu ->
Options -> Open pawn.properties).


Troubleshooting
---------------

* **No syntax highlighting when editing *.inc files**

  There's probably another language file imported that uses the same file
  extension. Try commenting out the `#import *` in SciTEGlobal.properties
  and adding these instead:

  ```
  import others
  import cpp
  ```
