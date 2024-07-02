#!/usr/bin/env sh

# makefile_replace_string_in_file.sh
# author: smikhail <halleberry>
# created: Mon Jul  1 19:53:49 MDT 2024
# updated: Mon Jul  1 19:55:44 MDT 2024

_old = ${1}  # orders
_new = ${2}  # schedules
_infile = ${3}  # replace_string_in_file.txt
_outfile = ${4}  # replace_string_out_file.txt


sed "s/${_old}/${_new}/g" ${_infile} > ${_outfile}
