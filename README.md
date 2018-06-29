![Wizard!](wizard.png)

Print a wizard in your shell.

Because you are a **Wizard**.

# Test if the wizard is up

    $ (exec 9>/dev/tcp/wizard.host.fr/1337) 2>/dev/null && { echo "Wizard is up."; } || { echo "Wizard is down."; }
    $ Wizard is down.

# If the wizard is down, start the wizarding server

    $ python wizarding.py &

# Cast your Wizard spell

    $ echo -e "$({ wget -e use_proxy=no -qO- wizard.host.fr:1337 | openssl enc -base64 -d | gunzip ; } 2>/dev/null )"

> Shazaaamm
