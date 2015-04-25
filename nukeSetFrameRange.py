for i in nuke.allNodes():
           if i.Class() == 'Read':
                     i.knob('last').setValue(115)