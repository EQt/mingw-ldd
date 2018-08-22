# `mingw-ldd`

Tool to [list dynamic dependencies][wiki] of a dll using the Python module `pefile`, similar to the Unix tool.


Kudos to yan12125 for the original script:
https://gist.github.com/yan12125/63c7241596e628553d21

## Requirements

- Python
- `pefile` (available via
  [`pip`](https://pypi.org/project/pefile/) or 
  [`conda-forge`](https://anaconda.org/conda-forge/pefile))

## Usage

    $ ./mingw-ldd.py /usr/i686-w64-mingw32/bin/libpng16-16.dll
            libgcc_s_sjlj-1.dll => /usr/i686-w64-mingw32/bin/libgcc_s_sjlj-1.dll
            KERNEL32.dll => not found
            msvcrt.dll => not found
            libwinpthread-1.dll => /usr/i686-w64-mingw32/bin/libwinpthread-1.dll
            zlib1.dll => /usr/i686-w64-mingw32/bin/zlib1.dll

## See also

You can also checkout another similar tool:
https://github.com/LRN/ntldd


[wiki]: https://en.wikipedia.org/wiki/Ldd_(Unix)
