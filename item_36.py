import subprocess as sp

'''
proc = sp.Popen(['echo', 'Hello from the child!'], shell=True, stdout=sp.PIPE)
out, err = proc.communicate()
print(out.decode('utf-8'))
'''
'''
proc = sp.Popen(['sleep', '0.3'], shell=True)
while proc.poll() is None:
    print('Working...')

print('Exit status', proc.poll())
'''

def run_sleep():
    