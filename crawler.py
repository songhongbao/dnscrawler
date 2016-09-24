#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers.insert(0, '114.114.114.114')
resolver.lifetime = resolver.timeout = 10.0
answers = resolver.query('www.baidu.com')
for answer in answers:
    print answer