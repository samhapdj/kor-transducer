# Finite State Transducer for Korean

**NOTE: Use the precompiled hangul.hfst, if your machine does not have  more than 12gb of RAM or Swap partition enabled. This it due to the large size of hangul.lexc(contains all legal hangul syllable blocks).**
      
For more information on the transducer, visit [here.](https://wikis.swarthmore.edu/ling073/User:Dmin1/Final_project)

## Quick Start Up Guide ##

Run  
```
$ ./autogen.sh
```


Run 
```
$ make install
```

Run 
```
$ echo 우리는 집에 간다." | apertium -d . kor-morph
```
to test


# apertium-kor
===============================================================================

This is an Apertium monolingual language package for Korean. What
you can use this language package for:

* Morphological analysis of Korean
* Morphological generation of Korean
* Part-of-speech tagging of Korean

Requirements
===============================================================================

You will need the following software installed:

* lttoolbox (>= 3.3.0)
* apertium (>= 3.3.0)
* vislcg3 (>= 0.9.9.10297)
* hfst (>= 3.8.2)

If this does not make any sense, we recommend you look at: www.apertium.org

Compiling
===============================================================================

Given the requirements being installed, you should be able to just run:

```
$ ./configure
$ make
```

You can use ./autogen.sh instead of ./configure if you're compiling
from SVN.

If you're doing development, you don't have to install the data, you
can use it directly from this directory.

If you are installing this language package as a prerequisite for an
Apertium translation pair, then do (typically as root / with sudo):

```
$ make install
```


You can give a --prefix to ./configure to install as a non-root user,
but make sure to use the same prefix when installing the translation
pair and any other language packages.

Testing
===============================================================================

If you are in the source directory after running make, the following
commands should work:

```
$  echo "TODO: test sentence" | apertium -d . kor-morph
```
TODO: test analysis result

```
$ echo "TODO: test sentence" | apertium -d . kor-tagger
```
TODO: test tagger result

Files and data
===============================================================================

* apertium-kor.kor.dix           - Monolingual dictionary
* apertium-kor.kor.lexc          - Morphotactic dictionary
* apertium-kor.kor.twol          - Morphophonological rules
* apertium-kor.kor.rlx           - Constraint Grammar disambiguation rules
* apertium-kor.post-kor.dix      - Post-generator
* hangul.lexc                    - Contains all legal Korean syllable block mappings and other necessary characters
* kor.prob                       - Tagger model
* modes.xml                      - Translation modes

For more information
===============================================================================

* http://wiki.apertium.org/wiki/Installation
* http://wiki.apertium.org/wiki/apertium-kor
* http://wiki.apertium.org/wiki/Using_an_lttoolbox_dictionary
* https://wikis.swarthmore.edu/ling073/User:Dmin1/Final_project

Help and support
===============================================================================

If you need help using this language pair or data, you can contact:

* Mailing list: apertium-stuff@lists.sourceforge.net
* IRC: #apertium on irc.freenode.net

See also the file AUTHORS included in this distribution.

