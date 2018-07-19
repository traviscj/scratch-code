#!/usr/bin/env python3
# created_at: 2018-07-19 14:19:37 -0700
# remove w/: rm $HOME/scratch/python/Scratch_dZ9fya.py

import glob
import os
import random
import string
import sys

import arrow
import click
import pystache

SCRATCH_ROOT = os.path.expanduser("~/scratch")

SCRATCHES = []

def initialize():
    for f in glob.glob(os.path.expanduser(SCRATCH_ROOT + "/*/template*")):
        lang_template_file = f.replace(SCRATCH_ROOT + "/", "")
        lang, template_file = lang_template_file.split('/')
        template_ext = template_file.replace("template.", "")
        SCRATCHES.append({"lang": lang, "template_ext": template_ext, "f": f})

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_template(lang):
    return [s for s in SCRATCHES if s["lang"] == lang or s["template_ext"] == lang][0]

def create(lang):
    scratch_def = get_template(lang)
    
    unique_name = id_generator()
    class_name = "Scratch_" + unique_name
    file_name = SCRATCH_ROOT + "/" + scratch_def["lang"] + "/" + class_name + "." + scratch_def["template_ext"]

    with open(scratch_def["f"]) as template_file:
        template = template_file.read()
        rendered_template = pystache.render(template, {'classname': class_name, 'created_at': arrow.get()})
        with open(file_name, 'w') as template_out:
            template_out.write(rendered_template)
        return file_name

def show():
    for s in SCRATCHES:
        print(s)

def main():
    initialize()
    lang = sys.argv[1]
    fn = create(lang)
    print("created", fn)
    click.edit(filename=fn)

if __name__ == "__main__":
    main()
