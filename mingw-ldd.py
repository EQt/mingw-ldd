#!/usr/bin/env python
# WTFPL - Do What the Fuck You Want to Public License
"""
print dll dependencies
"""
from __future__ import print_function
import pefile
import os
import sys


def get_dependency(filename):
    deps = []
    pe = pefile.PE(filename)
    for imp in pe.DIRECTORY_ENTRY_IMPORT:
        deps.append(imp.dll.decode())
    return deps


def dep_tree(root, prefix=None):
    if not prefix:
        arch = get_arch(root)
        # print('Arch =', arch)
        prefix = '/usr/'+arch+'-w64-mingw32/bin'
        # print('Using default prefix', prefix)
    dep_dlls = dict()

    def dep_tree_impl(root, prefix):
        for dll in get_dependency(root):
            if dll in dep_dlls:
                continue
            full_path = os.path.join(prefix, dll)
            if os.path.exists(full_path):
                dep_dlls[dll] = full_path
                dep_tree_impl(full_path, prefix=prefix)
            else:
                dep_dlls[dll] = 'not found'

    dep_tree_impl(root, prefix)
    return (dep_dlls)


def get_arch(filename):
    type2arch = {pefile.OPTIONAL_HEADER_MAGIC_PE: 'i686',
                 pefile.OPTIONAL_HEADER_MAGIC_PE_PLUS: 'x86_64'}
    pe = pefile.PE(filename)
    try:
        return type2arch[pe.PE_TYPE]
    except KeyError:
        sys.stderr.write('Error: unknown architecture')
        sys.exit(1)


if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('dll', nargs='+', help='file which should be analyzed')
    args = p.parse_args()

    for filename in args.dll:
        print(filename + ':')
        for dll, full_path in dep_tree(filename).items():
            print(' ' * 7, dll, '=>', full_path)
