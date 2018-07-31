import time
from datetime import datetime as dt


def get_host_paths(alt_hosts_path=r''):
    default_host_path = r"C:\Windows\System32\drivers\etc\hosts"

    if alt_hosts_path == '':
        hosts_path = default_host_path
    else:
        hosts_path = r"%s" % alt_hosts_path
    return hosts_path


def get_sites(sites=r''):
    sites_that_kill_me = []
    sitelist = sites.split(',')
    while 1:
        if len(sitelist) == 0:
            try:
                raise IOError
            except IOError:
                print('Please enter at least one website')
        else:
            for wsite in sitelist:
                if 'www.' not in wsite:
                    site = r"www." + r"%s" % wsite
                    sites_that_kill_me.append(site)
                    sites_that_kill_me.append(wsite)
            break
    return sites_that_kill_me


def set_start_time():
    count = 0
    start_help = 'Type in the hour of the day you want the filter to start working. '
    '\n we are using a 24 hour clock EG if you want it'
    ' to start working by 5am type 5 but if you want 5pm type 17\n Please type only digits '
    'no letters '
    while 1:
        raw_start = input('Type in the hour of the day you want the filter to start working. '
                          '\n we are using a 24 hour clock EG if you want it'
                          ' to start working by 5am type 5 but if you want 5pm type 17\n by default this is set to 9am '
                          'or 9 O\'clock in the morning. Please type only digits no letters or press enter to use '
                          'default time of 9am: ')
        if raw_start == '':
            raw_start = 9
            start = raw_start
            break
        elif raw_start in range(0, 25):
            start = raw_start
            break
        else:
            print('Please type a number between 1 and 24')
            count += 1
            if count == 5:
                print(start_help)
                count = 0
    return start


def set_stop_time():
    count = 0
    stop_help = 'Type in the hour of the day you want the filter to stop working. '
    '\n we are using a 24 hour clock EG if you want it'
    ' to stop working by 5am type 5 but if you want 5pm type 17\n Please type only digits '
    'no letters '
    while 1:
        raw_stop = input('Type in the hour of the day you want the filter to stop working. '
                         '\n we are using a 24 hour clock EG if you want it'
                         ' to stop working by 5am type 5 but if you want 5pm type 17\n by default this is set to 5pm'
                         ' or 1700 hours Please type only digits no letters: ')
        if raw_stop == '':
            raw_stop = 9
            stop = raw_stop
            break
        elif raw_stop in range(0, 25):
            stop = raw_stop
            break
        else:
            print('Please type a number between 1 and 24')
            count += 1
            if count == 5:
                print(stop_help)
                count = 0
    return stop


def check_time(start=9, stop=17):

    if dt(dt.now().year, dt.now().month, dt.now().day, start) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                              dt.now().day, stop):
        return True
    else:
        return False


def modify_host(hosts_path, sites_that_kill_me, redirect, check):
    if check is True:
        print('Working Time!!')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site + '\n')
        time.sleep(60000)
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_that_kill_me):
                    file.write(line)
            file.truncate()
        print('Time to play')
        time.sleep(60000)


def main():
    sites = input('type the url of the sites you wish to block separated by commas')
    host_path = input('Type in the path of your hosts file if you are not on a windows system \nor'
                      ' if you changed the location ELSE press enter: ')
    redirect = '127.0.0.1'
    hosts_path = get_host_paths(host_path)
    site_that_kill_me = get_sites(sites)
    start = set_start_time()
    stop = set_stop_time()
    check = check_time(start, stop)
    while 1:
        modify_host(hosts_path, site_that_kill_me, redirect, check)


if __name__ == '__main__':
    main()
