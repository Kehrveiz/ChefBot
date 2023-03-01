#-*- coding: utf-8 -*-
from colorclass import Color
from datetime import datetime

_version_ = '1.0'
_name_ = 'ChefBot'
_token_ = ""
_channel_url_ = 'https://t.me/+i__huMdK4-JhYWIx'
_admins_ = [1114278840]


def is_admin(_id): 
    return _id in _admins_


def get_time(_lang): 
    today = datetime.now()
    hour = today.hour
    
    if hour < 20 and hour > 6: 
        return '🤖 ⏰Hora del sistema: {}'.format(today.strftime('%H:%M'))
    else: 
        return '🤖 ⏰Time of system: {}'.format(today.strftime('%H:%M'))


def gcb(cb, number): 
    code = cb.split('-')[0]
    return int(code) == number


def _logging(msg): 
    print(Color(
        '{autogreen}[{/green}{autoyellow}+{/yellow}{autogreen}]{/green} {autocyan}'\
        '{msg}{/cyan}').format(msg=msg))


def _logging_error(msg): 
    print(Color(
        '{autored}[{/red}{autoyellow}!{/yellow}{autored}]{/red} {autored}'\
        '{msg}{/red}').format(msg=msg))


def convert_time(m=None, h=None, d=None): 
    '''Conversion de tiempo en segundos'''
    
    convert_table = {
        's': 1,
        'm': 60,
        'h': 3600,
        'd': 86400
    }
    
    t = 's'
    s = 1
    if m is not None: 
        t, s = 'm', m
    elif h is not None: 
        t, s = 'h', h
    else: 
        t, s = 'd', d
    
    return convert_table[t] * s
    