# Kills a process named killmenow
exec {'process killer':
    command  => '/usr/bin/pkill -f killmenow', }
