from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.hooks import TryNext
import statprof

@magics_class
class StatprofMagics(Magics):

    def __init__(self, *a, **kw):
        super(StatprofMagics, self).__init__(*a, **kw)
        self.enabled = False
        self.once = False
        self.has_started = False
        self.is_active = False

    @line_magic
    def statprof(self, parameter_s=''):
        r'''statprof => Enable/disable inline statprof

        %statprof
        Toggle statprof on/off

        %statprof once
        Turn statprof on for the next call
        '''

        self.has_started = False

        if parameter_s == '':
            self.enabled = not self.enabled
            self.once = False
            self.print_state()
        elif parameter_s == 'once':
            self.enabled = True
            self.once = True
            self.print_state()
        else:
            print 'Unknown parameter: ' + parameter_s

    def print_state(self):
        print 'Statprof %s%s' % (
            'enabled' if self.enabled else 'disabled',
            ' (once)' if self.once else '')

    def pre_run_code_hook(self, ip):
        if not self.enabled:
            raise TryNext

        if statprof.is_active(): # play it safe
            statprof.state.reset()
        statprof.reset()

        self.has_started = True
        statprof.start()
        raise TryNext

    def post_execute(self):
        if not self.enabled or not self.has_started:
            return

        if self.once:
            self.enabled = False
            self.once = False
            
        self.has_started = False
        statprof.display()
        statprof.stop()
        if statprof.is_active(): # play it safe
            statprof.state.reset()
        statprof.reset()

def load_ipython_extension(ip):
    s = StatprofMagics(ip)
    ip.register_magics(s)
    ip.set_hook('pre_run_code_hook', s.pre_run_code_hook, 0)
    ip.register_post_execute(s.post_execute)
