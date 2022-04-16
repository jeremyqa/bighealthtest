# What is this?

This me doing the take home test for Big Health.  

If you're reading this and you're not me or someone who works there, something has gone wrong.

It uses pytest and selenium to do some simple browser testing. 

Written on python 3.8.5. It uses f"strings" so if you're on <3.6 you might have a problem. I don't think I used anything else new.

# How do I use this?
First install the deps with  `pip install -r requirements.txt`  (You probably want to do it in a virtualenv)

You'll need Chromedriver on your path. You can probably install it with brew if you're on a mac, or hop over to https://chromedriver.chromium.org/downloads and get the appropriate version. 

Run the tests with pytest from src with `pytest`

# What should I see when it runs?

It should open the browser, fly through the onboarding, and report tests passed. 

If something isn't working you can add `--pdb` to the pytest call to drop into the debugger. `pdb++` is included in the deps so you'll get color coding and other QoL perks.



