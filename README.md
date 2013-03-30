IPython-statprof
================

_[Statprof](https://github.com/bos/statprof.py) magic for statistical profiling inside IPython_

Installation
------------

    # On the shell:
    git clone https://github.com/andreasjansson/ipython-statprof.git
    sudo pip install statprof
    ipython

    # In IPython:
    %install_ext ipython-statprof/statprofmagic.py

Now, IPython will tell you that you can use the extension right away by `%load_ext statprofmagic`. 
That probably won't work, instead just restart IPython.

The extension has been tested on IPython 0.13 / Python 2.7.

Usage
-----

First, load the extension:

    %load_ext statprofmagic

Then enable it:

    %statprof

To disable, just type `%statprof` again.

While statprof is enabled, all input lines will be profiled.
To enable statprof for a single line only:

    %statprof once

Sample output
-------------

    In [83]: %load_ext statprofmagic

    In [84]: %statprof
    Statprof enabled

    In [85]: import pickle, random, string; pickle.dumps([random.choice(string.ascii_letters) for _ in range(100000)]);
      %   cumulative      self          
     time    seconds   seconds  name    
     17.72      0.14      0.09  pickle.py:279:save
     16.46      0.08      0.08  pickle.py:277:save
     15.19      0.08      0.08  random.py:274:choice
     10.13      0.51      0.05  <ipython-input-16-739ab051d7f2>:1:<module>
      7.59      0.04      0.04  pickle.py:267:get
      6.33      0.03      0.03  random.py:272:choice
      6.33      0.32      0.03  pickle.py:615:_batch_appends
      5.06      0.03      0.03  pickle.py:616:_batch_appends
      3.80      0.02      0.02  pickle.py:269:save
      3.80      0.02      0.02  pickle.py:272:save
      2.53      0.01      0.01  pickle.py:333:persistent_id
      1.27      0.02      0.01  pickle.py:271:save
      1.27      0.01      0.01  pickle.py:261:get
      1.27      0.01      0.01  pickle.py:278:save
      1.27      0.01      0.01  pickle.py:260:get
      0.00      0.35      0.00  pickle.py:224:dump
      0.00      0.35      0.00  pickle.py:600:save_list
      0.00      0.51      0.00  interactiveshell.py:2746:run_code
      0.00      0.35      0.00  pickle.py:1374:dumps
      0.00      0.51      0.00  ipython2:7:<module>
      0.00      0.51      0.00  interactiveshell.py:586:interact
      0.00      0.51      0.00  interactiveshell.py:2617:run_cell
      0.00      0.51      0.00  interactiveshell.py:467:mainloop
      0.00      0.51      0.00  ipapp.py:389:launch_new_instance
      0.00      0.35      0.00  pickle.py:286:save
      0.00      0.51      0.00  ipapp.py:363:start
      0.00      0.51      0.00  interactiveshell.py:2696:run_ast_nodes
    ---
    Sample count: 79
    Total time: 0.510000 seconds

    In [86]: %statprof
    Statprof disabled
