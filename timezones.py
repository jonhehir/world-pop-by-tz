from tzpop.timezones import Timezone


for t in Timezone.all():
    print("\t".join(map(str, [t.iana_name, t.winter_offset, t.summer_offset])))
