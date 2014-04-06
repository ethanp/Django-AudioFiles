#!/usr/bin/env bash

# Created 4/4/14
# Ethan Petuchowski

case "$1" in
        start )
            source /Users/Ethan/Dropbox/CSyStuff/Conversation/venv/bin/activate
            ;;

        pathit )
            export PATH="${PATH}:~/Dropbox/CSyStuff/Conversation"
            ;;

        credentials )
            echo "Username: ethan, Password: 4321"
            ;;

        stop )
            deactivate
            ;;

        syncdb )
            python manage.py syncdb
            ;;

        serve )
            python manage.py runserver
            ;;

        count )
            cloc . --exclude-dir="venv"
            ;;

        # even works for no args passed
        * )
            less /Users/Ethan/Dropbox/CSyStuff/Conversation/setupEnv.sh
            exit 1
esac
