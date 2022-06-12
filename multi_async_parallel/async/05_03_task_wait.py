from collection_s import namedtuple

Service = namedtuple('service', ('name', 'url', 'ip_attr'))

Services = {
    Service('ipify', '')
}
