# scratch

Just run

    $ scratch [lang]

to open an editor with a skeleton file in that language and start hacking!

## setup

### installing

    virtualenv venv
    . venv/bin/activate
    pip3 install --editable .

### set up templates
1. Create a `~/scratch` directory.
2. Create a `[lang]/template.[lang ext]` template file with `{{classname}}` and `{{created_at}}` in them.

### sample template
My `~/scratch/python/template.py` file is

    #!/usr/bin/env python3
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

which works pretty well!

## future work
- make `scratch` just create the most used file type
- make some create/list/edit template commands
