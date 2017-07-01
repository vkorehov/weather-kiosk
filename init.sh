#!/bin/bash
### BEGIN INIT INFO
# Provides:        weather
# Required-Start:  $network $remote_fs $syslog
# Required-Stop:   $network $remote_fs $syslog
# Default-Start:   2 3 4 5
# Default-Stop:
# Short-Description: Start Network service
### END INIT INFO

. /lib/lsb/init-functions

case $1 in
        start)
                (cd /home/pi/weather && python ./weather.py 1>/dev/null 2>/dev/null &)
                ;;
        stop)
                pkill -f "python ./weather.py"
                ;;
        restart|force-reload)
                $0 stop && sleep 2 && $0 start
                ;;
        status)
                ps -ef | fgrep "python ./weather.py"
                ;;
        *)
                echo "Usage: $0 {start|stop|restart|status}"
                exit 2
                ;;
esac

