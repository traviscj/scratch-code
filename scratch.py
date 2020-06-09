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

@click.group()
def cli(): pass

SCRATCH_ROOT = os.path.expanduser("~/scratch")

SCRATCHES = []

@cli.command()
def firstinit():
    if not os.path.exists(SCRATCH_ROOT):
        os.mkdir(SCRATCH_ROOT)
        print(f"created {SCRATCH_ROOT}")

@cli.command()
@click.argument("lang", default="py")
@click.argument("langext", default="py")
def init_lang(lang, langext):
    """
    initializes a template folder for a new language

    :param lang:
    :param langext:
    :return:
    """
    language_dir = f"{SCRATCH_ROOT}/{lang}"
    if not os.path.exists(language_dir):
        os.mkdir(language_dir)
    template_filename = f"{language_dir}/template.{langext}"
    if not os.path.exists(template_filename):
        with open(template_filename, 'w') as template_file:
            body = """#!/usr/bin/env python3
# created_at: {{created_at}}
# remove w/: rm $HOME/scratch/python/{{classname}}.py

class {{classname}}(object):
    def __init__(self):
        print("constructor")

def main():
    print("main")

if __name__ == "__main__":
    print("global")
    main()
"""
            template_file.write(body)

    pass


"""
~/scratch/<lang>/template.<langext>
"""

def initialize():
    for f in glob.glob(os.path.expanduser(SCRATCH_ROOT + "/*/template*")):
        lang_template_file = f.replace(SCRATCH_ROOT + "/", "")
        lang, template_file = lang_template_file.split('/')
        template_ext = template_file.replace("template.", "")
        SCRATCHES.append({"lang": lang, "template_ext": template_ext, "f": f})

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_template(lang):
    if not lang or lang == "":
        raise Exception("Must pass an language to generate a scratch for!")
    return [s for s in SCRATCHES if s["lang"] == lang or s["template_ext"] == lang][0]

@cli.command()
@click.argument("lang")
def create(lang):
    scratch_def = get_template(lang)
    
    unique_name = id_generator()
    class_name = "Scratch_" + unique_name
    matched_lang = scratch_def["lang"]
    matched_lang_ext = scratch_def["template_ext"]
    file_name = f"{SCRATCH_ROOT}/{matched_lang}/{class_name}.{matched_lang_ext}"

    with open(scratch_def["f"]) as template_file:
        template = template_file.read()
        context = {
            'classname': class_name,
            'created_at': arrow.get(),
        }
        rendered_template = pystache.render(template, context)
        with open(file_name, 'w') as template_out:
            template_out.write(rendered_template)
        click.echo(f"created {file_name}")
        click.edit(filename=file_name)
        return file_name

@cli.command()
def show():
    for s in SCRATCHES:
        print(s)

def main():
    initialize()
    cli()

if __name__ == "__main__":
    main()
