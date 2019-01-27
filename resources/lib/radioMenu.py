# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import sys
import re
import urllib
import urllib2 
import cookielib

__addon__           = xbmcaddon.Addon()
__addon_id__        = __addon__.getAddonInfo('id')
__addonname__       = __addon__.getAddonInfo('name')
__icon__            = __addon__.getAddonInfo('icon')
__addonpath__       = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__            = __addon__.getLocalizedString
__path__            = os.path.join(__addonpath__, 'resources', 'lib' )
__path_img__        = os.path.join(__addonpath__, 'resources', 'media' )

sys.path.append(__path__)
sys.path.append (__path_img__)

class Main:
        
    def start(self, selfGet):
    
        def getSettingBool(setting):
            return __addon__.getSetting(setting).strip().decode('utf-8').lower() == "true"
		
        # vars
        self = selfGet
        
        list = [
        ['radio Slovakia', sys.argv[0] + '?sk', 'radioSlovakia.png', '', getSettingBool('radio_Slovakia')],
        ['radio Czech Republic', sys.argv[0] + '?cz', 'radioCzechRepublic.png', '', getSettingBool('radio_Czech_Republic')],
	['favourite SK', sys.argv[0] + '?topSK', 'favouriteSK.png', '', getSettingBool('favourite_SK')],
        ['favourite CZ', sys.argv[0] + '?topCZ', 'favouriteCZ.png', '', getSettingBool('favourite_CZ')],
        ['radio Netherland', sys.argv[0] + '?nl', 'radioNetherlands.png', '', getSettingBool('radio_Netherland')],
        ['radio Germany', sys.argv[0] + '?ger', 'radioGermany.png', '', getSettingBool('radio_Germany')],
        ['radio Polskie', sys.argv[0] + '?pl', 'radioPolskie.png', '', getSettingBool('radio_Polskie')],
        ['radio Austria', sys.argv[0] + '?au', 'radioAustria.png', '', getSettingBool('radio_Austria')],
        ['radio Russian Federation', sys.argv[0] + '?ru', 'radioRussianFederation.png', '', getSettingBool('radio_Russian_Federation')],
        ['radio France', sys.argv[0] + '?fr', 'radioFrance.png', '', getSettingBool('radio_France')]
                    ]
                
        for v in list:
            if not v[4]: continue
            listItem = xbmcgui.ListItem(label=v[0], iconImage=__path_img__ + '//' + v[2])
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=v[1], listitem=listItem, isFolder=True)
        
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        if self.opt != '':
            
            Title = list[int(self.opt)][0]
            Icon = list[int(self.opt)][2]
            URL = list[int(self.opt)][3]
            
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
