#!/usr/bin/env bash

function trace(){
    msg=$1;
    echo "$(date '+%d/%m/%Y %H:%M:%S') - ${msg}";
}

function passing_command_in_the_wp_container(){
    command=$1; #The command string
    docker exec -it docker-wordpress-1 sh -c "$command"
}

function main(){
uid_host=$(id -u)
gid_host=$(id -g)

trace "setting the host userid (${uid_host}) as the container www-data user";
passing_command_in_the_wp_container  "usermod -u ${uid_host} www-data";
ret1=$?;
trace "setting the host grouprid (${gid_host}) as the container www-data group";
passing_command_in_the_wp_container  "groupmod -g ${gid_host} www-data";
ret2=$2;
trace "giving all whordpress files www-data:www-data user/group";
passing_command_in_the_wp_container "chown -R www-data:www-data /var/www/html";
ret3=$?;
}

# main prog
log_file="./$(basename $0)_$(date '+%d%m%Y_%H%M%S').log";
main 2>&1 | tee $log_file;

