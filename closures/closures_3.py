def html_tags(tag):
    def wrap_text(msg):
        print("<{0}> {1} </{0}>".format(tag, msg))
    return wrap_text


print_h1 = html_tags('h1')
print_h1('Heading')
print_h1('Another Heading')

print_p = html_tags('p')
print_p("Hello world")
