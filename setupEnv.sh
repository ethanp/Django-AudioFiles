#!/usr/bin/env bash
# 4/4/14
# Ethan Petuchowski

case "$1" in
        start )
            source venv/bin/activate
            ;;

        credentials )
            echo "Username: ethan, Password: 4321"

        stop )
            stop
            ;;

        count )
            cloc . --exclude-dir="venv"
            ;;

        # even works for no args passed
        * )
            echo $"Usage: $0 {start|stop|credentials}"
            exit 1

esac
